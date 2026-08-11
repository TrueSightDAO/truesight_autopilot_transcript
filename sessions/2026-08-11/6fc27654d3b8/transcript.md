# Autopilot Session — 2026-08-11

**Session**: `6fc27654d3b8`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Check the HS code and the HTS code required for exporting this from China into USA

It is the HaoYue15 model

[Attachment auto-processed: **4cbf0f40528f4df9b79786024c3df744.jpg**]
- Type: Image (OCR confidence: 0.0%, quality: poor)

*(No text detected in image)*


### 🤖 Autopilot

[2 tool result(s) compacted: list_directory, web_search — detail in artifacts]


### 🤖 Autopilot

[2 tool result(s) compacted: web_search, scan_qr_from_file — detail in artifacts]


### 🤖 Autopilot

[2 tool result(s) compacted: ocr_image, web_search — detail in artifacts]


### 🤖 Autopilot

The image didn't OCR (no text detected) — let me try harder to read it and verify the vehicle specs in parallel.
[2 tool result(s) compacted: ssh_run, web_search — detail in artifacts]


### 🤖 Autopilot

The image is stubborn — no text OCR'd. Let me try Chinese OCR and check if I have a vision tool on the box to actually see what's in the photo.
[2 tool result(s) compacted: ssh_run, ssh_run — detail in artifacts]


### 🤖 Autopilot

[2 tool result(s) compacted: ssh_run, ssh_run — detail in artifacts]


### 🤖 Autopilot

OCR is completely failing on this image (likely a dark photo). Let me check the grok_client for vision capability to actually "see" the image.
[1 tool result(s) compacted: read_local_file — detail in artifacts]


### 🤖 Autopilot

There's a Grok vision client on the box. Let me use it to actually see the image.
[1 tool result(s) compacted: ssh_run — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: ssh_run — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: ssh_run — detail in artifacts]


### 🤖 Autopilot

The key is in the autopilot's own .env. Let me load it and run Grok vision.
[1 tool result(s) compacted: ssh_run — detail in artifacts]


### 🤖 Autopilot

Grok vision read the label as **"Haoyue T5"** — a prefabricated modular cabin/tiny home (white structure with orange accents), not a car. Let me verify what product this actually is and pin down the correct classification.
[2 tool result(s) compacted: web_search, web_search — detail in artifacts]


### 🤖 Autopilot

Grok read the label as **"Haoyue T5"** — a white prefabricated modular cabin/tiny home with orange accents. Given you said "HaoYue15," this is the Haoyue brand modular prefab house. Now let me pin down the exact China HS code (8-digit) and US HTS code (10-digit) for prefabricated buildings.
[2 tool result(s) compacted: web_search, web_search — detail in artifacts]


### 🤖 Autopilot

I have the classification confirmed. Let me check the latest tariff status (Section 301 + IEEPA "reciprocal" tariffs, which changed a lot in 2025) so the duty figures are current, not stale.
[2 tool result(s) compacted: web_search, web_search — detail in artifacts]


### 🤖 Autopilot

Tariff landscape confirmed (SCOTUS struck down IEEPA Feb 2026; Section 301 25% remains; Section 122 10% replaced by new forced-labor 301 tariff in July 2026). Let me verify the authoritative current HTS structure and the exact China export code.
[1 tool result(s) compacted: web_extract — detail in artifacts]


### 🤖 Autopilot

[2 tool result(s) compacted: http_fetch, web_search — detail in artifacts]


### 🤖 Autopilot

I have everything I need. Let me persist the image analysis to the transcript per the attachment workflow, then give you the answer.
[1 tool result(s) compacted: append_to_transcript — detail in artifacts]


### 🤖 Autopilot

Here's what I found, Gary.

