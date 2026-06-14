# Autopilot Session — 2026-06-14

**Session**: `c23dae4547b5`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=3926] Nora who runs Kopi Bay just joined us as a new retail partner to agroverse. Are you familiar with the SOP for onboarding new partners onto our website and our ledger? Let's discuss first


### 🤖 Autopilot

Welcome, Gary! Let me pull up the relevant SOPs for onboarding a new retail partner. I'll check the context files.


### 🤖 Autopilot

Let me search more broadly for the relevant playbooks.


### 🤖 Autopilot

Let me read the two key playbooks.


### 🤖 Autopilot

Let me also check the technical onboarding doc referenced in the playbook.


### 🤖 Autopilot

Great — I've got the full picture now. Here's a summary of the SOP for onboarding Nora / Kopi Bay:

---

## Onboarding SOP for a New Retail Partner (Kopi Bay)

The process splits into **two phases** — the sales/agreement phase (already done — Nora said yes) and the **technical onboarding** phase (what we need to do now).

### Phase 1: Already done ✅
Nora has joined as a retail partner — so we're past the outreach/field-visit stage.

### Phase 2: Technical Onboarding (what's next)

Per **`RETAILER_TECHNICAL_ONBOARDING.md`**, here's the sequence:

| Step | What | Tool |
|------|------|------|
| **1** | Submit `[CONTRIBUTOR ADD EVENT]` for Nora — name format: `Nora - Kopi Bay` | Edgar via `dao_client` |
| **2** | Set her mailing address on the Contributors row (col U) | Direct sheet write |
| **3** | Append a row to `Agroverse Partners` sheet with slug, partner page URL, status=`active`, location, partner type | Direct sheet write |
| **4** | Build the website partner page at `agroverse.shop/partners/kopi-bay/` | Clone template → edit in `agroverse_shop` repo |
| **5** | Add Kopi Bay to `partners-data.js` (lat/lon, about blurb, logo/hero images) | Edit in `agroverse_shop` repo |
| **6** | Add to wholesale stockists directory page | Edit in `agroverse_shop` repo |
| **7** | Record the opening-order bag movement — `[INVENTORY MOVEMENT]` from source manager (Kirsten?) to Kopi Bay's venue inventory | Edgar via `dao_client` |
| **8** | Sync runs pick it up — `partners-inventory.json` and `partners-velocity.json` auto-update | Automated |

### Inputs I need from you to proceed

Before I can start executing, I need:

1. **Nora's full name** (just "Nora" or a last name?)
2. **Nora's email** (for the contributor record)
3. **Kopi Bay's full address** (street, city, state)
4. **Partner type** — Consignment (default) or Wholesale?
5. **Kopi Bay's public website URL** (if any)
6. **A short about/mission blurb** (2-3 sentences about Kopi Bay)
7. **Opening-order QR codes** — the list of bag codes going to Kopi Bay
8. **Source manager** — is the stock coming from Kirsten's inventory?

Want to start filling those in, or shall we discuss any questions first?

