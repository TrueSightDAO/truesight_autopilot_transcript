# Autopilot Session — 2026-06-04

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

I am thinking for this process 
https://beta.truesight.me/lineage-register.html

instead of the governor approving after reviewing and then the orchestration, 
when the governor approves after reviewing a proposal should be submitted here 
https://dapp.truesight.me/view_open_proposals.html

Using all the inputs provided by the submitter as well as modifications of the inputs by the governor... because there will probably be a bunch of back and forth clarification isnt it? 

And then the DAO members can review it and submit their votes once the voting is past, then the governor can trigger an orchestration?


### 🤖 Autopilot

Let me read the relevant context files to understand the current lineage registration process and the DAO proposal/voting system.


### 🤖 Autopilot

Now let me look at the lineage-register page and the view_open_proposals page to understand the current flow.


### 🤖 Autopilot

The lineage-register page is 404 — let me check the dapp_prod repo and also look at the beta URL directly.


### 🤖 Autopilot

Now let me check the beta URL for the lineage-register page to see what it does:


### 🤖 Autopilot

Now let me read the lineage-register.js to understand the current flow:


### 🤖 Autopilot

Now let me also check the truesight_me repo for the lineage-register page source:


### 🤖 Autopilot

Now I have a clear picture. Let me also check the existing proposal system — how Edgar processes proposals and how they become GitHub PRs:


### 🤖 Autopilot

Now I have a thorough understanding of the entire flow. Let me summarize my analysis and proposal.

---

Gary, I've read through the full codebase. Here's my analysis of the current flow vs. what you're proposing:

## Current Flow (lineage-register.html)

1. **Visitor fills form** on `truesight.me/lineage-register.html` (email, program name, description, capabilities, etc.)
2. **On submit**, `lineage-register.js` fires **two signed events** directly to Edgar:
   - `[EMAIL REGISTERED EVENT]` — registers email + public key, triggers verification email
   - `[PROGRAM REGISTRATION REQUEST]` — the actual request with all form fields
3. **Governor reviews** the raw Edgar submission (no structured proposal page)
4. **Governor approves** → manually provisions the program

## What You're Proposing

Instead of the governor reviewing raw Edgar submissions and then orchestrating manually, the flow should be:

1. **Submitter fills form** on `lineage-register.html`
2. **Back-and-forth clarification** between submitter and governor (via the form inputs being editable/modifiable)
3. **Governor approves** → this creates a **formal DAO proposal** visible at `dapp.truesight.me/view_open_proposals.html`
4. **DAO members vote** on the proposal
5. **After voting passes**, the governor triggers the orchestration (provisioning)

## Key Changes Needed

This is a significant architectural shift. Here's what it requires:

### 1. `lineage-register.html` — Add a "review & submit as proposal" stage
   - After the governor reviews and modifies the inputs, the page needs to submit a `[PROPOSAL CREATION]` event (like `create_proposal.html` does) instead of just `[PROGRAM REGISTRATION REQUEST]`
   - The proposal body would contain the finalized program registration details

### 2. A new "Governor Review Dashboard" page (or modify existing)
   - Shows pending program registration requests
   - Lets the governor edit/modify fields
   - Has a "Submit as DAO Proposal" button that creates the proposal

### 3. The existing `view_open_proposals.html` / `review_proposal.html` handles voting
   - This already works — proposals are GitHub PRs, DAO members vote
   - The proposal type would be "Program Registration" or similar

### 4. After voting passes → trigger orchestration
   - Edgar or a GAS webhook detects the proposal passed
   - Fires the provisioning (create ledger, subdomain, etc.)

## My Suggestion

This is a **multi-repo change** touching:
- **`truesight_me_prod`** — `lineage-register.html` + `js/lineage-register.js` (add proposal submission path)
- **`dapp_beta`** — new governor review page (or modify existing)
- **`tokenomics`** — GAS backend for the proposals web app (already exists at `proposals` endpoint)
- **`sentiment_importer`** (Edgar) — possibly a new Sidekiq worker to detect passed proposals and trigger provisioning

Would you like me to:
1. **Open a design PR** in `agentic_ai_context` with a detailed proposal document for this architecture?
2. **Start coding** — which piece should we tackle first?

The biggest design question is: **where does the governor review + edit the submission?** On `truesight.me` (the lineage page itself, with a governor-only mode) or on `dapp.truesight.me` (a new page in the DApp)?

