# Autopilot Session — 2026-08-16

**Session**: `19ea98eb37d3`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=11042] Task tracking 

Matheus still stuck on nota fiscal exportação 

Orlantildes from Coopercabruca working on MAPA 

Orlantildes has delivered cacao butter for 5 kg that Kirsten requested 

Ling is working on the mobile space capsule details 

Jerrie still translating my pdf for Mobile UN Aora modules to PPT so that can first present to Mr Liu via Evan’s for certification and then to Cao for distribution 

Jerrie still translating my PDF for cacao ceremonial and cacao tea to PPT for discussion with Win 

I need to follow up with PODream on their tech 

I need to follow up with farmers of Gianluca on the technology implementations 

Where is the best place to track these??


### 🤖 Autopilot

Let me check the context for existing tracking structures for these people and projects before recommending a home.


### 🤖 Autopilot

Found relevant pieces. Let me read the follow-up monitor plan and search for the other project terms to see what's already tracked.


### 🤖 Autopilot

Not in context docs yet. Per protocol let me also search the code repos org-wide before concluding, and check for any existing people/task tracking structures.


### 🤖 Autopilot

Let me look at the full structure of OPEN_FOLLOWUPS.md and the TRACK_MAP to see what tracking homes already exist.


### 🤖 Autopilot

The rest of TRACK_MAP is offloaded — let me read the remainder, and check the Aora-related docs since several items (Ling, Jerrie, Mr Liu) appear to be Aora program work.


### 🤖 Autopilot

Let me see the rest of both key files to give a precise answer.


### 🤖 Autopilot

Let me find where AORA_EXPERIENCE_PLAN.md actually lives, and check the Pending section structure of OPEN_FOLLOWUPS for how people-tracked items are recorded.


### 🤖 Autopilot

Let me verify what's already tracked for Matheus / the follow-up monitor status so my recommendation is accurate.


### 🤖 Autopilot

I have a good picture now. Let me verify the followup-monitor build status so I can tell you whether the machine-chasing path is live yet or not.


### 🤖 Autopilot

Based on my full review of the tracking infrastructure, here's the answer.

## Where these belong — three homes, not one

Your list splits naturally into **3 categories**, and the DAO already has a home for each. Don't invent a new file — the context explicitly warns against variant backlogs (a duplicate split the backlog 2026-05-31 and became a tombstone).

### 1. Multi-day / human-driven follow-ups → `OPEN_FOLLOWUPS.md` (the single backlog)
These are exactly the "would rot in chat transcripts" items that file is for:

- **Matheus — nota fiscal exportação** (stuck — this is the CNAE/IE/NF-e gate; already heavily documented in `TRACK_MAP.md` + `BRAZIL_TO_SF_FREIGHT_PREFLIGHT_CHECKLIST.md`, but the *live chase* belongs in OPEN_FOLLOWUPS under a ```` ```followup ```` block so I can auto-ping)
- **PODream — tech follow-up** (you need to chase their tech)
- **Gianluca's farmers — technology implementation follow-up**

These three are "I need to follow up with X" — the exact case for a `followup` block with `condition: gmail_reply` / `elapsed_days`. **Caveat:** the durable follow-up loop (`add_followup` / `followup_loop`) is still **parked GO-ready in `plans/SOPHIA_FOLLOWUP_MONITOR_PLAN.md`, not yet built** (no `app/followups.py`, no comb loop). So for now filing them in OPEN_FOLLOWUPS gives you a durable human-readable backlog; the auto-chase engine isn't live yet.

### 2. Active operational tracks with dependencies → `TRACK_MAP.md`
- **Orlantildes / Coopercabruca — MAPA** → belongs in the **GACC / Brazil Compliance** track (Coopercabruca is already the preferred cooperative there; Orlantildes Santos Pereira is named in the GACC guide). MAPA is a China-gate dependency.
- **Orlantildes — cacao butter delivery (5 kg, Kirsten)** → this is a **physical inventory event**, not a follow-up. The right home is the **ledger / INVENTORY MOVEMENT** (Kirsten is the SF manager; this is a Coopercabruca→Kirsten movement). Track it there, not in a prose file.

### 3. Aora program work (Ling, Jerri, Mr Liu, Evan, Cao, Win) → the `aora` repo + `AORA_EXPERIENCE_PLAN.md`
The aora README says it plainly: **"Roadmap: Tracked in `agentic_ai_context/AORA_EXPERIENCE_PLAN.md`"** — and Jerri is already documented there as the China-translation owner. So:
- **Ling — mobile space capsule details** → Aora module work (the "space capsule" is part of the experiential learning program; the aora repo's `data/exercises.json` / session-generator is the natural home)
- **Jerrie — Mobile UN Aora modules PDF→PPT** (for Mr Liu via Evan's → certification → Cao for distribution) → Aora roadmap, module `index.zh-CN.md` translation work
- **Jerrie — cacao ceremonial + cacao tea PDF→PPT** (for Win) → also Aora-adjacent product/program work

## My recommendation

| Item | Home |
|------|------|
| Matheus / nota fiscal | `OPEN_FOLLOWUPS.md` (followup block, chase) |
| PODream tech | `OPEN_FOLLOWUPS.md` (followup block) |
| Gianluca farmers tech | `OPEN_FOLLOWUPS.md` (followup block) |
| Orlantildes / MAPA | `TRACK_MAP.md` → GACC track |
| Cacao butter 5 kg | Ledger INVENTORY MOVEMENT (Coopercabruca→Kirsten) |
| Ling / capsule | `AORA_EXPERIENCE_PLAN.md` + aora repo |
| Jerrie / Mobile UN PPT | `AORA_EXPERIENCE_PLAN.md` (Mr Liu/Evan/Cao path) |
| Jerrie / cacao ceremonial PPT | `AORA_EXPERIENCE_PLAN.md` (Win) |

**Want me to file these?** I can:
1. Add the three `followup` blocks (Matheus, PODream, Gianluca) to `OPEN_FOLLOWUPS.md` under `## Pending` via PR
2. Update `TRACK_MAP.md` with the Coopercabruca/MAPA + cacao butter status
3. Add the Ling/Jerrie Aora items to the Aora roadmap

One question first: **what thread do you want the follow-up blocks to ping when they strike?** (This thread — 11042 — or a dedicated Aora/ops thread?) The plan requires a `thread_id` per follow-up.

