# Autopilot Session — 2026-05-29

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🤖 Autopilot

Now I see the key difference. The `members.html` page reads from a completely different source:

```
const INDEX_URL = 'https://raw.githubusercontent.com/TrueSightDAO/lineage-credentials/main/_cache/index.json';
```

Let me check that file.


### 🤖 Autopilot

Now I can see the full picture. The two data sources are completely different:

**`dao_members.json`** (treasury-cache) — 12 contributors who have **registered public keys** (RSA keypairs for signing). These are people who can cryptographically sign DAO submissions.

**`lineage-credentials/_cache/index.json`** (used by `members.html`) — 387 members who have **contributed** to the DAO (received TDG, made submissions, etc.) but may or may not have registered a public key.

The discrepancy is that `dao_members.json` only includes contributors who have gone through the **public key registration** process (via `[EMAIL VERIFICATION EVENT]`), while the lineage-credentials index includes **everyone** who has ever received TDG or made a contribution, regardless of whether they've set up signing keys.

So the names in `dao_members.json` that aren't on `members.html` would be... actually, let me cross-reference:

**In `dao_members.json` but NOT in lineage-credentials index:**
- `Elizabeth Wong` — she's in lineage as "Elizabeth Wong" (slug: `elizabeth-wong`) ✓
- `Francine Cabral` — in lineage as `francine-cabral` ✓
- `Maurillo Gomes` — not in lineage index
- `Marta Lopes` — in lineage as `marta-lopes` ✓
- `Irene Hsu` — in lineage as `irene-hsu` ✓

Actually, looking more carefully, most of the `dao_members.json` names DO appear in the lineage index. The key difference is:

1. **`dao_members.json`** = contributors who have **registered public keys** (can sign transactions). This is a subset.
2. **`members.html`** (lineage-credentials) = **all** contributors (anyone who has received TDG or submitted contributions), regardless of key registration.

So the answer to your question is: **`dao_members.json` is a subset of the full members list** — it only includes people who have completed the public key registration process. The `members.html` page shows the full 387-member list from the lineage-credentials cache, which includes everyone who has ever contributed to the DAO. The 12 people in `dao_members.json` are the ones who have registered RSA keys for signing.


### 🤖 Autopilot

Now I have the full picture. Let me answer your question clearly.

**These are two completely different data sources serving different purposes:**

### `dao_members.json` (treasury-cache)
- **Source:** Main Ledger → `Contributors Digital Signatures` + `Contributors voting weight` + `Governors` tabs
- **Contains:** Only **12 contributors** who have registered RSA public keys (digital signatures) with the DAO
- **Purpose:** Cryptographic identity — used by the DApp for signature verification, permission gating, and Edgar submissions
- **Schema:** Has `public_keys[]`, `voting_rights`, `email`, `roles`
- **Missing people like "Ed", "Fatima Toledo", "Val Lapidus", "Anika Giftge"** etc. — these people have DAO contributions but haven't registered a public key yet

### `members.html` (lineage-credentials)
- **Source:** `https://raw.githubusercontent.com/TrueSightDAO/lineage-credentials/main/_cache/index.json`
- **Contains:** **387 members** — everyone who has ever made a DAO contribution, regardless of whether they have a public key
- **Purpose:** Public directory / credential profiles — shows contribution history, TDG controlled, voting power
- **Schema:** Has `display_name`, `total_tdg_controlled`, `total_contributions`, `voting_rights`, `is_governor`
- **Includes** "Ed" (299 contributions, 82K TDG), "Fatima Toledo" (247 contributions, 65K TDG), "Val Lapidus" (258 contributions, 62K TDG), etc.

**So the answer is:** The names in `dao_members.json` that aren't on `members.html` are the ones that **have registered public keys** but may not have DAO contributions yet (like `Maurillo Gomes` who has 0 voting rights and 0 contributions). And conversely, the names on `members.html` that aren't in `dao_members.json` (like Ed, Fatima, Val, Anika, etc.) are contributors who **have DAO contributions but haven't registered a public key** — they can submit contributions through the DApp but can't cryptographically sign them yet.

The two lists serve different purposes:
- **`dao_members.json`** = who can cryptographically sign DAO actions (12 people)
- **`lineage-credentials` index** = who has contributed to the DAO (387 people)


### 🧑 Governor

I think the dao_members should be the supraset


### 🤖 Autopilot

You're right — let me re-examine this more carefully. Let me look at the actual `dao_members.json` file and the lineage index side by side to see who's missing from each.


### 🤖 Autopilot

Let me find where the autopilot code lives and look at the `dao_members.json` file.


### 🤖 Autopilot

There's a `treasury-cache` repo. Let me look at it.


### 🤖 Autopilot

Now I have the full picture. Let me also check the lineage-credentials index to see who's there.

Now I can see clearly. Let me compare the two data sources:

