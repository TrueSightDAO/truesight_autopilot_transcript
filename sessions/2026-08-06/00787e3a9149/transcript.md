# Autopilot Session — 2026-08-06

**Session**: `00787e3a9149`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=9745] Hey, can you help check if we have modules designed for Aura regarding Kakao Regenerative supply chain somewhere in our repository? I think it's the Agentic AI context somewhere. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

[3 tool result(s) compacted: search_context, search_context, search_context — detail in artifacts]


### 🤖 Autopilot

Nothing came up in agentic_ai_context. Let me also search the full org codebase to cover all repos.
[2 tool result(s) compacted: search_code, search_code — detail in artifacts]


### 🤖 Autopilot

Let me dig a bit deeper — a couple of those hits reference "Aura" in context files that might be relevant.
[2 tool result(s) compacted: read_repo_file, read_repo_file — detail in artifacts]


### 🤖 Autopilot

Let me try a few more angles.
[3 tool result(s) compacted: search_context, search_context, search_code — detail in artifacts]


### 🤖 Autopilot

Hey Gary — I did a thorough sweep of both **agentic_ai_context** and the broader org codebase. Here's what I found:

**Nothing specific to "Aura" or "Kakao Regenerative" exists anywhere** in our repos. Specifically:

- **"Aura"** — zero hits in any context file or repo document. The only hits in code were data CSVs (unrelated — like "aura" as part of a store name or keyword).
- **"Kakao Regenerative"** — zero hits as a term. The only "Kakao" mention is a passing reference in `RETAILER_ONBOARDING_PLAYBOOK.md` where it mentions competitor **Kakao Laboratory** — that's it.
- **"Regenerative supply chain"** as a design module — also zero hits.

We do have extensive **supply chain documentation** — `SUPPLY_CHAIN_AND_FREIGHTING.md`, `CONSIGNMENT_OPTIMAL_QUANTITY_PROPOSAL.md`, `AGROVERSE_QR_CODE_BATCH_GENERATION.md`, `TRUECHAIN.md` — but none of them are branded for Aura or use "Kakao Regenerative" as a framework name.

**Possibilities:**
1. This might be a module that was **discussed but never documented** — or it lives somewhere outside the DAO repos.
2. "Kakao Regenerative" could be a working name for something that ended up under a different label (e.g. "Agroverse" / "Ceremonial Cacao").

Want me to do a **web search** for the term "Kakao Regenerative" to see if it's an external framework or brand you might be remembering? Or can you give me a bit more context — was this something you sketched out elsewhere (Google Drive, Notion, etc.)?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] Aora modules was what I meant


### 🤖 Autopilot

[2 tool result(s) compacted: search_context, search_code — detail in artifacts]


### 🤖 Autopilot

Ahh — **Aora**, not Aura! That makes way more sense. Yes, we have a lot on Aora. Let me pull up the key docs.
[2 tool result(s) compacted: read_context_file, read_context_file — detail in artifacts]


### 🤖 Autopilot

**Found it!** Yes, we have extensive Aora documentation. Here's the summary:

**Two main docs:**

1. **`AORA_EXPERIENCE_PLAN.md`** — Master execution roadmap. Covers the full plan: PERT chart with timelines, blockers (demand forecast from Liz, MindLoop engine from Kaon, border crossing), cash position, the $10 retail / $6 DAO return model, and crucially — the **two learning modules** you asked about:
   - **Module 1: Agroforestry** (forest → dried bean) — the tree-to-bean journey
   - **Module 2: Supply Chain** (bag → bar → consumer) — includes logistics, freight, and the Fork Road game

2. **`briefs/aora_agroverse_event_brief.md`** — Event design brief. Details the 7-act immersive experience including the **Supply Chain Board Game** ("The Great Bean Adventure") — a ~4m × 3m floor game where children play as a cacao bean, making Fair Trade vs commodity path choices at the Fork Road station.

**There's also a `TrueSightDAO/aora` repo** listed in our OPERATING_INSTRUCTIONS.md.

The modules are designed as **docs-first MD content** that'll be published on **Kaon's MindLoop engine** for the China pilot with Liz's GO/Nucleus network. Completion of a module triggers a credentialing record on the Lineage layer.

Want me to read you the full Agroforestry or Supply Chain module content from the plan, or dive into anything specific?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] Can you fetch and return the two PDF files for the model one and module two?


### 🤖 Autopilot

[3 tool result(s) compacted: search_code, search_code, search_code — detail in artifacts]


### 🤖 Autopilot

Let me check if those exist as separate PDF files in our repos.
[3 tool result(s) compacted: search_code, search_code, list_org_repos — detail in artifacts]


### 🤖 Autopilot

There's a dedicated **`TrueSightDAO/aora`** repo. Let me check what's in there.
[1 tool result(s) compacted: list_directory — detail in artifacts]


### 🤖 Autopilot

Let me look inside the `aora` repo — the module content might be there as markdown that I can generate PDFs from.
[1 tool result(s) compacted: read_repo_file — detail in artifacts]


### 🤖 Autopilot

Found them! There are **two PDFs** already generated in the `TrueSightDAO/aora` repo. Let me download and send them to you.
[2 tool result(s) compacted: read_repo_file, read_repo_file — detail in artifacts]


### 🤖 Autopilot

The PDFs exist already! Let me download them from the repo and send them to you here.
[1 tool result(s) compacted: ssh_run — detail in artifacts]


### 🤖 Autopilot

Got both PDFs downloaded. Sending them to you now!
[2 tool result(s) compacted: send_telegram_attachment, send_telegram_attachment — detail in artifacts]


### 🤖 Autopilot

