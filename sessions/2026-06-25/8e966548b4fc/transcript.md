# Autopilot Session — 2026-06-25

**Session**: `8e966548b4fc`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Please inspect the attached file.

[Attachment auto-processed: **addec1320ccd4e1d9bbc2577db9fa508.jpg**]
- Type: Image (OCR confidence: 77.6%, quality: good)

Extracted text:
```
bof Pee 2 iwWOORIVers TON TO LAST ers = Ss - Shirley Lin® =. GamesBeatSummit SS 8 Al driven Web4, isn’t it already happening? Tiny Vikings - Texas A&M University United States 500+ connections She/Her fe aasim, Quynh and 41 other mutual a Satofo) aya -re1 (0a) Fics Highlights Fs] Shirley Lin® started a new position as Strategic Advisor at Tiny Vikings
```


### 🤖 Autopilot

Let me process this attachment.
[1 tool result(s) compacted: ocr_image — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: append_to_transcript — detail in artifacts]


### 🤖 Autopilot

Got it, Gary. Here's what the image shows:

**It's a LinkedIn screenshot of Shirley Lin's profile.** Key details:

- **Name:** Shirley Lin®
- **New role:** **Strategic Advisor at Tiny Vikings** (just started)
- **Background:** Texas A&M University, based in the United States
- **Connections:** 500+
- **Mutual connections:** aasim, Quynh, and 41 others
- **Also visible:** GamesBeatSummit, mentions of "AI driven Web4, isn't it already happening?"

Looks like a potential connection or lead worth noting. Shirley Lin has joined **Tiny Vikings** as a Strategic Advisor — Tiny Vikings could be relevant to our ecosystem (Web4 / gaming / AI). Want me to:

1. **Search for Tiny Vikings** to see what they do and whether there's a partnership angle?
2. **File a follow-up** in OPEN_FOLLOWUPS.md about Shirley Lin as a potential partner contact?
3. Something else?

———
**✅ Done this turn — actions taken:**
• `append to transcript` → Script exited 1: Traceback (most recent call last): File "/opt/truesight_autopilot/scripts/append_to_transcript.py", line 248, in <module> m


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=7699] Do you think you can help do a research online on all the web pages to find her email address for me? [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me search for Shirley Lin's contact info online.
[1 tool result(s) compacted: web_search — detail in artifacts]


### 🤖 Autopilot

Let me dig deeper specifically for the Shirley Lin who's a Strategic Advisor at Tiny Vikings.
[2 tool result(s) compacted: web_search, web_search — detail in artifacts]


### 🤖 Autopilot

Let me check the ZoomInfo result — that's the most promising lead for an email.
[1 tool result(s) compacted: web_extract — detail in artifacts]


### 🤖 Autopilot

ZoomInfo is paywalled. Let me try a few more angles.
[2 tool result(s) compacted: web_search, web_search — detail in artifacts]


### 🤖 Autopilot

Let me check the PGC Summit speaker page — that often has contact info.
[1 tool result(s) compacted: web_extract — detail in artifacts]


### 🤖 Autopilot

Let me also check if she has a presence on any other platforms that might list an email.
[2 tool result(s) compacted: web_search, web_search — detail in artifacts]


### 🤖 Autopilot

Let me check her personal contact page and also look for her on RocketReach.
[1 tool result(s) compacted: web_extract — detail in artifacts]


### 🤖 Autopilot

That's just a contact form, no public email. Let me check RocketReach for a more specific lead.
[1 tool result(s) compacted: web_extract — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: web_search — detail in artifacts]


### 🤖 Autopilot

Here's what I found, Gary.

**Shirley Lin (the one from your screenshot — LinkedIn: shirleylinc)** is a well-known figure in gaming/Web4. She's:
- **Strategic Advisor at Tiny Vikings** (new role)
- Co-founder & Managing Partner at **1000 Rivers**
- VP of BizDev at **Blueberry AI**
- Also associated with **FuturePIXEL**, **DOGI**, and emcee at **GamesBeat Summit 2025**

**On finding her email — here's what I turned up:**

Unfortunately, a direct public email for *this specific* Shirley Lin isn't freely available online. LinkedIn doesn't expose it, ZoomInfo and RocketReach have it behind paywalls, and her personal site (shirleylin.com) only has a contact form.

**What I *did* find that might help:**

1. **LinkedIn** — Her profile is `linkedin.com/in/shirleylinc`. You could send her an InMail or connect. She has 4,600+ followers and is active at gaming conferences.
2. **Her personal site** — `shirleylin.com/contact` has a contact form you can fill out.
3. **Facebook** — `facebook.com/shirleylinc` is listed as another contact point.
4. **ZoomInfo** has her email but requires a subscription.

**Best approach I'd suggest:** Connect on LinkedIn first — mention Tiny Vikings and GamesBeat Summit, and she'll likely respond. She's clearly active in the gaming/Web4 conference circuit and seems approachable based on her posts.

Want me to draft a LinkedIn outreach message or file a follow-up in OPEN_FOLLOWUPS.md to track this lead?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=7699] Do you have the coresondppng dao client for this Dapp

