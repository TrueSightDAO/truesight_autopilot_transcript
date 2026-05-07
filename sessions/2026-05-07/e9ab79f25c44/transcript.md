# Autopilot Session — 2026-05-07

**Session**: `e9ab79f25c44`


---


### 🧑 Governor

any reason why I keep seeing Loading your TDG holdings… in this view http://localhost:8080/chat.html?


### 🤖 Autopilot

Let me check the relevant code to understand what's happening.


### 🤖 Autopilot

Now let me check the `tdg_balance.js` script that's loaded on this page:


### 🤖 Autopilot

Found it. Here's what's happening:

**"Loading your TDG holdings…" is stuck because the badge can't resolve your public key.**

The flow is:

1. `tdg_balance.js` runs on every DApp page (including chat.html via `<div id="tdgBalanceBadge">`)
2. It tries **two sources** to look up your public key:
   - **GitHub cache** (`treasury-cache/main/dao_members.json`) — fast, CDN-served
   - **GAS fallback** (`assetVerify` endpoint) — slower, Google Apps Script

3. If **both fail** (cache miss + GAS timeout/error), the catch handler just clears the container silently — but the **initial "Loading…" text** is set before the fetch, and if the fetch chain takes a long time or hangs, you see "Loading your TDG holdings…" indefinitely.

**Most likely causes:**

| Cause | Why |
|---|---|
| **Public key not in the cache snapshot** | If you recently created your digital signature, it hasn't been published to the `dao_members.json` cache yet. The cache is updated on email verification + contribution events. |
| **GAS cold-start timeout** | The fallback GAS endpoint can take 5+ seconds on cold start, and if it times out, the catch fires silently — leaving the "Loading…" text in place. |
| **No public key in localStorage** | If you're not signed in (no `publicKey`), the script returns early — but the "Loading…" text was already set. |

**Quick fix to check:** Open your browser console (`F12`) and run:

```js
localStorage.getItem('publicKey')
```

If that returns `null`, you need to create a digital signature at [create_signature.html](http://localhost:8080/create_signature.html).

If it returns a key, try:

```js
fetch('https://raw.githubusercontent.com/TrueSightDAO/treasury-cache/main/dao_members.json').then(r => r.json()).then(d => console.log('Found keys:', d.contributors?.flatMap(c => c.public_keys?.map(k => k.public_key))))
```

If your key isn't in that list, you need to get your email verified so the cache snapshot includes you.

**Want me to open a fix PR** to make the "Loading…" state timeout gracefully (e.g. show a fallback message after 5 seconds instead of hanging forever)?


### 🧑 Governor

It finally resolved... why did it have to hit the GAS?


### 🤖 Autopilot

Good question. Let me trace exactly why it fell through to GAS.

The cache fetch logic in `tdg_balance.js` does this:

```js
fetchFromCache(publicKey)
  .catch(function() { return fetchFromGas(publicKey); })
```

And `fetchFromCache` tries two paths:

1. **`window.DaoMembersCache.findByPublicKey(publicKey)`** — a shared session-memoized helper. If that's not loaded on the page, it falls through to...
2. **Inline fetch of `dao_members.json`** from GitHub raw — then iterates all contributors looking for your public key.

If **either** of those throws an error, it falls back to GAS.

Let me check whether `DaoMembersCache` is loaded on `chat.html`:


### 🤖 Autopilot

Now check if `chat.html` actually loads `dao_members_cache.js`:

Looking at the `<script>` tags in `chat.html`:

```html
<script src="./menu.js?v=20260430"></script>
<script src="./tdg_balance.js"></script>
<script src="./scripts/edgar_payload_helper.js"></script>
```

**No `dao_members_cache.js` is loaded on chat.html.** So `window.DaoMembersCache` is `undefined`, and the code falls through to the inline fetch path. Let me check what happened there:

```js
// In tdg_balance.js, fetchFromCache inline path:
fetch(CACHE_URL, { cache: 'no-cache' })
  .then(function(r) {
    if (!r.ok) throw new Error('cache HTTP ' + r.status);
    return r.json();
  })
```

**Here's the likely culprit:** `{ cache: 'no-cache' }` — this sends a `Cache-Control: no-cache` header which forces a **revalidation with the origin server**. GitHub raw can sometimes respond slowly or with a stale-while-revalidate delay, especially on the first hit from a local dev environment.

**Why it hit GAS:**

1. `DaoMembersCache` not loaded → skip shared path
2. Inline fetch to GitHub raw with `no-cache` → **timed out or threw** (maybe a CORS issue from `localhost`, or the request just took too long)
3. `.catch()` → fell through to GAS
4. GAS eventually responded → badge rendered

**The root cause:** `chat.html` doesn't include `dao_members_cache.js`, so `tdg_balance.js` has to do its own raw fetch — and the `no-cache` directive makes it slower/more fragile than necessary.

**Want me to open a PR that:**
1. Adds `<script src="./scripts/dao_members_cache.js">` to `chat.html`
2. Removes the `no-cache` from the inline fallback (or adds a timeout)


### 🧑 Governor

yes, please do so and then once you are done can you share with me the approval dialogue to approve the PR or the link to go merge the PR


### 🤖 Autopilot

Let me first check the current state of things to make sure I understand the full picture before opening the fix.


### 🤖 Autopilot

Good. Now let me open the fix PR:


### 🤖 Autopilot

Here's the PR: **https://github.com/TrueSightDAO/dapp/pull/214**

It makes two changes:

1. **`chat.html`** — adds `<script src="./scripts/dao_members_cache.js">` before `tdg_balance.js` so the shared session-memoized cache is available, avoiding the slow inline fetch path
2. **`tdg_balance.js`** — adds a 5-second `AbortController` timeout to the inline GitHub raw fetch, so if it hangs, it falls through to GAS instead of leaving "Loading…" stuck forever

You can review and merge it at the link above. Want me to submit a DAO contribution for this work once it's merged?

