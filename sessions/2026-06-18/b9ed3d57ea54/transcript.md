# Autopilot Session — 2026-06-18

**Session**: `b9ed3d57ea54`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=6711] The other Sophia just complained about this

There's no report_contributor_add.py module in dao_client. The contributor add flow is only available through the DApp web page (governor_contributor_admin.html) — it's a governor-only action that requires your browser session's digital signature.

So to answer your question: No, there isn't a dao_client CLI method for adding a contributor. The only way is through the DApp page:

👉 https://dapp.truesight.me/governor_contributor_admin.html

You'll need to:
1. Open that page in your browser
2. Let it verify your governor digital signature
3. Fill in David Campbell / david@soha.center
4. Click Add contributor

That will create the contributor row and trigger the onboarding email to David with a link to self-register his device key.

———
✅ Done this turn — actions taken:
• ssh run ×4 → find /home/ubuntu -maxdepth 3 -name "dao_client" -type d 2>/dev/null; find /opt -maxdepth 3 -name "dao_client" -type d 2>/dev/null; pip3 sho; pip3 list 2>/dev/null | grep -i dao; ls /home/ubuntu/tokenomics/ 2>/dev/null | head -20; ls /home/ubuntu/tokenomics/python_scripts/ 2>/dev/null | head -30; ls /home/ubuntu/tokenomics/scripts/ 2>/dev/null | head -30; …(+1 more)

What are your thoughts?


### 🤖 Autopilot

She's right — and I appreciate the correction. Let me verify this myself by checking what's actually in the `dao_client` repo.


### 🤖 Autopilot

Let me also check what scripts actually exist in `dao_client`:


### 🤖 Autopilot

The `dao_client` repo seems to have been renamed/moved. Let me check what's actually installed on the autopilot:


### 🤖 Autopilot

Alright, I've done my own investigation. Here's what I found:

**She's right.** There is no `report_contributor_add.py` or any CLI script for adding a contributor anywhere in the tokenomics repo or the (now-moved/renamed) `dao_client` repo. The only scripts that touch "contributor" are:
- `tdg_aws_recurring_tokenization_monthly.py` — tokenization, not adding
- `digital_signature_processor.py` — signature processing, not adding
- `irs_tax_compiler.py` — tax, not adding
- `add_headers_to_gs_files.py` — headers, not adding

**My mistake.** I told you there was a CLI path when there isn't one. The contributor add flow is indeed DApp-only — the `governor_contributor_admin.html` page at **https://dapp.truesight.me/governor_contributor_admin.html** is the sole entry point, because it requires your browser session's digital signature.

**What I should have done** before answering you the first time: actually searched the codebase instead of assuming a script existed because the pattern sounded plausible. I'll do better.

So — back to your original ask: David Campbell / david@soha.center needs to be added via the DApp page. Want me to open that link for you?

———
**✅ Done this turn — actions taken:**
• `ssh run` ×4 → pip3 list 2>/dev/null | grep -i dao; pip3 show dao-client 2>/dev/null; pip3 show dao_client 2>/dev/null; ls /home/ubuntu/tokenomics/scripts/; ls /home/ubuntu/tokenomics/python_scripts/agroverse_cacao_processing/ 2>/dev/null; ls /home/ubuntu/tokenomics/python_scripts/tdg_inventory_m; find /home/ubuntu/tokenomics -name "*.py" | xargs grep -l "contributor" 2>/dev/null; find /home/ubuntu/tokenomics -name "*.py" | xargs grep ; …(+1 more)


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=6711] what are your thoughts about extending the dao_client with this new module? Also I wonder if edgar already provide parameters to explain how to submit for this


### 🤖 Autopilot

Great question — two angles: (1) adding the CLI module, and (2) whether Edgar already has the event schema for it.

Let me check Edgar's event catalog first.


### 🤖 Autopilot

Now let me look at how the existing `submit_contribution` tool works and what the DApp page does for this flow:


### 🤖 Autopilot

Let me read the key files — the GAS handler and the onboarding docs:


### 🤖 Autopilot

Now let me check the `submit_contribution` method for the CONTRIBUTOR ADD EVENT handling specifically:


### 🤖 Autopilot

Let me get the CONTRIBUTOR ADD EVENT handling specifically:


### 🤖 Autopilot

Now let me check if there's a CONTRIBUTOR ADD EVENT handler in the `trigger_immediate_processing` method:


### 🤖 Autopilot

Let me search for the CONTRIBUTOR ADD EVENT handling in the controller directly:


### 🤖 Autopilot

Now I have a clear picture. Let me also check how the `submit_contribution` method handles the CONTRIBUTOR ADD EVENT specifically in the text parsing:


### 🤖 Autopilot

OK, I have a thorough picture now. Here's my analysis:

---

**Yes, Edgar already has the event schema.** The `CONTRIBUTOR ADD EVENT` is a registered event type in Edgar's catalog with these fields:

| Field | Required |
|---|---|
| **Contributor Name** | ✅ |
| **Contributor Email** | ✅ |
| Initial Digital Signature | ❌ |
| Submitted At | ❌ |
| Submission Source | ❌ |

**The full pipeline already exists:**
1. **DApp page** (`governor_contributor_admin.html`) → POST to Edgar's `submit_contribution` endpoint
2. **Edgar** (sentiment_importer's `dao_controller.rb`) → logs to Telegram Chat Logs sheet, then fires `trigger_immediate_processing`
3. **GAS handler** (`ContributorAddHandler.js`) → reads Telegram Chat Logs, dedups, appends to "Contributors contact information" sheet, fires onboarding invitation email

**The gap:** There's no CLI path. The DApp page is the only way because it requires the governor's browser-session digital signature — that's the authorization gate. The `submit_contribution` endpoint on Edgar validates the signature before accepting the event.

**My thoughts on extending `dao_client`:**

**Option A — CLI wrapper that calls the DApp's signed endpoint** — This would require the governor's private key on disk, which is a security concern. The DApp keeps the key in browser session storage for a reason.

**Option B — CLI that generates a signed payload and POSTs to Edgar directly** — Feasible. The governor would need to provide their private key (or a path to it) at invocation time. The script would:
1. Take `--name "David Campbell" --email "david@soha.center"`
2. Sign the payload with the governor's RSA key
3. POST to `edgar.truesight.me/submit_contribution` with `[CONTRIBUTOR ADD EVENT]` text

**Option C — CLI that opens the DApp page pre-filled** — Just a URL builder. Low effort, no security concerns.

**My recommendation: Option B.** It follows the same pattern as the existing `submit_contribution` tool I already have in `truesight_autopilot` — I sign events with my registered identity and POST them directly. The governor would need to register their key with Edgar first (which they already have if they've used the DApp), then the CLI could accept `--key-path` or read from `~/.dao/identity.pem`.

Want me to prototype this as a PR against `dao_client`?

