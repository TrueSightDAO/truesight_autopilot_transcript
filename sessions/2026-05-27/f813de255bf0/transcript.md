# Autopilot Session — 2026-05-27

**Session**: `f813de255bf0`

**Governor**: Gary Teh


---


### 🤖 Autopilot

👋 **New topic detected!** Before we start, pick my role:

**1.** Content Marketing Researcher — market analysis, SEO, content strategy
**2.** Event Coordinator — plan DAO events and logistics
**3.** SRE / DevOps Engineer — fix bugs, deploy code, monitor infra
**4.** Retailer Outreach Coordinator — partner outreach, onboarding, followups
**5.** Logistics Analyst — import/export, supply chain, freight
**6.** Inventory Manager — QR codes, stock levels, inventory movements
**7.** General DAO Assistant — everything (all tools, no specialisation)

Reply with a number (1-7) or role name. I'll remember this for this topic.


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

what are the outstanding stuff regarding events?


### 🤖 Autopilot

Let me check the DAO context and any event-related documentation to find outstanding items.


### 🤖 Autopilot

No dedicated `EVENTS_CONTEXT.md` file exists. Let me search for any event-related documentation or references in the workspace.


### 🤖 Autopilot

I found the key reference. Let me read the events playbook document that was mentioned in the PROJECT_INDEX.


### 🤖 Autopilot

Now let me check the actual events directory and the index.json to see what's outstanding.


### 🤖 Autopilot

Let me check what's available on the filesystem.


### 🤖 Autopilot

Now I have a comprehensive picture. Let me summarize the outstanding events-related items for you, Gary.

---

## Outstanding Events Items

Here's what's on the plate, organized by priority:

### 🔴 Active / In-Progress

**1. Dual Tech Summit 2026 (≈Jun 26, SF) — Phase 0 still open**
- **Blocker:** Ken hasn't confirmed the exact date/venue (War Memorial vs "American Legion") and table/ClawCamp block timing.
- **Due:** ~May 31 for Gary to confirm with Ken.
- Full plan exists in `market_research/events/dualtechsummitjune26/` — proposal, roadmap, checklist, field assets, essay draft all written.
- Once date locks, Claude builds the event page + QR codes → newsletter signup → Hit List (Phase 2).

### 🟡 Upcoming / Near-Term

**2. SF Tech Fest (Jun 12, Milpitas)**
- Referenced in the EVENTS.md playbook as `sftechfestjune26` — but I don't see a dedicated folder or `event.json` for it yet. Needs scoping if it's still on.

**3. Onsen Global Forum (Jun 23)**
- Referenced as `onsenglobalforumjune23` in the naming convention doc — same question, needs a folder + checklist if active.

### 🟢 Infrastructure / Process Items

**4. Events directory not yet created locally**
- The `go_to_market/events/` folder structure (per EVENTS.md) doesn't exist on the local filesystem yet. The playbook is written but the actual `index.json`, `build_index.py`, and per-event folders need to be created and committed.

**5. No `index.json` registry built yet**
- The unified two-tier registry (upcoming + past events) needs `build_index.py` to be written and run. Past events need to be pulled from `agroverse_shop/event-details-registration/events.json`.

**6. Apple Reminder + Calendar check-in convention not yet automated**
- The EVENTS.md playbook describes creating Apple Reminders and Calendar events via `osascript` for Phase 0 host check-ins, but no script exists yet to automate this.

---

**Bottom line:** The **Dual Tech Summit** is the most concrete upcoming event — it has a full plan drafted but is **blocked on Ken confirming the date/venue**. Once that lands, the next steps are:

1. ✅ Gary confirms with Ken (~May 31)
2. 🔲 Claude builds event page + QR codes (~Jun 8-17)
3. 🔲 Dry run QR→signup loop (~Jun 18-20)
4. 🔲 Print placard, pull cacao, pack kit (~Jun 20-25)
5. 🔲 Event day (Jun 26)
6. 🔲 Post-event: leads → Hit List → follow-ups

Want me to start building the events directory structure and `build_index.py` so the registry is ready? Or should I draft the Apple Reminder automation script?

