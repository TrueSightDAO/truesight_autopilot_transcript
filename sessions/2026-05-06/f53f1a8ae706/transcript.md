# Autopilot Session — 2026-05-06

**Session**: `f53f1a8ae706`


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Read dapp/chat.html and review the current code for the governor chat approval UX. Check specifically: 1) Does restoreSession() re-render interactive proposal cards from ```json blocks in restored messages? 2) Does addPendingProposal() persist all proposals or only those with qr_code? 3) Is there an always-visible pending badge? If any of these are missing, identify exactly what needs to change.


### 🤖 Autopilot

Let me read the chat.html file to review the code.


### 🤖 Autopilot

Now let me analyze the three questions systematically.

---

## Review Results

### 1) Does `restoreSession()` re-render interactive proposal cards from ```json blocks in restored messages?

**YES — partially.** Here's the relevant code (lines ~750-760):

```js
async function restoreSession() {
    ...
    data.messages.forEach(function(msg) {
        var isUser = msg.role === 'user';
        var msgDiv = appendMessage(isUser ? 'You' : 'DAO Assistant', msg.content, isUser);
        if (!isUser) {
            var proposals = parseProposalsFromText(msg.content);
            proposals.forEach(function(p) { renderProposal(p); });
            reAddImageAttachments(msgDiv, msg.content);
        }
    });
}
```

It calls `parseProposalsFromText()` which uses this regex:

```js
var m = text.match(/```json\s*(\[[\s\S]*?\]|\{[\s\S]*?\})\s*```/);
```

**Issue found**: The regex uses `[\s\S]*?` (lazy) which will match the **first** occurrence only. If a message contains multiple separate ```json blocks, only the first one is captured. Also, the regex only captures a single array `[...]` or object `{...}`, not multiple blocks. This means **batch proposals** (arrays of objects) work, but if the assistant sends two separate proposal blocks in one message, only the first is parsed.

**Verdict**: Works for single-block cases. Could miss multi-block proposals.

---

### 2) Does `addPendingProposal()` persist all proposals or only those with `qr_code`?

**It persists ALL proposals**, but `removePendingProposal()` only resolves by `qr_code`:

```js
async function addPendingProposal(p) {
    await fetch(API_BASE_URL + '/pending/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-Public-Key': publicKey },
        body: JSON.stringify(p)
    });
}

async function removePendingProposal(p) {
    var qr = p.qr_code || '';
    if (qr) {
        await fetch(API_BASE_URL + '/pending/resolve', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-Public-Key': publicKey },
            body: JSON.stringify({ qr_code: qr, action: 'approved' })
        });
    }
    updatePendingUIFromServer();
}
```

**Bug**: If a proposal has no `qr_code` field (e.g. a generic `submit_contribution` or a `create_dao_submission` proposal), `removePendingProposal` does nothing — the `if (qr)` guard skips the server call entirely. The proposal stays in the server's pending list forever, and the UI badge never decrements for non-QR proposals.

**Verdict**: `addPendingProposal` persists everything. `removePendingProposal` only resolves QR-code proposals. Non-QR proposals get **orphaned** on the server.

---

### 3) Is there an always-visible pending badge?

**YES — two of them, but with caveats:**

1. **`#pending-badge`** — inside the hamburger menu toggle button (`.session-toggle`). Only visible when the toggle is visible. On mobile it's fine; on desktop it's in the top-left corner.

2. **`#pending-inline-badge`** — a separate floating badge at `top:0.5rem; left:4.5rem`. It's always positioned in the viewport.

Both are controlled by `renderPendingList()` which sets `display: none` when the list is empty, and `display: inline`/`display: block` when non-empty.

**Verdict**: Yes, always-visible pending badges exist. The inline badge is a good design — always in viewport, clickable to scroll to the pending section.

---

## Summary of Issues Found

| # | Issue | Severity | Fix Needed |
|---|-------|----------|------------|
| 1 | `parseProposalsFromText` regex only captures the **first** ```json block in a message | Medium | Use `/g` flag or loop to capture all matches |
| 2 | `removePendingProposal` only resolves proposals with `qr_code` — non-QR proposals get **orphaned** on the server | **High** | Add a fallback key (e.g. `title` or a generated `id`) for non-QR proposals |
| 3 | Pending badges exist and work, but the inline badge position (`left:4.5rem`) could overlap with the session toggle on very narrow screens | Low | Minor CSS tweak |

**The most impactful fix is #2** — non-QR proposals (like `create_dao_submission` or generic `submit_contribution`) can never be resolved from the pending list, meaning the badge count will be permanently wrong for those sessions.

Would you like me to open a PR to fix these issues?

