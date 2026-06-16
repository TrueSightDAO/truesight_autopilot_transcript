# Autopilot Session — 2026-06-16

**Session**: `5cd1cd74fbf8`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=2622] [Handoff context — auto-injected from SOPHIA_HANDOFFS.md: this Telegram topic (thread 2622) is the active handoff for `SOPHIA_FOLLOWUP_MONITOR_PLAN.md`. Before responding, read it with read_context_file("SOPHIA_FOLLOWUP_MONITOR_PLAN.md") and resume from its RESUME HERE marker. Treat a short go-signal in this topic ("go for it", "go", "proceed", "ship it") as the governor's full authorization to execute that plan through its gates, reporting progress in this topic.]

what is the status of this?


### 🤖 Autopilot

Let me check the handoff plan.


### 🤖 Autopilot

Let me read the full plan and check what's been done so far.


### 🤖 Autopilot

Let me check what's actually been implemented so far — any existing PRs or code.


### 🤖 Autopilot

Let me also check if there's any existing `followups` directory or related code on disk.


### 🤖 Autopilot

Interesting — the files already exist on disk! Let me check what's in them.


### 🤖 Autopilot

Let me also check for the tools file and tests.


### 🤖 Autopilot

Let me check the tests and whether the loop is wired in.


### 🤖 Autopilot

So the code files exist on disk but aren't wired into the app yet. Let me check if they're in GitHub at all (i.e., committed).


### 🤖 Autopilot

Let me check if the followup files are committed to GitHub or just exist locally.


### 🤖 Autopilot

So all 4 PRs have been committed and merged! Let me check the current state — is the loop actually running?


### 🤖 Autopilot

The followup code is committed and merged (PRs #164, #169, #170, #173), but it's **not wired into main.py** — the `followup_loop` isn't started in the lifespan block. Let me check the lifespan section of main.py to confirm.


### 🤖 Autopilot

Confirmed — the `followup_loop` is **not started** in the lifespan block. The code is all merged (PRs #164, #169, #170, #173) but the final wiring step is missing.

Let me also check if there are any existing follow-ups in OPEN_FOLLOWUPS.md.


### 🤖 Autopilot

Here's the full status:

---

## Durable Follow-up Monitor — Status

**All 4 PRs are merged** (code exists on disk and in GitHub), but the **final wiring step is missing** — the `followup_loop` is **not started** in `main.py`'s lifespan block.

### What's done ✅

| PR | What | Status |
|---|---|---|
| **PR1** (#173) | `app/followups.py` — parser + state sidecar for ````followup` blocks in OPEN_FOLLOWUPS.md | ✅ Merged |
| **PR2** (#164) | `app/tools/followup_tools.py` — `add_followup`, `list_followups`, `close_followup` tools | ✅ Merged |
| **PR3** (#169) | `app/followup_probes.py` — `elapsed_days` + `gmail_reply` probes | ✅ Merged |
| **PR4** (#170) | `app/followup_loop.py` — hourly comb loop + thread turn + escalation | ✅ Merged |

### What's missing ❌

**The loop isn't wired into `main.py`.** Looking at the lifespan block (lines 393-430), `email_poller`, `aws_monitor`, `branch_janitor`, `pending_janitor`, and `context_sync` are all started — but there's no:

```python
from .followup_loop import followup_loop
...
asyncio.create_task(followup_loop())
```

### What's in the backlog

There's **one active follow-up block** already in OPEN_FOLLOWUPS.md:

- **`chocolate-subscription-phase2`** — thread 1939, fires after 60 days (elapsed_days probe), reminds Gary to revisit Phase 2 fulfillment automation after Linda's 2nd shipment.

### Next step

Want me to open a PR to wire the `followup_loop` into `main.py`'s lifespan? It's a small change — add the import and one `asyncio.create_task()` call alongside the other background loops.

———
**✅ Done this turn — actions taken:**
• `ssh run` ×11 → find / -maxdepth 3 -name "truesight_autopilot" -type d 2>/dev/null | head -5; ls /opt/truesight_autopilot/app/ | head -30; find /opt/truesight_autopilot -name "test_followup*" -o -name "test*" | head -20; …(+8 more)

