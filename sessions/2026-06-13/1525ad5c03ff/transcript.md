# Autopilot Session — 2026-06-13

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] yup.


### 🤖 Autopilot

Let me check what's currently in the `.env` so I know what needs to be preserved, and also check the existing OPEN_FOLLOWUPS.md for any prior tracking of this gap.


### 🤖 Autopilot

Now I have the full picture. Let me also check what's in the `.env` to understand what needs preserving (just the variable names, not values).


### 🤖 Autopilot

Now I have everything. Let me also check the existing OPEN_FOLLOWUPS.md entry about credential vault for host-side secrets — it's already there under "Credential vault for service-account keys (AWS Secrets Manager)". Let me compile the deployment map and file the fix.

Here's the complete **Deployment Map** — I'll commit it to `agentic_ai_context` as a DR runbook, then also address the `.env` gap.

---

## 🗺️ TrueSight DAO Autopilot — Deployment Map

### 1. The Box

| Property | Value |
|---|---|
| **Instance ID** | `i-02c699d3d7efbdc82` |
| **Name** | `truesight-autopilot` |
| **Type** | `t3.medium` (2 vCPU, 4 GB RAM) |
| **AMI** | `ami-00403f401ee6a4b98` (Ubuntu 22.04) |
| **Disk** | 20 GB EBS (`vol-0159e886ea21577df`) — **72% full** |
| **Swap** | 2 GB |
| **Region / AZ** | `us-east-1` / `us-east-1d` |
| **VPC / Subnet** | `vpc-3a79715f` / `subnet-44257d33` |
| **Private IP** | `10.0.0.158` |
| **Public IP** | `52.200.38.206` (Elastic) |
| **Security Group** | `default` (`sg-e98f788e`) |
| **Key Pair** | `garyjob_aws` |
| **AWS Account** | `440626669078` (Explorya) |
| **IAM Role** | **None** — no instance profile |
| **Tags** | `Name=truesight-autopilot`, `Service=autopilot`, `Project=TrueSightDAO` |

### 2. Services (systemd)

| Unit | What | Port | Runs as |
|---|---|---|---|
| `truesight-autopilot.service` | Sophia FastAPI (2 workers) | `8001` | `ubuntu` |
| `truesight-autopilot-telegram.service` | Telegram bot adapter | — | `ubuntu` |
| `truesight-autopilot-watchdog.service` | Attention watchdog | — | `ubuntu` |
| `nginx.service` | Reverse proxy → sophia.truesight.me | `80`/`443` | `root` |
| `ssh.service` | SSH access | `22` | `root` |
| `monit.service` | System monitoring | `2812` | `root` |

### 3. Code & Data Layout

| What | Path |
|---|---|
| **App code** | `/opt/truesight_autopilot/` (git clone of `TrueSightDAO/truesight_autopilot`) |
| **Python venv** | `/opt/truesight_autopilot/.venv/` |
| **Environment secrets** | `/opt/truesight_autopilot/.env` |
| **Google SA keys** | `/opt/truesight_autopilot/config/google/` |
| **Gmail OAuth tokens** | `/opt/truesight_autopilot/config/gmail/` |
| **Systemd unit files** | `/opt/truesight_autopilot/systemd/` (symlinked into `/etc/systemd/system/`) |
| **Nginx config** | `/opt/truesight_autopilot/config/nginx/` (symlinked into `/etc/nginx/sites-enabled/`) |
| **Telegram session** | `/opt/truesight_autopilot/.telethon_watchdog.session` |
| **GitHub PAT** | `/home/ubuntu/CYPHER_DEFENCE_OPS_PAT` |
| **Clasp tokens** | `/home/ubuntu/.clasprc*.json` |
| **SSH key** | `/home/ubuntu/.ssh/id_ed25519_truesight_autopilot` |
| **Nginx logs** | `/var/log/nginx/sophia_access.log` + `sophia_error.log` |
| **App logs** | `journalctl -u truesight-autopilot*` |

### 4. Installed Software

- **Python 3.10** (system) + venv with FastAPI, uvicorn, boto3, google-api-client, httpx, etc.
- **Node.js v20** + `@google/clasp` (global)
- **Tesseract OCR** (eng + osd)
- **FFmpeg**
- **Nginx** + Let's Encrypt (certbot)
- **No Docker, no PM2, no Supervisor**

### 5. Fleet — Other Hosts (SSH reachable)

| Alias | Host | Purpose |
|---|---|---|
| `krake-nginx` | `54.226.114.186:2202` | Nginx reverse proxy (Nelanco) |
| `seni-ror` | `54.211.179.126` | Edgar Rails API server |
| `dao-protocol` | `98.93.94.86` | dao_protocol FastAPI (port 8010) |
| `seni-sk` | `34.234.193.80` | Sidekiq worker for Edgar |
| `seni-sql` | `44.193.55.205` | PostgreSQL for Edgar |
| `seni-redis` | `54.234.59.188` | Redis for Edgar |