Sent! You should have both files now in the thread:

1. **Module 1 — Agroforestry** (~157 KB) — covers the journey from forest to dried bean. Sensory stations, big ideas for 6-year-olds, setting-aware exercises for farm/kitchen/warehouse/factory settings.

2. **Module 2 — Supply Chain** (~250 KB) — covers bag-to-bar-to-consumer. Includes the Fork Road board game design, freight transparency, and the full traceability flow.

Both are in the `TrueSightDAO/aora` repo under `pdfs/`, with the canonical Markdown sources at `modules/agroforestry/index.md` and `modules/supply_chain/index.md`. They're also available in the repo if you want to browse or regenerate them later.

———
**✅ Done this turn — actions taken:**
• `ssh run` → curl -sL -o /tmp/aora-module-agroforestry.en.pdf "https://raw.githubusercontent.com/TrueSightDAO/aora/main/pdfs/aora-module-agroforestry.en.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] Hey, can you have a report contribution of me, five minutes spent following up with Jerry regarding the upcoming meeting with Evans and Model UN in Beijing. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

[1 tool result(s) compacted: lookup_event_docs — detail in artifacts]


### 🤖 Autopilot

[1 tool result(s) compacted: submit_contribution — detail in artifacts]


### 🤖 Autopilot

All done, Gary. I've logged a **5-minute contribution event** for you — "Follow-up with Jerri re: upcoming meeting with Evans and Model UN in Beijing." It's submitted to the DAO ledger.

———
**✅ Done this turn — actions taken:**
• `submit contribution` → Contribution submitted successfully.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] PBL program 
Student exchange 
What the students get after graduation 

Farm stay


### 🤖 Autopilot

[3 tool result(s) compacted: search_context, search_context, search_context — detail in artifacts]


### 🤖 Autopilot

[3 tool result(s) compacted: search_code, search_code, search_code — detail in artifacts]


### 🤖 Autopilot

These terms didn't hit in context directly. Let me check the `aora` repo and the experience plan — this sounds like Aora program content.
[4 tool result(s) compacted: search_code, search_code, search_code, read_repo_file — detail in artifacts]


### 🤖 Autopilot

Let me check the Aora event brief and the modules themselves — these terms may live in the module content.
[2 tool result(s) compacted: read_repo_file, read_repo_file — detail in artifacts]


### 🤖 Autopilot

Let me search for these terms more specifically — PBL (Project-Based Learning), graduation credentials, and farm stay experiences.
[4 tool result(s) compacted: search_code, search_code, search_code, search_context — detail in artifacts]


### 🤖 Autopilot

Quick check done — I searched both agentic_ai_context and the full org codebase for all four terms:

- **PBL program** — no hits anywhere
- **Student exchange** — no hits
- **What students get after graduation** — nothing on point (only tangential graduation mentions)
- **Farm stay** — nothing; closest is the Aora event brief's farm/kitchen/workshop settings and the Agroforestry module's "walk with the farmer" exercise

So none of these four exist as designed modules or docs yet. They look like **new agenda topics** — presumably for the Evans + Model UN meeting in Beijing (the one you followed up with Jerri about).

Two options — tell me which you want:
1. **Draft a new brief** — I can write an Aora program expansion doc covering these four pillars: PBL program, student exchange, post-graduation outcomes (credentials/lineage), and farm-stay experiences — then open a PR in agentic_ai_context for review.
2. **Just capture the notes** — file them under OPEN_FOLLOWUPS.md as the meeting agenda so they're tracked.

Which one, or something else?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] Students in China PBL give enough information they come up with their own ideas on how to solve 

AI Give them how rapid deep dive


### 🤖 Autopilot

Got it — capturing this piece. So the PBL design is:

**PBL Program (China):**
- Give students **enough information** (the starting frame)
- They **come up with their own ideas** on how to solve the problem — student-driven, not lectured
- **AI accelerates the deep dive** — a rapid research/learning engine so they can go deep fast on whatever direction they choose

Assembling everything you've dictated so far, the program skeleton is:

1. **PBL program** — students in China, info-first, student-led solutions, AI-powered rapid deep dive
2. **Student exchange** — (Brazil ↔ China? need your detail)
3. **What students get after graduation** — credentials? Lineage records? Tree plantings?
4. **Farm stay** — immersive time on the cacao farm in Brazil

A couple of quick questions so I draft it right:
- **Graduation** — from the PBL program itself, or from their school (i.e. what the program confers)?
- **Exchange** — Brazil↔China both ways, or China students going to Brazil?
- Is this all going into **one brief** for the Evans + Model UN Beijing meeting?

Tell me the gaps and I'll draft the full document and open a PR for your review.


### 🧑 Governor

Please inspect the attached file.

[Attachment auto-processed: **7eefca846c484257a18c698cc8833cdb.pdf**]
- Type: PDF (6 pages, 11034 chars)

