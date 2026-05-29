# Autopilot Session — 2026-05-29

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


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


### 🧑 Governor

are you able to clasp push and deploy?


### 🤖 Autopilot

Let me check if `clasp` is available on this server.


### 🤖 Autopilot

No `clasp` installed on this server. `clasp` is a Node.js tool for pushing to Google Apps Script projects — it's typically installed via `npm` and used from a developer's local machine or CI, not from this autopilot server.

The `dao_members_cache_publisher.gs` file is deployed as a Google Apps Script project (attached to the Main Ledger spreadsheet). To push the merged code, you'd need to:

1. **Install clasp locally** on a dev machine: `npm install -g @google/clasp`
2. **Clone the project**: `clasp clone <script-id>` (the script ID is in the Apps Script project settings)
3. **Push the updated code**: `clasp push`

Alternatively, you can deploy directly from the **Apps Script editor** in the browser:
1. Open the Main Ledger spreadsheet (`1GE7PUq-UT6x2rBN-Q2ksogbWpgyuh2SaxJyG_uEK6PU`)
2. Go to **Extensions → Apps Script**
3. Navigate to the `dao_members_cache_publisher.gs` file
4. Paste the updated code (from the merged PR)
5. Click **Deploy → Test deployments** or use the existing deployment

I don't have `clasp` or `npm` installed on this server, and I don't have access to the Google Apps Script project credentials needed to authenticate clasp. This would need to be done from a machine with the proper GAS project access. Would you like me to look into whether there's a CI/CD pipeline set up for this?


### 🧑 Governor

can you install it and then attempt to do a clasp push?


### 🤖 Autopilot

Let me check if Node.js is available first.


### 🤖 Autopilot

Let me check if Node.js is available on this server.


### 🤖 Autopilot

Node.js is not installed on this server. I could install it, but there's a bigger problem: **clasp requires OAuth authentication** (either via browser or a service account JSON file). Even if I install Node.js and clasp, I'd need:

