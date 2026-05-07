# Autopilot Session — 2026-05-07

**Session**: `5817ac6fdf35`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Diagnose this bug step by step. Do not propose fixes yet — just identify the root cause with exact code locations.

Problem: Opening http://localhost:8080/create_signature.html?em=test&vk=abc shows "Access restricted to authorized governors" styled as a DAO Assistant message (not the page's normal error format).

Read these files in order:
1. dapp/create_signature.html lines 390-410 — EDGAR_BASE logic  
2. dapp/chat.html lines 1035-1055 — how 403 errors are displayed
3. truesight_autopilot/app/auth.py lines 55-106 — verify_payload gate
4. truesight_autopilot/app/governor_registry.py lines 40-70 — _extract_governor_keys filter

The question: what call from create_signature.html's JS execution could trigger a 403 from autopilot's verify_payload, causing chat.html's error display to appear? 

If no direct path exists, consider: is there a service worker, redirect, or shared localStorage state that could cause chat.html's error UI to appear on create_signature.html?


### 🤖 Autopilot

Let me read all four files in order to trace the bug.


### 🤖 Autopilot

Now let me look at the service worker file and also check if there's a redirect or shared state mechanism:


### 🤖 Autopilot

Now I have the full picture. Let me trace the exact root cause.

---

## Root Cause Analysis

### The Bug

Opening `http://localhost:8080/create_signature.html?em=test&vk=abc` shows **"Access restricted to authorized governors"** styled as a DAO Assistant message (chat.html's error format), not create_signature.html's own error styling.

### Step-by-step Trace

**1. `create_signature.html` loads `routes.js` (line 11)**

`routes.js` defines `Routes.edgar.base = 'https://edgar.truesight.me'` (production) by default. On localhost, the `EDGAR_BASE` logic in `create_signature.html` (lines 390-410) **overrides** this to `http://localhost:3000` because `?local_edgar=1` is not set — but the URL params are `em=test&vk=abc`, not `local_edgar=1`. So `EDGAR_BASE` falls through to `window.Routes.edgar.base` which is `https://edgar.truesight.me`.

**2. `create_signature.html` also registers a Service Worker (line ~470)**

```javascript
navigator.serviceWorker.register('service-worker.js', { scope: './' })
```

The service worker caches `create_signature.html` and intercepts all fetches.

**3. The `onload` handler runs (line ~280)**

Since `?em=test&vk=abc` are present, `readVerifyParams()` returns `{ vk: 'abc', em: 'test' }`.

At line ~340, since `publicKey` and `privateKey` exist in localStorage, the code enters the `if (verifyParams)` branch. It shows the verify section and calls `setTimeout(() => { verifyBtn.click(); }, 0)` — which triggers `submitSignedEmailEvent` with event name `EMAIL VERIFICATION EVENT`.

**4. `submitSignedEmailEvent` calls Edgar at `https://edgar.truesight.me/dao/submit_contribution`**

This is the **production** Edgar URL (not localhost:3000). The function uses `EdgarPayloadHelper` to sign the payload and POSTs to `EDGAR_SUBMIT_URL`.

**5. Edgar's backend calls `verify_payload` in `auth.py` (line 55-106)**

Step 4 in `verify_payload` (line 97-101):
```python
if not settings.disable_governor_check and not is_governor(public_key_b64):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access restricted to authorized governors.",
    )
```

`is_governor` (line 104) calls `governor_registry.py`'s `is_governor` (line 96), which calls `_extract_governor_keys` (line 40-70). That function filters by `_governor_names()` — which defaults to `{"Gary Teh"}`. If the public key in localStorage belongs to someone NOT named "Gary Teh" (or the key isn't in the registry at all), the check fails → **403**.

**6. The 403 response arrives back at `create_signature.html`**

In `submitSignedEmailEvent` (line ~180):
```javascript
if (!resp.ok) {
    const base = (data && data.error) || rawText || `HTTP ${resp.status}`;
    throw new Error(String(base) + extra);
}
```

This throws `"Access restricted to authorized governors."` which propagates up to the `verifyBrowserButton` click handler's catch block (line ~310):
```javascript
setVerifyInlineStatus('Verification failed: ' + e.message, 'error');
```

So the error **does** appear in `create_signature.html`'s own inline status element (`#verifyInlineStatus`), styled with the `error` CSS class (red text).

### But wait — the user says it appears "styled as a DAO Assistant message"

This is the key. The message "Access restricted to authorized governors" is the **exact** string from `auth.py` line 99. But it's appearing in **chat.html's** error format, not create_signature.html's.

**The actual path is a redirect/reload chain:**

1. `create_signature.html` calls `verifyBtn.click()` → POST to production Edgar → **403** → error shown in `#verifyInlineStatus`.

