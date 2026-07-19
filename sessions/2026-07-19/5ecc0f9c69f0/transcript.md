# Autopilot Session — 2026-07-19

**Session**: `5ecc0f9c69f0`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=9320] Cory from UX.App and Wayne works for Jake Nelan who finances the AWS nelanco account 

Perhaps we should do a itemized list of DAO assets running in there

Check what was the discussion had with them 

I understand that Jake is VP of technology for Herbal life and their group also runs a 3PL logistics software app

Perhaps explore deeply how the various assets running in the DAO as well as how our DAO’s initiative could be linked up to them


### 🤖 Autopilot

Let me search for context on Cory, Wayne, Jake Nelan, and any prior discussions with them.


### 🤖 Autopilot

Let me look at the relevant context files for more detail on Wayne and the nelanco relationship.


### 🤖 Autopilot

Let me search for the specific Wayne onboarding discussion and the UX.App connection.


### 🤖 Autopilot

Let me search for the specific Wayne onboarding section and also look at what's running in the Nelanco AWS account.


### 🤖 Autopilot

Let me read the full context around that Wayne mention and also inventory the Nelanco AWS account.


### 🤖 Autopilot

Let me get the full EC2 inventory and also check other AWS services in the Nelanco account.


### 🤖 Autopilot

Let me get the full EC2 inventory more efficiently by querying just the tags and also check other services.


### 🤖 Autopilot

Let me also check for Route53 hosted zones and Lambda functions.


### 🤖 Autopilot

Now let me also check what the "restory" project is — that's likely the 3PL logistics software app you mentioned.


### 🤖 Autopilot

Now I have a comprehensive picture. Here's my analysis:

---

## What I Found

### Prior Discussion with Cory/Wayne/Jake
There's **very little** in the DAO context about them. The only mention is in `OPEN_FOLLOWUPS.md` line 795 — a passing reference to "Wayne @ UX.APP, 2026-05-20" in the context of onboarding. No detailed discussion records exist in the context files. This conversation thread is likely where the relationship is being developed.

### Who's Who (from web research)
- **Jake Nelan** — VP of Product Innovation at **Herbalife** (15+ years). Also President at **PlmTek**. He finances the **Nelanco AWS account** (account `767697632458`).
- **Wayne** — at **UX.App** (a UI/UX design + app development company).
- **Cory** — also from UX.App.

### Nelanco AWS Account — Full Asset Inventory

**EC2 Instances (all us-east-1, all running):**

| Instance Name | Type | Purpose |
|---|---|---|
| **seni_ror_200250915** | — | Edgar Rails (sentiment_importer) — main DAO backend |
| **seni_sql_2026** | — | PostgreSQL for Edgar |
| **seni_redis_2** | t2.large | Redis for Edgar/Sidekiq |
| **seni_sk_auto** (×2) | — | Sidekiq workers (auto-scaled) |
| **dao_protocol_nelanco** | t3.small | Standalone dao_protocol API server |
| **dao-protocol-beta** | — | Beta dao_protocol |
| **krake_ror** | — | Krake Rails (getdata.io) |
| **krake_nginx** | — | Nginx reverse proxy |
| **krake_data** | — | Krake data processing |
| **krake_sk_consolidated** | — | Krake Sidekiq (auto-scaled) |
| **GETDATA_REDIS** | t3a.small | Redis for Krake |
| **sophia-nelanco** (i-05276b8ae82d6b88c) | t3.medium | **This autopilot box** (migration-passive state) |
| **nelanco-claude-code** | — | Claude Code dev box |

**RDS:**
- **restory-instance-1** — Aurora PostgreSQL (serverless) — the **Restory** app database

**S3 Buckets (23 total):**
- **DAO-related:** `assets.truesight.me`, `aws-cloudtrail-logs-...`
- **Restory-related (the 3PL/logistics app):** `restory-file-storage-*` (dev/prod/input), `restory-auth2-*`, `restory-chat-prod-*`, `restory-graphql-api-*`, `restory-websocket-*`, `restory-analytics-*`, `restory-pulumi`
- **Other:** `81orli-zoyq37c`, `lx3tw89-n14mfa7`, `fm-bucket-bd5073b`, `chatwoot-restory-bucket`

**Lambda Functions (5):**
- `restory-auth2-prod-auth` — Auth service
- `restory-file-storage-prod-userPhotoProcess` — Photo processing
- `restory-graphql-api-prod-graphql` — GraphQL API
- `restory-websocket-dev-connectHandler` — WebSocket
- `lx3tw89-01u2lb` — Lambda@Edge for CloudFront

**Load Balancers:**
- `krake-ror-1` — ALB for Krake Rails

**No Route53 hosted zones** in this account.

### The Restory Project
The AWS resources reveal **Restory** is a significant app running in the Nelanco account — it's a **chat/customer service platform** (uses Chatwoot, has auth, file storage, GraphQL, WebSocket, analytics). This is likely the "3PL logistics software app" you mentioned, or at minimum a customer engagement platform that could interface with logistics.

---

## How the DAO's Assets Could Link Up

Here's the strategic picture:

### 1. DAO Assets Running on Nelanco's AWS
The DAO is already deeply embedded in Jake's infrastructure:
- **Edgar** (sentiment_importer Rails + PostgreSQL + Redis + Sidekiq)
- **dao_protocol** (the DAO API)
- **Sophia** (this autopilot box)
- **Krake/getdata.io** (data harvesting platform)

### 2. Potential Linkage Points

| DAO Initiative | UX.App / Restory / Herbalife Link |
|---|---|
| **Cacao supply chain tracking** (QR codes, consignments) | Restory's chat/customer platform could serve as the **customer-facing support layer** for farmers/partners tracking their cacao bags |
| **3PL logistics** (our consignment/freighting model) | If Restory has logistics capabilities, our `CONSIGNMENT_OPTIMAL_QUANTITY_PROPOSAL.md` and `SUPPLY_CHAIN_AND_FREIGHTING.md` could integrate — Restory handles the logistics UI, we handle the DAO tokenomics layer |
| **UX.App design services** | Wayne/Cory could design the **DApp UX**, the **truesight.me** site, or the **agroverse.shop** experience — we've been DIY on design |
| **Herbalife partnership** | Jake's Herbalife role (VP Product Innovation) opens a massive channel — Herbalife's global distributor network could carry **Agroverse ceremonial cacao** as a wellness product, or the DAO's credentialing/lineage system could certify Herbalife's supply chain |

### 3. Suggested Next Steps

1. **Itemized asset list** — I've compiled it above. We could formalize this as a doc in `agentic_ai_context` (e.g. `NELANCO_AWS_ASSET_INVENTORY.md`).

2. **Deepen the relationship** — Propose a call/meeting where we walk through:
   - What Restory does exactly (is it a 3PL platform or a customer chat platform?)
   - How UX.App could help with the DApp/Shop UI
   - Whether Herbalife's supply chain could use the DAO's **QR lineage tracking** for ingredient provenance

3. **Inventory file** — Want me to create a formal `NELANCO_AWS_ASSET_INVENTORY.md` in the context repo with the full itemized list? That way future sessions have it.

