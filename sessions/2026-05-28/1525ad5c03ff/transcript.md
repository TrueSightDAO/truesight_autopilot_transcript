# Autopilot Session — 2026-05-28

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🤖 Autopilot

Now I can see the full picture. Both the **Warehouse Manager** and **Recipient** dropdowns on this page use the same GAS endpoint:

```javascript
// Managers
const res = await fetch(`${DAO_FORMS_BASE}?list=true`);

// Recipients
const res = await fetch(`${DAO_FORMS_BASE}?recipients=true`);
```

Where `DAO_FORMS_BASE` is:
```
https://script.google.com/macros/s/AKfycbztpV3TUIRn3ftNW1aGHAKw32OBJrp_p1Pr9mMAttoyWFZyQgBRPU2T6eGhkmJtz7xV/exec
```

**Same root cause as the contributor list** — it's the same Google Apps Script cold-start problem. The page actually has a **treasury-cache** fallback for managers (lines ~920-960), but the **recipients list** has no cache — it always hits GAS.

Here's what happens on page load:
1. `loadManagers()` → tries treasury-cache first, falls back to GAS `?list=true`
2. `loadRecipients()` → **always** hits GAS `?recipients=true` (no cache)
3. `loadAllCurrencies()` → tries treasury-cache, falls back to GAS `?all_currencies=true`

So the **recipients** list is the slowest because it has no caching at all. And if the treasury-cache fails for managers, that's two GAS calls back-to-back.

Want me to open a fix PR that:
1. **Caches the recipients list in localStorage** (same approach as the contributor list fix)
2. Also caches the manager list in localStorage as a fallback if treasury-cache fails


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

can you check git history to figure out how come these two view stopped reading from the JSON caches on github and or they reading from it right now?


### 🤖 Autopilot

Let me check the git history for both pages to see what changed.


### 🤖 Autopilot

The git history for both pages shows the most recent commit touching them was `07a2b018` (May 12) — a cache-busting commit that only bumped `menu.js` and `notifications.js` versions. Neither page's actual HTML was modified in that commit.

Let me look further back to find when the contributor/recipient loading was changed to use GAS instead of the JSON cache.


### 🤖 Autopilot

Now I have the full picture. Here's what I found from the git history:

---

## Analysis: Why the contributor/recipient lists are slow

**These pages have never read the contributor/recipient lists from the GitHub JSON cache.** Here's the history:

### report_contribution.html
- **April 27, 2026** — Commit `5fb5422d` ("perf(dapp): cache-first signature verify") switched the **identity check** from GAS to `DaoMembersCache.findByPublicKey()` (the GitHub CDN JSON). This was a **huge speedup** for the "Verifying your digital signature..." step.
- But the **contributor dropdown** (`loadContributors()`) has **always** called the GAS endpoint `?recipients=true`. It was never migrated to the JSON cache.

### report_inventory_movement.html
- Same story. The **identity check** uses `DaoMembersCache` (fast), but:
  - **Managers** → tries treasury-cache first, falls back to GAS `?list=true`
  - **Recipients** → **always** calls GAS `?recipients=true` (no cache at all)
  - **All currencies** → tries treasury-cache, falls back to GAS

### Why it feels slow now

The **identity check** got fast (50-150ms via GitHub CDN), so the page renders quickly... but then you're staring at "Loading managers..." and "Loading recipients..." while the GAS endpoint cold-starts. The contrast makes it feel worse than before, even though the GAS call itself hasn't changed.

The **real fix** would be to also publish the full recipient/contributor list to the treasury-cache JSON (like `dao_members.json` does for registered members), so the pages can pull it from GitHub's CDN instead of hitting GAS. But that requires changes on the GAS publisher side.

A simpler frontend-only fix would be to **cache the GAS responses in localStorage** so subsequent page loads within the same session are instant. Want me to open a PR for that?


### 🧑 Governor

I think we should do have the real fix isnt it? But arent recipient/contributor list and dao_members.json the same set of people???


### 🤖 Autopilot

That's a great question. Let me check what data each source actually returns.


### 🤖 Autopilot

Now I can see the full picture clearly. Let me check what `dao_members.json` contains vs what the GAS `?recipients=true` returns.


### 🤖 Autopilot

Now let me check what the GAS endpoint returns for `?recipients=true` vs what `dao_members.json` contains. Let me look at the treasury-cache repo to see the schema.


### 🤖 Autopilot

Now I have the full picture. Here's the answer:

---

**Yes, the recipient/contributor list and `dao_members.json` are essentially the same set of people**, but with a key difference in data shape.

### What each source returns:

**`dao_members.json`** (from treasury-cache, served via GitHub CDN):
- Contains `contributors[]` with fields like `name`, `email`, `public_keys[]`, `roles[]`
- This is the **registered DAO members** — people who have completed the email verification flow and have a public key on file

**GAS `?recipients=true`** (from the `daoForms` endpoint):
- Returns `[{key, name}]` — a flat list of contributor keys and display names
- This is the **same set of people** — it's the Contributors sheet from the Main Ledger

**GAS `?list=true`** (managers):
- Returns `[{key, name}]` — warehouse managers
- These are a **subset** of contributors who have been assigned as managers of inventory

### So why can't we just use `dao_members.json` for the dropdowns?

We **can**, but there's a subtle issue: the `dao_members.json` only contains contributors who have completed the **full email verification flow** (have a public key). The GAS `?recipients=true` endpoint returns **all** contributors from the Main Ledger's Contributors sheet, including those who haven't registered a public key yet.

However, looking at the code more carefully, the **real fix** is simpler than I initially thought. The **managers** list already has a treasury-cache fallback (`getManagersFromTreasuryCache()`), but the **recipients** list (`loadRecipients()`) has **zero caching** — it always hits GAS directly.

The treasury-cache JSON (`dao_offchain_treasury.json`) already has a `managers` array, but it doesn't have a `contributors`/`recipients` array. So the real fix would be to either:

1. **Publish the full contributors list to the treasury-cache** (add a `contributors` array to `dao_offchain_treasury.json` alongside `managers`), OR
2. **Use `dao_members.json`** for the recipient dropdown (it's already CDN-cached), accepting that unregistered contributors won't appear until they verify their email

Option 2 is the simplest — `dao_members.json` is already loaded on every page via `DaoMembersCache`. The contributor names are right there. The only gap is contributors who haven't registered a public key yet, but those are typically edge cases (newly added contributors who haven't completed verification).

Want me to open a PR that switches both pages to use `DaoMembersCache` for the recipient/contributor dropdowns instead of the GAS endpoint?