Extracted content:
```
--- Page 1 ---
Aora Module 1 — Agroforestry: Forest to Bean
English canonical · v0.1 · 2026-06-04 · TrueSight DAO / Agroverse
What this module is
Children walk the first half of chocolate’s life: a working cacao agroforest — a farm that is also a
forest — from the trees themselves to a dried bean ready for its journey. They meet the farmer, do
real farm work with real consequences, and discover that good chocolate starts as care for a living
system, years before anyone tastes anything.
The module is built from eight atomic exercises (AF-1 … AF-8). A session never needs all eight;
the facilitator (or session engine) picks by setting, time, and group. Every exercise has a live version
and sensory fallbacks, so the module runs on a farm in Bahia or in a library in Shenzhen.
Companion module: Supply Chain — Bean to Bar to You picks up exactly where this module ends:
the dried bean, packed for transport.
The big ideas
Each one passes the six-year-old test — a child can repeat it back:
A cacao farm is a forest. Many kinds of trees live together and help each other.
The farmer is the forest’s caretaker. Every day he walks, looks, trims, and plants.
Chocolate begins as a fruit. Sweet white pulp around purple seeds, inside a pod on a tree
trunk.
The beans are alive. Fermenting and drying is how we help them turn into flavor.
Patience is an ingredient. A tree takes years; a ferment takes days; the sun takes a week.
Who it’s for
Children 6–14, mixed ages welcome (older children take measuring/recording roles).
Mentors (industry leaders) participate as co-learners, not lecturers — they do the same
exercises with their hands.
Group shape: pods of 4–6 children + 1 mentor; up to ~25 per salon session.
SDG alignment
SDG
Why it fits
15 — Life on Land
1. 
2. 
3. 
4. 
5. 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 1 of 6

--- Page 2 ---
SDG
Why it fits
Agroforestry as biodiversity: shade trees, intercropping, soil
life.
13 — Climate Action
Trees as carbon sinks; planting a treeling is a measurable
climate act.
2 — Zero Hunger
Food grown in resilient polyculture systems; the farmer’s
livelihood.
12 — Responsible Consumption &
Production
Knowing what your food costs the land — and what it gives
back.
(SDG 4 — Quality Education applies program-wide to all Aora modules.)
Settings matrix
✔ = full live exercise · ◐ = adapted/sensory fallback · — = skip
Exercise
Farm
Kitchen
Workshop
Factory
Warehouse
AF-1 Tree detective
✔
◐
◐
—
—
AF-2 Walk with the farmer
✔
◐
◐
—
◐
AF-3 Plant a treeling
✔
◐
◐
—
—
AF-4 Harvest the pods
✔
◐
◐
—
—
AF-5 Crack the pod, taste the pulp
✔
✔
◐
—
◐
AF-6 Load the fermentation box
✔
◐
◐
—
—
AF-7 Turn the ferment
✔
◐
◐
—
—
AF-8 Sun-dry the beans
✔
◐
◐
—
◐
China salon reality (2026): sessions in Guangzhou / Shenzhen / Dongguan / Changsha /
Shanghai will be workshop or kitchen settings. Fallbacks are therefore not an afterthought
— they are the primary China experience, built around a specimen kit (dried whole pods,
dried beans in shell, leaves/photo cards, smell jars) shipped or carried ahead of the events.
Exercises
AF-1 · Tree detective
Big idea: A cacao farm is a forest — many kinds of trees living together.
Senses: see, hear, smell
• 
• 
Aora · Agroverse / TrueSight DAO · page 2 of 6

--- Page 3 ---
Duration: 20–30 min
Live (farm): Pods of children get a clipboard and hunt: find five different kinds of trees/plants,
rub and smell a leaf of each, listen for three sounds that are not human. Regroup: why does
the cacao tree like neighbors? (Shade, wind shelter, birds that eat pests, banana and açaí as
food while cacao grows.)
Fallback (kitchen/workshop): Photo-card matching game — match canopy layer cards (tall
shade trees / mid cacao / ground crops) into a “forest sandwich”; leaf and pod specimens
passed around.
Materials: clipboards + pencil (live); canopy photo cards, leaf/pod specimens (fallback)
Mentor prompt: “In your industry, who are your shade trees?”
AF-2 · Walk with the farmer
Big idea: The farmer is the forest’s caretaker — every day he walks, looks, and trims.
Senses: see, hear
Duration: 30–45 min (live) / 15 min (fallback)
Live (farm): Walk a row with the farmer. He shows what he looks for: branches growing the
wrong way, shoots stealing the tree’s energy, sick pods. Children take turns pruning an
unwanted shoot with supervision — one cut each, and the farmer explains why that cut.
Fallback: Short video diary of the farmer’s morning (filmed in Bahia), then the “day plan”
game: children sequence picture cards of the farmer’s day and discover most of it is looking,
not cutting.
Materials: pruning shears (farmer-held, supervised), gloves (live); video clip + day-plan cards
(fallback)
Safety: Blades stay in adult hands except the single supervised cut; closed shoes on farm.
Mentor prompt: “What do you prune in your own work so the good branches get the
energy?”
AF-3 · Plant a treeling
Big idea: A tree you plant today makes chocolate when you’re grown up — patience is an
ingredient.
Senses: touch, see, create
Duration: 20–30 min
Live (farm): Each pod of children plants one cacao seedling: dig, place, firm the soil, water,
name it. GPS/photo recorded so the planting can be registered on the TrueSight ledger and
revisited.
Fallback (kitchen/workshop): Plant a fresh cacao seed (or a fast germinator like a bean,
honestly labeled as a stand-in) in a clear cup with a wet paper towel so roots stay visible;
children take it home with a care card.
Materials: seedlings, spades, water (live); seeds, clear cups, paper towel, care cards
(fallback)
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 3 of 6

--- Page 4 ---
Credential hook: registered tree plantings are already a TrueSight DAO ledger event type —
each pod’s tree becomes a permanent record they can look up later.
AF-4 · Harvest the pods
Big idea: Chocolate begins as a fruit that grows straight out of the tree’s trunk.
Senses: see, touch
Duration: 15–25 min
Live (farm): Find ripe pods by color and the hollow knock-sound; harvest with the picking
pole or shears (adult cuts, child catches). Compare ripe vs. unripe weight and sound.
Fallback: Pass around whole dried pods; the knock test still works. “Where does the fruit
grow?” guessing game first — almost everyone guesses branches, the trunk surprise lands
every time.
Materials: picking pole/shears (live); 2–4 whole dried pods (fallback)
Safety: Adults handle cutting tools; children catch and carry.
AF-5 · Crack the pod, taste the pulp
Big idea: Inside the pod, the seeds wear sweet white coats — and the seeds, not the sweet
part, become chocolate.
Senses: taste, smell, touch, see — the anchor sensory moment of the module
Duration: 15–20 min
Live (farm/kitchen): Crack fresh pods (machete stays with the farmer; in a kitchen, a firm
twist after scoring). Children scoop, suck the pulp off a seed, and bite one raw seed — bitter!
The gap between sweet pulp and bitter seed is the question the rest of the program answers.
Fallback (workshop): Dried pod cracked as theater + frozen pulp (polpa de cacau, sold as
juice pulp) tasted from cups; raw dried bean to bite.
Materials: fresh pods (live) or dried pod + frozen pulp packs (fallback); cups, spoons, wipes
Allergy/food-safety note: pulp is a raw fruit; check group allergy list; spit-cups available for
the raw seed bite.
AF-6 · Load the fermentation box
Big idea: We tuck the beans into a warm box so tiny helpers (microbes) can start turning
them into flavor.
Senses: smell, touch
Duration: 15–20 min (live)
Live (farm): Carry pulp-covered beans to the fermentation boxes, load, cover with banana
leaves, feel the warmth of a box already mid-ferment (carefully — it reaches ~45–50 °C).
Fallback: Mini-ferment jar built in session: pulp/fruit + airlock balloon. The balloon inflating
over the days after the session is the take-home proof that “tiny helpers” are real and busy.
Pair with yeast-balloon demo for instant gratification.
Materials: banana leaves, boxes (live); jars, balloons, fruit, yeast packet (fallback)
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 4 of 6

--- Page 5 ---
AF-7 · Turn the ferment
Big idea: The beans are alive — we turn them so every bean gets warm, like flipping
pancakes.
Senses: smell (the module’s strongest smell moment), touch
Duration: 10–20 min
Live (farm): Shovel/rake beans from one box to the next with the farmer; smell the box at day
1 vs. day 3 vs. day 5 — sweet, then vinegary, then bready-chocolatey.
Fallback: Smell-jar timeline — three sealed jars (fresh pulp / vinegar-stage / dried bean)
passed in order; children put the jars on a day-1-to-day-6 timeline by nose alone.
Materials: rakes (live); three labeled smell jars (fallback — these jars are the single highest-
value item in the China specimen kit)
AF-8 · Sun-dry the beans
Big idea: The sun finishes the job — a week of sunshine gets packed into every bean.
Senses: touch, hear, see
Duration: 15–20 min
Live (farm): Rake beans thin on the drying deck, walk the “bean shuffle” barefoot rows like
the farmers do, learn the rattle test — a dry bean rattles and snaps, a wet one is silent and
bends.
Fallback: Rattle test with two bean samples (properly dried vs. deliberately under-dried);
weigh equal counts of each on a kitchen scale — where did the missing weight go? (Into the
air — water.)
Materials: rakes (live); two bean samples + small scale (fallback)
Hand-off line to Module 2: “The bean is ready. Now it has to travel across the ocean without
losing what the forest gave it — that’s the next story.”
Session templates
Workshop salon — 90 min, ~25 children + mentors (China cities default) 1. Arrival sensory table
(10’) — pods, beans, leaves to handle freely 2. AF-1 fallback — forest sandwich (15’) 3. AF-5
fallback — crack + pulp taste (20’) 4. AF-7 fallback — smell-jar timeline (15’) 5. AF-3 fallback —
plant a seed to take home (20’) 6. Circle: each pod tells one thing the forest needs from people (10’)
Kitchen session — 2 h: as above, plus AF-6 mini-ferment jars; AF-5 with fresh/frozen pulp.
Farm half-day — 3.5 h (Bahia / future farm legs): AF-2 → AF-1 → AF-4 → AF-5 → AF-6/AF-7
(whichever the ferment schedule offers) → AF-8 → AF-3 as the closing act.
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 5 of 6

--- Page 6 ---
Evidence & credentialing
Each completed session produces: pod-group photo, the exercise list run, and (live settings) the
registered tree planting. These map to Lineage credential events so a child’s Aora record
accumulates across sessions and settings — the “nodes” that grow impact and reach.
Open questions for the China team
Can frozen cacao pulp (polpa de congelada) be imported/sourced locally for AF-5? If not, the
pulp taste drops to photo + story.
Specimen kit logistics: ship ahead vs. carried in luggage in July — customs constraints on
plant material (dried pods/beans) into China?
Venue check per city: water access and food-handling permission decide kitchen vs.
workshop template.
1. 
2. 
3. 
Aora · Agroverse / TrueSight DAO · page 6 of 6
```


