# SCHEMA.md — Canonical JSON shapes

Every structured file in this repo conforms to one of the schemas below. New fields are forward-compatible additions; consumers must ignore unknown fields and never crash on them.

All timestamps are **ISO-8601 UTC with `Z`** (e.g. `2026-05-08T20:56:42.123Z`). All token counts are integers. All USD costs are floats with up to 6 decimals.

Schemas are versioned via an optional `schema_version` field; if missing, assume `1`.

---

## 1. `sessions/<date>/<sid>/meta.json`

One file per session. Written once at session-end (not appended).

```json
{
  "schema_version": 1,
  "session_id": "03936a1deb60",
  "governor": "Gary Teh",
  "governor_email": "garyjob@agroverse.shop",
  "started_at": "2026-05-08T20:56:42.123Z",
  "ended_at":   "2026-05-08T21:14:09.882Z",
  "msg_count": 18,
  "providers_used": ["deepseek", "grok"],
  "models_used":    ["deepseek-chat", "grok-4-1-fast-non-reasoning"],
  "total_prompt_tokens": 41230,
  "total_completion_tokens": 2870,
  "total_tokens": 44100,
  "est_usd": 0.0123,
  "tool_calls_invoked": ["scan_qr_from_file", "lookup_qr_code"],
  "outcome": "completed",
  "client": "dapp.truesight.me/chat.html"
}
```

| Field | Type | Notes |
|---|---|---|
| `session_id` | string | Same as the directory name. Hex, 12 chars. |
| `governor` | string | Display name. May be `null` for anonymous chat. |
| `governor_email` | string | Email used for RSA-signed identity. May be `null`. |
| `started_at` / `ended_at` | string (ISO-8601 UTC) | First and last message timestamps. |
| `msg_count` | integer | Number of turns (`messages.jsonl` line count). |
| `providers_used` | string[] | Distinct provider names from `usage.jsonl`. |
| `models_used` | string[] | Distinct model names from `usage.jsonl`. |
| `total_prompt_tokens` etc. | integer | Sum across the session's `usage.jsonl`. |
| `est_usd` | float | Sum of per-call `est_usd` from `usage.jsonl`. May be `null` if pricing was unknown. |
| `tool_calls_invoked` | string[] | Distinct tool names invoked across the session. |
| `outcome` | string | `completed` \| `error` \| `interrupted`. |
| `client` | string | Caller hint: `dapp.truesight.me/chat.html`, `cli`, `email_poller`, etc. |

---

## 2. `sessions/<date>/<sid>/messages.jsonl`

One line per turn. Append-only during the session.

```json
{"schema_version":1,"ts":"2026-05-08T20:56:42.123Z","turn":1,"role":"user","content":"Re-scan the 19 files...","attachments":[]}
{"schema_version":1,"ts":"2026-05-08T20:56:45.901Z","turn":2,"role":"assistant","content":"I'll scan each of the 19 files...","tool_calls":[{"id":"call_xml_00","name":"scan_qr_from_file","arguments":{"file_path":"/Users/.../IMG_0997.HEIC"}}]}
{"schema_version":1,"ts":"2026-05-08T20:56:48.412Z","turn":3,"role":"tool","tool_call_id":"call_xml_00","name":"scan_qr_from_file","content":"{\"status\":\"no_qr\",\"file\":\"IMG_0997.HEIC\"}"}
```

| Field | Type | Notes |
|---|---|---|
| `ts` | string | ISO-8601 UTC. |
| `turn` | integer | 1-indexed within the session. |
| `role` | string | `user` \| `assistant` \| `tool` \| `system`. |
| `content` | string | The message text. May be empty for assistant turns whose only output was `tool_calls`. |
| `tool_calls` | array | Present on `assistant` turns that invoke tools. Each: `{id, name, arguments}` where `arguments` is a parsed object (NOT a JSON string). |
| `tool_call_id` | string | Present on `tool` turns; references the `tool_calls[i].id` of the assistant turn that requested it. |
| `name` | string | On `tool` turns: the tool name. |
| `attachments` | array | On `user` turns: `[{type, sha256, path_or_url, size_bytes}]` for uploaded images / files. May be empty. |

---

## 3. `sessions/<date>/<sid>/usage.jsonl`

One line per LLM call. Append-only during the session.

```json
{"schema_version":1,"ts":"2026-05-08T20:56:45.901Z","provider":"deepseek","model":"deepseek-chat","caller":"chat","session_id":"03936a1deb60","turn":2,"round":1,"prompt_tokens":4123,"completion_tokens":287,"total_tokens":4410,"cached_tokens":1024,"est_usd":0.000573,"latency_ms":3401,"had_tool_calls":true,"finish_reason":"tool_calls"}
```

