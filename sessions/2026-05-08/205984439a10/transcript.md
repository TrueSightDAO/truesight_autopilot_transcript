# Autopilot Session — 2026-05-08

**Session**: `205984439a10`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

## Task: fix the Hit List "warm-up dead-end" bug — open draft PR(s) only

### Evidence the pipeline is genuinely stuck (from 2026-05-06 ADVISORY_SNAPSHOT)

- 78 stores in `AI: Warm up prospect`, 49 with no warmup ever sent, **26 with ≥2 warmups and zero follow-ups**.
- 7 stores in `AI: Prospect replied`, **all 7 with zero follow-up sends logged**.

### Root-cause (not a code bug — a STATE-MACHINE GAP)

Read `read_context_file("HIT_LIST_STATE_MACHINE.md")`. Line ~62 explicitly documents:

> `Warmup --> [*]: no reply, stays as Warmup`

There is **no aged-out transition out of Warm-up** when the prospect doesn't reply. So warm-up drafts keep stacking on the same 26 rows instead of advancing them to `Manager Follow-up` where `suggest_manager_followup_drafts.py` would pick them up. This is an intentional design decision that has now become a pipeline blocker.

### Fix to implement (open as **draft PRs**, do not merge)

Gary's preferred path (he debated `Warm-up → Prospect replied → Manager Follow-up` and self-corrected to **direct → Manager Follow-up** for the no-reply case):

1. Add a new transition: **`AI: Warm up prospect` → `Manager Follow-up`** when ALL of:
   - col AU (sum logged warmup sends) ≥ 1
   - last warmup send was > **14 days** ago (configurable via `--age-days`)
   - col AV (sum logged follow-ups) = 0
   - status is still `AI: Warm up prospect` (no inbound reply)

   The `Warm-up → Prospect replied` transition (reply detection) stays exactly as-is — keep that as a separate, higher-signal trigger.

2. Implementation surfaces (touch BOTH repos):

   **`TrueSightDAO/go_to_market`** (cloned locally as `market_research/`):
   - Add a third subcommand `warmup-aged-out` to `scripts/hit_list_promote_status.py` next to the existing `shortlisted-to-enrich` and `email-to-warmup`. Mirror their argparse / dry-run / limit conventions.
   - Add a cron step to `.github/workflows/hit_list_status_promote.yml` (or a new workflow file). Suggested cadence: `:40 * * * *` so it slots between the existing `:35` enrich cron and the `:50` qualification cron.
   - Update `HIT_LIST_CREDENTIALS.md` if any new env var is needed (probably none — reuse the existing service account).

   **`TrueSightDAO/agentic_ai_context`**:
   - Update `HIT_LIST_STATE_MACHINE.md` to document the new transition: TL;DR, mermaid chart, `From AI: Warm up prospect` table (add the new row), Cron schedule table (add `:40` row), and Anti-patterns (replace "stays as Warmup forever" with the new aged-out behaviour).

3. **Safety constraints — must hold:**
   - PRs must be opened as **draft**. Do not merge.
   - Do NOT promote rows where AU = 0 — those need a first warmup, not a follow-up.
   - Default `--age-days 14`, default `--limit 10` (small batches; first run is high-stakes).
   - First production cron should be commented-out / behind `if: false` so Gary opts in by uncommenting after reviewing the first dry-run output.

### If you can't directly fix this — extend yourself

If `open_fix_pr` lacks the ability to operate on `go_to_market` or `agentic_ai_context`, OR if you need a tool that doesn't exist yet, open a **separate** draft PR to `TrueSightDAO/truesight_autopilot` that adds whatever capability is missing (new tool in `app/tools/`, expanded `open_fix_pr` repo allowlist, etc.) — then state in your reply that the autopilot self-extension PR must be merged + redeployed before the original fix can land. Do not try to bypass missing capability with hacks.

### Output I want from you

1. A short diagnosis paragraph confirming the state-machine-gap reading (or correcting me if you see it differently).
2. The list of PR URLs you opened, draft status, repo names.
3. If you couldn't open a PR, state exactly what tool/permission is missing so a follow-up extension PR can be scoped.

Begin.


### 🤖 Autopilot

Let me start by reading the state machine documentation to confirm the gap.


### 🤖 Autopilot

Now let me look at the existing `hit_list_promote_status.py` to understand the subcommand pattern, and check the workflow file.


### 🤖 Autopilot

The `market_research` repo redirects. Let me check the actual repo name — from the context, `market_research/` maps to `TrueSightDAO/content_schedule`. Let me also look for the `go_to_market` repo which is mentioned as the actual repo for the hit list scripts.


### 🤖 Autopilot

Found it — `go_to_market` is the repo. Let me read the promote script and workflow from there.


### 🤖 Autopilot

Now let me check the column layout to understand column AU (warmup sends) and AV (follow-ups):


### 🤖 Autopilot

Now I have a clear picture. Let me check the column layout — I need to confirm which columns are AU (warmup sends) and AV (follow-ups) in the Hit List sheet.

<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="read_repo_file">
<｜｜DSML｜｜parameter name="repo" string="true">go_to_market</｜｜DSML｜｜parameter>
<｜｜DSML｜｜parameter name="path" string="true">scripts/sync_email_agent_followup.py</｜｜DSML｜｜parameter>
</｜｜DSML｜｜invoke>
</｜｜DSML｜｜tool_calls>

