# truesight_autopilot_transcript

Append-only audit trail for [`TrueSightDAO/truesight_autopilot`](https://github.com/TrueSightDAO/truesight_autopilot) — the DAO's unified governor-chat + autonomous-SRE service.

Every governor session and every background-worker LLM call leaves evidence here so humans can audit what autopilot did, and future AIs can be pointed at this repo to learn how autopilot has reasoned in the past.

---

## Start here (AI agents)

→ **[`AGENTS.md`](AGENTS.md)** — single onboarding doorway. Read this first.

If you only have time for one file, that's the one.

## Reference

| File | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Cross-LLM onboarding doorway: purpose, layout, recipes for finding things. |
| [`SCHEMA.md`](SCHEMA.md) | Canonical JSON / JSONL shapes for every structured file in this repo. |
| [`PROVIDERS.md`](PROVIDERS.md) | LLM provider catalog: models, pricing (with last-verified dates), quirks. |
| [`ROADMAP.md`](ROADMAP.md) | Phased plan for the provider abstraction + usage logging that produce the files described above. |

## Layout

```
sessions/<YYYY-MM-DD>/<session_id>/
    transcript.md                    narrative log for humans (existing)
    meta.json                        session metadata (planned)
    messages.jsonl                   structured turns (planned)
    usage.jsonl                      per-LLM-call token / cost record (planned)
usage/<YYYY-MM-DD>/
    workers.jsonl                    background-worker LLM calls (planned)
    _daily_summary.json              rollup (planned)
pending/                             queued actions (existing)
```

See [`AGENTS.md`](AGENTS.md) and [`SCHEMA.md`](SCHEMA.md) for the full contract.

## Conventions

- Append-only. Never rewrite or delete existing transcripts.
- ISO-8601 UTC timestamps with `Z` suffix.
- JSONL (one record per line) for everything that grows over time.
- No secrets — API keys, RSA private keys, JWT secrets never appear here.

## Related

- [`TrueSightDAO/truesight_autopilot`](https://github.com/TrueSightDAO/truesight_autopilot) — the service that produces these transcripts.
- [`TrueSightDAO/agentic_ai_context`](https://github.com/TrueSightDAO/agentic_ai_context) — workspace context for all DAO AI agents.
