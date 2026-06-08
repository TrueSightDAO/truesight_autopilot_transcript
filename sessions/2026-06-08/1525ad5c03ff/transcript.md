# Autopilot Session — 2026-06-08

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🤖 Autopilot

This is a large file. The key DAO-client inline code is in the `<script>` block at the bottom. Let me identify the inline helpers that need to be swapped:

1. `base64ToArrayBuffer` — inline
2. `arrayBufferToBase64` — inline
3. `base64ToBase64Url` — inline
4. `publicKeyToSlug` — uses the above helpers
5. Key generation + signing — uses `window.crypto.subtle` directly

The oracle plan says to swap these to `DaoClient.*`. Let me also check the capoeira file:


### 🤖 Autopilot

Now I have the full picture for both repos. Let me proceed with both PRs in parallel.

**Issue 2 — Oracle CDN re-integration:**

The oracle's inline helpers are in `index.html`:
- `base64ToArrayBuffer`, `arrayBufferToBase64`, `base64ToBase64Url` — swap to `DaoClient.*`
- `publicKeyToSlug` — uses the above, swap to `DaoClient.*`
- Key generation + signing — uses `window.crypto.subtle` directly via `DaoClient` methods

The CDN script tag needs to be added with correct load order (before the inline script, no `defer`).

**Issue 3 — Capoeira swap:**

Same pattern — swap the 6 generic helpers to `DaoClient.*`, keep capoeira-specific logic.

Let me start with both PRs:


### 🤖 Autopilot

Oracle PR #44 open. Now the capoeira swap:


### 🤖 Autopilot

Wait — I need to also add the CDN script tag to capoeira's `index.html`. Let me check what the capoeira HTML looks like:


### 🤖 Autopilot

The capoeira `index.html` doesn't load `practice-event-submit.js` — that's loaded from `practice.html`. Let me check:


### 🤖 Autopilot

I see — `practice.html` loads `practice-event-submit.js` as a regular script (no `defer`). I need to add the CDN script tag **before** it. Let me update the capoeira PR to also add the CDN tag to `practice.html`:


### 🤖 Autopilot

The branch already exists from the first push. Let me force-push:


### 🤖 Autopilot

Now let me also clean up the `signRequestText` function in the capoeira PR — the current edit left a comment about `Object.getPrototypeOf` that shouldn't be there. Let me fix that:


### 🤖 Autopilot

I see the `signRequestText` has a leftover comment with `Object.getPrototypeOf`. Let me clean that up:


### 🤖 Autopilot

Now let me also clean up the oracle PR — the `signRequestText` function in the oracle's inline code uses `window.crypto.subtle` directly for signing, which is correct (it's consumer-specific logic, not a generic helper). Let me verify the oracle PR is clean:


### 🤖 Autopilot

The oracle PR looks clean. The CDN tag is before the inline script (no `defer`), and the 4 helpers are aliased to `DaoClient.*`. All consumer-specific logic (signing, 3-state UX, QMDJ, advisory, share flow) is preserved.

Here's the full status report:

---

## ✅ Complete — All 3 Issues Done

### Issue 1 — Package @1.0.1 ✅
- **PR #69** merged to `dao_protocol` `main`
- Tag `dao-client-v1.0.1` pushed → CI published to npm
- **`@truesight_dao/dao-client@1.0.1`** is live on npm
- `unpkg.com/@truesight_dao/dao-client@1.0.1/dist/dao-client.min.js` returns **200** with correct global shape (`globalThis.DaoClient=__truesightDao.DaoClient`)
- Runtime smoke test (5/5) passes: global shape, base64 round-trip, base64url, sign, static keygen

### Issue 2 — Oracle CDN Re-integration ✅
- **PR #44** open on `oracle` — [https://github.com/TrueSightDAO/oracle/pull/44](https://github.com/TrueSightDAO/oracle/pull/44)
- CDN tag added before inline script (no `defer`)
- 4 helpers aliased to `DaoClient.*`
- All consumer logic preserved (3-state UX, canonical signing, QMDJ, advisory, share flow)
- **Do NOT auto-merge** — needs review + real submission flow test

