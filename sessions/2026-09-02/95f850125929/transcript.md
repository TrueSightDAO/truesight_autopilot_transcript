# Autopilot Session — 2026-09-02

**Session**: `95f850125929`

**Governor**: Gary Teh


---


### 🧑 Governor

[observed, not directed at you — Nobody Will not DM you]: Can you find the supplier for cacao bean cracking and winnowing machine Alibaba listing

---

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=19718]


### 🤖 Autopilot

The context flags this as observed in-thread (not a direct ask to me), but it's a benign research request — let me check whether the DAO context already names a supplier/facility before I answer from the open web.


### 🤖 Autopilot

The DAO context has a "processing cost" concept but let me check the relevant section of the supply-chain doc (it mentions facility rows with contact/Alibaba columns) and any processing-cost sheet before answering purely from the web.


### 🤖 Autopilot

Here's what I found — treating this as observed ambient chatter (noted "Nobody Will not DM you"), so no outreach or actions taken on my side, just research.

**DAO context first:** There's no Alibaba cracker/winnower machinery supplier recorded anywhere in the context. The only "Alibaba" references in the ledgers are **kraft pouch stock** (supplier ref `269035810001023771`, ShenZhen Source Pack Co Ltd / Jessie Peng — packaging, not machinery), and the **Agroverse Cacao Processing Cost** sheet lists Brazilian *service* processors who do almonds→nibs by hand (Wesley–CIC @ R$7.5/kg, Santos @ R$8.7/kg), with WhatsApp contacts — no machines.

**Supplier candidates on Alibaba (live web):**

| Supplier / Brand | Product | Price (list) | Notes |
|---|---|---|---|
| **QDMECH** (m.alibaba.com showroom "cacao-winnower-for-sale") | Small Cocoa Peeling Machine / Coffee Bean Huller / Cacao Sheller | ~$639–940/set | Small-scale, single piece MOQ — best match for craft volumes |
| **Henan Qinbiao Industrial Development Co., Ltd.** | Cacao Sheller and Winnower, Small Cocoa Beans Sheller | $850–940, MOQ 1 pc | Verified 4-yr supplier, 4.2/5.0 rating |
| **Zhengzhou Auris Machinery Co., Ltd.** | Commercial Cocoa Bean Cracker and Winnower | $1,800–2,000 | Larger commercial duty |
| **ORME** (brand, via alibaba showroom) | Cocoa Pod Shell / Dehull / Peel-Cracking Winnow Machine | — | Cacao-specific line |
| **Sunrise Machinery** (via alibaba supplier analysis) | Cocoa bean winnowing machine, food-grade SS, >98% shell removal | $1,500–4,000 | Cocoa-specialist, 5–15 day sample lead |
| **Henan Unio** | Cocoa & Coffee Dehusking Winnower 220V 2.2kW | ~$800–2,500 | Mid-scale |
| General category page: **alibaba.com/countrysearch/CN/cocoa-bean-cracker.html** — 481 cocoa-bean-cracker listings, incl. "High Quality Cocoa Bean Cracker & Winnower, 300–400 kg/h, PSO Brand, $750" | | | |

**Relevance to the DAO:** cracking + winnowing is the almonds→nibs step currently outsourced to Wesley–CIC / Santos at ~R$7.5–8.7 per kg of nibs. If the conversation is about bringing that step in-house (Ilhéus facility), the small QDMECH-type units ($640–950) are the scale-comparable tier — but this is analysis only, and I have no record of a machinery purchase plan in the backlog.

**Suggested next step (needs a governor's go):** if Gary/Nobody wants, I can (a) pull the top 2–3 full product pages (specs: capacity kg/h, SS grade, motor, voltage for Brazil 220V/60Hz) and paste them here, (b) open an Alibaba RFQ draft, or (c) log "cacao cracking/winnowing machine sourcing" as a Pending item in OPEN_FOLLOWUPS.md so it isn't lost. Which one — or leave it for whoever raised it?


### 🧑 Governor

[observed, not directed at you — Nobody Will not DM you]: https://www.amazon.com/dp/B0CZ3LT543?ref=ppx_pop_mob_ap_share

This is for roasting

---

[observed, not directed at you — Nobody Will not DM you]: Also need a melanger. Could you find one on Alibaba

---

[Telegram context: chat_id=-1003919341801, thread_id=19718]


### 🤖 Autopilot

Two more observed research items in the thread — the roaster (Amazon ASIN) and a melanger sourcing ask on Alibaba. Let me pull both before answering.


### 🤖 Autopilot

Both observed items pulled. Here's the research digest:

## 1. Roaster — Amazon ASIN B0CZ3LT543 (reality-check)

| Field | Value |
|---|---|
| Product | **ATOLOMOTOR 110V-240V Electric Coffee Roaster** — roller-type drum, stainless steel |
| Capacity | **250 g** |
| Power | **14 W** (very low — this is a rotating-drum warmer, not a true convection roaster) |
| Rating | 3.5★ with only **2 reviews**; BSR #4.2M in Home & Kitchen |
| Manufacturer | "KathyLiely" (generic marketplace seller brand) |

**Flags for cacao use:** 250 g/batch is hobby-scale — for context, our *smallest* outsourced processing runs (Wesley–CIC) were 160 kg of nibs; Santos works per-kg. Cacao roasting also wants 120–150 °C with airflow + chaff management; a 14 W roller drum at 250 g won't match craft batch volumes. If this is for **recipe/experiment development** at home scale it's fine-ish, but if it's meant as production roasting for Agroverse, I'd treat it as a sampler, not the real unit. (Also: it's spec'd for coffee/peanuts — no cacao endorsement in the listing.)

## 2. Melanger — Alibaba candidates

| Supplier / listing | Capacity | Price | Notes |
|---|---|---|---|
| [Chocolate Melanger — Cocoa Nibs Grinder Refiner, Stone Mill](https://www.alibaba.com/countrysearch/CN/chocolate-melanger.html) | 4L / 10L | **$1,600–1,800** /set | 12-yr CN supplier, MOQ 1 set |
| [Chocolate Melanger Machine Twin Stone Grinder](https://www.alibaba.com/product-detail/Chocolate-Melanger-Machine-Twin-Stone-Grinder_1601718355139.html) | twin-stone, nib refining + conching | **$3,340** (1 pc) | Larger commercial class |
| Chocolate Stone Grinder Melanger (French Alibaba listing) | 350×450×600 mm (40 kg) up to 1160×800×1290 mm (280 kg) | — | 220V 50Hz, **550 W → 2.2 kW**, SS — note 50 Hz matters for Brazil (60 Hz) |
| Chocolate Melanger (chocomachines.com) | 7L / 25L / 60L per batch | — | Bean-to-bar line reference |

**DAO tie-in:** the melanger is the nibs→mass/bar step currently outsourced — Santos charges R$40/kg (nibs→bars) and Wesley–CIC R$48.5/kg; Dennis Lim's Shiok Kitchen does it at **US$10/kg** in Menlo Park. A 4–10L melanger ($1.6–1.8k) is the craft-tier match if in-house refining is ever on the table — and it would need **220V/60Hz** confirmation for Brazil (several listings are 50 Hz, which would need a converter or a 60 Hz variant).

Still all ambient chatter on my side — no outreach, no actions taken. Want me to (a) pull full specs on the 4–10L melanger listing, (b) check whether this Amazon roaster has any cacao-specific reviews via a deeper search, or (c) leave it here for whoever's driving that conversation?

