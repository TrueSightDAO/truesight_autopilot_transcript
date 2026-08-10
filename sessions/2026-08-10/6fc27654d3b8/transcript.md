# Autopilot Session — 2026-08-10

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


### 🤖 Autopilot

There's a Grok vision client on the box. Let me use it to actually see the image.


### 🤖 Autopilot

The key is in the autopilot's own .env. Let me load it and run Grok vision.


### 🤖 Autopilot

Grok vision read the label as **"Haoyue T5"** — a prefabricated modular cabin/tiny home (white structure with orange accents), not a car. Let me verify what product this actually is and pin down the correct classification.


### 🤖 Autopilot

Grok read the label as **"Haoyue T5"** — a white prefabricated modular cabin/tiny home with orange accents. Given you said "HaoYue15," this is the Haoyue brand modular prefab house. Now let me pin down the exact China HS code (8-digit) and US HTS code (10-digit) for prefabricated buildings.


### 🤖 Autopilot

I have the classification confirmed. Let me check the latest tariff status (Section 301 + IEEPA "reciprocal" tariffs, which changed a lot in 2025) so the duty figures are current, not stale.


### 🤖 Autopilot

Tariff landscape confirmed (SCOTUS struck down IEEPA Feb 2026; Section 301 25% remains; Section 122 10% replaced by new forced-labor 301 tariff in July 2026). Let me verify the authoritative current HTS structure and the exact China export code.


### 🤖 Autopilot

I have everything I need. Let me persist the image analysis to the transcript per the attachment workflow, then give you the answer.


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