## Product identification
The photo (read via Grok vision — the file itself wouldn't OCR) shows a **white prefabricated modular cabin/tiny home** with orange accent trim, labeled **"Haoyue T5"**, sitting on a deck in a desert setting. So "HaoYue15" = the **Haoyue brand prefab modular house**, not a vehicle. This is a factory-built dwelling unit, not a car.

## China export — HS code (Customs of China)
| Code | Description |
|---|---|
| **9406.90.00** (8-digit) | Prefabricated buildings, other (not steel modular units) |
| **9406.90.00.90** (10-digit export declaration) | Other prefabricated buildings, n.e.s. |

This is the standard China customs classification used for prefab/container/modular houses exported under 9406 (prefabricated buildings). Your supplier's customs broker should confirm the exact 10-digit line — it may also be reported at 9406.20.00.10 if it's literally a steel shipping-container-style module; but for a finished dwelling cabin, 9406.90.00.90 is the usual choice.

## USA import — HTS code (USITC)
| Code | Description | Base duty |
|---|---|---|
| **9406.90.01.30** | Prefabricated buildings: Other: **Of metal**: Other | **2.9%** ad valorem |

CBP rulings for exactly this type of product (NY N314354 — "microhomes"; N341297 — prefab housing structure) place a finished prefab dwelling under **9406.90.01.30**, not 9406.20.00 (which is reserved for steel modular units designed to assemble into a permanent building).

**Unit of quantity:** m² (floor area when assembled).

## ⚠️ Tariffs on China-origin goods (this is the big one)
As of now (mid-2026), the duty stack on a Chinese prefab cabin into the US is roughly:
- **2.9%** MFN base duty
- **+25%** Section 301 (List 3) — must also report Chapter 99 code **9903.88.03**
- **+12.5%** Section 301 forced-labor tariff (replaced the IEEPA/§122 surcharges after SCOTUS struck those down in Feb 2026)

→ **Total ≈ 40%** ad valorem, CIF-based, plus any local/state fees. This changes frequently — **confirm with your customs broker at the time of shipment**. Also note: these prefab units usually ship as breakbulk/RO-RO or on flat racks, so freight and ISF/entry paperwork matter as much as the code.

## Caveats
- The label in the photo read as "Haoyue **T5**" to the vision model — T5 vs 15 doesn't change the classification (still 9406), but confirm the exact model and **construction material** with the supplier: if the frame is steel → 9406.90.01.30; if it's predominantly wood/other → a different statistical line under 9406.90 (e.g. 9406.90.00.30/00.35) with the same 2.9% base rate.
- I'd get a **binding ruling request** (or at least a broker's written classification) before the first shipment — a $10k+ cabin with ~40% duty is worth getting right on the entry.