### 6. Credential Inventory & DR Status

| Credential | Location | Backed up? |
|---|---|---|
| `.env` (all API keys) | `/opt/truesight_autopilot/.env` | ❌ **Not backed up** |
| Google SA keys (3) | `config/google/*.json` | ✅ In `credential_vault` (laptop) |
| Gmail OAuth tokens | `config/gmail/*.json` | ✅ In `credential_vault` |
| GitHub PAT | `/home/ubuntu/CYPHER_DEFENCE_OPS_PAT` | ❌ Regeneratable from GitHub |
| SSH key | `~/.ssh/id_ed25519_truesight_autopilot` | ✅ In `credential_vault` |
| Clasp tokens | `~/.clasprc*.json` | ✅ In `credential_vault` |
| Telegram session | `.telethon_watchdog.session` | ❌ Must re-login |
| SSL cert | `/etc/letsencrypt/live/sophia.truesight.me/` | ✅ Auto-renewed |

### 7. Disaster Recovery — Spin Up a Replacement

**Steps (estimated ~45 min):**

1. **Launch** a new `t3.medium` from Ubuntu 22.04 AMI in `us-east-1d`, same security group, attach the Elastic IP
2. **Install deps:** `sudo apt install -y python3 python3-pip python3-venv nginx certbot tesseract-ocr ffmpeg nodejs npm`
3. **Clone the repo:** `sudo git clone https://github.com/TrueSightDAO/truesight_autopilot.git /opt/truesight_autopilot && sudo chown -R ubuntu:ubuntu /opt/truesight_autopilot`
4. **Create venv:** `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
5. **Recreate `.env`** — **critical gap** (see below)
6. **Copy Google SA keys + Gmail tokens** from `credential_vault` restore (laptop backup)
7. **Copy SSH key** from `credential_vault` → `~/.ssh/`
8. **Set up Nginx:** `sudo ln -sf /opt/truesight_autopilot/config/nginx/sophia.conf /etc/nginx/sites-available/ && sudo ln -sf /etc/nginx/sites-available/sophia /etc/nginx/sites-enabled/ && sudo certbot --nginx -d sophia.truesight.me`
9. **Install systemd units:** `sudo cp /opt/truesight_autopilot/systemd/*.service /etc/systemd/system/ && sudo systemctl daemon-reload && sudo systemctl enable --now truesight-autopilot truesight-autopilot-telegram truesight-autopilot-watchdog`
10. **Run Telegram login:** `python3 scripts/telethon_login.py` (interactive — needs TELEGRAM_API_ID/HASH in `.env`)

---

### ⚠️ The Critical Gap: `.env` is NOT backed up

The `credential_vault` (laptop DR) already backs up the Google SA keys, Gmail tokens, clasp tokens, and SSH key. But the **`.env` file on this box** — which holds the GitHub PAT, DeepSeek API key, Grok API key, Tavily key, Edgar private key, Telegram API credentials, AWS keys, Bugsnag key, JWT secret — is **not in any backup system**.

The existing `OPEN_FOLLOWUPS.md` has an entry for "Credential vault for service-account keys (AWS Secrets Manager)" but that's scoped to the fleet hosts, not this box's `.env`.

Let me fix both: commit this deployment map as a DR runbook, and open a follow-up to add the autopilot `.env` to the credential vault.


### 🤖 Autopilot

Now let me also add the follow-up entry to `OPEN_FOLLOWUPS.md` to track the `.env` backup gap:


### 🤖 Autopilot

Good — the existing "Credential vault for service-account keys" entry covers the fleet hosts' Google SA keys but doesn't mention the autopilot's own `.env`. Let me add a focused follow-up entry for that specific gap, and also update the existing entry to reference the autopilot `.env` as a sibling concern.


### 🤖 Autopilot

The branch already exists from the first push. Let me update it with the additional change.


### 🤖 Autopilot

The branch already has the first commit pushed. Let me use a new branch name for the follow-up entry.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] I like the idea of AWS secrets Manager in Explorya account for you.


### 🤖 Autopilot

Good call. That's the right long-term fix — attach an IAM instance profile to this box so it can fetch its own secrets at boot, no manual SCP needed.

Let me check what it would take to set that up.


### 🤖 Autopilot

Here's the summary of what I've done:

---

## ✅ Done

**Two PRs opened:**

### PR #397 — `AUTOPILOT_DEPLOYMENT_MAP.md`
The full deployment map is now committed to `agentic_ai_context`. It covers:
- Box specs (instance, disk, network, tags)
- All 6 systemd services with their ports
- Code/data layout on disk
- Installed software inventory
- Fleet SSH targets (6 hosts)
- Credential inventory with DR status (✅/❌ per item)
- **Step-by-step recovery procedure** — 10 steps, ~45 min estimated
- Flags the critical `.env` backup gap

### PR #398 — Follow-up entry in `OPEN_FOLLOWUPS.md`
Tracks the `.env` backup gap with two options:
1. **Quick win (~10 min):** Add the box `.env` to `credential_vault`'s manifest so laptop backups include it
2. **Better (~30 min):** Auto-snapshot the `.env` on every deploy

---

### The Critical Gap

The **single biggest DR risk** is `/opt/truesight_autopilot/.env` — it holds ~15 secrets and has **zero backup**. Everything else (Google SA keys, Gmail tokens, SSH key, clasp tokens) is already in `credential_vault` on your laptop. The `.env` is the one thing that would take 30–60 min to reconstruct from scratch if the box dies.

**Want me to do the quick win right now?** I can:
1. `scp` the live `.env` from this box to a temp location
2. Open a PR on `credential_vault` to add it to `MANIFEST.txt`
3. Then you'd just run `backup.sh` on your laptop once to snapshot it

Or if you prefer the AWS Secrets Manager route (longer-term), I can start on that instead.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] [Handoff context — this Telegram topic (thread 3) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/HANDOFF_MANIFEST.md + SOPHIA_HANDOFFS.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

you there?

---

[Telegram context: chat_id=-1003919341801, thread_id=3] [Handoff context — this Telegram topic (thread 3) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/HANDOFF_MANIFEST.md + SOPHIA_HANDOFFS.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

how is progress?

---

[Telegram context: chat_id=-1003919341801, thread_id=3] [Handoff context — this Telegram topic (thread 3) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/HANDOFF_MANIFEST.md + SOPHIA_HANDOFFS.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

How is progress??

---

[Telegram context: chat_id=-1003919341801, thread_id=3] [Handoff context — this Telegram topic (thread 3) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/HANDOFF_MANIFEST.md + SOPHIA_HANDOFFS.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

How is your evening?

---

[Telegram context: chat_id=-1003919341801, thread_id=3] Do you think you could share me a link of the URL to the RSA identification flow for that is being used for Kapoeira and What is that? Oracle. Yeah [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me check the handoff registry first since this topic (thread 3) may have an active execution plan.


### 🤖 Autopilot

I'm here! My evening's going well — just finished building the deployment map for this box and filed two PRs. How about yours?

Now, about the RSA identification flow for capoeira and the oracle — let me find those URLs for you.


### 🤖 Autopilot

Got it! Here are the two URLs you're asking about:

**1. The RSA identification flow** — that's the **create_signature** page. It generates an RSA keypair in your browser (stored in localStorage) and registers your email with the DAO. Used by capoeira, the oracle, and the DApp for signing events:

➡️ **`dapp.truesight.me/create_signature.html`**

**2. The Oracle** — the I Ching oracle that also uses the same RSA identity flow:

➡️ **`oracle.truesight.me`**

Both share the same keypair — if you generate keys on one, they're automatically reused on the other (same localStorage keys `publicKey`/`privateKey`). The oracle also has a dedicated draw page at **`oracle.truesight.me/draw.html`** for performing coin tosses and recording them as signed practice events.

Want me to send these as clickable links in a separate message?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] You know, just a random thought over the past week as I observe multiple instances of you as well as the other LRM's getting confused whenever needing to do some changes. I wonder if conflating the trading dashboard with the Dow Protocol service both into the same name at Gar, under the domain, at Gar true site taught me is actually a good idea and maybe we should start splitting them apart and if we do so, I don't know, what do you think? Maybe one of them should have a new name. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

That's a really sharp observation. Let me think through it.

You're talking about **Edgar** — the Rails app at `edgar.truesight.me` — which currently does two very different things:

1. **Trading dashboard** — sentiment analysis, backtester, stock data, the `/compare` view, market signals
2. **DAO Protocol service** — contribution submissions, QR code checks, email registration, partner onboarding, inventory events

They share the same codebase (`sentiment_importer`), same domain, same deployment. And you're right — every time an LLM or human goes to make a change, they have to figure out which "Edgar" they're dealing with. The extraction work we already did (pulling `/dao/*` routes into `dao_protocol` on its own box) was a step in this direction, but the naming confusion persists.

I think splitting them is a **good idea**, and here's why:

**The trading dashboard** is a financial tool — it's about markets, tickers, sentiment, backtesting. That's a distinct product with its own users, its own mental model.

**The DAO protocol** is operational infrastructure — it's about cacao bags, QR codes, partner check-ins, contributor identities, supply chain events. Completely different audience and purpose.

Keeping them under one roof means:
- Every deploy risks one side breaking the other
- Newcomers (human or LLM) have to learn both domains to touch either
- The codebase accumulates cross-cutting concerns that don't serve either well

**What I'd suggest:**

- **Keep `edgar.truesight.me`** for the trading dashboard — it's established, has history, and "Edgar" fits a financial tool
- **Move the DAO protocol fully to its own identity** — `dao_protocol` is already the service name on its own box. Give it its own domain like **`protocol.truesight.me`** or **`dao.truesight.me`**, clean up the remaining Rails routes that haven't been ported yet, and let it stand on its own

The extraction plan already has PR8d queued up to delete the ported Rails actions after the soak period ends (~June 25). That would complete the technical separation. A domain split and rename would be the final piece — and it would stop the confusion cold.

What do you think? Want me to sketch out what a full rename + domain split would look like?


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=3] Yeah, I mean, your naming approach makes sense. Although when I think about it, there's a lot of places on the system as well as the code base that assumes that Edgar is the protocol at this point, isn't it? So shifting the protocol to a new domain might end up be more of a breaking change than maybe shifting the trading system to a new domain. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

That's a really good point. Let me check — you're right that a lot of the system has already shifted to treating Edgar as the protocol.


### 🤖 Autopilot

You're absolutely right. Let me check the actual blast radius — how many places reference `edgar.truesight.me` vs how many reference `dao_protocol` or the protocol routes.


### 🤖 Autopilot

Hit the rate limit, but I already know enough from context. Here's my take:

**You're right — Edgar *is* the protocol now.** The extraction work we did (pulling `/dao/*` routes to `dao_protocol` on its own box) was a *technical* split, but the *identity* is still Edgar. The DApp submits contributions to Edgar. The QR code checks go through Edgar. Email registration goes through Edgar. The newsletter pipeline goes through Edgar. The trading dashboard is actually the smaller, less-coupled piece at this point.

So the cleaner move would be:

**Keep `edgar.truesight.me` as the DAO protocol** — that's where all the operational traffic already flows, and renaming that would break a lot more.

**Move the trading dashboard to something new** — a new subdomain like `markets.truesight.me` or `sentiment.truesight.me` or even a completely new name. The trading stuff (backtester, sentiment, stock data) is more self-contained and has fewer external consumers hitting it programmatically.

That said — the trading dashboard is also the older, more established identity. "Edgar" has been the financial tool name since the beginning. So there's a case for the opposite too.

What feels right to you? If we're going to do a rename, I'd want to pick the one that causes less downstream breakage. Want me to do a proper blast-radius analysis once the rate limit resets?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] Well, I mean, and I think about it, other than myself, no one else really used the trading system as a tool. What rate limit do you mean you hit? [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

That settles it then — if you're the only user of the trading dashboard, moving that is way lower risk. The protocol side has all the automated consumers (the DApp, dao_client, the autopilot, GAS scanners, partner systems) hitting it constantly. Moving *that* would be a much bigger coordination problem.

So the plan would be: **Edgar stays as the DAO protocol** at `edgar.truesight.me`, and the trading dashboard gets a new home — maybe `markets.truesight.me` or something with a distinct identity.

And the rate limit — GitHub API. I was searching across repos to count how many places reference "edgar" and hit the 60-requests-per-hour limit for unauthenticated searches. It's not a real blocker, just means I'd need to do the blast-radius analysis more carefully (or use the PAT). Nothing broken.

Want me to sketch out what moving the trading dashboard would look like?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3] So, well, imagine you had a steward, actually you had a steward of the ecosystem. What is a appropriate name for the trading dashboard to house it under? Let me know your thoughts. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Ooh, I like this framing — a steward of the ecosystem, not just a trading tool.

A few directions that come to mind:

**Thematic / ecosystem-aligned:**
- **Krake** — this already exists as the brand for the data/sentiment engine (Krake.io, krake_sinatra). The trading dashboard is essentially Krake's frontend. Naming it `krake.truesight.me` ties the tool to its engine and gives it a distinct identity from Edgar.
- **Sentinel** — a steward that watches. Fits the DAO's guardian-of-the-rainforest mission. But might conflict with your Sentinel governance concept for me.
- **The Observatory** — `observatory.truesight.me`. A steward watches and interprets. The trading dashboard is essentially an observatory for market signals.

**Practical / descriptive:**
- **Markets** — `markets.truesight.me`. Boring but clear. Everyone knows what it is.
- **Signals** — `signals.truesight.me`. Captures the sentiment analysis + market data angle.

**My favorite: Krake.** It's already the brand for the data engine underneath. The trading dashboard is Krake's face. Putting it at `krake.truesight.me` would:
- Give the trading tool its own identity
- Strengthen the Krake brand as a DAO sub-project
- Make the architecture clearer — Krake is the data/sentiment arm, Edgar is the protocol arm
- No naming collision with anything else in the DAO

What resonates with you?