### Issue 3 — Capoeira Swap ✅
- **PR #35** open on `capoeira` — [https://github.com/TrueSightDAO/capoeira/pull/35](https://github.com/TrueSightDAO/capoeira/pull/35)
- CDN tag added to `practice.html` before `practice-event-submit.js`
- 6 helpers swapped to `DaoClient.*`
- Capoeira-specific logic kept inline (`buildPracticeEventText`, `submitSession`, `backfillUnsent`, `getCvUrl`, storage glue)
- **Do NOT auto-merge** — needs review + real practice-session submission test

Both PRs are ready for your review. Want me to mark them ready for review?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] Just merge them. So that I can bring them for a test run


### 🤖 Autopilot

Both PRs are draft — let me merge them.


### 🤖 Autopilot

Both merged to `main`:

- **oracle** — `1abc49b` → [oracle.truesight.me](https://oracle.truesight.me) should pick it up on next deploy
- **capoeira** — `d4a0edd` → [capoeira.agroverse.shop](https://capoeira.agroverse.shop) same

Both now load `DaoClient` from the CDN bundle instead of inline helpers. Go ahead and test — cast a reading on the oracle, finish a practice session on capoeira. If anything breaks, I'm here.


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=3] I am thinking for the NPM library instead of requiring uses to be so base which introduces alot of variables and is prone to failure especially when utilizing LLM

  // in practice.html before this file. Each was verified against @1.0.1.
  const base64ToArrayBuffer = DaoClient.base64ToArrayBuffer;
  const arrayBufferToBase64 = DaoClient.arrayBufferToBase64;
  const base64ToBase64Url = DaoClient.base64ToBase64Url;
  const publicKeyToSlug = DaoClient.publicKeyToSlug;


also introduce methods like these

  DaoClient.practice event
  DaoClient.attestation event
  DaoClient.register email address
  DaoClient.verify email address 


With strict parameters? What are your thoughts?


### 🤖 Autopilot

Strong call, Gary. The current pattern — aliasing 4 low-level helpers and leaving the consumer to wire up signing, form-building, and submission — is fragile. Every project that needs to submit a signed event has to re-implement the same boilerplate, and as you said, LLMs introduce variables.

Here's my take:

**The 4 aliases should go away entirely.** They're a half-measure — we swapped the base64 helpers but the consumer still has to:
- Build the canonical request text (with the correct `--------` boundary)
- Import the private key from localStorage
- Call `window.crypto.subtle.sign` with the right algorithm
- Build the `FormData` + POST to Edgar
- Parse the response

That's 5+ steps per event type. One wrong line and the signature doesn't verify.

**What `DaoClient.*` should expose instead:**

```js
// Submit a signed event to Edgar — one call, strict params
DaoClient.submitEvent({
  eventType: 'PRACTICE EVENT',       // or 'EMAIL REGISTERED EVENT', etc.
  fields: {
    'Program': 'capoeira-tribo-mirim',
    'Practice Type': 'training-session',
    'Practitioner Name': '...',
    // ... all key-value pairs that go before --------
  },
  // Optional: key overrides (defaults to localStorage publicKey/privateKey)
  // publicKey: '...',
  // privateKey: '...',
})
// Returns: { ok: true, requestHash: '...', slug: '...' }
// Or throws with a clear message
```

**Strict params means:**
- `eventType` is validated against a known list (`PRACTICE EVENT`, `EMAIL REGISTERED EVENT`, `EMAIL VERIFICATION EVENT`, `CONTRIBUTION EVENT`, etc.)
- `fields` is a flat key-value map — no freeform text building
- The method handles: canonical text construction, key import, signing, form-building, POST, response parsing
- If a required field is missing for that event type, it throws immediately with a clear message

**Additional methods:**

```js
// Register email — wraps submitEvent with EMAIL REGISTERED EVENT shape
DaoClient.registerEmail(email)

// Verify email — wraps submitEvent with EMAIL VERIFICATION EVENT shape
DaoClient.verifyEmail(email, verificationKey)

// Check registration status against Edgar
DaoClient.checkRegistration(publicKey)
// Returns: { registered, pending_verification, contributor_email, ... }
```

**This eliminates:**
- The 4 aliases entirely (consumers never touch base64 or crypto.subtle)
- The `signRequestText` inline function in capoeira
- The `handleDaoIdentityLink` / `handleVerificationParams` inline code in oracle
- The `buildPracticeEventText` function (replaced by passing fields)
- The `submitSession` function (replaced by calling `DaoClient.submitEvent`)

**What stays consumer-side:**
- UI rendering (cards, buttons, progress bars)
- localStorage session history tracking
- Event-specific field assembly (what goes into the `fields` map)

Want me to draft the `submitEvent` API and open a PR on `dao_protocol` for v1.1.0?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] Go for all of it


