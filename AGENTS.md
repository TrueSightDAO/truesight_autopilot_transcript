# AGENTS.md — TrueSight Autopilot Transcript Repo

**Audience:** Any AI agent (Claude Code, OpenAI Codex, Cursor, Gemini CLI, Aider, custom autopilot processes) reading this repository to understand or audit `truesight_autopilot`.

This file is the doorway. If you only read one file, read this one.

---

## 1. What this repo is

This repo is the **append-only audit trail** for [`TrueSightDAO/truesight_autopilot`](https://github.com/TrueSightDAO/truesight_autopilot) — a unified AI service for the TrueSight DAO that does two things:

1. **Reactive** — governor chat at `dapp.truesight.me/chat.html` (RSA-signed or JWT, currently DeepSeek-V3 with tool calls).
2. **Proactive** — background workers (Gmail polling for GitHub Action / GAS errors, AWS CloudWatch + Cost Explorer monitoring, autonomous PR opening).

Every governor session and every background-worker LLM call should leave evidence here so:

- Humans can audit *what autopilot did* on any given day.
- Future LLMs can be pointed at this repo to learn how autopilot has reasoned in the past, what decisions were made, and what models / providers / prompts were used.
- The DAO can review token spend across providers without trusting a single dashboard.

The autopilot code lives in [`TrueSightDAO/truesight_autopilot`](https://github.com/TrueSightDAO/truesight_autopilot). This repo is **only the audit trail**. Code changes go there; transcripts and usage logs go here.

---

## 2. Layout

```
truesight_autopilot_transcript/
├── README.md                       human-friendly overview, points at this file
├── AGENTS.md                       (you are here) AI onboarding doorway
├── SCHEMA.md                       canonical JSON shapes for every *.json / *.jsonl
├── PROVIDERS.md                    LLM provider list, model catalog, pricing (last-verified date)
├── ROADMAP.md                      phased plan for provider abstraction + usage logging
├── sessions/
│   ├── INDEX.json                  [{date, sid, governor, started_at, msg_count, total_tokens, est_usd}]  (planned, see ROADMAP.md)
│   └── <YYYY-MM-DD>/<session_id>/
│       ├── transcript.md           narrative log for humans (existing)
│       ├── meta.json               session metadata (planned)
│       ├── messages.jsonl          structured turn-by-turn (planned)
│       └── usage.jsonl             one line per LLM call (planned)
├── usage/
│   ├── <YYYY-MM-DD>/
│   │   ├── workers.jsonl           background-worker calls — no session_id (planned)
│   │   └── _daily_summary.json     {provider × model → tokens, est_usd, call_count} (planned)
│   └── _summary.json               rolling all-time + month/quarter rollups (planned)
├── pending/
│   └── *.json                      pending action queue (existing)
└── scripts/
    ├── append_usage.py             autopilot calls this from the EC2 host (planned)
    ├── rebuild_indexes.py          regenerates INDEX.json + summaries (planned)
    └── summarize_usage.py          CLI: tokens & USD by provider/model/day/caller (planned)
```

Everything tagged **(planned)** is described in `ROADMAP.md` and not yet implemented. Everything tagged **(existing)** is what's already on disk today.

---

## 3. Where to look for X (recipes for AI agents)

| You want to know… | Read this |
|---|---|
| What conversations a governor had on a date | `sessions/<date>/INDEX.json` (planned) → `sessions/<date>/<sid>/transcript.md` (existing) |
| Structured turn-by-turn (no prose parsing) | `sessions/<date>/<sid>/messages.jsonl` (planned) |
| Tokens / USD spent on a date | `usage/<date>/_daily_summary.json` (planned) |
| All-time spend per provider × model | `usage/_summary.json` (planned) |
| Why autopilot made a particular tool call | `sessions/<date>/<sid>/messages.jsonl` (planned) — look at the turn before the `tool_call` |
| What pending actions are queued | `pending/*.json` (existing) |
| Which LLM providers are in use | `PROVIDERS.md` |
| Schema for any file in this repo | `SCHEMA.md` |
| The plan for new infrastructure | `ROADMAP.md` |
| The autopilot code itself | [github.com/TrueSightDAO/truesight_autopilot](https://github.com/TrueSightDAO/truesight_autopilot) — see its `README.md` |
| Workspace-wide DAO context | [github.com/TrueSightDAO/agentic_ai_context](https://github.com/TrueSightDAO/agentic_ai_context) — start at `OPERATING_INSTRUCTIONS.md` |

---

## 4. Conventions for writers (autopilot processes, future agents)

Whether the writer is the autopilot service itself or a developer-driven backfill:

1. **Append-only.** Never rewrite or delete existing transcripts. If something was wrong, append a correction transcript or note in `sessions/<date>/<sid>/notes.md`.
2. **JSONL over JSON arrays** for any file that grows over time (`messages.jsonl`, `usage.jsonl`, `workers.jsonl`). One record per line. Streamable, grep-friendly, append-safe.
3. **ISO-8601 UTC timestamps** with the `Z` suffix everywhere (`2026-05-08T20:56:42.123Z`). No localized strings, no offsets.
4. **Stable shapes.** If a JSON line's keys change, bump a `schema_version` field (see `SCHEMA.md`). Consumers should ignore unknown fields, never crash.
5. **Idempotency.** Writes from autopilot should be safe to retry — a failed `git push` should not produce duplicate lines on the next attempt.
6. **No secrets.** API keys, RSA private keys, JWT secrets never appear here. If a tool call result contains one, the autopilot must redact before logging.
7. **Path stability.** A session's directory `sessions/<date>/<sid>/` is permanent. Once written, the path is a stable URL for human / LLM links.

---

## 5. Conventions for readers (this means you, future LLM)

1. **Start at this file (`AGENTS.md`)**. Do not crawl `sessions/` blindly — there are thousands of files.
2. **For date-ranged questions**, read `INDEX.json` and `_daily_summary.json` first. Drill into individual transcripts only if needed.
3. **Trust `SCHEMA.md`** as the source of truth for field meanings. If a JSONL line has fields not in `SCHEMA.md`, treat them as forward-compatible additions.
4. **The narrative `transcript.md` is for humans.** Do not parse it with regex when a `messages.jsonl` exists alongside it — the JSONL is the canonical structured form.
5. **Do not write to this repo unless you are autopilot itself or a maintainer running a backfill script.** This repo is the audit trail; ad-hoc agent edits dilute its trustworthiness. If you need to record something, do it via the autopilot service, which knows how to write here correctly.

---

## 6. Related repos

| Repo | Role |
|---|---|
| [`TrueSightDAO/truesight_autopilot`](https://github.com/TrueSightDAO/truesight_autopilot) | The service that produces these transcripts. Code, deploy, config. |
| [`TrueSightDAO/agentic_ai_context`](https://github.com/TrueSightDAO/agentic_ai_context) | Workspace context for all DAO AI agents — read this first if you're new to the DAO. |
| [`TrueSightDAO/dao_client`](https://github.com/TrueSightDAO/dao_client) | Python CLI / library for `[CONTRIBUTION EVENT]` and other Edgar submissions. |
| [`TrueSightDAO/dapp`](https://github.com/TrueSightDAO/dapp) | DApp frontend; `chat.html` is the governor-chat UI that talks to autopilot. |

---

## 7. Last reviewed

2026-05-08 — initial AGENTS.md introduced alongside `SCHEMA.md`, `PROVIDERS.md`, `ROADMAP.md`. See `ROADMAP.md` for what's planned next.
