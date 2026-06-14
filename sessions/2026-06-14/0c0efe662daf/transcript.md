# Autopilot Session — 2026-06-14

**Session**: `0c0efe662daf`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=3966] Now that Nora and increasingly more and more partners are joining our network, I am foreseeing more and more volume of money flowing through. Right now Matheus is using his private entity in Brazil to channel the exports, while I am using my own bank account to collect the funds. TrueTech INc is the importing entity.

Nora who runs Kopi bar in berkeley is even thinking of channeling sales proceeds from each cup of coffee to planting a tree. MIght be interesting to figure out how to provide her with tax write offs for her business.  

I am thinking what is the best way to setup the holdings.. What are your thoughts?

Kirsten surfaced DUNA, Paloma surfaced Prospera holding entity and then a corresponding CNPJ in brazil for the exports.

This surfaced during friday's tech fest

Should either get the DUNA setup or a proper dedicated checking account for TrueTech Inc setup as an interim now that the expecting volume of transactions passing through the network seems like it is heading for a scaling phase… 

The managing partner of Progressive Ventures from yesterday mentioned that impact funds usually are after tax write offs when they finance projects…. 

Nora mentioned that for each cup of cacao she sells from her store, she wants to contribute part of the proceeds to the rainforest restoration efforts.

The signal for the tax write off part of our infrastructure in the USA jurisidiction is gradually to turn from grey (_not a priority_) to red (_get done ASAP_)… 

Will speak with the folks from SVH capital during the meetup happening on the 26th of June.. If I don’t remember wrongly, Stanley mentioned they are specialized in web3 specific legal entity structuring within the USA jurisdiction.

_PS: the convergence seems to be accelerating…_

on the 26th we will be having cacao circle with the folks of SVH capital. I wonder if there might be something to consult them about.

Go do as deep a research as you can, come up with various proposed structure for legal entity representing our DAO see our ledger to figure what will most likely map well. Surface ongoing cost concerns as well as what are some clarifying questions that might be interesting to speak with the SVH folks about on the 26th when we are over at their space. 

YOur output should be a .md file as well as a corresponding PDF


### 🤖 Autopilot

I'll start by gathering context from our existing documentation and then do deep research on the legal entity structures mentioned.
[6 tool result(s) compacted: read_context_file, read_context_file, read_context_file, search_context, search_context, search_context — detail in artifacts]


### 🤖 Autopilot

[4 tool result(s) compacted: read_context_file, read_context_file, read_context_file, read_context_file — detail in artifacts]


### 🤖 Autopilot

Now let me do deep research on DUNA, Prospera, and the legal entity structures mentioned.
[3 tool result(s) compacted: web_search, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

[3 tool result(s) compacted: web_extract, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

[3 tool result(s) compacted: web_search, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

[3 tool result(s) compacted: web_extract, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

Now let me look at our ledger to understand the current financial flows and what maps well.


### 🤖 Autopilot

Let me get the partner data and look at the supply chain docs for the full picture.


### 🤖 Autopilot

Now let me check what the ledger looks like for partners and the current offchain asset location to understand the financial flows.


### 🤖 Autopilot

Excellent. I now have a comprehensive picture. Let me also check the whitepaper for the legal entity references.


### 🤖 Autopilot

Now I have a thorough picture. Let me compile the research into the .md file and generate the PDF.


### 🤖 Autopilot

Now let me generate the PDF version.


### 🤖 Autopilot

Now let me upload the PDF to GitHub alongside the .md file.


### 🤖 Autopilot

Here's the full output. Both files are in PR **#487** on `agentic_ai_context`.

---

## Summary of what I found and built

### The core insight

The tax-write-off signal is indeed turning from grey to red — and **Nora's use case** is the catalyst that makes it urgent. A for-profit C-corp (TrueTech Inc) **cannot** issue tax-deductible receipts. For Nora to give her customers a per-cup → tree-planting tax write-off, the receiving entity must be a qualified nonprofit.

### Recommended structure: Three-Entity Stack

```
Wyoming DUNA (nonprofit, 501(c)(3) aspirant)
    ↓ Service Agreement
TrueTech Inc (Delaware C-corp, import/distribution)
    ↓ Inter-company agreement
Brazilian LTDA (CNPJ, export/sourcing)
```

### Why DUNA over DAO LLC

| Factor | DUNA Wins | DAO LLC Wins |
|--------|-----------|--------------|
| Tax-deductible receipts for Nora's customers | ✅ | ❌ |
| Impact fund compatibility | ✅ | ❌ |
| Mission alignment (nonprofit) | ✅ | ❌ |
| Profit distribution to TDG holders | ❌ | ✅ |

The DUNA's nonprofit constraint actually **aligns perfectly** with the mission (restore 10,000 hectares). TrueTech Inc remains the for-profit engine that generates revenue; the DUNA is the mission wrapper that receives donations, plants trees, and issues tax receipts.

### Immediate action item (this week)

**Open a dedicated business checking account for TrueTech Inc.** This is the $0-$500 fix that stops the commingling risk immediately, regardless of which long-term structure you choose.

### 13 questions for SVH Capital on June 26

The most important ones to lead with:

1. **Nora's use case first:** A Berkeley café wants per-cup → tree-planting with tax write-offs. Is DUNA + 501(c)(3) the cleanest path, or is fiscal sponsorship by an existing 501(c)(3) a simpler interim structure?

2. **DUNA + 501(c)(3) feasibility:** Has SVH seen a DUNA successfully get 501(c)(3) status? Timeline?

3. **UNA stepping stone:** Can we start with a Wyoming UNA (no 100-member minimum) and convert to DUNA later? OtoCo offers this on-chain.

4. **DUNA owning a for-profit:** Can the DUNA wholly own TrueTech Inc, or must they be separate with a service agreement?

### Files delivered

| File | Location |
|------|----------|
| **Markdown** | `agentic_ai_context/LEGAL_ENTITY_STRUCTURING_PROPOSAL.md` (PR #487) |
| **PDF** | Same PR — `LEGAL_ENTITY_STRUCTURING_PROPOSAL.pdf` |

Both are on branch `legal-entity-structuring-proposal` — ready for your review before the SVH meeting.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=3966] the tax write off is a nice to have for their cafe. BUt I am thinking more from the perspective of what the venture partner mentioned, having a tax write off facility will allow us to approach organizations that want to do tax write off isnt it?


### 🤖 Autopilot

You're right — I was framing it too narrowly around Nora's café. Let me reframe.

The venture partner's point is the **real strategic signal**: a tax-deductible donation facility is a **fundraising channel**, not just a nice-to-have for retail customers. It unlocks:

- **Impact funds** (like Progressive Ventures' LPs) — they can write tax-deductible checks instead of needing equity structures
- **Corporate ESG budgets** — companies get a tax write-off + verified carbon offsets = easy budget approval
- **High-net-worth donors** — individuals who want to support rainforest restoration and reduce their tax liability
- **Foundation grants** — most foundations can only grant to 501(c)(3) entities

Without it, we can only approach these organizations for **equity investments or revenue-share deals**, which is a much harder conversation. With a DUNA + 501(c)(3), we can approach them with a **donation pathway** — lower friction, faster decisions, aligned incentives.

So the priority order flips:

1. **DUNA formation** (not just a bank account) — unlocks the fundraising channel
2. **501(c)(3) application** — makes the channel real
3. **Nora's café** — becomes a downstream beneficiary of infrastructure we built for the bigger play

Does that reframe match what you're thinking? If so, I can update the proposal to lead with the **fundraising/institutional channel** framing rather than the retail café use case.