https://dapp.truesight.me/governor_contributor_admin.html


### 🤖 Autopilot

Let me look into what DAO client corresponds to that DApp page.


### 🤖 Autopilot

Let me also check the `dao_client` repo for the corresponding CLI tool.


### 🤖 Autopilot

That repo seems to have been renamed or moved. Let me check what's actually there.


### 🤖 Autopilot

Great — found it. Here's the picture:

**The DApp page** `governor_contributor_admin.html` (at `dapp.truesight.me/governor_contributor_admin.html`) is the **browser-based** way to add a contributor — it uses a browser digital signature.

**The corresponding DAO client** is the **`truesight-dao-add-contributor` CLI**, which lives in the **`dao_protocol`** repo (not `dao_client` — that repo seems to have been renamed/moved). Specifically:

- **Repo:** `TrueSightDAO/dao_protocol`
- **CLI command:** `truesight-dao-add-contributor`
- **Module:** `truesight_dao_client/modules/add_contributor.py`
- **Fields:** `--contributor-name`, `--contributor-email`

There's already a PR open for it — **dao_protocol PR #123**. It uses the same `build_event_cli` pattern as the partner add tool.

**Status:** PR #123 is open but not yet merged. Once merged and deployed to the autopilot box, I'll be able to run it directly when you say "add [name] as a contributor" — no browser needed.

Want me to check on PR #123's current state and see if it's ready to merge?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=7699] Merge it. 

The DApp requires that I provide email address. I don’t alway have the email address of DAO members 

Can we make the field optional? For both DAPP and dao cloent?


### 🤖 Autopilot

Let me check the current state of PR #123 and also look at the DApp page and CLI code to understand the email requirement.


### 🤖 Autopilot

I don't see PR #123 in the open list — it may have been closed or the number shifted. Let me check the actual `add_contributor.py` module and the DApp page to understand the email requirement before making changes.


### 🤖 Autopilot

The `add_contributor.py` module doesn't exist yet in `dao_protocol` — the plan says PR #123 was supposed to add it but it's not there. Let me look at the existing `add_partner.py` for the pattern, and also check the DApp page's email handling.


### 🤖 Autopilot

It does exist! Let me read it.


### 🤖 Autopilot

Now let me check the DApp page's email handling and the Edgar event docs to understand what's truly required.


### 🤖 Autopilot

Now let me look at the DApp page's JavaScript to see how it handles the email field.


### 🤖 Autopilot

Let me see the JavaScript section at the bottom of the DApp page to understand how it validates and submits.


### 🤖 Autopilot

Now I have the full picture. Let me also check the `pyproject.toml` for the CLI entry point.


### 🤖 Autopilot

Now I have the full picture. Let me also check the `build_event_cli` to understand how `required_labels` works.


### 🤖 Autopilot

Now I have the full picture. Let me also check the `build_event_cli` function to see how `required_labels` works.


### 🤖 Autopilot

Now I have the complete picture. Here's the situation:

---

**PR #123 doesn't exist as an open PR** — the `add_contributor.py` module already exists on `main` of `dao_protocol`, and the console script `truesight-dao-add-contributor` is already registered in `pyproject.toml`. So there's nothing to merge there — it's already live in the codebase. It just needs to be installed on the autopilot box.

**On making email optional — here's the analysis:**

There are **3 layers** that enforce email as required:

### 1. Edgar event schema (backend)
The `CONTRIBUTOR ADD EVENT` has `Contributor Email` as a required field in Edgar's catalog. This is the core issue — even if we make the DApp and CLI optional, Edgar will reject submissions without an email.

### 2. DApp page (`governor_contributor_admin.html`)
- The email `<input>` has `required` attribute
- The JS validation at submit time checks `if (!name || !email)` and blocks submission
- The hint text says *"Hard-required. The contributor will use this email to self-register..."*

### 3. CLI (`add_contributor.py`)
- `required_labels=['Contributor Name', 'Contributor Email']` — the `build_event_cli` enforces this

**The question is:** should we change the backend schema to make email optional, or should we keep it required but find another way?

The email is currently used for the **self-registration flow** (contributor gets an onboarding email to register their device key). Without an email, that flow breaks. But if you're okay with that — contributors without emails can be registered manually by a governor later — then we'd need to:

1. **Change Edgar's event schema** to make `Contributor Email` optional
2. **Update the DApp page** — remove `required` from the email field, update the validation, change the hint text
3. **Update the CLI** — remove `Contributor Email` from `required_labels`

That's a multi-layer change. Want me to proceed with all three? Or would you prefer a simpler approach — keep email required on the backend but make the DApp/CLI accept a placeholder like `"pending@example.com"` when you don't have the real one?

