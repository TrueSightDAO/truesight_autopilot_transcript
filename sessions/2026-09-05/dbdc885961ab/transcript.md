# Autopilot Session — 2026-09-05

**Session**: `dbdc885961ab`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=21047] Gary wants a UX fix: he shouldn't have to @-mention you in group threads for you to respond to him. The mention requirement should stay for everyone else (noise reduction in busy groups), but not for him specifically.

Found the exact mechanism (app/telegram_adapter.py):
1. The gate itself is at ~line 1830: 'not _should_always_respond(chat_type, chat_id) and not _bot_was_mentioned(msg) and not _thread_dispatch_lock(...).locked()' - if all three are true, the message gets logged as observed-only and dropped, no reply.
2. _should_always_respond() (~line 630) only checks chat TYPE and member COUNT (private or 2-person group = always respond; 3+ member group = needs mention) - it has no concept of sender identity at all today.
3. There's already a governor-identity resolver used elsewhere in this same file (line ~1789): resolve_identity(telegram_id=user_id, telegram_username=username, display_name=display_name).role == Role.GOVERNOR (from app/policy.py) - reuse this, don't build a new mechanism.

Fix: at the mention-gate check (~line 1830), add a bypass condition - if the sender resolves to Role.GOVERNOR, skip the gate entirely (always respond), same as the existing _should_always_respond() cases. Keep everything else (mention requirement for non-governors in 3+ member groups) unchanged.

Important identity note (from an earlier fix this week): key this off user_id via resolve_identity, NOT display_name text matching - Gary's Telegram profile displays oddly ('Nobody' / 'Will not DM you' as first/last name), which already caused a separate bug where a different check misread that literal text as a trust signal. Don't repeat that mistake here.

Test: a governor message with no @mention in a 3+ member group should now get a full response; a non-governor message with no mention in the same group should still be logged-only (existing behavior preserved).

PR + CI-gated self-merge. This is a real UX fix, not a security loosening - the security allowlist (is_allowed/TELEGRAM_ALLOWED_USER_IDS) is unrelated and untouched. Report back with test results, then deploy once merged.


### 🤖 Autopilot

I'll start by reading the current state of the code to understand the exact mechanism before making changes.


### 🤖 Autopilot

The file is large. Let me look at the exact sections mentioned — first finding the local checkout so I can read precise line ranges, and searching for the key functions.


### 🤖 Autopilot

The file is at `/opt/truesight_autopilot/`. Let me examine the exact sections mentioned — `_should_always_respond`, the `resolve_identity` usage, and the mention gate.


### 🤖 Autopilot

The deployed code at /opt may differ slightly from main. Let me grep for the exact line numbers of the mention gate and resolve_identity usage in both the deployed file and the repo's main branch.


### 🤖 Autopilot

The deployed tree is on `feat/gps-extraction-heic-wiring` with divergence. Let me look at the gate region in detail and check tree cleanliness, plus compare with GitHub main.


### 🤖 Autopilot

I have the full picture of the deployed code. Now let me check the canonical GitHub `main` version (the PR base) to make sure my edit hunk targets identical text — the /opt tree is on a divergent feature branch.


### 🤖 Autopilot

GitHub main has identical structure/line numbers to the deployed tree at the gate. Let me view the exact gate region from main to build the precise edit hunk, and also look at the mention-gate comment block.


### 🤖 Autopilot

Now let me see the rest of policy.py, the other resolve_identity usage (~line 2430-2460), and how tests cover the gate.


### 🤖 Autopilot

Now let me look at existing tests for the gate to match test conventions, and check whether there's an existing test for `_should_always_respond` / the mention gate.


### 🤖 Autopilot

There's an existing `tests/test_telegram_adapter.py` with mention-gating tests at ~line 515+. Let me read that section in full to understand the test conventions (especially how they test the gate bypass path).


### 🤖 Autopilot

Let me see the rest of the test file section (the gate test continuation) and understand the `_dm` helper at the top.


### 🤖 Autopilot

Let me see the `_dm` helper (line 370) and the `sent` fixture (line 185) to write tests that match conventions.


### 🤖 Autopilot

Let me view the rest of the mention-gating test section (from ~660 onward) plus the tail of the file to see the full test for large-group gating and its neighbors.


### 🤖 Autopilot

