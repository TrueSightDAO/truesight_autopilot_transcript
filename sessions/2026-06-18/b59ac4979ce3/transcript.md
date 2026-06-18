# Autopilot Session — 2026-06-18

**Session**: `b59ac4979ce3`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=6551] Feels like there are quite a few separate track happening right now within the DAO

My sense is if there is a PERT chart or Flow chart or some form not GANTT (which makes it hard to decipher which task belongs to which track) it might make it easier to help DAO members know what is going on isn't it?


### 🤖 Autopilot

Gary, you're right — there are several active tracks running in parallel, and without a visual map it's easy for members (and even me) to lose the thread of which task belongs to which track.

Let me pull together what's actually live right now so we can design the right artifact.


### 🤖 Autopilot

Now let me also check what's actually in flight right now — the active PRs and recent activity:


### 🤖 Autopilot

Now let me check the other active repos:


### 🤖 Autopilot

Good — I now have a clear picture. Here's my analysis:

---

Gary, you're spot on. There are **at least 6 distinct tracks** running in parallel right now, and without a visual map it's genuinely hard for anyone (including me) to see which PR belongs to which track, what's blocking what, and where a new member could jump in.

Here's what I see as the active tracks:

---

## 🗺️ The 6 Active Tracks (June 2026)

| # | Track | Repos | Open PRs | Status |
|---|-------|-------|----------|--------|
| **1** | **Governor Vault & Key Registry** | truesight_autopilot, tokenomics, agentic_ai_context | ~8 PRs (PR1-PR4, vault worker, policy resolver, etc.) | 🟧 Heavy — 4-phase build, PR3 merged, PR4 held |
| **2** | **Chocolate Subscriptions** | agroverse_shop_beta, tokenomics, dao_protocol | ~10 PRs (subscribe flow, CORS fix, GAS endpoints, E2E tests, sandbox) | 🟧 Phase 1 done, Phase 2 deferred, sandbox needed |
| **3** | **Edgar/Perch Separation** | dao_protocol, truesight_me_beta, agentic_ai_context | ~6 PRs (protocol landing page, Perch page, nav updates) | 🟧 Perch live, Edgar getting protocol page |
| **4** | **Partner Onboarding & Retail** | agroverse_shop_beta, dapp_beta, tokenomics | ~5 PRs (Kopi Bar, partner page template, partner_add fix, partner pokes) | 🟧 Active — new partners landing |
| **5** | **Legal Entity Structuring** | agentic_ai_context | ~4 PRs (DUNA, Wise banking, SVH Capital prep) | 🟧 Pre-fundraising research |
| **6** | **GACC / Brazil Compliance** | agentic_ai_context | ~4 PRs (product tables, packaging fixes, coopercabruca removal) | 🟧 Regulatory filing prep |

Plus **infrastructure hygiene** (ruff CI, unit test fixes, deploy scripts, NPM token rotation) running underneath all of them.

---

## What a PERT/Flow chart would solve

A Gantt is chronological — it tells you *when* things happen but not *which task belongs to which mission thread*. What you're describing sounds like a **track-based dependency map**:

```
Track 1: Vault ───── PR1 ──→ PR2 ──→ PR3 ──→ PR4 (held)
                                        ↓
Track 2: Subscriptions ── Phase 1 ──→ [sandbox] ──→ Phase 2
                                            ↑
Track 3: Edgar/Perch ──→ split live ───────┘
```

Each track is a horizontal swimlane. Dependencies are vertical arrows between lanes. A new member can look at the map and say "I see Track 4 has no blockers — I can pick up a partner page PR."

**I can build this.** A few options:

1. **Mermaid flowchart** — lives in `agentic_ai_context/TRACK_MAP.md`, renders in any markdown viewer. I update it as tracks move. Lowest friction.
2. **SVG** — more polished, embeddable on truesight.me/dashboard or the Beer Hall. Needs a build step.
3. **Google Sheet** — interactive, filterable by track/status/owner. DAO members can click through to PR links.

I'd recommend **option 1 first** (Mermaid in a `TRACK_MAP.md` — I can draft it now), then graduate to an SVG or sheet if the map proves useful. Want me to draft the initial track map?

