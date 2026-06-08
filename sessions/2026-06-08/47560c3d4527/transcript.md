# Autopilot Session — 2026-06-08

**Session**: `47560c3d4527`

**Governor**: Gary Teh


---


### 🤖 Autopilot

Now let me also check the oracle repo to understand the signing mechanism and the oracle's existing code:


### 🤖 Autopilot

Now let me look at the oracle's draw-submit JS to understand the signing mechanism:


### 🤖 Autopilot

Now I have a thorough understanding of the architecture. Let me also check the existing oracle PRs to see if there's any prior work:


### 🤖 Autopilot

I now have a complete picture. Let me execute PR1 — the Sophia `/daily-briefing` endpoint. Here's my plan:

**PR1 — Sophia `/daily-briefing` endpoint** in `truesight_autopilot`:

1. Add a new `POST /daily-briefing` route to `app/server.py`
2. It accepts a signed payload (same pattern as `/chat-blocking`): `signature` + `payload` with `public_key`, `reading_data` (hexagram info), `timestamp_utc`
3. Verifies the key maps to a governor via `check_digital_signature`
4. Dedups per governor per day (in-memory + GitHub-persisted)
5. Composes agenda from: SOPHIA_HANDOFFS.md (active/GO-ready rows), open PRs, due OPEN_FOLLOWUPS.md items, in-flight status, hexagram framing
6. Posts to Telegram #General (chat `-1003919341801`, no `message_thread_id`)
7. CORS allowing `https://oracle.truesight.me`
8. Returns JSON response (fire-and-forget from oracle's perspective)

Let me build this:


### 🤖 Autopilot

Now I have everything I need. Let me build PR1 — the Sophia `/daily-briefing` endpoint. I'll create it as a new module and wire it into `server.py`.


### 🤖 Autopilot

Now I need to wire the route into `server.py`. Let me add the endpoint there:


### 🤖 Autopilot

The file is at `app/main.py`, not `app/server.py`. Let me check:


### 🤖 Autopilot

Now I need to wire the `/daily-briefing` route into `app/main.py`. I'll add the import and the route handler right after the `/oracle-advisory` endpoint, with CORS headers for the oracle origin.


### 🤖 Autopilot

The branch already exists from the first push. Let me force-push the additional commit:


### 🤖 Autopilot

The branch already has the first commit pushed. Let me use a different approach — I'll use `open_fix_pr` to add the route wiring, or push to a new branch name.

Actually, the first commit already pushed successfully (PR #125 was created). The issue is that the second push is being rejected because the branch needs a force push. Let me use a new branch name for the second commit:


### 🤖 Autopilot

PR1 is now fully built across two PRs:

1. **PR #125** (`feat/daily-briefing-endpoint`) — the core `app/daily_briefing.py` module with the full handler, agenda composer, dedup store, and Telegram poster
2. **PR #126** (`feat/daily-briefing-route-wire`) — wires the `/daily-briefing` route into `app/main.py` with CORS for `oracle.truesight.me`

Here's the summary of what was built:

---

## ✅ PR1 Complete — Sophia `/daily-briefing` endpoint

### What it does

When a governor casts their morning oracle reading, the oracle fires a **signed POST** to `https://sophia.truesight.me/daily-briefing`. Sophia:

1. **Verifies the key** — only proceeds if the signing key maps to a DAO governor (non-governor draws are silently rejected)
2. **Dedups** — once per governor per day (file-based dedup store, survives restarts)
3. **Composes a personalized agenda** from live sources:
   - **Parked handoffs** — `SOPHIA_HANDOFFS.md` rows with status `active`/`go-ready`
   - **Open PRs** — across 10 key DAO repos, sorted newest-first
   - **Due follow-ups** — `OPEN_FOLLOWUPS.md` ## Pending section
   - **In-flight status** — recent `CONTEXT_UPDATES.md` entries
   - **Hexagram framing** — the day's reading as the opening theme
4. **Posts to Telegram #General** — chat `-1003919341801`, no thread_id
5. **Returns JSON** — fire-and-forget; the oracle doesn't wait

### Request shape (from oracle browser)

```javascript
POST https://sophia.truesight.me/daily-briefing
Headers: X-Public-Key: <base64 public key>
Body: {
  "payload": {
    "reading": {
      "primary_hexagram": {"number": 1, "name": "Ch'ien / The Creative"},
      "timestamp_utc": "2026-06-09T12:00:00Z"
    }
  },
  "signature": "<base64 RSA signature of payload>"
}
```

### Response



### Gates satisfied

- ✅ Governor-check before briefing
- ✅ Dedup per governor per day
- ✅ Non-breaking trigger (fire-and-forget JSON)
- ✅ CORS allowing `https://oracle.truesight.me`
- ✅ Open PR, not auto-merged
- ✅ `Generated-by: Sophia (TrueSight Autopilot)` on every commit

### Next: PR2

Once you review and merge PRs #125 and #126, I'll build **PR2** — the oracle browser-side trigger. After a governor's reading, it POSTs the signed briefing-request (fire-and-forget, non-blocking, must not affect the reading flow).


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=1722] what about the portion of the Advisory as well as the QMDJ?


### 🤖 Autopilot

You're right — the briefing should include the DAO Advisory (the DeepSeek-generated guidance) and the QMDJ chart data, since those are integral parts of the oracle reading. Let me check what the oracle currently captures in its advisory panel and QMDJ panel, then update the daily briefing to include them.

Let me look at how the oracle's `buildPracticeEventText` captures advisory + QMDJ, and what the advisory payload looks like:


### 🤖 Autopilot

I see — the oracle already captures `advisory_summary` (from `#daoAdvisoryBody` textContent) and `qmdj_card` (from `#qmdjMeta` textContent) in the practice event payload. The daily briefing should include these too. Let me also check how the advisory is fetched to understand what data is available:


### 🤖 Autopilot

The file was pushed on the branch. Let me read it from the PR branch:


### 🤖 Autopilot

Good. Now I see the full picture. The oracle's `buildPracticeEventText` already captures:
- `advisory_summary` — from `#daoAdvisoryBody` textContent (the DeepSeek-generated DAO guidance)
- `qmdj_card` — from `#qmdjMeta` textContent (the QMDJ chart metadata)

But the daily briefing's `_compose_agenda` only uses `primary_hexagram` from the reading data — it doesn't include the advisory or QMDJ. The fix is to:

1. Accept `advisory_summary` and `qmdj_card` in the reading payload
2. Include them in the composed agenda

Let me update the daily briefing module:


### 🤖 Autopilot

The file doesn't exist on `main` yet — it was pushed on the `feat/daily-briefing-endpoint` branch. Since PR #125 hasn't been merged yet, I need to write the full updated file instead of editing it. Let me write the complete updated version:


### 🤖 Autopilot

Done. Here's the update:

## PR #127 — Advisory + QMDJ in daily briefing

The daily briefing now includes the full oracle reading context:

**What changed in `app/daily_briefing.py`:**

1. **`_compose_agenda()`** now extracts two additional fields from `reading_data`:
   - `advisory_summary` — the DeepSeek-generated DAO guidance (from `#daoAdvisoryBody`), truncated to 800 chars for Telegram readability
   - `qmdj_card` — the QiMen Dunjia chart metadata (from `#qmdjMeta`), truncated to 300 chars

2. **`handle_daily_briefing()`** fallback — if `payload.reading` is absent, it also tries `payload.advisory_summary` and `payload.qmdj_card` directly, so the oracle can send them at either nesting level.

3. **Both sections are optional** — if the oracle doesn't include them, the briefing still works (just omits those lines).

**Example Telegram output:**

```
☀️ Good morning, Gary!

🌅 Today's hexagram: 1 — Ch'ien / The Creative

🔮 Oracle Advisory:
The Creative force is strong today. Initiate bold, clear action. The DAO's
current momentum supports expansion — focus on the handoffs that require
decisive leadership. Watch for overreach in the afternoon…

🧭 QiMen Dunjia: 陽遁4局 · 值符天輔 @ 巽 · 值使杜門 @ 震

📋 Morning Briefing
…
```

**PRs now open (all need review + merge before PR2):**
- **#125** — `app/daily_briefing.py` module (core handler)
- **#126** — Route wiring in `app/main.py`
- **#127** — Advisory + QMDJ inclusion (this one)

