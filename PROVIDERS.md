# PROVIDERS.md — LLM provider catalog

Every LLM provider used by `truesight_autopilot` is listed here, with the model catalog, current pricing, and quirks worth knowing. The autopilot's per-call usage logs reference `provider` and `model` strings that come from this file — keep them stable.

> ⚠️ **Pricing drifts.** Treat the per-million-token rates as advisory, not authoritative. Each block has a **Last verified** date — re-check the provider's pricing page before relying on `est_usd` for finance decisions. Any agent or maintainer who updates a rate must also bump that date.

---

## 1. DeepSeek (default)

- **Provider key:** `deepseek`
- **Base URL:** `https://api.deepseek.com`
- **API style:** OpenAI-compatible (`/chat/completions`).
- **Env vars:** `DEEPSEEK_API_KEY` (or fallback `DEEPSEEK_SDK`), optional `DEEPSEEK_BASE_URL`, `DEEPSEEK_MODEL`, `DEEPSEEK_MAX_TOKENS`, `DEEPSEEK_TEMPERATURE`.
- **Used by:** governor chat (`caller=chat`), autonomous fix loop (`caller=fix_agent`), email diagnosis (`caller=email_poller`).

### Models in use

| Model | Context | $/M input (cached) | $/M input (uncached) | $/M output | Notes |
|---|---|---|---|---|---|
| `deepseek-chat` | 64K | 0.07 | 0.27 | 1.10 | Default. V3.2-Exp (subject to change as DeepSeek revs). |

### Quirks

- **XML tool-call fallback.** `deepseek-chat` sometimes emits tool calls as `<function_calls><invoke name="...">...</invoke></function_calls>` XML in `content` instead of the standard `tool_calls` array. The autopilot's DeepSeek provider parses both forms transparently. The DSML-prefixed variant (`<||DSML||...>`) is also handled.
- **Prompt caching.** DeepSeek reports `prompt_cache_hit_tokens` / `prompt_cache_miss_tokens`. Map these into `cached_tokens` in `usage.jsonl`.
- **Rate limits.** Generous on paid tier; free tier is bursty. The fix loop occasionally hits 429s — back off + retry.

**Last verified:** 2026-05-08

---

## 2. BigModel.cn / 智谱AI / Zhipu

- **Provider key:** `bigmodel`
- **Base URL:** `https://open.bigmodel.cn/api/paas/v4`
- **API style:** OpenAI-compatible.
- **Env vars:** `BIGMODEL_CN_API` (planned: also accept `BIGMODEL_API_KEY`), optional `BIGMODEL_MODEL`.
- **Used by:** *not yet wired up* — see `ROADMAP.md` Phase 4. Provided by a DAO contributor.

### Models worth considering

| Model | Context | Notes |
|---|---|---|
| `glm-4.6` | 200K | Latest flagship; strong tool calling. Recommended starting point for swap-tests. |
| `glm-4.5-air` | 128K | Cheaper, fast. Good for diagnosis-heavy email-poller workloads. |
| `glm-4-plus` | 128K | Older flagship, kept for parity testing. |

Pricing tier depends on the contributor's API tier; populate the `pricing` table once the autopilot's `BigModelProvider` is live and we've sampled a few calls.

### Quirks

- **Tool calls.** GLM-4.5+ supports OpenAI-style `tool_calls` natively. Older `glm-4` was flakier and sometimes returns arguments as already-parsed objects (not JSON strings); the provider wrapper should normalize this.
- **Data residency.** Mainland China. Prompts and tool-call results flow through Chinese infra. Consider this for any sensitive governor-chat content.
- **Throughput.** Free / lower tiers rate-limit aggressively; check the contributor's tier before pointing the fix loop at it.

**Last verified:** 2026-05-08 (catalog only — no live pricing sampled yet)

---

## 3. Kimi / Moonshot AI

- **Provider key:** `kimi`
- **Status:** previously dropped (cost). May return as an alternative to DeepSeek if BigModel proves unreliable.
- **Base URL:** `https://api.moonshot.cn/v1` (CN) or `https://api.moonshot.ai/v1` (intl).
- **API style:** OpenAI-compatible.

Listed for completeness; not currently wired. Re-add in Phase 5 if needed.

**Last verified:** 2026-05-08

---

## 4. Grok / xAI (vision)

- **Provider key:** `grok`
- **Base URL:** `https://api.x.ai/v1`
- **API style:** OpenAI-compatible (`/chat/completions` with multimodal `image_url` parts).
- **Env vars:** `GROK_API_KEY` (fallback: `market_research/.env`).
- **Used by:** `app/grok_client.py` for QR-scan vision fallback (`caller=qr_scan_grok`).

### Models in use

| Model | Mode | Notes |
|---|---|---|
| `grok-4-1-fast-non-reasoning` | vision | Fast, low-detail; used as second-opinion to pyzbar. |

### Quirks

- Returns one JSON object in `content`. Code fence stripping handled by `_parse_grok_response`.
- Confidence score per QR-code guess is provider-specific to our prompt, not a Grok feature.

**Last verified:** 2026-05-08

---

## 5. Gemini / Google AI Studio (vision fallback)

- **Provider key:** `gemini`
- **API style:** Google `generativeai` SDK (NOT OpenAI-compatible).
- **Env vars:** `GEMINI_API_KEY` (fallback: `market_research/.env`).
- **Used by:** `app/gemini_client.py` as final fallback after pyzbar + zbarimg + Grok in the QR scanner pipeline (`caller=qr_scan_gemini`).

### Models in use

| Model | Mode | Notes |
|---|---|---|
| `gemini-2.0-flash-exp` | vision | Experimental flash model. May be retired without notice — keep an alternate model name in config. |

### Quirks

- Different SDK shape than OpenAI-compatible providers; the generic `OpenAICompatibleProvider` will not work here. Needs its own adapter.
- Vision responses returned as plain text; same regex-extract-JSON pattern as Grok.
- Token usage is reported via `response.usage_metadata` rather than the `usage` block.

**Last verified:** 2026-05-08

---

## 6. Provider-key registry (source of truth)

The autopilot's `app/llm/registry.py` (planned in `ROADMAP.md` Phase 1) MUST keep its provider name strings in sync with the keys above:

```
"deepseek" | "bigmodel" | "kimi" | "grok" | "gemini"
```

Adding a new provider means:

1. Append a section to this file with model catalog + pricing + quirks.
2. Add a class implementing the provider ABC in autopilot.
3. Add the key to `_PROVIDERS` in `registry.py`.
4. Update `ROADMAP.md` if it changes the rollout sequence.

---

## 7. Last reviewed

2026-05-08 — initial catalog. Pricing rows for BigModel, Kimi, Gemini are stubs and need a real verification pass once those providers go live.