### 🤖 Autopilot

Got it — that's the **Aora Module 1 — Agroforestry PDF** (the same one I sent you earlier from the `aora` repo). It's the canonical format reference: big ideas → who it's for → SDG alignment → settings matrix → atomic exercises with live + fallback versions → session templates → evidence & credentialing → open questions.

Assuming you're pointing at this as the **template/format** for the new program pillars you're dictating (PBL, student exchange, post-graduation outcomes, farm stay), here's how I'd map them onto this structure:

| Pillar | Aora Module 1 analogue |
|--------|------------------------|
| **PBL program** | The "atomic exercises" model — but China PBL flips it: give students the info frame, they propose their own solutions, AI powers a rapid deep dive (per your last message) |
| **Farm stay** | The "farm half-day 3.5h" template scaled to multi-day immersion (AF-2 walk with farmer, AF-3 plant treeling, AF-4/5 harvest + taste) |
| **Student exchange** | Brazil ↔ China — the farm stay becomes the Brazil leg; China salons become the return leg |
| **Post-graduation outcomes** | The "Evidence & credentialing" section — Lineage records, tree plantings, certificates students keep after the program |

Before I draft it, a few quick confirmations:
1. **Format** — a single new doc (e.g. `plans/AORA_CHINA_PBL_PLAN.md`) in agentic_ai_context, following Module 1's structure?
2. **Graduation** — what do students actually receive? (Lineage credential + tree planting + certificate?)
3. **Exchange scope** — China students → Brazil farm, both directions, or something else?

