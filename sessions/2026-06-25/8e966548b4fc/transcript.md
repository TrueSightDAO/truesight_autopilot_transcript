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


### 🤖 Autopilot

Let me dig deeper specifically for the Shirley Lin who's a Strategic Advisor at Tiny Vikings.


### 🤖 Autopilot

Let me check the ZoomInfo result — that's the most promising lead for an email.


### 🤖 Autopilot

ZoomInfo is paywalled. Let me try a few more angles.


### 🤖 Autopilot

Let me check the PGC Summit speaker page — that often has contact info.


### 🤖 Autopilot

Let me also check if she has a presence on any other platforms that might list an email.


### 🤖 Autopilot

Let me check her personal contact page and also look for her on RocketReach.


### 🤖 Autopilot

That's just a contact form, no public email. Let me check RocketReach for a more specific lead.


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

