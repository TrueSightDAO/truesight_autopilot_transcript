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