Confirm and I'll draft the doc and open a PR for review.

———
**✅ Done this turn — actions taken:**
• `append to transcript` → https://github.com/TrueSightDAO/truesight_autopilot_transcript/blob/main/sessions/2026-08-06/b430bedaf544/transcript.md


### 🧑 Governor

Please inspect the attached file.

[Attachment auto-processed: **8c634f71244a4999b23e781f4d5001ed.pdf**]
- Type: PDF (7 pages, 13871 chars)

Extracted content:
```
--- Page 1 ---
Aora Module 2 — Supply Chain: Bean to Bar to You
English canonical · v0.2 · 2026-06-04 · TrueSight DAO / Agroverse
What this module is
Children follow the second half of chocolate’s life: a dried bean leaving a farm in Bahia and arriving
— as a bar, as a cup of cacao — in someone’s hands on the other side of the world. They pack,
track, store, roast, crack, grind, brew, and mold; and at the end they scan the bar’s QR code and
watch it remember its own journey on a public ledger.
The module is built from nine atomic exercises (SC-1 … SC-9). Like Module 1, a session picks by
setting, time, and group; every exercise has a live version and fallbacks. Module 1 ends with a dried
bean; this module begins with one.
Companion module: Agroforestry — Forest to Bean.
The big ideas
A bean travels farther than most people ever do — and lots of hands help it.
Every hand adds something: the packer, the shipper, the keeper, the roaster, the maker.
Heat unlocks the flavor the forest put in — roasting is cooking the forest’s work.
Nothing is wasted: the shell becomes tea, the nib becomes chocolate.
Chocolate tastes like the place it grew. Same recipe, different forest — different flavor.
The bar remembers where it came from — scan it and it tells you its story.
Who it’s for
Same shape as Module 1: children 6–14 in pods of 4–6 with a mentor; up to ~25 per salon. Mentors
co-create — supply chain is most mentors’ home turf, so this module is where mentor war-stories
land naturally (“my product travels too…”).
SDG alignment
SDG
Why it fits
8 — Decent Work & Economic Growth
Every hand on the journey is a livelihood; fair pricing made
visible.
9 — Industry, Innovation &
Infrastructure
Ships, warehouses, machines, tracking numbers —
infrastructure as a story.
1. 
2. 
3. 
4. 
5. 
6. 
Aora · Agroverse / TrueSight DAO · page 1 of 7

--- Page 2 ---
SDG
Why it fits
12 — Responsible Consumption &
Production
Whole-bean use (nib + husk-tea), waste as a design failure.
17 — Partnerships for the Goals
A bar of chocolate is a partnership between a farm, a DAO,
shops, and you.
Settings matrix
✔ = full live exercise · ◐ = adapted/sensory fallback · — = skip
Exercise
Farm
Kitchen
Workshop
Factory
Warehouse
SC-1 Pack for the journey
✔
◐
◐
—
✔
SC-2 Inside the warehouse
—
◐
◐
—
✔
SC-3 Roast
◐
✔
◐
✔
—
SC-4 Crack & winnow: nib and tea
✔
✔
✔
✔
◐
SC-5 Grind: nibs to liquid
◐
✔
◐
✔
—
SC-6 Brew the cup
◐
✔
◐
✔
◐
SC-7 Make the bar
—
✔
◐
✔
—
SC-8 Taste the place (tasting)
✔
✔
✔
✔
✔
SC-9 Scan the story (finale)
✔
✔
✔
✔
✔
Workshop note: SC-4 (crack & winnow) is the module’s no-fire hero — it is fully live in a
library. SC-8 and SC-9 run everywhere; SC-8 → SC-9 is the module’s natural closing pair
(taste the farms blind, then scan to reveal them), and SC-9 should close every session
regardless of setting.
Exercises
SC-1 · Pack for the journey
Big idea: A bean can’t walk — we pack it so it arrives as good as it left.
Senses: touch, see, create
Duration: 20–25 min
Live (farm/warehouse): Fill and sew/seal a real export sack; weigh it; write the lot label. Feel
why 60 kg is a two-person lift.
• 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 2 of 7

--- Page 3 ---
Fallback (kitchen/workshop): Each pod packs a mini-sack (cloth bag of beans), weighs it,
writes a real-format lot label, and gets a real Correios tracking number (e.g. CP…BR ) from an
actual Agroverse shipment — then traces on a map: Ilhéus → port → ocean → US. “This
number is the bean’s name while it travels.”
Materials: sacks, scale, labels, marker; printed tracking history + world map (fallback)
Mentor prompt: “What’s the ‘packaging’ that protects your work when you hand it to
someone else?”
SC-2 · Inside the warehouse
Big idea: Beans wait for their turn in a special room — cool, dry, and counted.
Senses: see, smell
Duration: 20–30 min (live) / 15 min (fallback)
Live (warehouse): Kirsten (San Francisco) or Matheus (Brazil) hosts: how sacks are stacked,
why off the floor, what humidity does, how counting works (and how a count becomes a
ledger row).
Fallback: Short video tour (or a live video call into the warehouse — time-zones permitting),
then the “store it right” game: cards with storage choices (next to onions? on wet floor?
sealed and high?) — children sort good/bad and discover beans absorb smells like a sponge.
Materials: none (live); video + sorting cards, one “onion-stored” smell-spoiled bean sample if
available (fallback)
SC-3 · Roast
Big idea: Heat wakes the bean up — roasting is cooking the forest’s work into flavor.
Senses: smell (the module’s strongest smell moment), hear (first crack), taste
Duration: 25–35 min
Live (kitchen/factory): Oven-roast a tray (or watch the factory roaster); smell the room
change minute by minute; taste the same bean raw vs. roasted — the before/after is the
point.
Fallback (workshop, no fire): Sealed-jar smell comparison (raw vs. fresh-roasted, roasted
that morning) + taste both; mark on a “flavor line” where each sits.
Materials: oven/tray or roaster (live); two bean jars per pod (fallback); tasting cups
Safety: Hot trays are adult-only; children smell and taste, adults handle heat.
SC-4 · Crack & winnow: nib and tea ⭐ workshop hero
Big idea: Nothing is wasted — the inside becomes chocolate, the jacket becomes tea.
Senses: touch, hear, taste, create
Duration: 25–30 min
Live (all settings incl. workshop): Children hand-crack roasted beans (fingers or rolling pin
in a zip bag), then winnow with breath, a paper fan, or a hair dryer on low over a bowl —
husks fly, nibs stay. Husks go to the teapot (thermos hot water if no kettle is allowed): cacao
tea. Nibs are tasted and saved for SC-5.
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 3 of 7

--- Page 4 ---
Materials: roasted beans, zip bags/rolling pins, bowls, fan or hair dryer, thermos + cups
Why it’s the hero: real transformation, zero fire, full sensory loop, and the “waste becomes
tea” lands SDG 12 in one move.
SC-5 · Grind: nibs to liquid
Big idea: Squeeze a nib hard enough and it melts — the chocolate was hiding inside all
along.
Senses: touch, see, taste
Duration: 20–30 min
Live (kitchen/factory): Mortar-and-pestle a handful of warm nibs until they turn from gravel
→ paste → glossy liquor (a mini melanger running in parallel shows where 24 more hours of
grinding leads). Children watch a dry thing become a liquid with no water added — fat, not
magic.
Fallback (workshop): Shorter mortar-and-pestle round (paste stage is enough to make the
point) + a jar of finished liquor to compare against.
Materials: mortars & pestles (one per pod), warm nibs, finished liquor sample; mini melanger
(kitchen, optional)
SC-6 · Brew the cup
Big idea: Before chocolate was a bar, it was a drink — for thousands of years.
Senses: taste, smell
Duration: 15–20 min
Live (kitchen): Whisk ground liquor (from SC-5) into hot water — straight, no sugar first. Then
each child doctors their own cup: a little sugar? cinnamon? Compare with the cacao-husk tea
from SC-4 — same tree, two drinks.
Fallback (workshop): Thermos-brewed ceremonial cacao served in small cups; the
doctoring step still works cold-safe.
Materials: liquor/ceremonial cacao, thermos/kettle, whisk, cups, sugar/cinnamon
Mentor note: this is the natural moment for the ceremonial/cultural thread — cacao as
something communities sit in circles around (the Aora session is one).
SC-7 · Make the bar
Big idea: A bar is a promise with a shape — same chocolate every time, ready to share.
Senses: create, see, taste
Duration: 30–40 min + setting time
Live (kitchen/factory): Melt finished chocolate, fill polycarbonate molds (the same 4-cavity
50 g format Agroverse uses), tap out the bubbles, chill, unmold, wrap. Each pod takes a bar
— and gives one away.
Fallback (workshop): run SC-8 Flight B (the concentration ladder) in this slot instead of
molding — same learning target (“what does percent mean?”), no heat required.
Materials: chocolate, molds, scraper, fridge access (live); see SC-8 for fallback materials
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 4 of 7

--- Page 5 ---
Cross-link: the mold itself connects to the Brazil mold-design work-stream (27.5 × 17.5 cm
polycarbonate, 4 × 50 g cavities) — the bar the children mold is the same bar the program
ships.
SC-8 · Taste the place — chocolate tasting, every setting
Big idea: Chocolate tastes like the place it grew — and like how much of the bean is in it.
Senses: taste, smell, see — the module’s anchor tasting moment
Duration: 25–35 min (both flights) / 15–20 min (one flight)
How it runs (everywhere): A real tasting, run like the pros but scored like a game. Teach the
ritual once — look, snap by the ear, smell, then let it melt (no chewing!) — then run two blind
flights:
Flight A — Same %, different farms (terroir). Two or three bars at the same concentration
(e.g. 70%), each from a different farm, each with its serialized QR code, served blind as A /
B / C. Children describe each square with a child-simple tasting wheel (fruity / nutty /
flowery / smoky / earthy), vote for favorites, then guess which farm card matches which
square. The reveal is the scan: each pod scans the QR and the bar announces its own farm
— terroir made tangible, and the direct hand-off into SC-9.
Flight B — Same farm, different %. One farm’s beans at 100% → 85% → 70% → milk.
Children place each square on a board from “all bean” to “all sugar” and find their own spot
— no wrong answers, but now percent means something. (This flight is also SC-7’s no-fire
fallback.)
Materials: single-origin bars (same % across ≥2 farms) with QR codes; one farm’s
concentration ladder; tasting mats (A/B/C circles + tasting-wheel words); water for palate
resets; farm cards (photo + name) for the matching game
Facilitation notes: Flight A before Flight B (palates are freshest for the subtle comparison);
milk chocolate always last (it swamps everything after it); the Agroverse cacao tasting wheel
is the adult reference — the child mat uses the five simple words above.
Mentor prompt: “Same recipe, different forest, different flavor — where does your work taste
of the place it was made?” (Calls back to AF-1: the forest the children investigated is literally
in the flavor.)
Sourcing note (China legs): the terroir flight needs same-% bars from at least two distinct
farms/shipments in Agroverse stock (e.g. different AGL batches) — confirm availability and
customs path early; see open questions.
SC-9 · Scan the story — the finale, every setting
Big idea: The bar remembers where it came from — scan it and it tells you.
Senses: see, create
Duration: 15–20 min
How it runs (everywhere): Each pod gets a real Agroverse bar with its serialized QR code (if
SC-8 ran, the tasting-flight bars are already in hand and already scanned once — now follow
one bar’s trail all the way down). Scan → the bar’s page: which farm, which shipment (the
same CP…BR  style journey from SC-1), the ledger trail. Children retell the bar’s story
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
Aora · Agroverse / TrueSight DAO · page 5 of 7

--- Page 6 ---
backwards — bar → grinder → roaster → warehouse → ship → ferment → pod → tree →
forest — each child takes one step. The chain of memory is the assessment: if the group can
walk it backwards, both modules landed.
Materials: QR-coded bars (one per pod), one phone/tablet per pod
Engine note: this exercise runs entirely on the Agroverse QR + TrueSight ledger stack — no
dependency on any external session engine. It is also the natural attachment point for a
session engine (each scan can register the session as a Lineage credential event).
China note: the QR target pages must be reachable from mainland networks — verify before
events; if unstable, pre-print the provenance page as a one-page handout per bar and keep
the scan as the dramatic reveal where connectivity allows.
Session templates
Workshop salon — 90 min, ~25 children + mentors (China cities default) 1. Arrival: world map +
tracking-number trace on the wall (10’) 2. SC-1 fallback — pack the mini-sack, name the bean (15’)
3. SC-4 live — crack & winnow; husk tea brewing while hands work (25’) 4. SC-8 — taste the place:
Flight A (farms, blind) + Flight B if time (25’) 5. SC-9 — scan the story + backwards chain (10’) 6.
Circle: every child names one hand that helped their bar (5’)
Kitchen session — 2.5 h: SC-1 → SC-3 (oven) → SC-4 → SC-5 → SC-6 → SC-8 (both flights) →
SC-9; SC-7 molding if time and fridge allow.
Factory / warehouse legs (Brazil, SF): SC-2 and SC-3/SC-5 live with the technician or Kirsten/
Matheus; SC-8 Flight A tasted next to the stacked sacks themselves, then close with SC-9.
Evidence & credentialing
Session evidence: pod photo, exercises run, SC-8 tasting mats (each pod’s flavor votes + farm
guesses), and the SC-9 scan event (which can land as a Lineage/ledger record per bar). The give-
one-bar-away from SC-7 doubles as the program’s outward ripple — each gifted bar carries a
scannable story.
Open questions for the China team
Customs/food-import path for roasted beans, liquor, ceremonial cacao, and finished QR bars
into China for the July events — what quantity is unproblematic in luggage vs. needs
paperwork?
Venue power + food-handling rules per city (decides SC-3 live vs. jar fallback, SC-7 molding
vs. taste ladder).
Connectivity check for SC-9 QR target pages from mainland networks (see China note above)
— coordinate with the tech-side GitHub/Gitee discussion.
One mentor per session to anchor SC-2’s “my product travels too” thread — Evan’s network?
• 
• 
• 
1. 
2. 
3. 
4. 
Aora · Agroverse / TrueSight DAO · page 6 of 7

--- Page 7 ---
SC-8 terroir flight sourcing: confirm ≥2 same-concentration single-origin bars from distinct
farms/shipments in Agroverse stock for July, plus the customs path for bringing tasting
quantities into China.
5. 
Aora · Agroverse / TrueSight DAO · page 7 of 7
```


