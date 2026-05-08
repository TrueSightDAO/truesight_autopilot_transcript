# Autopilot Session — 2026-05-08

**Session**: `d395a37a9db2`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Submit this contribution to Edgar using submit_contribution:

event_name: CONTRIBUTION EVENT
attributes:
  Type: AI Agent (software & documentation)
  Title: Autopilot self-extension: QR batch scanning, Governor Chat UX fixes, BigModel provider, production deploy
  Description: ## What changed

### Autopilot self-extension (truesight_autopilot)
- **HEIC auto-conversion** in `scan_qr_from_file` (#14) — QR scanner can now read Apple HEIC photos directly
- **list_directory tool** (#15) — new filesystem tool to discover files in local directories
- **Grok vision fallback** (#16) — when pyzbar/zbarimg find no codes, Grok vision model attempts to read QR codes from images
- **read_local_file tool** (#17) — read local text files (`.env`, credentials) not on GitHub
- **Grok prompt optimization** (#23, #26) — high-detail images + focused batch-code prompt + zero temperature → 100% hit rate on batch 2 cacao bag photos
- **Gemini integration removed** — deprecated library, non-functional API key; Grok handles all vision
- **BigModel (ZhipuAI/GLM-4.5) LLM provider** — new provider with automatic DeepSeek fallback; ~20x cheaper than DeepSeek
- **Deploy script key parity check** — aborts deployment if production-only `.env` keys would be lost

### DApp Governor Chat UX (dapp)
- **Session restore re-renders proposal cards** (#210) — interactive Approve/Ignore/Reject cards recreated when reloading chat sessions
- **All pending proposals tracked** (#210) — non-QR proposals now appear in sidebar, not just QR-coded ones
- **Always-visible pending badge** (#210) — pending approval indicator visible without opening sidebar
- **removePendingProposal title fallback** (#211) — non-QR proposals can be resolved from pending list
- **Global regex for multi-block parsing** (#211) — captures all proposal JSON blocks in restored messages
- **routes.js localhost probe fix** (#213) — prevents infinite reload loop on localhost

### Documentation (agentic_ai_context)
- **Local debugging workflow** — authentication, DRY_RUN, golden rule (never bypass autopilot)
- **QA testing workflow** — Playwright templates, common checks, example test
- **Production deployment guide** — `.env` key parity, deploy/verify commands

## Why

Autopilot can now autonomously process batches of cacao bag QR code photos end-to-end:
1. List files in a directory
2. Convert HEIC to JPEG
3. Scan with pyzbar → Grok vision fallback
4. Look up codes in DAO ledger

Governor chat approval UX was broken: prior approvals weren't accessible on reload, new approvals were invisible in the sidebar. All three issues fixed and QA verified with Playwright.

BigModel reduces LLM costs ~20x with automatic DeepSeek fallback for reliability.

## Pull requests

- https://github.com/TrueSightDAO/truesight_autopilot/pull/14
- https://github.com/TrueSightDAO/truesight_autopilot/pull/15
- https://github.com/TrueSightDAO/truesight_autopilot/pull/16
- https://github.com/TrueSightDAO/truesight_autopilot/pull/17
- https://github.com/TrueSightDAO/truesight_autopilot/pull/23
- https://github.com/TrueSightDAO/truesight_autopilot/pull/26
- https://github.com/TrueSightDAO/dapp/pull/210
- https://github.com/TrueSightDAO/dapp/pull/211
- https://github.com/TrueSightDAO/dapp/pull/213


### 🤖 Autopilot

I'll submit this contribution to Edgar for you.


### 🤖 Autopilot

The submission failed because it's missing required fields. Edgar requires these canonical labels for CONTRIBUTION EVENT:

- **Type** ✓ (you provided: "AI Agent (software & documentation)")
- **Amount** ❌ (missing - e.g., "120 minutes" or "$500")
- **Description** ✓ (you provided the detailed description)
- **Contributor(s)** ❌ (missing - who contributed?)
- **TDG Issued** ❌ (missing - how much TDG to issue?)

Could you provide values for:
1. **Amount** (time spent or dollar value)
2. **Contributor(s)** (who made these contributions)
3. **TDG Issued** (how much TDG should be issued)

Then I'll resubmit to Edgar.

