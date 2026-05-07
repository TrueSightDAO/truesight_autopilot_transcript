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