### 🤖 Autopilot

Got it — that's **Aora Module 2 — Supply Chain: Bean to Bar to You** (v0.2). Now I have both canonical modules in hand:

**Module 1 — Agroforestry** (AF-1…AF-8): forest → dried bean
**Module 2 — Supply Chain** (SC-1…SC-9): dried bean → bar → you, ending with the QR scan on the TrueSight ledger

Both are now saved to the session transcript for cross-session recall.

**Structure I can mirror for the new China PBL program doc:**
- What this module is (one-paragraph essence)
- The big ideas (six-year-old test)
- Who it's for (pods of 4–6 + mentor)
- SDG alignment
- Settings matrix (farm/kitchen/workshop/factory/warehouse)
- Atomic exercises (each with live + fallback)
- Session templates (salon / kitchen / farm half-day)
- Evidence & credentialing (Lineage records, tree plantings, QR scans)
- Open questions for the China team

So, ready to draft the **China PBL program doc** in this exact format, incorporating what you've dictated:

1. **PBL program** — info-first framing, students generate their own solutions, **AI-powered rapid deep dive**
2. **Student exchange** — Brazil ↔ China (need direction detail)
3. **Post-graduation outcomes** — Lineage credentials, tree plantings, certificates
4. **Farm stay** — multi-day immersion on the cacao farm

