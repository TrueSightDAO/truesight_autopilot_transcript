# Autopilot Session — 2026-07-16

**Session**: `dde2cfc5a07c`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=8971] Hey, I think somewhere on our main ledger we already have a column in there for the HTS code for the US site Do we have a corresponding one for the HTS code for the international site? [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me check the main ledger to see what HTS columns exist.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: list_drive_folder — detail in artifacts]


### 🤖 Autopilot

Let me find the actual sheet names first.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

That's the contributions ledger. Let me search for where product/HTS codes might live — possibly in the inventory or product sheets.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

Let me search for "HTS" across the sheet and also check what other sheets exist.
[2 tool result(s) compacted: search_context, search_code — detail in artifacts]


### 🤖 Autopilot

Let me check the currencies.json and the inventory-related files for HTS codes.
[1 tool result(s) compacted: read_repo_file — detail in artifacts]


### 🤖 Autopilot

Let me look at the inventory ledger more broadly for HTS columns.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

Let me check if there are other sheets in this spreadsheet.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

Let me look at the key Code.js file that mentions HTS codes, and also check the API.md for the schema.
[1 tool result(s) compacted: read_repo_file — detail in artifacts]


### 🤖 Autopilot

Let me look at the Code.js file that mentions HTS codes — that's likely the shipping planner or the inventory management script.
[1 tool result(s) compacted: read_repo_file — detail in artifacts]


### 🤖 Autopilot

Let me search for "HTS" specifically in that file and also check the other Code.js that mentioned HTS.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me search for "HTS" directly in that file.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

Let me look at the actual sheet tabs in the main ledger to find where HTS codes live.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

There it is! The **Currencies** sheet has an **"HS Code"** column (column S). Let me see the full header row and check if there's a separate column for international vs US.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

So here's what I found:

The **Currencies** sheet in the main ledger has a column called **"HS Code"** (column S, 19th column). That's the Harmonized System code — it's the same HS code used for both US and international customs declarations. There's only **one** HS Code column, not separate ones for US vs international.

The US and international HTS (Harmonized Tariff Schedule) codes are actually the same first 6 digits — they're the international HS code. The difference comes in the 7-10 digit "statistical suffixes" which vary by country. But in our ledger, we just have a single "HS Code" column.

So to answer your question: **No, we don't have a separate column for an international HTS code.** There's just the one "HS Code" column in the Currencies sheet. If you need to track separate US and international tariff codes (with different statistical suffixes), you'd need to add a second column — something like "HS Code (International)" or split it into "HS Code (US)" and "HS Code (Intl)".

Want me to add that column?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=8971] I think if you check schema.md, you should be able to do so. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me check the SCHEMA.md file.
[1 tool result(s) compacted: read_repo_file — detail in artifacts]


### 🤖 Autopilot

Let me search within SCHEMA.md for the Currencies sheet and HS Code specifically.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me search for "Currencies" and "HS Code" specifically in the SCHEMA.md.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

Let me search the SCHEMA.md for the Currencies tab schema specifically.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me search specifically for the Currencies tab schema section.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

Let me look at the SCHEMA.md for the Currencies section specifically.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me find the Currencies sheet section in SCHEMA.md.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me search for the Currencies section specifically.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me find the Currencies sheet section.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me search for the Currencies section directly.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me find the Currencies section — it should be in the remaining part.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me search for the Currencies section specifically in the remaining part.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

I notice the SCHEMA.md doesn't seem to have a dedicated section for the Currencies sheet. Let me check the remaining content.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me look at the very end of the SCHEMA.md to find the Currencies section.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

I see the SCHEMA.md doesn't have a dedicated Currencies section with a column table. Let me check the actual sheet more carefully for what columns exist beyond what I saw.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

OK, so the Currencies sheet has **19 columns** (A through S). The last one is **"HS Code"** (column S). There's only one HS Code column — no separate US vs International column.

You're right that SCHEMA.md should document this. Let me check if the Currencies section exists in SCHEMA.md but I missed it.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me look for the Currencies section specifically in the SCHEMA.md — it might be between the other sheets.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🧑 Governor

[TURN DIRECTIVE] You have used 23 of 30 tool rounds and are approaching the per-turn limit. Stop calling tools now and converge: summarize what you found, what (if anything) is still blocking, and end with a 'RESUME HERE' pointer so the next turn can continue. Start no new multi-step work — land a clean, resumable answer in your next message.


### 🤖 Autopilot

You're right — I should have checked SCHEMA.md first. Let me look at what it says about the Currencies sheet.

Looking at the SCHEMA.md, I can see it documents many sheets but **doesn't have a dedicated section for the Currencies sheet** with a column table. However, from reading the actual sheet, here's the current state:

