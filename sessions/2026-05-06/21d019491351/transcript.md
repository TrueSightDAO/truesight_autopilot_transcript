# Autopilot Session — 2026-05-06

**Session**: `21d019491351`


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Hello! What repos can you access and what tools do you have?


### 🤖 Autopilot

Let me check what repos are available in the TrueSightDAO organization.


### 🤖 Autopilot

Great, here's a full rundown for you, Gary.

---

## 🗂️ Repos I Can Access

I have **read access** to all public repos in the TrueSightDAO org. The key ones I work with regularly:

| Repo | Purpose |
|------|---------|
| **agentic_ai_context** | Runbooks, operating instructions, DAO context files |
| **truesight_autopilot** | My own source code (self-improvement) |
| **dao_client** | DAO API client — used for submitting transactions |
| **tokenomics** | Token/ledger automation, balances, scoring |
| **dapp** | DAO dApp |
| **truesight_me_prod** | Main landing page (production) |
| **agroverse_shop_prod** | Agroverse shop (production) |
| **qr_codes** | Auto-generated QR code records |
| **TrueChain** | Private Ethereum network for notarization |
| **agroverse-inventory** | Inventory management |
| **agroverse-freight-audit** | Freight auditing |
| **point-of-sales-integrations** | POS integrations |
| *(and ~15 more)* | Documentation, compliance, proposals, etc. |

---

## 🛠️ Tools Available to Me

| Tool | What It Does |
|------|-------------|
| **`list_org_repos()`** | Lists all repos in the org |
| **`read_context_file(path)`** | Reads runbooks/instructions from `agentic_ai_context` |
| **`read_repo_file(repo, path)`** | Reads any file from any repo (content API) |
| **`submit_contribution(event, attrs)`** | Submits a signed transaction to Edgar (bags, sales, contributions) |
| **`create_dao_submission(title, body, pr_urls, ...)`** | Compiles a [CONTRIBUTION EVENT] for AI agent work |
| **`open_fix_pr(repo, description)`** | Diagnoses & opens a fix PR via agentic loop |
| **`scan_qr_from_file(path)`** | Scans a single image for QR codes |
| **`scan_qr_batch(paths)`** | Batch-scans multiple images for QR codes |
| **`lookup_qr_code(code)`** | Looks up a QR code's DAO ledger record |
| **`lookup_qr_batch(codes)`** | Batch-lookup of QR codes |

---

## 🔐 Key Rules

- **No auto-merge** — all PRs go through human review
- **No secrets exposed** — I never reveal credentials or private keys
- **Transaction approval gate** — before any `submit_contribution`, I present a JSON proposal block so the frontend renders Approve/Reject buttons
- **Context-first** — I always read the relevant runbook before acting

What would you like to do today?