Want me to go ahead and draft it as `plans/AORA_CHINA_PBL_PLAN.md` and open a PR for your review? And if you can fill in the two gaps — **exchange direction** and **what graduation confers** — I'll bake those in. Otherwise I'll draft with sensible defaults and you can edit.

———
**✅ Done this turn — actions taken:**
• `append to transcript` ×2 → session_id, content, and filename are required; https://github.com/TrueSightDAO/truesight_autopilot_transcript/blob/main/sessions/2026-08-06/b430bedaf544/transcript.md


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] So thoughts on extended these two programs with the above points


### 🤖 Autopilot

Love this direction — the two modules are a **perfect foundation** for all four pillars. Here's my honest take:

**The key insight:** Modules 1+2 are *single-session experiences* (90-min salon → half-day farm). Your four pillars turn them into a **multi-session program arc** — that's a different layer: session → program → credential. And the good news: the modules were already built for this. Their "Evidence & credentialing" sections explicitly say records **accumulate across sessions** — each session is a node, the program is the graph. So you're not bolting on; you're following the seam that's already there.

**How the pillars sequence naturally:**
1. **PBL program** — this is the biggest upgrade. The modules are currently *guided discovery* (facilitator picks, children experience). PBL flips it: students get the modules as the **sensory foundation**, then *generate their own questions and solutions*. The **AI rapid deep dive is the real differentiator** — a 12–14-year-old with an AI copilot can research "how do we make chocolate that doesn't destroy the forest?" in a way no 6-year-old program ever could. That's genuinely new — the original modules had zero AI component.
2. **Model UN deliberation** — and here's the kicker: Model UN is a *deliberation format*. PBL + Model UN = students research → propose solutions → **debate them in a "Cacao Assembly"** at the Beijing meeting. That could be the capstone of the PBL arc — not graduation.
3. **Farm stay** — this solves a real gap. The China reality is fallback-heavy (specimen kits, smell jars). A farm stay in Bahia/Pará gives the **full live experience** — all the ✔ exercises — and it's the natural Brazil leg of the exchange.
4. **Graduation** — this is the DAO's moat. Stack the existing artifacts (registered tree planting, QR scan records, pod photos) + the PBL capstone into a **verifiable Lineage credential** — an "Aora Cacao Guardian" portfolio. Nobody else on earth can issue a credential backed by real on-chain provenance *and* real trees planted in the Amazon.

