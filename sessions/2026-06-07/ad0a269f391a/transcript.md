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

Merge it. 

Next item is that we used to experiment with including pricing data of crypo-currencies. It added a lot of junk. And then coingecko stopped providing us with that data feed. And no only really looks at the data of those crypto anyways and they really cause the lookup via the search bar to look shitty. I am not sure if it slows things down as well for the lookup, it might. 

On the companies table their exchange = "crypto"

I wonder what are your thoughts of what we should do about these records?


### 🤖 Autopilot

Let me first merge that PR, then investigate the crypto records situation.


### 🤖 Autopilot

I see 14 open PRs. Which one did you want me to merge? The most recent one is #317 — "Follow-up: Graziela/Seacos airline quote still pending — poke Monday". Or did you mean a different one?

Meanwhile, let me investigate the crypto records situation.


### 🤖 Autopilot

Let me read the key files to understand the crypto infrastructure.


### 🤖 Autopilot

The default branch isn't `main`. Let me check what branches exist.


### 🤖 Autopilot

Good, I can read the files via the blob URL. Let me read the key ones.


### 🤖 Autopilot

Now let me check how the search bar works and how crypto records affect it.


### 🤖 Autopilot

Now let me check the database to see how many crypto records exist and what the search bar looks like.


### 🤖 Autopilot

Let me try via the database directly.


### 🤖 Autopilot

Now let me check what the search bar looks like and how crypto records affect it.


### 🤖 Autopilot

Now I have a clear picture. Let me also check the Sidekiq queues for crypto workers.


### 🤖 Autopilot

Let me check the sidekiq queues and cron jobs for crypto.


### 🤖 Autopilot

Excellent — now I have the full picture. Let me also check how many crypto records have stale/zero market cap (dead coins).


### 🤖 Autopilot

Now I have the full picture. Here's my analysis:

---

**On the merge** — which PR did you want merged? There are 14 open PRs in `agentic_ai_context`. The most recent is #317 ("Follow-up: Graziela/Seacos airline quote still pending"). Let me know which one.

---

**On the crypto records** — here's the situation:

**Scale of the problem:**
- **11,747 crypto companies** out of **57,077 total** = **20.6%** of all records
- **8,228** of those (70%) have **zero market cap** — dead/shitcoins that never had value
- **11,719** still have daily_trade records (price history)
- The `CryptoImporter` worker already has `return # Deprecated` at the top — it's dead code
- `CryptoMarketCapRefresher` also has `return # Deprecated`

**Impact on the search bar:**
The search bar (`SearchController#auto_complete`) calls `Company.search(params["q"]).limit(10)` — which searches across ALL companies including crypto. Since 20% of the DB is crypto junk, about 2 of every 10 autocomplete results are crypto noise. And since the search prioritizes exact symbol matches, typing something like "BTC" or "ETH" would pull up crypto before real stocks.

**Performance impact:** The `Company.search` query does `LOWER(stock_symbol) LIKE` and `LOWER(name) LIKE` across the full 57K-row table. The 11K extra crypto rows add ~20% more rows to scan. Not catastrophic but not nothing.

**My recommendation:** Clean them up in layers:

1. **Delete dead coins** — the 8,228 with `market_cap = 0` (never had value, never will). These are pure noise.
2. **Delete or soft-delete the rest** — the remaining ~3,500 that had market cap but whose data feed (CoinGecko) is dead. Nobody looks at them.
3. **Remove the crypto workers from Sidekiq cron** — `CryptoImporter`, `CryptoMarketCapRefresher`, `CryptoLargeDipIndexRefresher`, `LargeCryptoSpikeIndexRefresher` — they're all deprecated but may still be scheduled.
4. **Remove the crypto-related code paths** — the `exchange == "crypto"` guards in `Company` model (which skip fundamentals refresh, description refresh, etc.) become unnecessary.

Want me to open a PR for this?

