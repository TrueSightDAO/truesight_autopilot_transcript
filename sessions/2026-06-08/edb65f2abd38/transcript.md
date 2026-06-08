# Autopilot Session — 2026-06-08

**Session**: `edb65f2abd38`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

go for it


### 🤖 Autopilot

Morning, Gary. Ready to go. What's on the agenda?


### 🧑 Governor

This 📡 Oracle CDN re-wire — PR1 kickoff

Context: @truesight_dao/dao-client@1.0.0 is PUBLISHED and CDN-live (unpkg + jsDelivr both 200; global `DaoClient`). The oracle is currently inline after the 2026-06-08 hotfix (#40) reverted the broken #38/#39 CDN refactor (unpublished package → 404) and #36's syntax errors.

Plan read: ORACLE_CDN_REWIRE_PLAN.md (latest commit c3bf913). Hard guards confirmed:
- ✅ CDN URL https://unpkg.com/@truesight_dao/dao-client@1.0.0/dist/dao-client.min.js returns HTTP 200
- ✅ Pin @1.0.0 (no floating tag)
- ✅ node --check on every changed JS + extracted inline <script> before merge
- ✅ Map each inline helper to DaoClient.* before deleting
- ✅ Preserve canonical-signing fix, 3-state identity UX, SW kill-switch
- ✅ Every commit carries Generated-by: Sophia (TrueSight Autopilot) trailer

Starting PR1 now: add the verified CDN <script> tag to index.html, replace inline DAO-client helpers with DaoClient.* where the package matches exactly, preserve all 2026-06-08 fixes.


### 🤖 Autopilot

Let me start by reading the plan and the current state of the code.


### 🤖 Autopilot

Good — I have the full plan and the current `index.html`. Now let me check what `DaoClient` exposes so I know exactly which inline helpers map to package methods.


### 🤖 Autopilot

Now let me check what internal modules the `DaoClient` uses to understand exactly what inline helpers it replaces:


### 🤖 Autopilot

Now I have a complete picture. Let me analyze the inline code in `index.html` against what `DaoClient` provides:

**Inline helpers in index.html that map to DaoClient:**

1. **`base64ToArrayBuffer`** → `DaoClient.base64ToArrayBuffer()` ✓
2. **`arrayBufferToBase64`** → `DaoClient.arrayBufferToBase64()` ✓
3. **`base64ToBase64Url`** → `DaoClient.base64ToBase64Url()` ✓
4. **`publicKeyToSlug`** → `client.getSlug()` or `DaoClient.publicKeyToSlug()` (static) ✓
5. **Key generation** → `new DaoClient()` auto-generates on construction ✓
6. **Signing** → `client.sign()` / `client.submit()` ✓
7. **Storage** → `DaoClient` handles via `StorageManager` with prefix `truesight_dao_` — but the oracle uses `publicKey`/`privateKey` keys (no prefix). Need to check compatibility.

Wait — the oracle stores keys as `publicKey` and `privateKey` (bare, no prefix). The `DaoClient` uses `truesight_dao_public_key` / `truesight_dao_private_key`. This is a **storage key mismatch**. The oracle's existing keys won't be found by `DaoClient` unless we handle this.

Let me check the oracle's storage keys more carefully:

The oracle uses:
- `localStorage.getItem('publicKey')` and `localStorage.getItem('privateKey')`

The DaoClient uses:
- `truesight_dao_public_key` and `truesight_dao_private_key`

This means if I just swap to `new DaoClient()`, existing oracle users will lose their keys. I need to either:
1. Pass a custom `storagePrefix: ''` to match the oracle's bare keys, OR
2. Keep the inline storage helpers and only replace the crypto/payload/edgar parts

Let me also check what the `DaoClient` constructor does with the storage prefix — if I pass `storagePrefix: ''`, the keys become `public_key` and `private_key`, not `publicKey`/`privateKey`. So that won't match either.

The cleanest approach: keep the oracle's existing storage helpers (they're simple getItem/setItem calls) and only replace the crypto/signing/payload helpers with `DaoClient.*` static methods. The `DaoClient` constructor auto-generates keys which we don't want — we want to keep the oracle's existing lazy key-gen pattern.

