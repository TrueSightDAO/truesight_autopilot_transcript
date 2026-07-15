# Autopilot Session — 2026-07-15

**Session**: `d33f628f755f`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=8856] https://truesight.me/treasury/ 

https://truesight.me/index.html


USD Treasury Balance figures are different


### 🤖 Autopilot

Let me check both URLs to see what's happening.


### 🤖 Autopilot

I can see the issue. Let me look at the actual data sources behind both pages to compare the numbers.


### 🤖 Autopilot

Both pages load data from a GAS (Google Apps Script) feed. Let me find the JavaScript that fetches the treasury data to understand the data source.


### 🤖 Autopilot

Let me look at the inline script in the treasury page HTML to find the data source URL.


### 🤖 Autopilot

Now I see the architecture. Both pages call the **same GAS endpoint** (`?type=treasury_breakdown`). The landing page likely calls a different `?type=` parameter for its headline stat. Let me check what the landing page uses.


### 🤖 Autopilot

Let me search for the landing page's treasury stat fetch call.


### 🤖 Autopilot

The prod repo's search index may be stale. Let me check the actual live page data by hitting the GAS endpoint directly.


### 🤖 Autopilot

Now let me check what the landing page's headline stat fetches. Let me look at the landing page's inline script for the treasury stat.


### 🤖 Autopilot

Let me search for the landing page's treasury stat fetch — it's likely in a separate JS file or inline script.


### 🤖 Autopilot

The GitHub search index for this repo seems empty. Let me look at the beta repo instead, which is the source.


### 🤖 Autopilot

Let me search the beta repo for the treasury stat fetch code.


### 🤖 Autopilot

The GitHub search index for these repos seems to not be working. Let me check the GAS source that computes the data.


### 🤖 Autopilot

Now let me find the `computeTreasuryBreakdown` function and the landing page's headline stat function.


### 🤖 Autopilot

Let me search for the specific functions that compute the headline stat vs the treasury breakdown.


### 🤖 Autopilot

Rate limited. Let me search the file I already have open.


### 🧑 Governor

[TURN DIRECTIVE] You have used 23 of 30 tool rounds and are approaching the per-turn limit. Stop calling tools now and converge: summarize what you found, what (if anything) is still blocking, and end with a 'RESUME HERE' pointer so the next turn can continue. Start no new multi-step work — land a clean, resumable answer in your next message.


### 🤖 Autopilot

Good catch. Let me land this cleanly.

---

**What I found:**

Both pages call the **same GAS endpoint** (`?type=treasury_breakdown`) which returns:

```
total_usd: $15,619.03
  ├─ off_chain_assets_usd: $14,442.61
  ├─ usdt_vault_usd: $0.00
  └─ agl_equity total: $1,176.42
       ├─ AGL14: $456.49
       ├─ AGL8: $268.06
       ├─ AGL7: $242.86
       ├─ AGL10: $193.91
       ├─ AGL6: $15.10
       └─ AGL2: ~$0.00
```

**The discrepancy you're seeing** is likely because the **landing page** (`index.html`) fetches a **different stat** — the "USD Treasury Balance" tile on the landing page may be pulling from a different `?type=` parameter (e.g. `?type=performance_stats` or the default `doGet` response), which could be stale or computed differently.

The `/treasury/` page explicitly uses `?type=treasury_breakdown` and shows the full breakdown. The landing page's headline stat tile uses a separate fetch — I hit the GitHub rate limit before I could find its exact `?type=` parameter in the GAS code.

**To diagnose the gap:**
1. Open both pages side-by-side in a browser
2. Right-click → Inspect → Network tab → reload both
3. Compare the JSON payloads each one fetches from the GAS endpoint

If the landing page stat is **higher**, it may be pulling a cached `USD_TREASURY_BALANCE` from the Performance Statistics sheet that hasn't been refreshed. If it's **lower**, it may be pulling a different formula (e.g. off-chain only, excluding AGL equity).

**RESUME HERE** — Next turn: search the GAS file for the `doGet` function's default `?type=` handling and the `updateTotalDAOAssetOnWix` function to see what value gets written to the Performance Statistics sheet vs what `treasury_breakdown` computes. The GAS file is at `tokenomics/google_app_scripts/1ZQjgSZvAXL2PB3e3YW289xY7Ork4S5wV4uKTXJyw83xQT4R0lh_hwNWn/tdg_wix_dashboard.js` — search for `doGet` and `updateTotalDAOAssetOnWix` in it.

