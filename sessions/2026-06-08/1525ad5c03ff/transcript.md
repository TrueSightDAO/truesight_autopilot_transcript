# Autopilot Session — 2026-06-08

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=3] You there?


### 🤖 Autopilot

Yes, I'm here, Gary. What do you need?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] What is the current thread_id?


### 🤖 Autopilot

The current thread_id is **3**.


### 🧑 Governor

Consolidated handoff for ALL @truesight_dao/dao-client integration fixes — this thread (3) is now the single coordination tracker. FIRST refresh your repo view, then read agentic_ai_context/DAO_CLIENT_INTEGRATION_FIXES.md via read_repo_file (GitHub main). Post a kickoff here confirming you've read it and restating the sequence. SUMMARY of what it consolidates: Root cause — @truesight_dao/dao-client@1.0.0's browser global is the module namespace, so DaoClient.base64ToArrayBuffer is undefined (broke oracle prod twice). Issue 1 (BLOCKER, topic 1638): republish @1.0.1 with window.DaoClient = the class + a RUNTIME smoke test that loads the actual bundle and asserts the global shape (node --check cannot catch this). Issue 2 (oracle, topic 1638, currently reverted to working inline): re-do the CDN adoption against @1.0.1, fix load order (no blind defer), preserve canonical-signing + 3-state identity UX + SW kill-switch. Issue 3 (capoeira, topic 1658, parked): swap practice-event-submit.js generic helpers to DaoClient.*, keep buildPracticeEventText/submitSession/backfillUnsent/getCvUrl inline. SHARED Definition of Done for every consumer swap: depend on @1.0.1 + pin + verify unpkg 200 in-PR; runtime smoke test (not node --check); correct load order; map-each-helper-before-deleting; preserve consumer-specific logic; OPEN PR but DO NOT auto-merge (both deploy from main, report here for local review first); Generated-by: Sophia trailer on every commit + PR. SEQUENCE: Issue 1 first (it unblocks 2 and 3); then 2 and 3 in parallel, each its own reviewed PR. Keep detailed work in 1638/1658 if you like, but report consolidated status here in thread 3. Reply with your understanding + current state (you're working Issue 1 in 1638, with 2 and 3 parked).


### 🤖 Autopilot

Let me refresh my view and read the consolidated plan.


### 🤖 Autopilot

Got it. Here's my understanding and current state:

---

## Confirmed — I've read the consolidated plan from GitHub `main`

**Root cause:** `@truesight_dao/dao-client@1.0.0`'s esbuild `--global-name=DaoClient` wraps the module namespace, not the class. So `window.DaoClient.base64ToArrayBuffer` is `undefined` — the class is at `DaoClient.DaoClient`. Broke oracle prod twice.

### Sequence (as documented):

| # | Unit | Repo | Topic | Status |
|---|------|------|-------|--------|
| **1** 🔴 | **Package `@1.0.1`** (fix global + runtime smoke test + republish) | `dao_protocol` | **1638** | **→ Working now** |
| 2 ⏸ | Oracle CDN re-integration against `@1.0.1` | `oracle` | 1638 | Parked until Issue 1 lands |
| 3 ⏸ | Capoeira swap against `@1.0.1` | `capoeira` | 1658 | Parked until Issue 1 lands |

### Shared DoD for every swap:
1. Pin `@1.0.1+` + verify unpkg 200 in-PR
2. Runtime smoke test (load actual bundle, assert global shape + sign round-trip)
3. Correct load order (no blind `defer`)
4. Map each helper before deleting
5. Preserve consumer-specific logic
6. Open PR, **do NOT auto-merge** — report here for local review first
7. `Generated-by: Sophia (TrueSight Autopilot)` on every commit + PR

### Current state:
- **I am working Issue 1** (package fix in `dao_protocol`, topic 1638)
- Issues 2 and 3 are **parked** — they proceed in parallel once `@1.0.1` is published and verified

This thread (3) is the single status tracker. I'll report progress here and keep detailed work in 1638. Ready to proceed with Issue 1.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] Did Claude already handed off to you?


### 🤖 Autopilot

No, there's been no handoff from Claude to me on this. The `DAO_CLIENT_INTEGRATION_FIXES.md` file exists on GitHub `main` with the plan, but I haven't received any prior work-in-progress, branch, PR, or partial fix from Claude (or any other agent) on Issue 1.

I'm starting from a clean slate on `dao_protocol` — I'll read the current state of the package build files and go from there. Shall I begin?

