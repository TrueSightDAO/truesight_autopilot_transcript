# Autopilot Session — 2026-06-09

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=3] By the way, I am curious, do we already have a. deployment map of how all the services as well as all the repos you have within your Ec2 Box? that way in case something happens to your current box, we can easily setup a new one that functions the same and then continue to oeprate without much frustration. Make sure it is easy for humans to read too


### 🤖 Autopilot

Great question. Let me inventory everything — the EC2 box itself, the services running on it, and all the repos. I'll build a deployment map.

Let me start by surveying the box and the org.


### 🤖 Autopilot

Now let me check the AWS account this box is in and what repos we have.


### 🤖 Autopilot

Now I have the full picture. Let me also check the `credential_vault` repo since it's relevant for DR.


### 🤖 Autopilot

Excellent. I now have the complete picture. Let me compile this into a clear, human-readable deployment map.

---

## 🗺️ TrueSight DAO — Autopilot Deployment Map

### 📦 The Box (EC2)

| Property | Value |
|---|---|
| **Instance ID** | `i-02c699d3d7efbdc82` |
| **Name tag** | `truesight-autopilot` |
| **Type** | `t3.medium` (2 vCPU, 4 GB RAM) |
| **AMI** | `ami-00403f401ee6a4b98` (Ubuntu 22.04) |
| **Disk** | 20 GB EBS (`vol-0159e886ea21577df`) — **72% full** (14 GB used) |
| **Swap** | 2 GB |
| **Region / AZ** | `us-east-1` / `us-east-1d` |
| **VPC / Subnet** | `vpc-3a79715f` / `subnet-44257d33` |
| **Private IP** | `10.0.0.158` |
| **Public IP** | `52.200.38.206` (Elastic — survives stop/start) |
| **Security Group** | `default` (`sg-e98f788e`) |
| **Key Pair** | `garyjob_aws` |
| **AWS Account** | `440626669078` (Explorya) |
| **IAM Role** | **None** — no instance profile attached (uses no AWS credentials natively) |
| **Tags** | `Name=truesight-autopilot`, `Service=autopilot`, `Project=TrueSightDAO` |

---

### 🚀 Services Running on the Box

| Service | Port | What it does | Systemd Unit |
|---|---|---|---|
| **Sophia (FastAPI)** | `8001` | Main autopilot API — SRE + dev assistant | `truesight-autopilot.service` (2 workers) |
| **Telegram Adapter** | — | Telegram bot interface (private chat) | `truesight-autopilot-telegram.service` |
| **Attention Watchdog** | — | Telegram session watchdog (read-only nudges) | `truesight-autopilot-watchdog.service` |
| **Nginx** | `80` / `443` | Reverse proxy → `sophia.truesight.me` | `nginx.service` |
| **SSH** | `22` | Remote access | `ssh.service` |
| **Monit** | `2812` | System monitoring | `monit.service` |

**Nginx config:** `/etc/nginx/sites-enabled/sophia` → proxies `sophia.truesight.me` → `127.0.0.1:8001` with SSL via Let's Encrypt.

---

### 📁 Code & Data on Disk

Everything lives under **`/opt/truesight_autopilot/`** — a git clone of `TrueSightDAO/truesight_autopilot` (main branch).

| What | Path |
|---|---|
| **App code** | `/opt/truesight_autopilot/app/` |
| **Python venv** | `/opt/truesight_autopilot/.venv/` |
| **Environment secrets** | `/opt/truesight_autopilot/.env` |
| **Systemd unit files** | `/opt/truesight_autopilot/systemd/` (also symlinked into `/etc/systemd/system/`) |
| **Nginx config** | `/opt/truesight_autopilot/config/nginx/` |
| **Telegram session** | `/opt/truesight_autopilot/.telethon_watchdog.session` |
| **Logs** | `/var/log/nginx/sophia_access.log` + `sophia_error.log` + `journalctl` |

**No Docker, no PM2, no Supervisor** — all services are native systemd units.

---

### 🔑 Credentials & Secrets

