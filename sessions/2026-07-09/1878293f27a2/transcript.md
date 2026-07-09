# Autopilot Session — 2026-07-09

**Session**: `1878293f27a2`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=8354] https://truesight.me/buy-back-reserve/


### 🤖 Autopilot

Let me look into what's at that URL.


### 🤖 Autopilot

That's the **Buy-Back Reserve** page on truesight.me — it shows the accumulated USD provisions set aside for voting rights cash-outs and TDG buy-backs.

Key points from the page:

- **What it is**: The total USD provisions in the DAO's off-chain asset balance sheet under *"USD - provisions for voting rights cash out"*.
- **How it grows**: Daily buy-back budget = (Last 30 days DAO revenue ÷ 30) × min(Asset per TDG, 1 − Treasury Yield).
- **Data source**: Read from the off-chain asset balance sheet → `syncAllPerformanceStatistics()` populates the `BUY_BACK_RESERVE` key in the Performance Statistics sheet.
- **Current state**: The page shows "Loading reserve data..." with a dash — it may need a refresh cycle or the data source may not have populated yet.

What's your interest in the buy-back reserve, Gary? Want me to dig into the actual reserve value from the ledger, or look at the blog post explaining the formula?