2. But there's a **second path**: the `routes.js` probe (lines ~90-110). On page load, `routes.js` fires an async fetch to `script.google.com` with a 3-second timeout. If that fails, it sets `localStorage.routesMode = 'proxy'` and calls **`window.location.reload()`**.

3. The reload causes the page to re-initialize. On reload, `readVerifyParams()` still sees `?em=test&vk=abc`, so the verify flow fires again. But now there's a **race condition** with the service worker.

4. **The service worker** (`service-worker.js`) caches `create_signature.html` and intercepts all GET requests. On the reload, the service worker may serve a cached version of `create_signature.html` — but crucially, the service worker's `install` event also caches `./chat.html` (listed in `URLS_TO_CACHE` as `'./'` which resolves to `index.html`, but `chat.html` is NOT in the cache list).

5. **However**, the real issue is simpler: the `routes.js` probe failure + reload causes the page to reload **while the verify fetch is in flight**. The reload interrupts the fetch, and on the new page load, the service worker serves the cached `create_signature.html`. But the `em` and `vk` params are still in the URL, so the verify flow fires again — creating a **loop** of 403 errors.

### The Actual Root Cause

**The `routes.js` probe** (lines 90-110 in `routes.js`):

```javascript
fetch(directGas.assetVerify, {
    method: 'GET',
    mode: 'no-cors',
    cache: 'no-store',
    signal: controller.signal
}).catch(function () {
    clearTimeout(timeoutId);
    localStorage.setItem('routesMode', 'proxy');
    window.location.reload();  // ← THIS
});
```

On `localhost:8080`, the `routes.js` probe fires a `no-cors` GET to `script.google.com`. This **will fail** (CORS or network), triggering `window.location.reload()`. The reload preserves the `?em=test&vk=abc` query params. On reload:

- The service worker serves the cached `create_signature.html`
- `onload` fires again
- `readVerifyParams()` returns the params again
- The verify flow fires again
- The 403 from Edgar appears again
- `routes.js` probe fires again → fails → reload again

**This creates an infinite reload loop.** Each reload, the 403 error flashes briefly before the page reloads. The user perceives the 403 error message as appearing on `create_signature.html` — which it does — but the reload is so fast they may not notice the page flicker.

### Why "styled as a DAO Assistant message"?

The user's description is slightly imprecise. The 403 error **does** appear in `create_signature.html`'s own `#verifyInlineStatus` element (styled with CSS class `error` = red text). But because the page reloads immediately after (from the `routes.js` probe failure), the user may be seeing the error flash in a context that looks like a chat bubble — or more likely, they're conflating it with the **chat.html** error format they've seen before.

**However**, there IS a scenario where chat.html's error UI could appear: if the user previously had `chat.html` open in the same tab, and the service worker's cached response for `create_signature.html` somehow serves chat.html's content. Looking at the service worker cache list — `chat.html` is **not** in `URLS_TO_CACHE`. But `'./'` (index.html) is. If the service worker's scope matching is loose, a navigation to `create_signature.html` could be served from a cached `index.html` response. But that's unlikely given the explicit path matching.

### Summary

| Step | File | Line(s) | What Happens |
|------|------|---------|--------------|
| 1 | `create_signature.html` | 390-410 | `EDGAR_BASE` resolves to production `https://edgar.truesight.me` (no `?local_edgar=1`) |
| 2 | `create_signature.html` | ~280 | `onload` detects `?em=test&vk=abc` via `readVerifyParams()` |
| 3 | `create_signature.html` | ~340 | Enters `if (verifyParams)` branch, calls `verifyBtn.click()` after 0ms timeout |
| 4 | `create_signature.html` | ~170 | `submitSignedEmailEvent` POSTs to production Edgar |
| 5 | `auth.py` | 97-101 | `verify_payload` → governor check fails → **403** `"Access restricted to authorized governors."` |
| 6 | `create_signature.html` | ~180 | `submitSignedEmailEvent` throws the 403 error |
| 7 | `create_signature.html` | ~310 | Catch block calls `setVerifyInlineStatus('Verification failed: Access restricted...', 'error')` |
| 8 | `routes.js` | 90-110 | Async probe to `script.google.com` fails → `window.location.reload()` |
| 9 | — | — | Page reloads with `?em=test&vk=abc` still in URL → loop back to step 2 |

**Root cause**: The `routes.js` probe (line 106: `window.location.reload()`) creates a reload loop on localhost because the `no-cors` fetch to `script.google.com` always fails. Each reload re-triggers the verify flow, which hits production Edgar's governor gate and gets a 403. The error message flashes in `create_signature.html`'s inline status element before the next reload.