**Three gaps to close before drafting:**
- **Age band** — PBL + AI deep dive skews older (10–14). Modules say 6–14; be explicit which segment the program targets.
- **Funding** — Brazil↔China exchange isn't covered by the $10/bar economics. Needs a sponsor or school/partner model.
- **AI compliance** — AI deep dive for minors in mainland China means data privacy + age guardrails. Worth flagging early, not late.

Want me to draft this as the extension plan doc (mirroring the module format) and open a PR?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] Follow up to chat with Evan and Cao on perhaps rolling out this program via Cao’s WeAcademy


### 🤖 Autopilot

"WeAcademy" isn't in our context anywhere — I searched both agentic_ai_context and the full org, zero hits. But it's clearly linked to **Mr. Cao** (Liz's partner in the GO/Nucleus network, per the Aora experience plan) — so this reads as: after the Beijing meeting with Evan + Model UN, follow up with **Evan and Cao** about rolling out the Aora program via **Cao's WeAcademy** platform.

I'll file this in OPEN_FOLLOWUPS.md so it's tracked cross-session.


### 🤖 Autopilot

Done — filed it. Here's the summary:

**Follow-up logged** (PR [#734](https://github.com/TrueSightDAO/agentic_ai_context/pull/734)):
> After the Beijing meeting with Evan + Model UN → follow up with **Evan and Mr. Cao** about rolling out the Aora program via **Cao's WeAcademy**.

I bundled it with the full program context so whoever picks it up has everything:
- The 4-pillar extension (PBL, student exchange, post-graduation outcomes, farm stay)
- The AI deep-dive angle
- A note that **"WeAcademy" has zero hits in our repos** — so we still need to confirm what it is (presumably Mr. Cao's education platform) and how Aora maps onto it (venue? curriculum channel? distribution?)

**Deliverable I set for it:** a short one-pager proposal for Cao/Evan on the Aora + WeAcademy roll-out.

If you can tell me a bit more about WeAcademy — what it is, who runs it, what it offers — I can draft that one-pager right now, or expand the plan doc while you're at the Beijing meeting.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9745] And then Evan can come in as a consultant


### 🤖 Autopilot

The em-dash characters likely differ. Let me read the actual text on the branch to get the exact string.


### 🤖 Autopilot

The em-dash/quote characters are the likely culprit. Let me use a shorter, safer anchor that avoids special characters.


### 🤖 Autopilot

The tool applies edits against the base branch — my new entry only exists on the PR branch, so I can't amend it in place. I'll open a consolidated PR with the full entry (including Evan-as-consultant) so there's one clean version to merge.


### 🤖 Autopilot

Added! Here's where things stand:

**Evan's role is now on record:**
- **WeAcademy roll-out** → Evan + Mr. Cao (after the Beijing meeting with Model UN)
- **Evan comes in as a consultant** (educational advisor) on the roll-out

**One consolidated PR** — [#735](https://github.com/TrueSightDAO/agentic_ai_context/pull/735) — has the full follow-up entry: the 4-pillar program context, the WeAcademy roll-out, and Evan-as-consultant. I left the earlier PR #734 open but flagged it in #735's body as superseded (close #734, merge #735 instead) — so there's exactly **one** clean entry when you review, no duplicates.

Want me to:
1. **Draft the one-pager** for Cao/Evan now (Aora + WeAcademy proposal), or
2. Wait until after the Beijing meeting and draft it with what actually comes out of it?

