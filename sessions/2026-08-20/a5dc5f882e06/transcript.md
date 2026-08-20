# Autopilot Session — 2026-08-20

**Session**: `a5dc5f882e06`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=11578] FounderHaus has a lot of loose cacao tea, they are proposing they want to package these and sell them as well for visitors to their venue. can you help research how much is the cost price of 25 grams of cacao tea?


### 🤖 Autopilot

Found key leads. Let me dig into the tea cost basis — there are two candidate figures (bulk raw vs repacked). Checking provenance:


### 🤖 Autopilot

Let me pull the full treasury cache to see all cacao-tea-related items and their cost basis:


### 🤖 Autopilot

Two tea cost bases are surfacing — let me resolve which is the right one for loose cacao tea, and check the repack composition:


### 🤖 Autopilot

Let me verify the AGL13 cacao tea cost basis and check for a "loose cacao tea" inventory line:


### 🤖 Autopilot

Let me check the canonical currency definitions and the AGL13/AGL8 tea ledgers to pin down the actual cost basis:


### 🤖 Autopilot

Let me pull the authoritative unit costs from the Main Ledger sheet and search the treasury cache for all tea/husk lines:


### 🤖 Autopilot

The sheet surfaced a key line. Let me pin down the exact tea cost basis lines in the treasury and check what loose tea FounderHaus specifically relates to:


### 🤖 Autopilot

Let me pin down the remaining tea lines (Santos AGL13 tea + loose-grams AGL8 tea) in the treasury cache:


### 🤖 Autopilot

The AGL13 tea line matches the freight manifest exactly. Let me confirm the cargo lines in the freight checklist and check how FounderHaus fits in:


### 🤖 Autopilot

I have almost everything. Let me confirm the exact treasury line for the Santos AGL13 tea to nail the cost basis:


### 🤖 Autopilot

Let me check the remaining tea/husk lines in the treasury cache (loose grams variants) to complete the picture:


### 🤖 Autopilot

## Cost price of 25g loose cacao tea

Based on the ledger, treasury cache, and the June 2026 freight manifest, the answer is **~$0.25 per 25g** (i.e. **$10.18/kg**).

### Where that comes from

| Source | Line | Unit cost |
|---|---|---|
| **AGL13 — "Cacao Tea (Kilograms) Santos 20260213"** (treasury: `unit_cost_usd = 10.1823`, inventory_type *Cacao Tea*) | 21 kg in the SSA→SFO manifest @ $10.18/kg = $213.83 | **$10.18/kg** |
| AGL8 — "Cacao Tea … Paulo 2024" (Ilhéus) | 14.68 kg, **$0 cost basis** recorded (manifest flags it as nominal $0.01) | $0/kg (unpriced) |
| Repacked "Cacao Tea 1g … Fazenda São Jorge" (Jul 2026) | 229 g, $0.1125/g | $112/kg — **outlier**, byproduct of bar-making from $100.89/kg organic almonds, not bulk tea economics |

### The math

- **$10.18/kg ÷ 1000 g × 25 g = $0.2545** → **~$0.25 per 25 g pack** (tea content only)
- That AGL13 price is the *landed* cost basis already on the ledger for the Santos-processed loose tea (same product family as husk, NCM 2106.90.00).

### If they want it retail-ready (25g sachet), add packaging

| Component | Cost |
|---|---|
| Tea (25 g) | ~$0.25 |
| Small pouch/sachet (proxy: Joyberg kraft envelope $0.07 / 1-gal ziploc $0.14) | ~$0.10–0.15 |
| Label (Sticker Mule) | ~$0.55 (less for small runs w/ generic stock) |
| **Total COGS per 25 g sachet** | **~$0.90–1.00** |

### Context notes
- The AGL8 Paulo tea has **no cost basis** on the books — if they use that stock, the recorded cost is $0 (freight already sunk). The $10.18/kg Santos tea is the honest, documented number to quote FounderHaus.
- **Selling reference:** cacao tea/husk to apothecaries is fixed at **$20/lb** (~$1.10 per 25 g) — so a 25 g sachet at ~$0.25–1.00 COGS leaves healthy margin even before venue markup.
- FounderHaus already carries one Agroverse line ("8 Ounce Package Kraft Pouch QN226716310BR – FounderHaus Brazil", 3 units @ $8.59) — so this is an extension of an existing consignment relationship, not a cold start.

Want me to draft a pricing/margin proposal for FounderHaus (COGS → suggested retail per 25 g sachet), or log this research somewhere?

