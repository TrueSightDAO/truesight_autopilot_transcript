# Autopilot Session — 2026-06-18

**Session**: `3471d4eb0b22`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=6311] what are the various methods you can call via dao_client?


### 🤖 Autopilot

Let me search the context and codebase for dao_client methods.


### 🤖 Autopilot

Let me look at the dao_client repo directly to see what CLI commands and modules are available.


### 🤖 Autopilot

Let me check the repo structure differently.


### 🤖 Autopilot

The repo seems to have been renamed/moved. Let me check the actual repo name.


### 🤖 Autopilot

Let me look at the actual dao_client repo (it seems the repo name might have changed — let me check the actual code on the autopilot box where it's installed).


### 🤖 Autopilot

Now I can see the modules. Let me look at the full list of modules and the CLI entry points.


### 🤖 Autopilot

Now let me check the CLI entry points (console_scripts) to see what commands are actually callable.


### 🤖 Autopilot

Here's the complete list of **dao_client CLI commands** (from `pyproject.toml` `[project.scripts]`):

---

### 🔐 Auth & Identity
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-auth` | `auth:main` | Login / register / manage RSA keypairs |

### 🤖 Agent Communication
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-ping-sophia` | `ping_sophia` | Governor-signed one-shot ping to Sophia's `/chat-blocking` |

### 📦 Inventory & QR Codes
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-register-qr-code` | `register_qr_code` | Register new QR codes in the ledger |
| `truesight-dao-update-qr-code` | `update_qr_code` | Update QR code metadata/status |
| `truesight-dao-batch-qr-generator` | `batch_qr_generator` | Batch-generate QR codes |
| `truesight-dao-scanner` | `scanner` | Scan QR codes |
| `truesight-dao-report-inventory-movement` | `report_inventory_movement` | Record inventory movements (bags changing hands) |

### 💰 Financial Events
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-report-sales` | `report_sales` | Record a sales event |
| `truesight-dao-report-contribution` | `report_contribution` | Record a human contribution (time/USD) |
| `truesight-dao-report-ai-agent-contribution` | `report_ai_agent_contribution` | Record an AI agent contribution (requires PR URLs) |
| `truesight-dao-report-capital-injection` | `report_capital_injection` | Record capital injection |
| `truesight-dao-report-asset-receipt` | `report_asset_receipt` | Record receipt of an asset |
| `truesight-dao-report-dao-expenses` | `report_dao_expenses` | Record DAO expenses |
| `truesight-dao-report-dapp-permission-change` | `report_dapp_permission_change` | Record DApp permission changes |
| `truesight-dao-report-tree-planting` | `report_tree_planting` | Record tree planting events |

### 🌱 Supply Chain & Farming
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-register-farm` | `register_farm` | Register a farm in the ledger |
| `truesight-dao-repackaging-planner` | `repackaging_planner` | Plan repackaging operations |

### 🗳️ Governance
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-create-proposal` | `create_proposal` | Create a governance proposal |
| `truesight-dao-review-proposal` | `review_proposal` | Review/vote on a proposal |
| `truesight-dao-withdraw-voting-rights` | `withdraw_voting_rights` | Withdraw voting rights |

### 📜 Notarization
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-notarize` | `notarize` | Notarize documents/media |

### 🗄️ Cache Readers (read-only)
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-cache-freight` | `cache.freight` | Read freight cache |
| `truesight-dao-cache-treasury` | `cache.treasury` | Read treasury cache |
| `truesight-dao-cache-compositions` | `cache.compositions` | Read compositions cache |
| `truesight-dao-cache-contributors` | `cache.contributors` | Read contributors cache |

### 🖥️ Server (dao_protocol)
| Command | Module | Purpose |
|---|---|---|
| `truesight-dao-protocol-server` | `server.main` | Start the FastAPI dao_protocol server (port 8010) |

---

**Total: 26 CLI commands** across auth, inventory/QR, financial events, supply chain, governance, notarization, cache reads, and the server itself.

There are also **additional module files** that have `main()` functions but aren't wired as CLI entry points yet (they'd be callable via `python -m` or direct import):
- `add_hit_list_store` — Add a store to the hit list
- `check_in_partner` — Partner check-in
- `link_attestations_to_trees` — Link attestations to trees
- `mint_donation` — Mint a donation
- `onboard_partner` — Onboard a partner
- `report_currency_conversion` — Report currency conversion
- `update_store` — Update store data
- `lookup_qr_code` — Look up QR code (read-only)

Want me to show the arguments/flags for any specific command?

———
**✅ Done this turn — actions taken:**
• `ssh run` ×9 → pip show truesight-dao-client 2>/dev/null || pip show dao-client 2>/dev/null; echo "---"; which truesight-dao- 2>/dev/null; compgen -c trues; pip list 2>/dev/null | grep -i dao; echo "---"; ls /home/ubuntu/dao_protocol/ 2>/dev/null || ls /home/ubuntu/dao_client/ 2>/dev/null || echo; find / -name "*.py" -path "*dao*" -maxdepth 5 2>/dev/null | head -30; echo "==="; pip list 2>/dev/null | grep -i true; echo "==="; ls /home/; …(+6 more)