Let me map exactly what to replace:

**Replace with `DaoClient.*` static methods:**
- `base64ToArrayBuffer` → `DaoClient.base64ToArrayBuffer`
- `arrayBufferToBase64` → `DaoClient.arrayBufferToBase64`
- `base64ToBase64Url` → `DaoClient.base64ToBase64Url`
- `publicKeyToSlug` → `DaoClient.publicKeyToSlug` (static — need to check if it's exposed as static... it's an instance method on `CryptoUtils`, not static on `DaoClient`)

Actually, looking at the `DaoClient` class more carefully:
- `DaoClient.arrayBufferToBase64` — static ✓
- `DaoClient.base64ToArrayBuffer` — static ✓
- `DaoClient.base64ToBase64Url` — static ✓
- `DaoClient.generateKeyPair` — static ✓
- `publicKeyToSlug` — instance method only, not static

For `publicKeyToSlug`, the oracle calls it as `publicKeyToSlug(pub)` which is a local function. The `DaoClient` exposes it as `client.getSlug()` (instance) or via `CryptoUtils` internally. Since we're keeping the oracle's key storage pattern (not using `new DaoClient()`), we'd need to either:
1. Keep the inline `publicKeyToSlug` function (it's small — just SHA-256 hash + base64url)
2. Or instantiate a `DaoClient` just for the slug

Let me keep the inline `publicKeyToSlug` since it's small and the `DaoClient` doesn't expose it as a static. The key replacements are:

1. **Add CDN `<script>` tag** for `@truesight_dao/dao-client@1.0.0`
2. **Replace `base64ToArrayBuffer`** → use `DaoClient.base64ToArrayBuffer`
3. **Replace `arrayBufferToBase64`** → use `DaoClient.arrayBufferToBase64`
4. **Replace `base64ToBase64Url`** → use `DaoClient.base64ToBase64Url`
5. **Keep `publicKeyToSlug`** inline (no static equivalent)
6. **Keep storage helpers** inline (key name mismatch)
7. **Keep the signing/verification logic** inline (it uses the storage keys directly)

Actually, let me re-examine. The signing logic in the oracle uses `window.crypto.subtle.importKey` and `window.crypto.subtle.sign` directly — these are the same underlying operations that `DaoClient.crypto.sign()` does. But the oracle's signing code is interleaved with its specific payload format (the `requestText` with `[EMAIL REGISTERED EVENT]` etc). The `DaoClient.submit()` uses a generic `PayloadBuilder` format.

The plan says: "replace inline DAO-client helpers with DaoClient.* only where the package matches exactly". So I should replace the **utility functions** (base64 encode/decode, base64url) that have exact static equivalents, and keep the oracle-specific logic (signing flow, storage, key gen, slug) as-is since those are oracle-specific.

Let me now create the PR.


### 🤖 Autopilot

Now I have the full picture. Let me also verify the CDN URL works:


### 🤖 Autopilot

CDN URL returns 200. Now let me also check the jsDelivr equivalent:


### 🤖 Autopilot

Both CDNs return 200. Now let me create the PR. Here's my analysis of what to change:

**Replacements in `index.html`:**

1. **Add CDN `<script>` tag** for `@truesight_dao/dao-client@1.0.0` (unpkg with jsDelivr fallback comment)
2. **Replace `base64ToArrayBuffer`** → `DaoClient.base64ToArrayBuffer` in the inline `<script>` block
3. **Replace `arrayBufferToBase64`** → `DaoClient.arrayBufferToBase64` in the inline `<script>` block
4. **Replace `base64ToBase64Url`** → `DaoClient.base64ToBase64Url` in the inline `<script>` block

**Replacements in `assets/js/oracle-draw-submit.js`:**
5. **Replace `base64ToArrayBuffer`** → `DaoClient.base64ToArrayBuffer`
6. **Replace `arrayBufferToBase64`** → `DaoClient.arrayBufferToBase64`
7. **Replace `base64ToBase64Url`** → `DaoClient.base64ToBase64Url`

**Keep inline:**
- `publicKeyToSlug` — no static equivalent on `DaoClient`
- Storage helpers — key name mismatch (`publicKey` vs `truesight_dao_public_key`)
- Key generation — oracle uses its own lazy pattern
- Signing — oracle-specific payload format
- All oracle-specific logic (identity linking, QMDJ, advisory, etc.)

Let me also check if the `DaoClient` static methods are actually exposed on the global. The esbuild IIFE uses `--global-name=DaoClient`, so `DaoClient.arrayBufferToBase64` etc. should work as static methods on the class.

Let me verify by checking the built output:


### 🤖 Autopilot

The minified bundle confirms `DaoClient.arrayBufferToBase64`, `DaoClient.base64ToArrayBuffer`, and `DaoClient.base64ToBase64Url` are all exposed as static methods on the global `DaoClient`. 

Now let me create the PR. I need to:

1. Add the CDN `<script>` tag to `index.html` (before the existing scripts, so `DaoClient` is available)
2. Replace the three base64 helpers in the inline `<script>` block of `index.html`
3. Replace the three base64 helpers in `assets/js/oracle-draw-submit.js`


### 🤖 Autopilot

**PR1 is open** → [#42](https://github.com/TrueSightDAO/oracle/pull/42)

Here's what was done:

### Changes

**`index.html`**
- Added CDN `<script>` tag for `@truesight_dao/dao-client@1.0.0` (unpkg primary, jsDelivr comment) — placed before `hexagram_texts.js` so `DaoClient` global is available to all downstream scripts
- Replaced 3 inline base64 helpers with `DaoClient.*` static calls:
  - `base64ToArrayBuffer` → `DaoClient.base64ToArrayBuffer`
  - `arrayBufferToBase64` → `DaoClient.arrayBufferToBase64`
  - `base64ToBase64Url` → `DaoClient.base64ToBase64Url`

**`assets/js/oracle-draw-submit.js`**
- Same 3 replacements

### What stayed inline (intentionally)
| Helper | Reason kept |
|---|---|
| `publicKeyToSlug` | No static equivalent on `DaoClient` (instance method only) |
| Storage keys (`publicKey`/`privateKey`) | DaoClient uses `truesight_dao_` prefix — changing would break existing users' keys |
| Key generation | Oracle's lazy-gen pattern differs from DaoClient's constructor auto-gen |
| Signing flow | Oracle-specific payload format (`[EMAIL REGISTERED EVENT]`, `[PRACTICE EVENT]`) |

### Hard guard status
| Guard | Status |
|---|---|
| CDN URL HTTP 200 | ✅ Verified |
| jsDelivr HTTP 200 | ✅ Verified |
| Pin `@1.0.0` | ✅ No floating tag |
| `node --check` before merge | ⏳ Run before merging |
| Preserved 2026-06-08 fixes | ✅ Canonical signing, 3-state UX, SW kill-switch all untouched |
| `Generated-by:` trailer | ✅ On commit |

Ready for review. Want me to run `node --check` on the changed files now?


### 🧑 Governor

yeah. Give it a shot


### 🤖 Autopilot

`oracle-draw-submit.js` clean. Now extract the inline `<script>` from `index.html`:


### 🤖 Autopilot

All clean. Summary:

| File | `node --check` |
|---|---|
| `assets/js/oracle-draw-submit.js` | ✅ OK |
| `index.html` (inline `<script>`) | ✅ OK |

Both pass. The PR is ready to merge whenever you give the word.


### 🧑 Governor

just merge it


### 🤖 Autopilot

**PR1 merged** → `oracle@main` (176eac6).

The CDN `<script>` tag for `@truesight_dao/dao-client@1.0.0` is live on `main` — next deploy to `oracle.truesight.me` will pick it up. Want me to record the DAO contribution and move to PR2 (dapp parity)?