1. The **Google Apps Script project ID** for the `dao_members_cache_publisher` script
2. A **service account JSON key** with access to that GAS project (or browser-based OAuth which isn't possible headless)

I don't have access to either of those credentials on this server. The GAS project is bound to the Main Ledger spreadsheet and is deployed via the Apps Script editor in the browser.

However, I can check if there's a CI/CD pipeline or a webhook that could trigger a redeploy. Let me look at the context files for any deployment instructions.


### 🤖 Autopilot

I found the key info in the context file. Let me look at the clasp notes:


### 🤖 Autopilot

Now I see the full picture. The `dao_members_cache_publisher.gs` is deployed as a Google Apps Script project. Let me check if there's a clasp mirror for it.


### 🤖 Autopilot

I can see the clasp mirrors but I don't see a specific mirror for `dao_members_cache_publisher`. The file is in `tokenomics/google_app_scripts/tdg_identity_management/dao_members_cache_publisher.gs`. Let me check if there's a clasp mirror for the TDG - Email Identity Management project which is the closest match.

Looking at the index, **"TDG - Email Identity Management"** (`1K1wcXFAopSA0cI7oBpu5bl1sagrJ2Quv44B0ppjiIxtl3MKJ_PCsppCf`) is the project that would contain the `dao_members_cache_publisher.gs` code. But I don't have Node.js installed on this server, and clasp requires OAuth credentials that I don't have access to.

Let me be straightforward with you, Gary:

**I can't do a clasp push from this server** for two reasons:

1. **Node.js is not installed** — I'd need to install it first (`apt install nodejs npm`)
2. **Clasp requires authentication** — even after installing, I'd need either:
   - A browser-based OAuth flow (impossible headless on a server)
   - A **service account JSON key** with access to the GAS project (`1K1wcXFAopSA0cI7oBpu5bl1sagrJ2Quv44B0ppjiIxtl3MKJ_PCsppCf`)

However, I can install Node.js + clasp and attempt a **`clasp login --creds`** if you have a service account JSON file that has access to that Apps Script project. Do you have one I can use? Or would you prefer to just deploy it manually from the Apps Script editor?

The editor URL for the TDG - Email Identity Management project is:
**https://script.google.com/home/projects/1K1wcXFAopSA0cI7oBpu5bl1sagrJ2Quv44B0ppjiIxtl3MKJ_PCsppCf/edit**

You can paste the updated code from the merged PR into the `dao_members_cache_publisher.gs` file there and save it. The daily cron trigger will pick it up automatically.


### 🧑 Governor

Ok, no worries. you will gain what you need during your next incarnation when you get rebooted. Meanwhile. I was looking through contribution summary portion of https://dapp.truesight.me/report_contribution.html once its submitted. I wonder if the format I used for my description could be preserved?? Perhaps wrap it in <pre>??


### 🤖 Autopilot

Let me look at the contribution report page and understand how descriptions are rendered.


### 🤖 Autopilot

Now I can see the issue. Let me look at how the description is rendered in the contribution summary. The key part is:

```javascript
document.getElementById('summaryDescription').textContent = description;
```

This uses `.textContent` which strips all HTML formatting. Your descriptions with structured formatting (like the ones you paste with line breaks and indentation) get flattened into a single block of text.

Let me also check how the description is formatted in the `requestText` that gets submitted:

```javascript
const formattedDescription = description.replace(/\r?\n/g, '\n  ');
```

So line breaks are preserved in the submission text, but the **summary display** on the page uses `.textContent` which renders it as plain text without any formatting.

The fix is simple — in the `renderContributionSummary` function, change the description rendering to preserve line breaks. Using `<pre>` would work but might be too aggressive with font. A better approach is to use `white-space: pre-wrap` or convert newlines to `<br>` tags.

Let me open a fix PR.


### 🤖 Autopilot

I've opened **PR #2** on `dapp_prod`. The fix is simple — I added `white-space: pre-wrap;` to the `.summary-value` CSS class in the contribution summary section, which preserves line breaks and indentation from your original description without introducing any XSS risk (since it still uses `.textContent`).

The PR URL is: **https://github.com/TrueSightDAO/dapp_prod/pull/2**

Would you like me to mark it ready for review or merge it?


### 🧑 Governor

Also make sure to do your code changes in dapp_beta instead


### 🤖 Autopilot

You're right — the workflow is to land changes in `dapp_beta` first, then promote to `dapp_prod`. Let me close that PR and open one in `dapp_beta` instead.


### 🤖 Autopilot

Good, `dapp_beta` has the same code. Let me close the `dapp_prod` PR and open one in `dapp_beta` instead.


### 🤖 Autopilot

Done. The `dapp_prod` PR was the wrong target — I've now opened **PR #11** on `dapp_beta` instead.

**PR URL:** https://github.com/TrueSightDAO/dapp_beta/pull/11

The fix adds `white-space: pre-wrap;` to the `.summary-value` CSS in the contribution summary, so your structured descriptions with line breaks and bullet points will render exactly as you typed them. Once merged to `dapp_beta`, it can be promoted to `dapp_prod` via `gh repo sync`.

Would you like me to mark it ready for review or merge it?


### 🧑 Governor

What about a pre in the dapp modules that you touched here 

https://github.com/TrueSightDAO/dapp_beta/pull/10


### 🤖 Autopilot

Let me look at PR #10 to see what was changed there.


### 🤖 Autopilot

I see — PR #10 is the same file but I can see it's the current `main` branch content (no changes yet). Let me check what PR #10 actually changes.


### 🤖 Autopilot

There's no PR #10 on `dapp_beta` — the only open PRs are #6 and #11. Maybe you're thinking of a different repo or the PR number was from `dapp_prod`? Let me check `dapp_prod`:


### 🤖 Autopilot

There's no PR #10 anywhere. But I think I understand what you're getting at — you want the description in the **Contribution Summary** to be wrapped in a `<pre>` tag (monospace, preserved formatting) rather than just using `white-space: pre-wrap`. Let me update PR #11 on `dapp_beta` to use `<pre>` instead.

Actually, looking more carefully at the code — the issue is that `renderContributionSummary` uses `.textContent` for the description, which strips all HTML. To use `<pre>`, I'd need to either:

1. Change it to use `.innerHTML` with a `<pre>` wrapper (after HTML-escaping for safety), or
2. Add a `<pre>` element in the HTML and populate it with `.textContent`

Let me update the PR to use a `<pre>` approach.


### 🤖 Autopilot

I've opened **PR #12** on `dapp_beta` which uses a `<pre>` element (with `white-space: pre-wrap` and `font-family: inherit`) instead of a `<span>`. This will preserve your exact formatting — line breaks, indentation, bullet points, everything — while keeping the same visual style as the rest of the summary.

**PR URL:** https://github.com/TrueSightDAO/dapp_beta/pull/12

I'll close PR #11 since #12 supersedes it with the `<pre>` approach you wanted.

Would you like me to mark it ready for review or merge it?