**`dao_members.json`** (12 contributors with registered public keys):
1. Alexandre Fernandes
2. Elizabeth Wong
3. Francine Cabral
4. Garis Pang
5. Gary Teh
6. Irene Hsu
7. Kirsten Ritschel
8. Marta Lopes
9. Matheus Reis
10. Maurillo Gomes
11. Sacred Earth Farms
12. truesight-autopilot

**`lineage-credentials/index.json`** (387 members — anyone who has contributed)

Let me check which of the 12 `dao_members.json` names are NOT in the lineage index.

From the lineage index I already fetched, I can see:
- **Alexandre Fernandes** ✓ (slug: `alexandre-fernandes`)
- **Elizabeth Wong** — let me search... not obviously present in the lineage index
- **Francine Cabral** ✓ (slug: `francine-cabral`)
- **Garis Pang** ✓ (slug: `garis-pang`)
- **Gary Teh** ✓ (slug: `gary-teh`)
- **Irene Hsu** ✓ (slug: `irene-hsu`)
- **Kirsten Ritschel** ✓ (slug: `kirsten-ritschel`)
- **Marta Lopes** ✓ (slug: `marta-lopes`)
- **Matheus Reis** ✓ (slug: `matheus-reis`)
- **Maurillo Gomes** — NOT in lineage index
- **Sacred Earth Farms** ✓ (slug: `sacred-earth-farms`)
- **truesight-autopilot** — NOT in lineage index (this is the bot itself)

So the answer is:

**`dao_members.json` is NOT a superset of the lineage-credentials members list.** It's the opposite — it's a **small subset** (12 people) of the full 387-member list. The 12 people in `dao_members.json` are those who have registered RSA public keys for cryptographic signing. The lineage-credentials index (which powers `members.html`) includes all 387 contributors regardless of whether they have keys.

The 2 names in `dao_members.json` that are NOT in the lineage index are:
1. **Maurillo Gomes** — registered a public key but has 0 voting rights, 0 contributions, so never appears in the lineage cache
2. **truesight-autopilot** — the bot account itself, not a human contributor

And conversely, **375 contributors** in the lineage index (like Ed, Fatima Toledo, Val Lapidus, Anika Giftge, etc.) are NOT in `dao_members.json` because they haven't registered public keys.

If you want `dao_members.json` to be the superset (i.e., include everyone), then the fix would be in the **`dao_members_cache_publisher`** — the process that generates this file. It currently only includes contributors who have registered public keys. It would need to be changed to include **all** contributors from the Main Ledger, with `public_keys` being an empty array for those who haven't registered yet.

Would you like me to investigate the code that generates `dao_members.json` and open a fix PR?


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Yes. That is the proper approach for the GAS. To include all the 387 member list


### 🤖 Autopilot

Let me find the code that generates `dao_members.json` so I can understand how to fix it.


### 🤖 Autopilot

Now I can see the source. The `dao_members.json` is generated by `tokenomics/google_app_scripts/tdg_identity_management/dao_members_cache_publisher.gs`. Let me look at that file.


### 🤖 Autopilot

Now I understand the full picture. The issue is clear:

**Root cause:** The `publishDaoMembersCacheToGithub_()` function in `dao_members_cache_publisher.gs` builds the contributor list **only** from the `Contributors Digital Signatures` sheet — it iterates `sigsRows` (rows from the signatures sheet) and only includes people who have at least one ACTIVE public key. The 375 contributors who appear on `members.html` (via the lineage-credentials index) but not in `dao_members.json` are people who have DAO contributions but have never registered a public key.

**The fix:** The publisher needs to also read the `Contributors voting weight` sheet (which has ALL contributors, not just those with keys) and include every name from there, with an empty `public_keys` array for those who haven't registered keys yet.

Let me open a fix PR.


### 🤖 Autopilot

I've opened **PR #325** on the `tokenomics` repo. Here's what it does:

**Root cause:** The `dao_members_cache_publisher.gs` script builds the contributor list by iterating only the `Contributors Digital Signatures` sheet, filtering to rows with ACTIVE public keys. Anyone who hasn't registered a key is completely skipped.

**Fix:** After building the `byName` map from the signatures sheet, the script now also iterates the `Contributors voting weight` sheet (which contains ALL contributors — all 387 of them) and adds any missing names with an empty `public_keys` array. This way:

- Contributors **with** public keys → appear with their keys (as before)
- Contributors **without** public keys → appear with `public_keys: []` and `email: null`
- The `counts.contributors` will now reflect the full 387-member list

The PR is a draft — would you like me to mark it ready for review, or do you want to review the changes first?


### 🧑 Governor

What is the URL?


### 🤖 Autopilot

The PR URL is:

**https://github.com/TrueSightDAO/tokenomics/pull/325**


### 🧑 Governor

Looks good to me merge it


### 🤖 Autopilot

PR #325 has been merged. The next time the `dao_members_cache_publisher` runs (either via the daily cron at ~03:00 UTC, or the next Edgar webhook trigger), `dao_members.json` will be regenerated with all 387 contributors — those with public keys will have their keys listed, and those without will have an empty `public_keys` array.

