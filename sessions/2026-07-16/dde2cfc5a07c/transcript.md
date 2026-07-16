# Autopilot Session — 2026-07-16

**Session**: `dde2cfc5a07c`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=8971] Hey, I think somewhere on our main ledger we already have a column in there for the HTS code for the US site Do we have a corresponding one for the HTS code for the international site? [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me check the main ledger to see what HTS columns exist.


### 🤖 Autopilot

Let me find the actual sheet names first.


### 🤖 Autopilot

That's the contributions ledger. Let me search for where product/HTS codes might live — possibly in the inventory or product sheets.


### 🤖 Autopilot

Let me search for "HTS" across the sheet and also check what other sheets exist.


### 🤖 Autopilot

Let me check the currencies.json and the inventory-related files for HTS codes.


### 🤖 Autopilot

Let me look at the inventory ledger more broadly for HTS columns.


### 🤖 Autopilot

Let me check if there are other sheets in this spreadsheet.


### 🤖 Autopilot

Let me look at the key Code.js file that mentions HTS codes, and also check the API.md for the schema.


### 🤖 Autopilot

Let me look at the Code.js file that mentions HTS codes — that's likely the shipping planner or the inventory management script.


### 🤖 Autopilot

Let me search for "HTS" specifically in that file and also check the other Code.js that mentioned HTS.


### 🤖 Autopilot

Let me search for "HTS" directly in that file.


### 🤖 Autopilot

Let me look at the actual sheet tabs in the main ledger to find where HTS codes live.


### 🤖 Autopilot

There it is! The **Currencies** sheet has an **"HS Code"** column (column S). Let me see the full header row and check if there's a separate column for international vs US.


### 🤖 Autopilot

So here's what I found:

The **Currencies** sheet in the main ledger has a column called **"HS Code"** (column S, 19th column). That's the Harmonized System code — it's the same HS code used for both US and international customs declarations. There's only **one** HS Code column, not separate ones for US vs international.

The US and international HTS (Harmonized Tariff Schedule) codes are actually the same first 6 digits — they're the international HS code. The difference comes in the 7-10 digit "statistical suffixes" which vary by country. But in our ledger, we just have a single "HS Code" column.

So to answer your question: **No, we don't have a separate column for an international HTS code.** There's just the one "HS Code" column in the Currencies sheet. If you need to track separate US and international tariff codes (with different statistical suffixes), you'd need to add a second column — something like "HS Code (International)" or split it into "HS Code (US)" and "HS Code (Intl)".

Want me to add that column?

