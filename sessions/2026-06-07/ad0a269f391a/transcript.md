# Autopilot Session — 2026-06-07

**Session**: `ad0a269f391a`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Do you have access to the sentiment_importer codebase and database?


### 🤖 Autopilot

Yes, I have access to both:

**Codebase** — `sentiment_importer` is a repo under TrueSightDAO. I can read files, search code, and open fix PRs there.

**Database** — The Edgar Rails backend (`seni_ror`) runs on EC2 (Nelanco account), backed by PostgreSQL on `seni_sql`. I can SSH into both hosts for diagnostics, log inspection, and service management.

What do you need to look into?


### 🧑 Governor

Just a thought I am looking at the data on this https://edgar.truesight.me/large_dips?the_date=2026-5-26, that day is not a trading day, the sell off showing up as actual correction level 25 is inaccurate.


### 🤖 Autopilot

Let me look into what's on that page and understand the data flow.


### 🤖 Autopilot

The page redirects to a login screen (I can't see the data directly without authentication). Let me read the key source files to understand how large dips are calculated and whether there's a trading-day filter.


### 🤖 Autopilot

The default branch isn't `main`. Let me find the right branch.


### 🤖 Autopilot

The SHA in the URLs is `62acafde74d3094ce1c9f706e5f667ff0556eb5f`. Let me read the key files using that ref.


### 🤖 Autopilot

Now let me look at the US market version (the non-crypto one) and the `DailySummary.sell_off_drivers` method to understand how the sell-off index is calculated.


### 🤖 Autopilot

Now I have a clear picture. Let me also check the config to see the `dip_cut_off_perc` and `dip_tracking_period_days` values.


### 🤖 Autopilot

Now I have a complete picture. Here's my analysis:

---

You're right. Here's what's happening:

**The root cause:** The large dip index has **no trading-day filter**. It runs against whatever dates exist in the `daily_trades` table.

Looking at the code flow:

1. **Controller** (`daily_trades_controller.rb` line 67): When you pass `?the_date=2026-5-26`, it uses that date directly — no check for whether it's a trading day.

2. **`mark_large_dips`** (`daily_trade.rb`): The SQL does a `LEFT JOIN` on `daily_trades` for the target date. If a date has *any* data in `daily_trades` (even stale/partial data), it will calculate a sell-off ratio. The query:
   ```sql
   select count(distinct company_id) as trade_count
   from daily_trades
   where date_published = '2026-05-26'
     and company_id in (select id from qualified_companies)
   ```
   If there are *some* trades recorded for that date (even if it's a holiday/weekend with thin or stale data), it produces a ratio.

3. **The sell-off threshold** is `config.sell_off_driver_threshold = 0.25` (25% in `application.rb` line ~130). If the ratio hits 0.25, it flags as "correction level 25."

**Why 2026-05-26 shows a false reading:** May 26, 2026 is a Tuesday — but it could be a non-trading day (e.g., Memorial Day observed in the US is the last Monday of May, which would be May 25, 2026 — so May 26 *should* be a trading day). Let me check what actually happened that day.


### 🤖 Autopilot

Now let me check the sell-off index value for that date:


### 🤖 Autopilot

Interesting — the actual sell-off ratio for 2026-05-26 is only **0.052** (5.2%), not 25%. But May 25 shows **0.25** (25%) with only **59 trades** — that's the problematic day.

Let me check what day of the week these fall on:


### 🤖 Autopilot

Now let me check what happened on May 25 (Monday) — Memorial Day 2026:


### 🤖 Autopilot

Now I have the full picture. Here's my analysis:

---

**Confirmed: May 25, 2026 was Memorial Day** — the US stock market was closed. But the database shows **59 trades** recorded for that day with **13 large dips**, producing a sell-off ratio of exactly **0.25** (25%). That's the "correction level 25" you saw.

The 59 trades are likely stale/partial data that got imported (possibly crypto or international securities, or a data provider artifact). With only 59 companies reporting on a closed day, a handful of dips can easily push the ratio to 0.25.

**The actual trading days (May 26–28)** show a healthy 5.2%–5.7% sell-off ratio — well below the 25% correction threshold — so there was no real correction.

**The root cause in the code:** There is **no trading-day filter** anywhere in the large dip pipeline:

1. **`most_recent_us_market_trading_date`** (`daily_trade.rb`) — correctly finds the last date with data, but it's used only for the *default* date navigation, not as a gate.

2. **`mark_large_dips`** — runs the SQL against whatever date is passed. If 59 companies have data on a holiday, it calculates a ratio from those 59.

3. **The controller** (`daily_trades_controller.rb` line 67) — when you pass `?the_date=2026-5-26`, it uses that date directly. The page then shows the sell-off index for that date, which for May 26 is actually fine (5.2%). But if you navigated to **May 25** (the holiday), it would show 25%.

4. **The `sell_off_drivers_query`** is disabled (returns empty), so the "sell-off drivers" section on the page is already a no-op.

**What should be fixed:** The `mark_large_dips` method (and/or the controller) should skip dates that aren't US market trading days. The simplest fix: add a check that the date has a meaningful number of trades (e.g., > 1000 qualified companies) before calculating the sell-off index, or maintain a trading-day calendar.

Want me to open a PR to add a minimum-trade-count guard to `mark_large_dips` so holidays with sparse data don't produce false correction readings?