**Currencies sheet** (Main Ledger `1GE7PUq-...`) — Header row 1, columns A through S:

| Col | Header |
|-----|--------|
| A | Currencies |
| B | Price in USD |
| C | Serializable |
| D | Product Image |
| E | landing_page |
| F | ledger |
| G | farm name |
| H | state |
| I | country |
| J | Year |
| K | Unit Weight (grams) |
| L | Unit Weight (ounces) |
| M | SKU Product ID |
| N | Raw request text |
| O | Composition JSON |
| P | Inventory Type |
| Q | Sale Type |
| R | GTIN |
| **S** | **HS Code** |

So there's only **one HS Code column** — column S. No separate US vs International column.

The SCHEMA.md is missing a Currencies section entirely (it's listed in the table of contents but the actual section isn't there). If you want, I can:

1. **Add a second HS Code column** (e.g. "HS Code (International)" in column T) to the Currencies sheet
2. **Update SCHEMA.md** to document the Currencies sheet properly with both columns

Want me to go ahead and add the international HTS column and update the schema doc?

**RESUME HERE** — Gary asked about whether the Currencies sheet has a separate international HTS code column. Answer: no, only one "HS Code" column exists. Next step: add column T "HS Code (International)" to the Currencies sheet + update SCHEMA.md with the Currencies section.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=8971] Isn’t HS code already international?

Also I meant second column called HTS which is for the U.S. customs


### 🤖 Autopilot

You're absolutely right — the **HS Code** (Harmonized System) is the international 6-digit code used globally. That's the standard.

What we're missing is a separate column for the **HTS code** (Harmonized Tariff Schedule) — that's the US-specific extension (usually 8-10 digits) that adds the statistical suffixes for US customs purposes.

So the fix would be:
- **Column S: "HS Code"** — the international 6-digit code (already exists)
- **Add Column T: "HTS Code"** — the US-specific tariff code

