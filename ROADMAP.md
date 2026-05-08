# ROADMAP.md — Provider abstraction + usage logging

This document describes the phased plan for two intertwined initiatives:

1. **Provider abstraction** — a single interface in `truesight_autopilot` that fronts every LLM provider (DeepSeek, BigModel, Kimi, Grok, Gemini, …) so call sites don't care which one is in use.
2. **Usage logging** — an audit trail in *this repo* (`truesight_autopilot_transcript`) recording every LLM call's tokens / cost / caller / latency, so humans (and future LLMs) can review spend by provider, model, or subsystem.

The two are coupled: the provider ABC is the natural place to emit the usage record. The plan below decouples landing them so neither phase risks breaking production.

---

## Guiding principles

1. **No phase deletes or renames anything that's running** until the next phase has soaked in production.
2. **Each phase is independently revertable** by `git revert` of a single PR.
3. **The default behaviour is unchanged** until an env flag is explicitly flipped (Phase 4+).
4. **Documentation lands before code.** That's why this file (and `AGENTS.md`, `SCHEMA.md`, `PROVIDERS.md`) exists in Phase 0.
5. **Backwards-compat shims stay** until grep proves there are zero callers (Phase 6).

---

## Phase 0 — Documentation only ✅ (this PR)

**Repos affected:** `truesight_autopilot_transcript`, `truesight_autopilot/docs/`.

**Deliverables:**
- This repo: `AGENTS.md`, `SCHEMA.md`, `PROVIDERS.md`, `ROADMAP.md`, `README.md` update.
- Autopilot repo: `docs/LLM_PROVIDER_ROADMAP.md` (mirror of this file scoped to internal implementation), small `README.md` link.

**Production risk:** none — no executable code changes.

**Acceptance:** PRs merged on both repos. Future agents reading either repo find a coherent plan.

---

## Phase 1 — Add `app/llm/` package alongside existing `llm_client.py`

**Repo:** `truesight_autopilot`.

**Plan:**
- Create new package `app/llm/` with:
  - `base.py` — `LLMProvider` ABC, `LLMResponse`, `LLMUsage` dataclasses.
  - `openai_compatible.py` — shared HTTP plumbing (used by DeepSeek, BigModel, Kimi).
  - `deepseek.py` — `DeepSeekProvider` (XML tool-call shim lives here).
  - `registry.py` — `get_provider(name)` switch; defaults to `"deepseek"`.
- **Nothing imports the new package yet.** It's pure addition; the existing `llm_client.LLMClient` stays untouched.
- Add unit tests that exercise `DeepSeekProvider` against the same fixtures as the legacy client.

**Production risk:** none — dead code on disk until Phase 2.

**Acceptance:** PR merged; CI green. `app/llm/` exists, `llm_client.py` unchanged.

---

## Phase 2 — Make `LLMClient` a thin shim

**Repo:** `truesight_autopilot`.

**Plan:**
- Rewrite `LLMClient.__init__` and `LLMClient.chat` to delegate to `DeepSeekProvider` from the new package.
- Same constructor signature, same return shapes (caller code unchanged).
- Soak on EC2 for at least 3 days; watch logs for `LLMError`, finish-reason changes, latency drift.

**Production risk:** low — same wire calls, same provider, same response shapes. Risk is import-error / regression only.

**Acceptance:** No new errors in `journalctl -u truesight-autopilot.service` for 3 days. Governor chat unchanged. Fix loop still opens PRs.

**Rollback plan:** `git revert` the shim PR; original `LLMClient` returns.

---

## Phase 3 — Wire usage logging (off by default)

**Repos affected:** `truesight_autopilot`, `truesight_autopilot_transcript`.

**Plan:**
- Add `app/llm/usage_log.py` — a writer that accepts `LLMUsage` records and appends to disk.
- Provider ABC base class calls the writer after every successful call.
- Two write paths:
  - **Per-session** (`caller in {chat}`): append to `${SESSION_LOG_DIR}/<sid>/usage.jsonl`. The existing transcript-emitting code already pushes session dirs to this repo — usage.jsonl rides along.
  - **Per-worker** (`caller in {fix_agent, email_poller, aws_monitor, …}`): batch in-memory, flush every 60 seconds OR at process exit, append to `usage/<date>/workers.jsonl` in this repo via the same `gh api PUT /contents/...` path used for transcripts today.
- Gated behind env var `LLM_USAGE_LOG_ENABLED=1` — off by default.
- Add `scripts/rebuild_indexes.py` to this repo: regenerates `INDEX.json`, `_daily_summary.json`, `_summary.json` from the JSONL on disk. Run via a GitHub Action on push.

