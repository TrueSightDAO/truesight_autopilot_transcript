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


### 🧑 Governor

Stop investigating column layouts — you have enough. Here is everything you need:

- Column **AU** = sum of logged warmup sends per row (numeric, populated by `sync_email_agent_followup.py` via `Email Agent Follow Up` tab).
- Column **AV** = sum of logged follow-up sends per row (same source).
- The `Email Agent Follow Up` tab has a `last_send_at` timestamp column you can read to compute "warmup sent > 14 days ago".
- Status column is column **A** of the `Hit List` tab.
- The new `warmup-aged-out` subcommand should mirror the structure of the existing `email-to-warmup` subcommand in `scripts/hit_list_promote_status.py` — same gspread/dotenv loaders, same `--limit` + `--dry-run` flags, plus a new `--age-days` (default 14).
- Default `--limit 10`, default `--age-days 14`.
- Predicate to advance a row: status == `AI: Warm up prospect` AND AU >= 1 AND AV == 0 AND most-recent warmup send timestamp older than `--age-days` days.
- Target status to write: `Manager Follow-up`.

**Now open the two draft PRs using `open_fix_pr`. No more reads. Both must be DRAFT.**

PR 1 — repo `go_to_market`:
- Add `warmup-aged-out` subcommand to `scripts/hit_list_promote_status.py` with the predicate above.
- Add a workflow step (commented-out / `if: false` initially so Gary opts in) at `:40 * * * *` in `.github/workflows/hit_list_status_promote.yml`.
- Title: `feat(hit_list): warmup-aged-out promotion to Manager Follow-up`
- Body must include: rationale ("78 stores stuck in Warm-up, 26 over-warmed, no aged-out path"), the 14-day default with reasoning, the AU>=1 / AV==0 guard so we never promote a row that never got a warmup, and a TODO note that the workflow step is gated until first dry-run output is reviewed.

PR 2 — repo `agentic_ai_context`:
- Update `HIT_LIST_STATE_MACHINE.md`:
  - TL;DR section — add the new transition.
  - Mermaid chart — add `Warmup --> ManagerFollowup: aged-out (>14d, no reply, AU>=1)`.
  - "From `AI: Warm up prospect`" transitions table — add a third row for the aged-out trigger.
  - Cron schedule table — add a `:40` row for the new workflow step.
  - Anti-patterns — replace "stays as Warmup forever" with the new aged-out behaviour.
- Title: `docs(hit_list): document Warm-up → Manager Follow-up aged-out transition`
- Body: short, links to PR 1.

If `open_fix_pr` lacks repo write access for either repo, **also** open a third draft PR to `truesight_autopilot` extending the allowlist or adding the missing capability.

Output the PR URLs only. Do not summarise the diffs.


### 🤖 Autopilot

Let me open both draft PRs now.


### 🤖 Autopilot

As I suspected — `open_fix_pr` doesn't have `go_to_market` in its allowed repo list. I need to extend the autopilot first. Let me check the current allowlist.


### 🤖 Autopilot

<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="read_repo_file">
<｜｜DSML｜｜parameter name="path" string="true">open_fix_pr.py</｜｜DSML｜｜parameter>
<｜｜DSML｜｜parameter name="ref" string="true">main</｜｜DSML｜｜parameter>
<｜｜DSML｜｜parameter name="repo" string="true">truesight_autopilot</｜｜DSML｜｜parameter>
</｜｜DSML｜｜invoke>
</｜｜DSML｜｜tool_calls>


### 🧑 Governor

PR #103 was opened but is incomplete (only +1 line) and not draft — that is fine, treat it as the doc placeholder. Root cause of the `go_to_market` failure: the allowlist in `app/config.py:34` of `truesight_autopilot` lists the **local clone name** `market_research`, but the **actual GitHub repo** is `go_to_market`. PROJECT_INDEX.md flags this mismatch explicitly: "GitHub (automation source): TrueSightDAO/go_to_market — clone name may differ locally (content_schedule, etc.)".

**Open exactly one more PR — a self-extension PR — using `open_fix_pr` against `truesight_autopilot`.**

Required edit: in `app/config.py`, in the `allowed_repos` list, **add `"go_to_market"` to the list** (do NOT remove `market_research` — keep it for back-compat). The relevant snippet you'd be touching:

```
    allowed_repos: list[str] = [
        "dapp", "tokenomics", "truesight_me", "truesight_me_prod",
        "agroverse_shop", "agroverse_shop_prod", "dao_client",
        "market_research", "sentiment_importer", "truesight_autopilot",
        "agentic_ai_context",
    ]
```

becomes:

```
    allowed_repos: list[str] = [
        "dapp", "tokenomics", "truesight_me", "truesight_me_prod",
        "agroverse_shop", "agroverse_shop_prod", "dao_client",
        "market_research", "go_to_market", "sentiment_importer",
        "truesight_autopilot", "agentic_ai_context",
    ]
```

Title: `fix(allowlist): add go_to_market to allowed_repos`
Body: short — explain that `market_research` is the local clone name but the canonical GitHub repo is `go_to_market` (per PROJECT_INDEX.md), so the autopilot was unable to open fix PRs against the hit-list automation. Note that after this merges + redeploys, the `feat(hit_list): warmup-aged-out` change can be opened against `go_to_market` in a follow-up turn.

Output ONLY the PR URL on a single line. No explanation, no diff summary.


### 🤖 Autopilot

https://github.com/TrueSightDAO/truesight_autopilot/pull/19