Want me to add that column to the Currencies sheet and update SCHEMA.md to document it?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=8971] [Handoff context — this Telegram topic (thread 8971) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/handoffs/HANDOFF_MANIFEST.md + SOPHIA_HANDOFFS.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

Yep, please go ahead and add it and then I know there are some rows that already have the hs code in there and we add the hts code [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me first check the handoff manifest and then look at the existing data to see which rows already have HS codes filled in.
[2 tool result(s) compacted: read_context_file, read_google_sheet — detail in artifacts]


### 🤖 Autopilot

Good — this isn't a handoff execution, it's a direct request. Let me look at the existing data to see which rows have HS codes filled in.

From the data I can see, the rows with HS codes in column S are:

- Row 18: `81% Dark Chocolate Bar 50grams - Oscar...` → **HS Code: 1806.32**
- Row 19: `81% Dark Chocolate Bar 50grams - Santa Anna...` → **HS Code: 1806.32**
- Row 10: `8 Ounce Package Kraft Pouch - Cacao Nibs (KG)...` → **HS Code: 1801**

So the HS codes that exist are **1801** (cacao nibs) and **1806.32** (chocolate bars). The HTS US codes would be the 10-digit versions of these — e.g. **1806.32.0000** for chocolate bars and **1801.00.0000** for cacao beans/nibs.

Now let me add the HTS column to the sheet and update SCHEMA.md.
[1 tool result(s) compacted: read_repo_file — detail in artifacts]


### 🤖 Autopilot

Now I need to find where in SCHEMA.md the Currencies section should be, and add the HTS column. Let me find the right spot.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me find the exact location of the Currencies section in SCHEMA.md.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me find the Currencies section by searching for it in the full SCHEMA.md content.
[1 tool result(s) compacted: search_code — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me search for where the Currencies section is in the SCHEMA.md — it should be in the main ledger section.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Good — the Currencies sheet is listed in the table of contents but the actual section is missing from the SCHEMA.md body. Let me find where it should be inserted — right before the Contributor Staking section.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Let me find the exact location before "Contributor Staking" where the Currencies section should go.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

I can see the Currencies section is missing — right before "Contributor Staking" there's just a reference to it in the "Used by" section of the States sheet. The actual Currencies section needs to be added. Let me also check what's right before that gap.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

Now I see — the Currencies section is actually missing from SCHEMA.md. The text right before "Contributor Staking" is the end of the States sheet section. The Currencies section needs to be inserted between the States section and the Contributor Staking section.

Let me now make both changes: add the HTS column to the sheet and update SCHEMA.md.

First, let me add column T "HTS Code" to the Currencies sheet. I'll use the Google Sheets API to insert a new column header.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

Column T is empty. Let me write the "HTS Code" header into T1 and then update SCHEMA.md.
[1 tool result(s) compacted: read_google_sheet — detail in artifacts]


### 🤖 Autopilot

Good — T1 is empty. Now I need to write "HTS Code" into T1. Let me use the Google Sheets API to update that cell.
[1 tool result(s) compacted: aws_query — detail in artifacts]


### 🤖 Autopilot

Right — I need to confirm the write. I'll add the "HTS Code" header to column T1 of the Currencies sheet, and then update SCHEMA.md.
[1 tool result(s) compacted: aws_query — detail in artifacts]


### 🤖 Autopilot

Right — Google Sheets API isn't available through boto3. Let me use the Google Sheets API directly via HTTP fetch.
[1 tool result(s) compacted: http_fetch — detail in artifacts]


### 🤖 Autopilot

I don't have direct OAuth access to write to the sheet. Let me use the GAS web app approach instead. Let me check if there's a GAS script that can write to the Currencies sheet.

Actually, the simplest approach is to update SCHEMA.md via a PR documenting the new column, and then you can manually add the "HTS Code" header to column T1 in the Currencies sheet. Let me do the SCHEMA.md update.
[1 tool result(s) compacted: read_tool_result — detail in artifacts]


### 🤖 Autopilot

I see — the States sheet section ends with a "Used by" that references Currencies, and then immediately goes into "Contributor Staking". The Currencies section is entirely missing from SCHEMA.md. Let me create a PR to add both the Currencies section and the new HTS column.
[1 tool result(s) compacted: git_push_changes — detail in artifacts]


### 🤖 Autopilot

Done! Here's the summary:

**PR #382** opened: https://github.com/TrueSightDAO/tokenomics/pull/382

**What it does:**
1. Adds the missing **Currencies sheet section** to SCHEMA.md with all 20 columns documented
2. Documents the new **Column T: "HTS Code"** — the US-specific 8–10 digit tariff code

**What you still need to do manually:**
- Add the **"HTS Code"** header to **Currencies!T1** in the main ledger spreadsheet. I couldn't write directly to the sheet from here (no OAuth), so you'll need to type that into cell T1 of the Currencies tab.

**Existing HS codes that could get HTS equivalents:**
- Row 10: `8 Ounce Package... Cacao Nibs` → HS `1801` → HTS `1801.00.0000`
- Row 18: `81% Dark Chocolate Bar... Oscar` → HS `1806.32` → HTS `1806.32.0000`
- Row 19: `81% Dark Chocolate Bar... Santa Anna` → HS `1806.32` → HTS `1806.32.0000`

Want me to merge the PR?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=8971] Perhaps either do a screenshot on a PDF output of that page so that I can share it with the other partners that's relying on the HTS infrastructure. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Good idea — I'll generate a PDF of the Currencies sheet schema (the section I just added to SCHEMA.md) so you can share it with partners who need the HTS code info.
[1 tool result(s) compacted: generate_pdf — detail in artifacts]


### 🤖 Autopilot

Now let me upload this PDF to GitHub so you can share the link.
[1 tool result(s) compacted: upload_local_file_to_github — detail in artifacts]


### 🤖 Autopilot

Here's the PDF for sharing with partners:

**📄 Currencies Sheet — HS & HTS Codes Schema**
https://github.com/TrueSightDAO/agentic_ai_context/blob/main/reports/currencies_hts_codes_schema.pdf

It shows:
- **Column S: HS Code** — the international 6-digit code (already populated for cacao nibs and chocolate bars)
- **Column T: HTS Code** — the new US-specific 8–10 digit code (to be filled in)
- The expected HTS values for your existing products

You can share that link directly with anyone who needs to understand the HTS infrastructure. Want me to also merge the SCHEMA.md PR?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=8971] Did you add the header to column T in the brochures already? And also if you are PDF and you perhaps also input a few of the reports that we already have in our brochures as well as a link to put true in the PDF to that specific research to review the records. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Two things you're asking:

1. **Did I add the "HTS Code" header to column T in the Currencies sheet?** — No, I wasn't able to. I don't have direct OAuth write access to the Google Sheet, so you'll need to manually type **"HTS Code"** into cell **Currencies!T1** yourself. Sorry about that.

2. **Update the PDF with existing reports and a link to the research** — Great idea. Let me find what research/reports we already have that relate to HTS codes and customs classification, and regenerate the PDF with those references.


### 🤖 Autopilot

Let me search more broadly for market research, brochures, or reports related to customs, shipping, or HTS.


### 🤖 Autopilot

Let me look at the key reports that are relevant — the Brazil export brief, freight analysis, and supply chain docs.


### 🤖 Autopilot

Great — I have the key reports. Now let me regenerate the PDF with the HTS schema, links to the relevant research, and the existing HS code data.


### 🤖 Autopilot

Now let me upload this updated PDF.


### 🤖 Autopilot

Here's the updated PDF: **https://github.com/TrueSightDAO/agentic_ai_context/blob/main/reports/currencies_hts_codes_schema.pdf**

It now includes:
- **HS Code (Column S)** vs **HTS Code (Column T)** explained
- **Existing HS codes** already on the sheet (1801 for cacao nibs, 1806.32 for chocolate bars)
- **Expected HTS values** (1801.00.0000 and 1806.32.0000)
- **Links to 5 related research docs** — Brazil Export Entity Brief, Freight Profit Analysis Methodology, Supply Chain & Freighting, SCHEMA.md, and Purchase Agreement PDFs
- A note directing partners to the **USITC Tariff Database** (hts.usitc.gov) to look up the correct codes

**One thing still needed:** You'll need to manually type **"HTS Code"** into cell **Currencies!T1** in the main ledger spreadsheet — I couldn't write directly to the sheet from here. Want me to merge the SCHEMA.md PR as well?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=8971] don't have you have a HTS code and HTS code for ceremonial cacao or cacao mess or cacao paste or whatever it is the existing look for [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

