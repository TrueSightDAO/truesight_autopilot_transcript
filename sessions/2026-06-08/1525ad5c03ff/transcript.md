# Autopilot Session — 2026-06-08

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

you there?


### 🤖 Autopilot

Yes, I'm here, Gary. What do you need?


### 🧑 Governor

So the tree repositories, capoeira, the butterfly effects club, as well as the Oracle, they all represent a front-end java script approach implementation towards integrating and interfacing with the Dow protocol. Today, what I observe is that when trying to hand-row the integration from scratch using Oracle, there was like a whole bunch of back-and-forth which was a waste of time. Maybe what we should do is for you to analyze all three repositories, come up with an implementation plan execution roadmap and then execution roadmap checklist. Two, perhaps, come up with a java script library which people that want to integrate directly, interface with the Dow protocol by a java script could just call in the future, rather than trying to figure out what the fuck's going on. What are your thoughts? [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Great question. Let me start by pulling context on all three repos so I can give you a grounded answer.


### 🤖 Autopilot

Good. Let me now read the three repos — **capoeira**, **butterfly-effect-club**, and **oracle** — to understand their architecture and what they share.


### 🤖 Autopilot

Let me look deeper into the oracle repo (it has no README on main) and the dao_protocol to understand the integration surface.


### 🤖 Autopilot

Now let me look at the oracle repo's structure and the dao_protocol to understand the integration surface.


### 🤖 Autopilot

Now let me look at the oracle repo's actual JS files to understand how it integrates with the DAO protocol.


### 🤖 Autopilot

Now I have a thorough understanding of all three repos. Let me also quickly check the capoeira practice event submit to see the pattern.


### 🤖 Autopilot

Now I have a complete picture. Here's my analysis:

---

**You're right on both counts.** Here's what I see across the three repos:

## The Pattern They All Share

Every single one — **capoeira**, **butterfly-effect-club**, and **oracle** — independently reimplements the same boilerplate:

1. RSA-2048 keypair generation (Web Crypto API)
2. `base64ToArrayBuffer` / `arrayBufferToBase64` / `base64ToBase64Url` — identical helper functions copy-pasted three times
3. `publicKeyToSlug()` — SHA-256 hash → base64url → `pk-` prefix, duplicated identically
4. Canonical payload formatting (`[EVENT NAME]\n- Label: value\n...`)
5. RSASSA-PKCS1-v1_5 signing
6. `FormData` + `fetch` POST to Edgar
7. `localStorage` key management (`publicKey`, `privateKey`)

The oracle even imports the **qimen-dunjia** library as a vendored standalone JS — that's a whole separate integration surface.

## The Problem

When you tried to hand-roll from scratch with the oracle, you had to rediscover all of this. Each new front-end project means re-inventing the same signing pipeline, the same key management, the same Edgar submission flow. That's the back-and-forth waste you felt.

## My Proposal

**Two deliverables:**

### 1. `@truesight/dao-client` — a single npm package

A zero-dependency JavaScript/TypeScript library that any front-end can import:

```js
import { DaoClient } from '@truesight/dao-client';

// One call — keypair auto-generated if missing
const client = new DaoClient();

// Submit any event type
await client.submit('PRACTICE EVENT', {
  'Program': 'truesight-grounding',
  'Practice Type': 'oracle-consultation',
  'Practitioner Public Key': client.publicKey,
  ...
});

// Or just sign and get the share text
const { shareText } = client.sign('CONTRIBUTION EVENT', {...});

// Get the credential slug
const slug = await client.getSlug();
```

This eliminates the copy-paste boilerplate across all three repos. One source of truth for key generation, signing, payload formatting, and Edgar submission.

### 2. An implementation plan + execution roadmap

I'll analyze all three repos, extract the common integration surface, and produce:
- A **roadmap document** showing the refactoring sequence
- A **checklist** for each repo (capoeira, butterfly-effect-club, oracle) to swap their inline code for the library import
- A **migration guide** so new front-ends (tribomirimbahia, future projects) start with the library from day one

---

Want me to start building? I'd begin with:

1. **Create the npm package** in a new `truesight-dao-client-js` repo (or add it to `dao_protocol` as a `packages/` subdirectory)
2. **Open PRs** against capoeira, butterfly-effect-club, and oracle to swap their inline code for the library import
3. **Write the roadmap** as a context file in `agentic_ai_context`

Say the word and I'll kick it off.


### 🧑 Governor

make sure to update the implementation plan, roadmap checklist, and the roadmap execution checklist as an MD file in the agentic AI context. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me first check what already exists in the context to avoid duplicating or conflicting with anything.


### 🤖 Autopilot

Good — nothing exists yet. Let me also check what's in the dao_protocol repo for any existing JS work, and look at the existing context files for roadmap patterns.


### 🤖 Autopilot

Good. I have the full picture. Let me now create the roadmap document and the npm package in one shot.


### 🤖 Autopilot

Now I'll create the roadmap document and the npm package in parallel.


### 🤖 Autopilot

Done. Here's what I've created:

**PR #359** — `TRUESIGHT_DAO_CLIENT_JS_ROADMAP.md` in `agentic_ai_context`

The roadmap covers everything:

### What's in the document

1. **Problem statement** — quantified the ~264 lines of identical boilerplate duplicated across capoeira, butterfly-effect-club, and oracle

2. **Pre-flight checklist** — repo home (recommend `dao_protocol/packages/dao-client-js/` alongside the Python client), npm org, package name `@truesight/dao-client`, build tooling, CDN distribution for static sites

3. **Library API design** — a `DaoClient` class with `sign()`, `submit()`, `getSlug()`, `getCredentialUrl()` — one import replaces ~80 lines of boilerplate per repo

4. **Sequenced plan (PR0–PR5):**
   - **PR0** — This roadmap ✅ (done)
   - **PR1** — Core library package in `dao_protocol/packages/dao-client-js/`
   - **PR2** — Swap capoeira
   - **PR3** — Swap butterfly-effect-club
   - **PR4** — Swap oracle
   - **PR5** — Migration guide + update `program-template`

5. **Resume tracker** — status table with **RESUME HERE → PR1** pointer

6. **Migration guide** — before/after code comparison showing how each repo's ~80 lines of duplicated helpers becomes a 3-line import

7. **CDN distribution plan** — ESM, CJS, and IIFE builds via `tsup` so static HTML sites can use it via `<script>` tag

Want me to start on **PR1** — actually building the npm package?


### 🧑 Governor

Merge PR #359 

Hold off on 2 and 3 for now. I am having a discussion with Claude


### 🤖 Autopilot

PR #359 merged. The roadmap is now live in `agentic_ai_context/TRUESIGHT_DAO_CLIENT_JS_ROADMAP.md`.

Understood on holding off PR2 and PR3 — the roadmap is there as the reference. When you and Claude land on the direction, just say the word and I'll pick up from the **RESUME HERE** pointer.