| Field | Type | Notes |
|---|---|---|
| `provider` | string | `deepseek` \| `bigmodel` \| `kimi` \| `grok` \| `gemini`. |
| `model` | string | Provider-native model name (e.g. `deepseek-chat`, `glm-4.6`). |
| `caller` | string | Subsystem hint: `chat` \| `fix_agent` \| `email_poller` \| `aws_monitor` \| `qr_scan_grok` \| `qr_scan_gemini`. |
| `session_id` | string \| null | Set for chat-initiated calls; `null` for background workers. |
| `turn` | integer \| null | Which `messages.jsonl` turn produced this call. `null` if no session. |
| `round` | integer | 1-indexed round inside the agentic loop (e.g. tool-call thrash). |
| `prompt_tokens` / `completion_tokens` / `total_tokens` | integer | From the provider's `usage` block. |
| `cached_tokens` | integer | Provider-reported prompt-cache hits. `0` if unsupported. |
| `est_usd` | float \| null | Computed locally from `PROVIDERS.md` rates. `null` if pricing unknown. |
| `latency_ms` | integer | Wall-clock time for the HTTP call. |
| `had_tool_calls` | boolean | `true` if the response contained `tool_calls`. |
| `finish_reason` | string | `stop` \| `tool_calls` \| `length` \| `content_filter` \| `error`. |

---

## 4. `usage/<date>/workers.jsonl`

Same shape as §3, but emitted by background workers without a session. `session_id` is `null`. One file per UTC date, all workers commingled.

---

## 5. `usage/<date>/_daily_summary.json`

Computed by `scripts/rebuild_indexes.py`. Source of truth is the JSONL files in the same date directory plus all session `usage.jsonl` files for that date.

```json
{
  "schema_version": 1,
  "date": "2026-05-08",
  "generated_at": "2026-05-09T00:05:01.000Z",
  "totals": {
    "calls": 412,
    "prompt_tokens": 1840293,
    "completion_tokens": 78211,
    "total_tokens": 1918504,
    "est_usd": 0.4731
  },
  "by_provider_model": [
    {"provider":"deepseek","model":"deepseek-chat","calls":380,"prompt_tokens":1700000,"completion_tokens":72000,"total_tokens":1772000,"est_usd":0.4102},
    {"provider":"grok",    "model":"grok-4-1-fast-non-reasoning","calls":32,"prompt_tokens":140293,"completion_tokens":6211,"total_tokens":146504,"est_usd":0.0629}
  ],
  "by_caller": [
    {"caller":"chat","calls":270,"total_tokens":1500000,"est_usd":0.36},
    {"caller":"fix_agent","calls":80,"total_tokens":350000,"est_usd":0.085},
    {"caller":"email_poller","calls":40,"total_tokens":50000,"est_usd":0.018},
    {"caller":"qr_scan_grok","calls":22,"total_tokens":18504,"est_usd":0.0099}
  ]
}
```

---

## 6. `usage/_summary.json`

All-time rollup, regenerated by `scripts/rebuild_indexes.py`.

```json
{
  "schema_version": 1,
  "generated_at": "2026-05-09T00:05:01.000Z",
  "first_date": "2026-05-08",
  "last_date":  "2026-05-08",
  "all_time": {
    "calls": 412,
    "total_tokens": 1918504,
    "est_usd": 0.4731
  },
  "by_month": [
    {"month":"2026-05","calls":412,"total_tokens":1918504,"est_usd":0.4731}
  ],
  "by_provider_model": [
    {"provider":"deepseek","model":"deepseek-chat","calls":380,"total_tokens":1772000,"est_usd":0.4102},
    {"provider":"grok",    "model":"grok-4-1-fast-non-reasoning","calls":32,"total_tokens":146504,"est_usd":0.0629}
  ]
}
```

---

## 7. `sessions/INDEX.json`

Computed by `scripts/rebuild_indexes.py`. Lists every session for fast lookup without crawling.

```json
{
  "schema_version": 1,
  "generated_at": "2026-05-09T00:05:01.000Z",
  "sessions": [
    {
      "date": "2026-05-08",
      "session_id": "03936a1deb60",
      "governor": "Gary Teh",
      "started_at": "2026-05-08T20:56:42.123Z",
      "msg_count": 18,
      "total_tokens": 44100,
      "est_usd": 0.0123,
      "providers_used": ["deepseek","grok"]
    }
  ]
}
```

---

## 8. `pending/<id>.json` (existing — pre-roadmap shape)

Preserved as-is for backwards compatibility. One pending action per file:

```json
[
  {
    "title": "Merge PR #217 on dapp",
    "qr_code": "",
    "summary": "Fix spacing in session panel hamburger menu",
    "action": "merge_pr",
    "created_at": "2026-05-07T03:24:07Z"
  }
]
```

A future schema version may merge this with the rest of the structured layout; until then, treat existing files as schema_version=0 and read leniently.

---

## 9. Versioning

When a backwards-incompatible change is needed:

1. Bump `schema_version` on the affected record.
2. Update this file with the new shape AND keep the old shape documented.
3. Consumers must branch on `schema_version`; never drop support for older versions until a maintainer-blessed migration has rewritten the historical files.

---

## 10. Last reviewed

2026-05-08 — initial schema covering meta / messages / usage / daily_summary / summary / sessions index. See `ROADMAP.md` for which phases introduce which files.