| Credential | Location | How to recover |
|---|---|---|
| **`.env`** (API keys, tokens) | `/opt/truesight_autopilot/.env` | **Not in credential_vault** (host-side gap) |
| **GitHub PAT** | `/home/ubuntu/CYPHER_DEFENCE_OPS_PAT` | Regenerate from GitHub |
| **SSH key** | `/home/ubuntu/.ssh/id_ed25519_truesight_autopilot` | In `credential_vault` (laptop backup) |
| **Clasp tokens** | `/home/ubuntu/.clasprc*.json` | In `credential_vault` |
| **Let's Encrypt SSL** | `/etc/letsencrypt/live/sophia.truesight.me/` | Auto-renewed by certbot |

---

### 🌐 Fleet — Other Hosts This Box Connects To

The autopilot SSH's into these (via `~/.ssh/config`):

| Host Alias | Real Host | Purpose |
|---|---|---|
| `krake-nginx` | `54.226.114.186:2202` | Nginx reverse proxy (Nelanco) |
| `seni-ror` | `54.211.179.126` | Edgar Rails API server |
| `dao-protocol` | `98.93.94.86` | dao_protocol FastAPI (port 8010) |
| `seni-sk` | `34.234.193.80` | Sidekiq worker for Edgar |
| `seni-sql` | `44.193.55.205` | PostgreSQL for Edgar |
| `seni-redis` | `54.234.59.188` | Redis for Edgar |

---

### 📚 All TrueSightDAO Repos (58 total)

**Core operational repos** (the ones that matter day-to-day):

| Repo | Purpose |
|---|---|
| `truesight_autopilot` | **This box** — the code you're talking to right now |
| `agentic_ai_context` | Runbooks, operating instructions, context files |
| `dao_client` | Edgar API client (contribution submissions) |
| `dao_protocol` | FastAPI server for DAO protocol |
| `tokenomics` | TDG scoring, GAS scripts, ledger automation |
| `dapp_beta` | DApp beta (beta.dapp.truesight.me) |
| `dapp_prod` | DApp production |
| `truesight_me_beta` | Landing page beta |
| `truesight_me_prod` | Landing page production |
| `agroverse_shop_beta` | Shop beta |
| `agroverse_shop_prod` | Shop production |
| `sentiment_importer` | News sentiment engine (Edgar backend) |
| `oracle` | I Ching oracle app |
| `credential_vault` | **Disaster recovery** — laptop credential backups |

**Data repos** (machine-written caches/ledgers):
`treasury-cache`, `places-cache`, `contributors-cache`, `truesight_autopilot_transcript`, `oracle_logs`, `lineage-credentials`, `lineage-assets`, `ecosystem_change_logs`, `qr_codes`, `sunmint`, `agroverse-inventory`, `store_interaction_attachments`

---

### ⚠️ Disaster Recovery — What You'd Need to Rebuild

If this box dies, here's the checklist to spin up a replacement:

1. **Launch a new `t3.medium`** from Ubuntu 22.04 AMI in `us-east-1d`, same security group, attach an Elastic IP
2. **Install deps:** `python3`, `pip`, `nodejs` (v20), `tesseract-ocr`, `ffmpeg`, `nginx`, `certbot`
3. **Clone `truesight_autopilot`** to `/opt/truesight_autopilot/`
4. **Create `.venv`** and `pip install -r requirements.txt`
5. **Recreate `.env`** — this is the **critical gap**. The `.env` file is NOT backed up anywhere (it's host-only). You'd need to reconstruct it from:
   - GitHub PAT (regenerate)
   - Telegram bot token (from BotFather)
   - Grok API key (from xAI)
   - Google service account JSONs (from GCP console)
   - OpenAI API key
   - Any other API tokens
6. **Copy SSH key** from `credential_vault` (laptop backup) → `~/.ssh/`
7. **Set up Nginx** from `config/nginx/` and run `certbot`
8. **Install systemd units** from `systemd/` and `systemctl enable --now` all three
9. **Verify** `sophia.truesight.me` responds

**The `.env` gap is the single biggest DR risk.** I'd recommend we fix that — I can file a follow-up to either:
- Add the `.env` to `credential_vault`'s manifest (it's currently scoped to laptop-only, but the pattern could extend)
- Or set up an AWS Secrets Manager secret that the autopilot reads at boot

Want me to open a PR to address that gap?

