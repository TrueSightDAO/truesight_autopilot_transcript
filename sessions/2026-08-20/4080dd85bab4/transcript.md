# Autopilot Session — 2026-08-20

**Session**: `4080dd85bab4`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=12111] I'm thinking there's some problem with the newly released auto-advanced feature in yourself to get pulled from the main branch and then figure out why when you like auto-advanced at some point you start picking up tasks from other threats that is not supposed to be in this threat. Find out the root cause of this reason and then get back to me. So every Sophia's threat should just be standalone and should not auto-advanced accidentally start picking up tasks from other threats. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Found the plan file. Let me dig into it and the actual code.


### 🤖 Autopilot

Let me read the rest of the plan and look at the actual implementation in truesight_autopilot.


### 🤖 Autopilot

PR #307 "feat: auto-advance through PR merges and UAT (run-to-UAT mode)" merged 2026-08-20 — that's the newly-released feature. Let me look at the actual implementation on main.


### 🤖 Autopilot

The nested output is truncating. Let me read the files directly from disk.


### 🤖 Autopilot

The file keeps truncating. Let me read it in chunks directly via shell.


### 🤖 Autopilot

Now let me look at the adapter's auto-advance loop and how it's keyed to threads.


### 🤖 Autopilot

Now the brain side — where the `advance` signal is computed and which plan it reads. That's the crux of the cross-thread question.


### 🤖 Autopilot

Now I see the shape of it. Let me check how the "active handoff" context block is injected (per-thread vs global), plus the PR #307 diff to see exactly what shipped.


### 🤖 Autopilot

Now the key part — how the handoff context and plan are resolved per thread, and what the brain sees globally. Let me read the adapter's handoff-resolution code.


### 🤖 Autopilot

Let me look at the brain's history/session keying and the context injection — that's where cross-thread bleed would live.


### 🤖 Autopilot

Now let me check how the handoff prefix is applied to messages and confirm the deployment flags.


### 🤖 Autopilot

The auto-advance is ON (both flags true). Now let me check the session keying and how history/queues are scoped — the cross-thread bleed suspects.


### 🧑 Governor

[TURN DIRECTIVE] You have used 23 of 30 tool rounds and are approaching the per-turn limit. Stop calling tools now and converge: summarize what you found, what (if anything) is still blocking, and end with a 'RESUME HERE' pointer so the next turn can continue. Start no new multi-step work — land a clean, resumable answer in your next message.


### 🤖 Autopilot

I've found the root cause. Let me land the diagnosis now.

## What shipped (the "newly released" feature)

- **PR #307** (merged 2026-08-20, commit `9ab6121`): *"feat: auto-advance through PR merges and UAT (run-to-UAT mode)"* — already deployed on this box, and both flags are **ON** in `.env`: `AUTO_ADVANCE=true` and `AUTO_ADVANCE_UNTIL_UAT=true`.
- It removed "merge to main/master" from the always-stop gates (Sophia now merges her own PRs and keeps going), and added run-to-UAT mode.

## Root cause — two compounding bugs in `_compute_advance_signal` (app/main.py)

1. **Generic fallback fires on ANY thread, not just handoff/plan threads.** When a thread has no plan file, the code does: *"if a PR was opened → return `{decision: auto, next_unit: "the next PR", plan: None}`"*. So a normal chat thread where Sophia opens any fix PR now auto-advances, even though there's no roadmap to scope it. The design (SOPHIA_AUTO_ADVANCE_PLAN.md §3) was that auto-advance only runs on plan/handoff threads; this fallback (widened further by #307 to accept `open_pr`/`merge_pr`) removed that scoping.

2. **run-to-UAT mode counts ANY tool call as "progress":** `if settings.auto_advance_until_uat and not opened_pr: opened_pr = bool(tool_trace)` — so even a turn that only did a read/`ssh_run`/lookup auto-advances. The loop can never settle.

**Why it picks up tasks from other threads:** the continue message is `"[AUTO-ADVANCE] Execute only the next unit (the next PR). Open and merge the next fix PR yourself…"` with **`plan: None`** — no plan pointer, no handoff prefix re-injection (`_handoff_prefix` is only applied to the *original* dispatch, not to the synthetic auto-advance message). The brain then has to guess what "the next PR" is, and its ambient context contains *every* plan in agentic_ai_context → it resolves to units from other plans/threads. Combined with per-thread parallel dispatch locks, an unscoped auto-advance in one topic bleeds into another topic's work.

## Fix (proposed, not yet opened)

- **Fail closed:** emit no auto signal unless a `plan_file` is found (handoff threads only) — restore "no RESUME HERE pointer → gate".
- In run-to-UAT mode, count only PR-opening/merging/UAT-test tools as progress, not *any* tool.
- Re-inject `_handoff_prefix(thread_id, …)` + plan ref into the auto-advance continue message so every synthetic turn is scoped to its own thread's plan.

**RESUME HERE:** open a fix PR in `truesight_autopilot` (branch e.g. `fix/auto-advance-thread-scoping`) implementing the three changes above with tests (`tests/test_auto_advance_signal.py`), run the local test suite (compileall → ruff → ruff format → pytest), then report the PR URL. Note: `truesight_autopilot` PRs are human-merged per the own-repo gate — I'll open, you merge.

———
**✅ Done this turn — actions taken:**
• `ssh run` ×22 → cd /root 2>/dev/null; ls -la; find / -maxdepth 3 -name "truesight_autopilot" -type d 2>/dev/null | head; ls ~ 2>/dev/null; cd /opt/truesight_autopilot && git log --oneline -30 && echo "---BRANCH---" && git branch -a && echo "---STATUS---" && git status; cd /opt/truesight_autopilot && grep -rn "auto.advance\|auto_advance\|AUTO_ADVANCE\|advance_after\|run-to-UAT\|run_to_uat" --include="*.py" -; …(+19 more)

