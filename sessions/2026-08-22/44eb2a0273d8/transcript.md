# Autopilot Session — 2026-08-22

**Session**: `44eb2a0273d8`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=13042] Remove the 3rd slide and then return it


### 🤖 Autopilot

The governor wants slide 3 removed from the EBCF Manicoré presentation (13-page PDF, `a7bf0c55a4aa4decbf4349290b4fc413.pdf` — same file as `8af93233d4964fc9a0124243dbbc3ca1.pdf`). Slide 3 = "Preliminary supply estimate Manicoré region". Let me verify the file and check the PDF tooling on the box.


### 🤖 Autopilot

Both `pymupdf` and `pypdf` are available. Let me confirm which page is slide 3 by extracting per-page text.


### 🤖 Autopilot

Page 3 confirmed as the "PRELIMINARY ESTIMATE OF POTENTIAL SUPPLY: MANICORÉ REGION" slide. Removing it now:


### 🤖 Autopilot

Removed slide 3 and now returning the updated PDF:


### 🤖 Autopilot

Done. ✅

**Removed slide 3** — *"PRELIMINARY ESTIMATE OF POTENTIAL SUPPLY: MANICORÉ REGION"* (the supply estimate / analysis levels slide) from the EBCF Manicoré Bioeconomy presentation.

**Result:**
- Original: 13 pages (6.7 MB)
- New: **12 pages** (6.7 MB) — slide 3 gone, slides 4–13 shifted up intact
- Verified each remaining page's content is preserved (slide order 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

The updated PDF was returned to this thread as an attachment: `ebcf_manicore_no_slide3.pdf`.

If you need the original back as well, or want a different slide removed/adjusted, just say the word.

———
**✅ Done this turn — actions taken:**
• `ssh run` ×3 → ls -la /tmp/tg_attachments/a7bf0c55a4aa4decbf4349290b4fc413.pdf && python3 -c "import fitz; print('pymupdf ok')" 2>/dev/null; python3 -c "im; python3 - <<'EOF' import fitz doc = fitz.open("/tmp/tg_attachments/a7bf0c55a4aa4decbf4349290b4fc413.pdf") print("pages:", len(doc)) for i, p; python3 - <<'EOF' import fitz src = fitz.open("/tmp/tg_attachments/a7bf0c55a4aa4decbf4349290b4fc413.pdf") out = fitz.open() # pages 1,2 then


### 🧑 Governor

Deck trimmed to 8 slides — Benchmark & Thank You pages removed, per your screenshot. Now: Park land → Açaí (×2) → Cacao → Municipality → 20,000 ha → Communities (~100,000 ha) → 400 ha SAF.

[Attachment auto-processed: **f8fe18ef49834fb1b6119ef3ef83cb81.pdf**]
- Type: PDF (8 pages, 2866 chars)

