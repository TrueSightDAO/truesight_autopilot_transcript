# Autopilot Session — 2026-08-24

**Session**: `0103dbca5a9b`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=13934] Gary asked (2026-08-24) that going forward, heavy/long-running compute against Perch's production DB (sentiment_importer, seni_sql) — multi-minute backtest-style analysis, forward-return computations across many signals, that kind of thing — should be run by you, not directly via SSH from Envoy's interactive session.

Scope: this is specifically about heavy/expensive analysis (the kind that takes multiple minutes and multiple background queries), not every read-only lookup — a quick schema check or single row count is still fine for Envoy to do directly. If it's genuinely ambiguous which bucket something falls in, default to asking Gary or starting here.

Going forward: when Gary or Envoy has a Perch backtest/signal-effectiveness question that needs real compute against the DB, expect it to land in a Telegram thread like this one rather than Envoy just running it via SSH. No action needed on this specific message — just flagging the standing convention. Logged on Envoy's side too (memory: perch_heavy_compute_to_sophia.md).


### 🤖 Autopilot

Understood — convention logged. Let me pin it so it survives context trims.


### 🤖 Autopilot

Got it, Gary. Convention acknowledged and pinned:

**Perch heavy compute convention (2026-08-24)**
- **Routed to me (this thread):** multi-minute backtests, forward-return analysis across many signals, heavy compute against the Perch prod DB (sentiment_importer / seni_sql).
- **Still fine for Envoy directly:** quick schema checks, single row counts, lightweight read-only lookups.
- **Ambiguous bucket:** default to asking you or starting here.

No action needed on this message — just acknowledging so we're aligned on both sides. When a backtest lands here, I'll run it against seni_sql via the fleet (likely with background query batching) and report results in-thread.