———
**✅ Done this turn — actions taken:**
• `ssh run` ×9 → cd /tmp/tg_attachments && python3 -c " from PIL import Image im = Image.open('4cbf0f40528f4df9b79786024c3df744.jpg') print(im.size, im.mode); sudo apt-get install -y tesseract-ocr-chi-sim >/dev/null 2>&1; tesseract --list-langs 2>/dev/null | head; echo "---CHI OCR---"; cd /tmp/tg_a; ls ~/truesight_autopilot 2>/dev/null; find / -maxdepth 4 -name "*grok*" -not -path "*/proc/*" -not -path "*/sys/*" 2>/dev/null | head; find ; …(+4 more)
• `append to transcript` → https://github.com/TrueSightDAO/truesight_autopilot_transcript/blob/main/sessions/2026-08-10/87ec40664bdd/transcript.md


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=10729] Can you do a full research to get the cost price?


### 🤖 Autopilot

Gary — full cost research on the Haoyue prefab house. Let me pull pricing from multiple angles: the manufacturer's own pricing, comparable modular house FOB China prices, and landed cost to the US.
[2 tool result(s) compacted: web_search, web_search — detail in artifacts]


### 🤖 Autopilot

Let me dig for the actual Haoyue manufacturer listing and the specific model pricing.


### 🤖 Autopilot

Found the likely manufacturer: **Haoyue Door & Window Co., Ltd. (Hunan Haoyue Intl, est. 1999)**. Let me get their actual listing prices and the freight/landed cost picture.


### 🤖 Autopilot

Let me pin down the exact Haoyue product line and get the precise landed-cost model. I have the manufacturer (Xiamen/Hunan Haoyue Door & Window Co., Apple Cabin range) — now let me verify model pricing and the specific shipping profile for a ~15㎡ cabin.


### 🤖 Autopilot

One more targeted check — the Haoyue factory's own listing prices, then I'll compile the full landed-cost model.


### 🤖 Autopilot

Here's the full cost research, Gary. Note: the photo label read "Haoyue **T5**" — I could not find an exact "HaoYue15" model listing online, so treat these as benchmarks for the **Haoyue-brand Apple Cabin / space-capsule type prefab house (~15㎡)**, which is what the photo shows. Prices are research estimates, not a quote.

## 1. Manufacturer identified
- **Xiamen Haoyue Door & Window Co., Ltd. / Hunan Haoyue Intl** (est. 1999, ~5,000㎡ factory) — maker of the "Apple Cabin" / modular prefab range. The Alibaba listing linked to this exact product family: *"Factory Wholesale 20Ft 40Ft Mobile Apple Cabin Prefab Space Capsule House."*
- Note: there are several "Haoyue" prefab makers; confirm with the supplier which factory + model this is before quoting.

## 2. FOB price (ex-China port) — benchmarks
| Source / product | Price (USD) |
|---|---|
| Apple Cabin FOB, made-in-china listings (several factories) | **$3,299 – $4,999 / unit** |
| 20ft pre-installed luxury apple cabin | $6,300 – 6,500 |
| Vesspod-style capsule house (2026) | $5,700 – 5,980 |
| Factory cost guide (rtophouse) real example | $3,863 – 4,863 / unit |
| Per-sqm pricing (Marscabin / Umd) | $200–280/sqm → **15㎡ ≈ $3,000–4,200** · $370–480/sqm → **15㎡ ≈ $5,550–7,200** |
| Factory tour (real walkthrough, 2026): 15㎡ unit | **≈ $7,500** · 80㎡ unit ≈ $16,000 |

**Realistic FOB for a Haoyue 15㎡ unit: $4,000 – $7,500**, depending on insulation, glass, bathroom fit-out, and appliances.

## 3. Ocean freight + insurance (China → USA)
| Component | Cost (USD) |
|---|---|
| 20ft FCL, China → US West Coast | $2,400 – 3,300 |
| 40ft FCL, China → US West Coast | $3,000 – 6,000 (East Coast +$1,000–2,000) |
| Transit time | 14–21 days WC / 25–35 days EC |
| Marine insurance | 0.3 – 0.5% of cargo value |

## 4. US duties (the big one) — HTS 9406.90.01.30
| Duty | Rate |
|---|---|
| MFN base | 2.9% |
| Section 301 (List 3, ch.99 **9903.88.03**) | +25% |
| Section 301 forced-labor tariff (2026) | +12.5% |
| **Total duty stack** | **≈ 40.4% ad valorem on CIF value** |

## 5. Total landed cost — worked example (mid-range)
Assumptions: FOB $5,500, 20ft FCL to West Coast $3,000, insurance 0.4%.

| Line item | Amount |
|---|---|
| FOB price | $5,500 |
| Ocean freight | $3,000 |
| Insurance (~0.4% of FOB+freight) | $34 |
| **CIF value** | **$8,534** |
| **US duties ≈ 40.4%** | **$3,448** |
| Port charges + drayage + brokerage | $800 – 1,500 |
| **Total landed (port of entry)** | **≈ $12,800 – 13,500** |

**Budget scenario** (FOB $4,000, freight $2,500): landed ≈ **$9,600 – 10,000**
**Premium scenario** (FOB $7,500, freight $4,000 EC): landed ≈ **$17,500 – 18,500**

Then add on-site costs (crane/rigging $1,000–3,000, foundation, utilities hookup) — typically +$5,000–10,000 depending on site.

## Key takeaways
1. **Duty is ~40%** — bigger than the freight. CIF-value-based, so it scales with your declared price.
2. Buying **CIF vs FOB** and using a **consolidated 20ft** can save $500–1,500 vs booking your own freight.
3. Confirm exact model + spec with the supplier — a bathroom/full kitchen vs shell changes FOB by $2,000+.
4. For US compliance on a wheeled unit, ANSI A119.5 certification matters (affects build spec, and thus price).

Want me to:
- **A)** generate a branded PDF of this cost research (Saffron Monk style) to share with the supplier/broker,
- **B)** draft a quote-request email to Xiamen Haoyue with the exact model questions, or
- **C)** run the same research for a different model/size?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=10729] [Handoff context — this Telegram topic (thread 10729) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/handoffs/HANDOFF_MANIFEST.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

Today Paying a visit to the manufacturers of these mobile capsules which I got to inspect while out in Inner Mongolia 

My sense is the thesis for climate change is somewhat holistic and complete 

Either we help reduce the impact of climate change through circular economy through regenerate supply chain like our cacao model or when they experience devastation of the climate change we sell them access to affordable infrastructure to continue living a life

It might be possible then to borrow SOHA’s David’s model. If the new mobile capsule residents are too broke to pay off all upfront we put a lien on their property and then sell it off. That was how he aggregated and have around 1% of the entire Texas property finance flow through him


### 🤖 Autopilot

Gary — this is a meaty strategic thread. Before I respond on the SOHA/David lien model and whether this is an execution handoff, let me check the registry and dig up what's already in our context on SOHA, liens, and any capsule-home plan.


### 🤖 Autopilot

Let me check whether there's any existing plan or context on this housing/climate thread before I respond.


### 🤖 Autopilot

No existing plan or context on capsule housing — this is a fresh strategic thread, not a handoff. Let me do one quick check on the David/SOHA lien model you referenced so my pushback is grounded, not vibes.


### 🤖 Autopilot

This is a strategic brainstorm, not a handoff — no plan exists in the registry, and "mobile capsule" has zero matches in our context. Here's my honest take.

## Where I agree with you
- **The climate thesis is coherent and holistic.** Two-sided: (1) reduce impact via regenerative/circular supply chains (our cacao model); (2) when climate events destroy housing, provide *affordable, quickly-deployable infrastructure* — mobile capsules hit that exactly. It's "mitigation today, resilience/response tomorrow." This is genuinely aligned with the mission (10,000 ha of Amazon rainforest / regeneration), and the capsule angle gives the DAO a **second, physical asset class** beyond cacao bags.
- **Visiting the manufacturer in Inner Mongolia is the right move** — inspecting actual product beats all the Alibaba pricing I can pull.

## Where I'd push back hard — the lien model as described
The way you phrased it — *"too broke to pay upfront → we put a lien on their property and sell it off"* — has a serious flaw I want to flag before it becomes strategy:

1. **Broke people don't have property to lien.** The lien works in David Campbell's model because his customers are **owner-financing Texas property** — they have the *land* as collateral. Climate-displaced capsule residents are, by definition, people who just **lost their home and land**. You can't secure a loan against collateral the disaster already destroyed. That's the core mismatch.

2. **A lien isn't a sale.** Even in Texas contract-for-deed, if you repossess, you have to follow a strict foreclosure/repossession process — and you're left holding a **used, depreciated mobile capsule** that cost you $5–12k to import and can't be repossessed across state lines easily. The "sell it off" recovery leg is much weaker than it sounds.

3. **It puts you in the repo business**, with all the optics/regulatory weight of predatory lending — which would poison the *other* side of your thesis (the regenerative, mission-driven brand).

## What *does* work (the model I'd actually borrow from David)
The durable insight isn't the lien — it's **installment ownership / revenue-backed financing**, done right:

| Element | How it could work for capsules |
|---|---|
| **Keep the asset as collateral** | Sell the *house* on an installment contract, but title stays with you until paid — the capsule IS the collateral (like David's deeds). This works even with no land. |
| **Repossession ≠ repo** | Structure terms so default → you reclaim the **module**, refurbish, redeploy. It's an asset, not a family's land. Less brutal optics. |
| **Land lease, not sale** | Where residents are on rented/leased land, you're selling a movable asset — much cleaner legally than real-property liens. |
| **Rent-to-own / subscription** | $X/month with title transfer at end — converts "too broke for upfront" into a cash-flow stream with a path to ownership. |
| **DAO-compatible** | This is exactly a **revenue-backed instrument** — you could tokenize the payment stream, and record capsule custody via QR/ledger (same TRUECHAIN pattern as cacao bags). The DAO's whole identity pipeline (QR registration → inventory movement → sale) maps 1:1 onto physical capsules. |

The real model that fits: **asset-backed installment sales with the unit as collateral**, on **leased land**, with clean repossession/refurb/redeploy. That's David's insight minus the parts that don't survive contact with a disaster zone.

## What I need from you to go deeper
This isn't in any existing plan or handoff. To turn it into an actionable plan I'd want to know:
1. **Who is the buyer?** Disaster-displaced families (retail), NGOs/FEMA-like orgs (B2G), insurers, or a mix?
2. **What's the financing surface?** Is the DAO itself the lender (balance-sheet), or a broker/facilitator matching third-party capital?
3. **Geography?** US (where SOHA/Texas context applies) or Latin America (where our rainforest mission is)?
4. **Is the capsule the unit of sale, or the "house + installation + hookup" package?**

I can turn this into a **CAPSULE_HOUSING_PLAN.md** in the handoff registry with a proper phase-1 (manufacturer visit checklist, cost model per unit, financing structure options, DAO ledger integration for capsule custody) — just say the word, or if you'd rather I keep it in this thread, I'll build the cost-model + financing-structure research next.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=10729] generate your insights as a PDF?


### 🤖 Autopilot

Gary — on it. Let me render the insights into a branded PDF and deliver it into this thread.


### 🤖 Autopilot

PDF generated. Sending it into this thread now.


### 🤖 Autopilot

✅ Sent — **`capsule_housing_insights.pdf`** posted into this thread (message 10771).

**The PDF covers:**
1. **Climate thesis** — mitigation (regenerative supply chains) + resilience (affordable post-disaster infrastructure)
2. **HS/HTS classification** — China 9406.90.00.90 → US 9406.90.01.30, ~40.4% duty stack
3. **Cost research** — FOB $4,000–7,500, freight $2,400–6,000, landed ≈ **$9,600–18,500** with worked examples
4. **The lien-model pushback** — broke people don't have collateral; the insight is installment ownership with the *capsule itself* as collateral, not land liens
5. **DAO-compatible financing structure** — rent-to-own, land lease, QR/ledger custody mapping 1:1 from cacao bags
6. **Open questions** (buyer, lender role, geography, unit of sale) + manufacturer-visit checklist

Want me to also push this into the repo (e.g. `agentic_ai_context` as a draft plan) or iterate on any section — e.g. build the full **CAPSULE_HOUSING_PLAN.md** for the handoff registry?