**Production risk:** none until enabled. When enabled, additional disk writes + git pushes; bounded by batching.

**Acceptance:** With the flag on for one week, all expected sessions/dates appear under `sessions/.../usage.jsonl` and `usage/<date>/workers.jsonl`. `_daily_summary.json` numbers reconcile against DeepSeek's billing dashboard within ±5%.

**Rollback plan:** Unset the env flag. The provider ABC reverts to no-op writes; existing data on disk stays.

---

## Phase 4 — Add `BigModelProvider` as opt-in

**Repo:** `truesight_autopilot`.

**Plan:**
- Implement `app/llm/bigmodel.py` extending `OpenAICompatibleProvider`.
- Read `BIGMODEL_CN_API` (already in `.env` per contributor handoff) → register key into config.
- Register `"bigmodel"` in `_PROVIDERS`.
- Smoke-test manually:
  - Governor chat: 5–10 messages including tool calls.
  - Fix loop: invoke `open_fix_pr` against a sandbox repo or branch; verify the produced PR matches what DeepSeek would've produced semantically.
  - Email poller: feed a synthetic GH Actions failure and inspect the diagnosis JSON.
- Document any quirks discovered in `PROVIDERS.md`.
- Default `LLM_PROVIDER` remains `"deepseek"` — flipping to `"bigmodel"` is a deliberate operator action.

**Production risk:** only if env is flipped on a host that doesn't have the contributor's key, OR if BigModel returns a tool-call shape the provider wrapper doesn't normalize.

**Acceptance:** Manual smoke tests pass. `PROVIDERS.md` updated with sampled pricing.

**Rollback plan:** Keep `LLM_PROVIDER=deepseek`. The new provider is dead code on the path that didn't choose it.

---

## Phase 5 — Unify Grok / Gemini under the provider ABC (optional)

**Repo:** `truesight_autopilot`.

**Plan:**
- `app/grok_client.py` becomes `app/llm/grok.py` implementing the ABC.
- `app/gemini_client.py` becomes `app/llm/gemini.py` — needs its own adapter since the Google SDK isn't OpenAI-compatible.
- Vision-specific helpers (`grok_analyze_images`, `gemini_analyze_image`) become methods on the provider that produce `LLMResponse` records with vision-specific fields.
- Usage logging reuses the same JSONL schema.

**Production risk:** medium — the QR scanner pipeline is actively in development (uncommitted code as of 2026-05-08). Do this phase only after the vision pipeline has stabilized.

**Acceptance:** QR scanner tests pass with no regressions. Vision calls now appear in `_daily_summary.json` alongside text-completion calls.

**Rollback plan:** Revert the migration PR; legacy `grok_client.py` / `gemini_client.py` paths are still present in git history.

---

## Phase 6 — Cleanup

**Repo:** `truesight_autopilot`.

**Plan:**
- `grep` the codebase for `LLMClient` / `from .llm_client import` — must return zero.
- Delete `app/llm_client.py`.
- Update any stale comments referring to the legacy client.

**Production risk:** low — gated on the grep being empty.

**Acceptance:** PR merged with no remaining references.

---

## Cross-cutting concerns

### Cost-table maintenance

`PROVIDERS.md` carries advisory pricing. After every quarter (or when a provider announces a price change), a maintainer must:

1. Re-check each provider's pricing page.
2. Update `PROVIDERS.md` and bump the **Last verified** date.
3. Optionally rerun `scripts/rebuild_indexes.py` with `--recompute-est-usd` to retroactively recost old `usage.jsonl` records.

### DAO ledger integration (later)

Once usage data has soaked, consider emitting a weekly `[LLM USAGE EVENT]` to Edgar (DAO ledger) so LLM spend appears in the same audit surface as AWS spend. Out of scope for this roadmap; tracked as a follow-up.

### What this roadmap does NOT cover

- Migrating prompt-engineering or system prompts. Out of scope.
- Vector storage / RAG / fine-tuning. Out of scope.
- Replacing the agentic loop architecture itself (separate proposal already in flight: `truesight_autopilot/pull/1` "Claude Agent SDK for the Tier 3 fix loop").

---

## Status as of 2026-05-08

| Phase | Status |
|---|---|
| 0 | 🟡 in this PR |
| 1 | ⚪ not started |
| 2 | ⚪ not started |
| 3 | ⚪ not started |
| 4 | ⚪ not started |
| 5 | ⚪ not started |
| 6 | ⚪ not started |

When a phase ships, update its row here and on the autopilot side's mirror.

---

## Last reviewed

2026-05-08 — initial roadmap.
