# Autopilot Session — 2026-06-29

**Session**: `3d08180da295`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=8084] Can we check how much cash reserves we have on each ledger and in total? breakdown by individual ledger as well as like the total in usd [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me check the ledgers for cash reserves.


### 🤖 Autopilot

Let me find the actual sheet names first.


### 🤖 Autopilot

That's the TDG ledger (contribution history), not cash. Let me look for the actual cash/treasury ledgers.


### 🤖 Autopilot

Let me check the treasury-cache repo and the tokenomics notes for cash ledger info.


### 🤖 Autopilot

There's a treasury cache. Let me read the actual JSON and also check the Main Ledger for the offchain asset location sheet.


### 🤖 Autopilot

Let me read the full output to get the totals and all the cash-like items.


### 🤖 Autopilot

Let me get the totals section and the rest of the items.


### 🤖 Autopilot

Let me get the totals section.


### 🤖 Autopilot

Let me get the totals section at the end of the JSON.


### 🤖 Autopilot

Now I have the full picture. Let me extract the cash-like items (USD, USDT, Brazilian Reis, and the provisions line) and break them down by ledger.

Here's the cash reserves breakdown from the treasury cache (generated June 29, 2026):

**Cash & Cash-Equivalent Currencies**

| Currency | Total Quantity | USD Value |
|---|---|---|
| **USD** | $20,817.30 | $20,817.30 |
| **USDT** | $66.93 | $66.93 |
| **Brazilian Reis** | R$2,748.87 | $638.56 |
| **USD - provisions for voting rights cash out** | $41.26 | $41.26 |
| **Total Cash** | | **$21,564.05** |

**Breakdown by Ledger (USD only)**

| Ledger | USD Amount |
|---|---|
| **AGL4** | $9,036.35 |
| **AGL15** | $5,101.34 |
| **Main Ledger** | $4,332.13 |
| **AGL6** | $1,337.59 |
| **AGL8** | $569.95 |
| **AGL10** | $330.83 |
| **BEC** | $93.12 |
| **SEF1** | $16.00 |
| **Total** | **$20,817.30** |

**Brazilian Reis by Ledger**
- Main Ledger: R$2,511.97 ($583.53 USD)
- AGL8: R$236.90 ($55.03 USD)

So total cash reserves across all ledgers come to about **$21,564 USD** — that's USD + USDT + Brazilian Reis converted at the treasury's recorded rate of 0.2323 USD/BRL. The bulk of it ($9K) sits in AGL4, with another $5K in AGL15 and $4.3K in the Main Ledger.