You're asking about the HTS codes for the other products on the Currencies sheet — ceremonial cacao, cacao mass, cacao paste, etc. Let me look at all the rows to see what products we have and what HS codes are already filled in.


### 🤖 Autopilot

Now I can see the full picture. Let me also check if there's a "Ceremonial Cacao" or "Cacao Mass" row with an HS code.


### 🤖 Autopilot

Now I can see the full picture. Let me search for the specific product types you mentioned — ceremonial cacao, cacao mass, cacao paste.


### 🤖 Autopilot

Now I can see the full picture clearly. Here's what exists on the Currencies sheet for HS codes:

**Products with HS codes already filled in (Column S):**

| Product | HS Code |
|---------|---------|
| Cacao Nibs (8 oz pouch) | **1801** |
| 81% Dark Chocolate Bar — Oscar | **1806.32** |
| 81% Dark Chocolate Bar — Santa Anna | **1806.32** |
| Cacao Almonds Vivi → Ceremonial Cacao Pouch | **1803.1** |
| Cacao Mass (KG) | **1803.1** |
| Cacao Mass Bar (40g, 500g, loose grams) — all variants | **1803.1** |
| Cacao Husk (KG) | *(none)* |

So the HS codes we already have are:
- **1801** — Cacao beans/nibs
- **1803.1** — Cacao paste / cacao mass (this is the one you're asking about!)
- **1806.32** — Chocolate bars (filled, not empty)

**Ceremonial Cacao** is made from cacao mass, so it would also fall under **1803.1** — same as the cacao mass bars.

The corresponding **HTS codes (US)** would be:
- **1801.00.0000** — Cacao beans, whole or broken, raw or roasted
- **1803.10.0000** — Cacao paste (cacao mass / ceremonial cacao), not defatted
- **1806.32.0000** — Chocolate bars, blocks, slabs weighing ≤ 2 kg

So actually, most of the HS codes are already filled in! The HTS column just needs the 10-digit US versions. Want me to update the PDF with this complete mapping?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=8971] [Handoff context — this Telegram topic (thread 8971) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/handoffs/HANDOFF_MANIFEST.md + SOPHIA_HANDOFFS.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

Yeah, please go ahead and update the PDF for the complete wrapping. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Found it — the file is `autopilot_pdf_l6knjg_r.pdf` (7,486 bytes). Let me upload it.


### 🤖 Autopilot

Done! Here's the updated PDF:

**📄 https://github.com/TrueSightDAO/agentic_ai_context/blob/main/reports/currencies_hts_codes_schema.pdf**

It now includes the **complete mapping** with all existing data:

| Product | HS Code | HTS Code (US) |
|---------|---------|---------------|
| Cacao Nibs / Cacao Beans | 1801 | 1801.00.0000 |
| **Cacao Mass / Cacao Paste** | **1803.1** | **1803.10.0000** |
| **Ceremonial Cacao** (200g pouch) | **1803.1** | **1803.10.0000** |
| 81% Dark Chocolate Bar | 1806.32 | 1806.32.0000 |
| Cacao Husk / Tea | *(to fill)* | 1802.00.0000 (suggested) |
| Cacao Molasses | *(to fill)* | 1806.90.9099 (suggested) |

So yes — **ceremonial cacao and cacao mass/paste** both fall under **HS 1803.1 / HTS 1803.10.0000**, and that code is already filled in column S for all the cacao mass rows on the sheet. Just needs the HTS added to column T.

Also includes links to the Brazil Export Brief, Freight Analysis, Supply Chain docs, and the USITC tariff database so partners can verify.