Extracted content:
```
--- Page 1 ---
LOCATION OF EBCF'S 10,000 
M2 LAND FOR THE 
INSTALLATION OF THE AGRO-
INDUSTRIAL PARK
PROJECTION OF THE FUTURE AGRO-INDUSTRIAL PARK OF EBCF

--- Page 2 ---
AÇAÍ FREEZE-DRYING – STAGE 1 AÇAÍ PROJECT

--- Page 4 ---
CACAO PRODUCTION · MANICORÉ
Cocoa · Agroforestry cultivation (SAF) · EBCF priority #3 · Target market: chocolate / functional foods
SUPPLY TRAJECTORY · MANICORÉ (t fruit / yr)
Current (sub)registered supply
300 · 500
Potential supply (not registered)
500 · 800
Captureable w/ structured program
700 · 1,000
Projected 2030 · base scenario
1,000 · 1,500
Projected 2035 · maturity scenario
1,500 · 2,500
Sourcing model:  Agroforestry cultivation (SAF) · extractivism + managed SAF
Ranked #3 in the Amazon Ingredients Matrix (EBCF priority list)
INDUSTRIAL REVENUE · CACAO (USD)
Stage 1 · Agro-industrial Park (initial)
900 t fruit  ·  ~101 t  (nibs, butter, dried almond)
@ USD 7 / kg  ·  USD 0.7 M / yr
Stage 2 · Expansion (2035 maturity)
2,000 t fruit  ·  ~225 t  (nibs, butter, dried almond)
@ USD 7 / kg  ·  USD 1.6 M / yr
ANVISA:  · approved
FDA:  ·· export-ready
Target market:  chocolate / functional foods · high added value
LAND FOOTPRINT · WHERE THE CACAO & THE PARK SIT
10,000 m²
Agro-industrial Park land ? EBCF, Manicoré
400 ha
open area for SAF cacao plantation (option to
buy / lease)
20,000 ha
EBCF properties in Manicoré
~100,000 ha
5 km extractive impact area · 80+ communities
EBCF · Manicoré, Amazonas  ·  Source: Bioeconomy Program · Master Plan Manicoré (supply & revenue scenarios)

--- Page 5 ---
MUNICIPALITY OF MANICORÉ
EBCF OFFICE IN MANICORÉ
AÇAÍ FACTORY IN MANICORÉ 
(LEASE WITH OPTION TO PURCHASE BY EBCF)
LOCATION: EBCF OFFICE AND AÇAÍ
FACTORY IN MANICORÉ

--- Page 6 ---
EBCF PROPERTIES IN MANICORÉ – 20,000 HA

--- Page 7 ---
5 KM RADIUS FOR EXTRACTIVE ACTIVITY 
IMPACTED AREA: ̃100,000 HECTARES
ID
Nome
1
Cristo_Rei
2
Auxiliadora
3
Santa_Fe
4
Laranjal
5
Santa_Maria_do_Marmelos
6
Marmelos
7
Santa_Helena
8
Cucura
9
Nazare_do_Retiro
10
Santa_Maria_De_Belem
11
Boca_do_Capana
12
Santo_Antonio
13
Agua_Azul
14
Boa_Esperanca
15
Escondido
16
Sao_Pedro_dos_Cardosos
17
Pocao
18
Barro_Alto
19
Esperanca
20
Estirao
21
Igarapezinho
22
Boa_Nova
23
Remanso
24
Ribamar
25
Barreira_do_Matupiri
26
Verdum
27
Santa_Cruz
28
Elegancia
29
Sao_Pedro
30
Delicia
31
Pinduri
32
Samauma
33
Boca_do_Atininga
34
Recreio_Atininga
35
Curralinho
36
jenipapo_I
37
Jenipapo
38
Nova_Esperanca
39
Cachoeirinha
40
Nova_Aparecida
41
Sao_Joao
42
Macaco_Prego
43
Itapinima
44
Sao_Pedro_do_Urua
45
Vencedor
46
Nazare_do_Urua
47
Sao_Carlos
48
Recreio
49
Dois_Irmaos
50
Santa_Rosa
51
Bacabal
52
Sao_Francisco
53
Terra_Preta_Capananzinho
54
Barreira_do_Capananzinho
55
Liberdade
56
Dotinha
57
Gonzaga
58
Pau_Queimado
59
Santa_Marta
60
Barreira_do_Curuca
80+ MAPPED EXTRACTIVE COMMUNITIES / 15 CURRENTLY SERVED BY EBCF (GREEN PIN)

--- Page 8 ---
OPEN AREA OF 400 HECTARES IN MANICORÉ FOR SAF (AGRO-FORESTRY SYSTEM) PLANTATION
OPTION TO BUY OR LEASE BY EBCF
```


### 🤖 Autopilot

The trimmed 8-slide deck is here. Let me verify it matches your described order and persist it to the transcript.


### 🤖 Autopilot

The 8-slide deck checks out — confirmed against the actual PDF:

**Verified order (matches your description exactly):**

| # | Slide |
|---|-------|
| 1 | Park land — 10,000 m², agro-industrial park projection |
| 2 | Açaí freeze-drying — Stage 1 |
| 3 | *(image-only Açaí slide — the ×2 block)* |
| 4 | Cacao Production · Manicoré (supply trajectory, revenue, land footprint) |
| 5 | Municipality of Manicoré (office + açaí factory) |
| 6 | EBCF Properties — 20,000 ha |
| 7 | 5 km radius extractive impact ~100,000 ha (60 communities listed, 80+ mapped / 15 served) |
| 8 | 400 ha SAF plantation — option to buy/lease |

**Checks:**
- Benchmark (slide 12) and Thank You (slide 13) — **removed** ✓
- 8 physical pages, no orphaned pages, all images intact (3–7 images per slide)
- `f8fe18ef…pdf` and `79e87418…pdf` are byte-identical (same MD5) — same file
- Slide 3 has no text layer (pure image) — that's why the auto-extraction jumped from Page 2 to Page 4

I've persisted the full deck content (including all 60 community names from slide 7) to the session transcript for cross-session recall.

The deck reads clean as a pitch flow: **land → product (açaí) → product (cacao) → place → scale → community → expansion option**. Nothing needed from me — but if you want any further trimming, reordering, or a text-layer pass on the image slides, say the word.

———
**✅ Done this turn — actions taken:**
• `ssh run` → md5sum /tmp/tg_attachments/f8fe18ef49834fb1b6119ef3ef83cb81.pdf /tmp/tg_attachments/79e87418300e464ca04001dbd9e3b184.pdf /tmp/tg_attachments
• `append to transcript` → https://github.com/TrueSightDAO/truesight_autopilot_transcript/blob/main/sessions/2026-08-22/4008a35ff7c9/transcript.md

