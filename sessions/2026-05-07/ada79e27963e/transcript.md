# Autopilot Session — 2026-05-07

**Session**: `ada79e27963e`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Fix the routes.js probe reload on localhost. When the DApp is served from localhost:8080, the no-cors probe to script.google.com always fails, triggering window.location.reload(). This creates a reload loop when combined with pages that have query params like create_signature.html?em=...&vk=...

Fix: in dapp/routes.js, skip the probe entirely when window.location.hostname is localhost or 127.0.0.1. Add a guard before the probe fires. Also skip the probe if in a ServiceWorker context (typeof window === 'undefined').

Open a DRAFT PR on the dapp repo with this fix."


### 🤖 Autopilot

Let me first read the relevant file to understand the current code.


### 🤖 Autopilot

I can see the issue clearly. The probe fires on `localhost` because there's no guard for it. Let me open the fix PR.


### 🤖 Autopilot

Done. Here's the summary:

**PR #213** → https://github.com/TrueSightDAO/dapp/pull/213

**What it fixes**: The `no-cors` probe to `script.google.com` fires on every page load in `direct` mode. On `localhost:8080`, it always fails (no CORS, no network route), which triggers `window.location.reload()`. This creates an infinite reload loop — especially destructive on pages like `create_signature.html?em=...&vk=...` where query params get lost or cause re-triggering.

**The fix**: Two guards added inside the `if (isWindow && mode === 'direct')` block, before the probe fires:

1. **Localhost guard** — if `hostname` is `localhost` or `127.0.0.1`, skip the probe entirely. Developers can manually pass `?route=proxy` if they need to test proxy mode.
2. **ServiceWorker guard** — already handled by the existing `isWindow` check, but the localhost guard sits inside that same block so it's clean.

It's a DRAFT PR — review and merge at your discretion.