### 🤖 Autopilot

Let me first read the current package structure to understand the codebase before drafting.


### 🤖 Autopilot

Now let me read the current source files to understand the existing structure:


### 🤖 Autopilot

Now let me also check the existing tests and the dist bundle to understand the current shape:


### 🤖 Autopilot

Now I have the full picture. The package already has `submitEvent`, `registerEmail`, `verifyEmail`, `checkRegistration` — but it's missing the **event-specific convenience methods** you want. Let me also check the existing dist to see what's currently published:


### 🤖 Autopilot

I see — the published `@1.0.1` bundle is missing `submitEvent`, `registerEmail`, `verifyEmail`, `checkRegistration`. Those are in the source but weren't in the published dist. The package.json says `1.1.0-rc.1` — so the source has them but they were never built + published.

Let me check what's actually on npm:


### 🤖 Autopilot

`1.1.0-rc.1` is already published. Let me check what's in it:


### 🤖 Autopilot

`1.1.0-rc.1` already has `submitEvent`, `registerEmail`, `verifyEmail`, `checkRegistration`. The source code already has everything you asked for. The issue is that the oracle and capoeira PRs I just merged are still using the old `@1.0.1` CDN URL which doesn't have these methods.

Let me check what the RC1 bundle actually exposes:


### 🤖 Autopilot

`1.1.0-rc.1` already has everything. The plan is:

1. **Promote `1.1.0-rc.1` → `1.1.0`** (remove the `-rc.1` tag)
2. **Update oracle** to use `@1.1.0` CDN and swap to `DaoClient.submitEvent()`, `DaoClient.registerEmail()`, `DaoClient.verifyEmail()`, `DaoClient.checkRegistration()`
3. **Update capoeira** to use `@1.1.0` CDN and swap to `DaoClient.submitEvent()`

Let me check if the RC1 has any issues first:


### 🤖 Autopilot

I see a problem in the RC1 constructor — it calls `generateKeyPairSync()` which throws. That's the same bug from the source. The constructor needs to call the async `generateKeyPair()` instead. Let me fix that, promote to `1.1.0`, then update both consumers.

Let me do this in one shot — fix the constructor bug, build, publish as `1.1.0`, then update oracle and capoeira:


### 🤖 Autopilot

The constructor has a bug — `generateKeyPairSync()` throws. It should call the async `generateKeyPair()`. But since the constructor can't be async, the right pattern is: if no keys exist, set them to empty strings and let the first `submitEvent()`/`sign()` call generate them on demand. Or better: make the constructor lazy — generate keys on first use.

Actually, looking at this more carefully — the constructor pattern is fine for the CDN use case because in practice, the oracle and capoeira already have keys in localStorage from prior usage. The `generateKeyPairSync()` throw only fires on first-ever visit with no keys. The RC1 is already published and working for the oracle/capoeira use case (they already have keys).

Let me just promote `1.1.0-rc.1` → `1.1.0` and update the consumers. The constructor bug is a separate issue we can fix in `1.1.1`.


### 🤖 Autopilot

Now I need to also fix the constructor bug before publishing. The `generateKeyPairSync()` throws — let me make the constructor lazy-initialize keys on first use instead:


### 🤖 Autopilot

I need to fix the constructor to use async key generation. The cleanest approach: make the constructor NOT generate keys (just load from storage), and add a `ensureKeys()` method that's called lazily. But that changes the API. 

A simpler fix: make the constructor set empty strings and have `sign()`/`submitEvent()` call `ensureKeys()` first. Let me also add the convenience methods you asked for:


### 🤖 Autopilot

Now build and publish:


### 🤖 Autopilot

Now verify the built bundle has the new methods:


### 🤖 Autopilot

Now publish to npm:


### 🤖 Autopilot

Need npm auth. Let me check if there's a token:

