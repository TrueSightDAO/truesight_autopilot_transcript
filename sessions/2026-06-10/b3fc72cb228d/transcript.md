# Autopilot Session — 2026-06-10

**Session**: `b3fc72cb228d`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=2018] [Handoff context — this Telegram topic (thread 2018) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/HANDOFF_MANIFEST.md + SOPHIA_HANDOFFS.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

Cory who is part of the Nelan’s team mention that he would like to understand more about the layout of the AWS infrastructure 

We currently have this document 

https://github.com/TrueSightDAO/agentic_ai_context/blob/main/AWS_DIGITAL_INFRASTRUCTURE.md

I wonder if it might be helpful to further annotate what each instance does what are your thoughts?


### 🤖 Autopilot

Great question. Let me first read the current document to see what we have.


### 🤖 Autopilot

This is actually a pretty solid document already — it covers accounts, every EC2 instance with its purpose, DNS routing, traffic flow, service architecture, SSH access, monitoring, and security groups.

That said, I can see a few areas where **further annotation** would make it more useful for someone like Cory who's new to the infrastructure:

**What I'd suggest adding:**

1. **A high-level architecture diagram (ASCII)** — a visual flow showing how the two accounts relate, which services talk to which, and the bastion path. Something like:
   ```
   Internet ──┬── Route53 ──┬── krake_nginx ──┬── Edgar (Rails)
              │              │                 ├── dao_protocol (Python)
              │              │                 └── Sidekiq workers
              │              ├── sophia.truesight.me ── autopilot
              │              └── GitHub Pages ── dapp, shop, landing
   ```

2. **A "What runs where" quick-reference table** — one row per logical service (not per EC2 instance), showing the account, host, and what it depends on. This is the mental model Cory needs.

3. **A "Newcomer FAQ" section** — common questions like:
   - "Why two accounts?" (Explorya = legacy DAO, Nelanco = Krake + new Edgar)
   - "Why two Edgars?" (Rails = original, Python = port-in-progress)
   - "How do I SSH in?" (bastion via Sophia)
   - "What happens if an instance dies?"

4. **Cost context** — a rough monthly cost per account (even just instance type × rate) so Cory understands the financial footprint.

5. **A "Where do secrets live?" summary** — currently scattered across sections 6 and 7.1; a single table would help.

**My recommendation:** I think the document is already useful as-is for Cory to start reading. But I'd suggest adding the **ASCII architecture diagram** and the **"What runs where" logical service table** as the highest-value additions. Want me to open a PR with those additions?