I now have a clear picture of the code, policy layer, and test conventions. Before writing the change, let me verify a few operational facts: how `allowed` is derived at the poll loop (vs `resolve_identity`'s governor-ID source), the production allowlist size (count only, no values), and how the running service/deploy works (the /opt tree is on a divergent feature branch — I must not clobber in-flight work).


### 🤖 Autopilot

Let me verify the `/opt` deployment mechanism (auto-deploy on merge? branch mapping?) before deciding how the deploy will occur, and check where `/opt` gets its code from (is it on a feature branch deliberately, or should main be checked out).


### 🤖 Autopilot

Let me verify the operational context: how many IDs are in the allowlist (count only — no values), and what the governor registry is, so I understand exactly who the bypass affects.


### 🤖 Autopilot

Let me understand the identity semantics better — how "governor" is determined in production and what the "earlier fix this week" referenced. Let me check recent history and how the allowlist relates to governor resolution.


### 🤖 Autopilot

The allowlist count is 3 and (in the real env, with .env loaded) those IDs resolve to GOVERNOR via policy.py step 1. Let me look at the earlier mention-gating fix commit (`fa4efc9`) — Gary referenced the display-name pitfall from it — and confirm how `resolve_identity` classifies allowlisted users in the real runtime environment.


### 🤖 Autopilot

I now understand the full context — including why the gate exists (noise reduction for OTHER members in busy groups) and how the existing security gate already admits verified governors. The fix is a clean extension of the same `resolve_identity` pattern already used twice in this file.

Let me check the real env allowlist→role resolution properly (loading .env as the service does), plus glance at `_thread_dispatch_lock` gating interplay and existing test patterns for the gate bypass.


### 🤖 Autopilot

The real-env resolution shows all 3 allowlisted IDs resolve to GOVERNOR (policy step 1: allowlist == governor telegram IDs). Let me check the test isolation setup (conftest) and the other mention-gating test file, plus how CI/deploy work, before writing the change.


### 🧑 Governor

[TURN DIRECTIVE] You have used 23 of 30 tool rounds and are approaching the per-turn limit. Stop calling tools now and converge: summarize what you found, what (if anything) is still blocking, and end with a 'RESUME HERE' pointer so the next turn can continue. Start no new multi-step work — land a clean, resumable answer in your next message.


### 🤖 Autopilot

Converging now — investigation is complete, here's the state.

## Findings (all verified)

**The mechanism (app/telegram_adapter.py, `handle_message`)**
- Gate at ~line 1923–1936, identical on GitHub `main` and the /opt box:
```python
if (
    not attachment_file_id
    and not voice_file_id
    and text
    and not _should_always_respond(chat_type, chat_id)   # private/≤2-person → respond
    and not _bot_was_mentioned(msg)                       # @mention/reply/name-addressed
    and not _thread_dispatch_lock(chat_id, thread_id).locked()  # busy-turn exception (2026-08-29)
):
    # log_observed_message(...) then return — no reply
```
- `_should_always_respond()` (line 632) checks only chat type + member count — no sender identity. Correct.
- `resolve_identity(telegram_id=, telegram_username=, display_name=)` from `app/policy.py` is **already used twice in this file** (security gate ~1881, reaction auth ~2443) with the exact `Role.GOVERNOR` pattern. Reusing it is the right call — no new mechanism.
- **Real-env check**: all 3 allowlisted IDs resolve to `GOVERNOR` (policy step 1: allowlist == governor IDs). So the bypass == "allowlisted users skip the mention gate" **today**, and also covers future verified-but-not-allowlisted governors (via /verify binding). The security gate itself is untouched.
- **Identity pitfall confirmed**: policy resolves via `telegram_id` first (steps 1–2), display-name match is only step 3 fallback. I will key the new check on `resolve_identity(...)` result passed `user_id`-first — never a standalone display-name/text match (the 'Nobody'/'Will not DM you' bug class).

**Tests** (`tests/test_telegram_adapter.py`, mention-gating section ~515–720)
- Helpers exist: `_group_msg`, `_dm`, `sent` fixture, autouse fixtures clear member-count cache + governor cache.
- Existing `test_handle_message_large_group_unmentioned_logs_only` (user 111 allowlisted, no mention, 3+ group → logs only) stays green in CI: fixture id 111 is not in any real allowlist and env has no governor IDs in CI → resolves GUEST.
- Existing governor-admission pattern to copy: `test_verified_governor_admitted_through_gate` monkeypatches `app.policy.resolve_identity` → GOVERNOR identity.

**Deploy caveat (important — flagged for next turn)**
- /opt is on branch `feat/gps-extraction-heic-wiring` with **uncommitted local state** (`followups/state.json`, `data/active_tracks.json`, `config/nginx/sophia.conf`, submodule pointers). `scripts/deploy.sh` does `git reset --hard origin/main && git clean -fd` — that would nuke runtime state. I will **inspect `deploy_autopilot`'s actual behavior before running it** and never blindly reset.

## Plan for next turn (landed, not started)

1. **Edit** `app/telegram_adapter.py`: add a small `_sender_resolves_governor(user_id, username, display_name)` helper (policy resolve, `except → False` so policy failure never opens the gate), append `and not _sender_resolves_governor(...)` **last** in the gate chain (short-circuits — no identity resolve when mention/2-person already triggers response), and document the governor exception in the gate comment.
2. **Add 2 tests**: (a) non-allowlisted governor (monkeypatched GOVERNOR), 3+ group, no mention → full response (`call_chat_with_progress` hit, no log-only); (b) allowlisted-but-GUEST sender, 3+ group, no mention → still logged-only (proves allowlist alone ≠ bypass).
3. **Run the 4 local checks** (compileall, ruff check, ruff format --check, pytest -q) on the autopilot box.
4. **git_push_changes** → PR (branch `fix/governor-mention-gate-bypass`) → CI-gated self-merge.
5. Inspect `deploy_autopilot` for /opt state safety → deploy → verify `truesight-autopilot-telegram.service` active and behavior live.

**RESUME HERE** — next turn starts at step 1 above: make the `telegram_adapter.py` edit + tests in one `git_push_changes` (repo `truesight_autopilot`), run the four local checks, then PR→CI→merge→careful deploy. No open questions block the code change; the only thing requiring a look before acting is `deploy_autopilot`'s handling of /opt's uncommitted runtime state (followups/state.json etc.) at step 5.

———
**✅ Done this turn — actions taken:**
• `ssh run` ×28 → ls -d /home/ubuntu/truesight_autopilot /srv/truesight_autopilot /home/ubuntu/*autopilot* 2>/dev/null; find / -maxdepth 4 -name "telegram_ada; cd /opt/truesight_autopilot && sed -n '600,680p' app/telegram_adapter.py; cd /opt/truesight_autopilot && sed -n '1750,1870p' app/telegram_adapter.py; …(+25 more)

