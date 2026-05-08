# Autopilot Session — 2026-05-08

**Session**: `3c19bac39481`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Your Grok vision fallback in scan_qr_from_file is producing weak results (e.g., finding "2024SA" instead of the full "2024SA_20251227_39"). A human uploaded the same images to Grok directly and got ALL 20 full codes correctly.

The bugs:
1. scan_qr_from_file passes a short inline prompt ("Read any visible QR codes...") instead of your full _QR_NAMING_CONTEXT system prompt from grok_client.py. The short prompt produces worse results.
2. You're using grok-4-1-fast-non-reasoning (a fast model). The human got good results with the standard Grok model.

Fix: Read app/grok_client.py and app/tools/qr_scanner.py. Modify the Grok fallback block in scan_qr_from_file to:
- Use the full grok_analyze_images function WITHOUT passing a custom prompt (so it uses the _QR_NAMING_CONTEXT default)
- OR use a richer prompt that asks specifically to read the bottom sticker area where batch codes like 2024SA_20251227_39 appear

Open a DRAFT PR with the fix.


### 🤖 Autopilot

Let me start by reading the relevant source files to understand the current implementation.


### 🤖 Autopilot

Now I have a clear picture of both bugs. Let me open a DRAFT PR with the fix.

**Bug 1**: The Grok fallback in `scan_qr_from_file` (line ~118-139 of `qr_scanner.py`) passes a short inline `user_context` prompt instead of letting `grok_analyze_images` use its default `_QR_NAMING_CONTEXT` system prompt. The short prompt lacks the detailed context about Agroverse QR code formats, label positioning, and confidence reporting.

**Bug 2**: It uses `GROK_MODEL` which is `"grok-4-1-fast-non-reasoning"` — a fast model. The fix should use the standard model for better accuracy.

**Fix**: Pass `user_context=""` (or omit it) so the system prompt `_QR_NAMING_CONTEXT` is the primary instruction, and use a richer model.


### 🤖 Autopilot

Here's the DRAFT PR: **https://github.com/TrueSightDAO/truesight_autopilot/pull/23**

### What it fixes

**Bug 1 — Weak prompt**: The Grok fallback in `scan_qr_from_file` passes a short inline `user_context` like *"Read any visible QR codes..."* instead of relying on the full `_QR_NAMING_CONTEXT` system prompt. The system prompt has detailed instructions about Agroverse QR code formats, bottom sticker areas, and confidence reporting — but the short user prompt dilutes it.

**Bug 2 — Fast model**: Uses `grok-4-1-fast-non-reasoning` which produces weaker results. The human got all 20 codes correctly using the standard Grok model.

### The fix

1. **Richer prompt**: Changed the Grok fallback to pass a detailed prompt that specifically asks to read the **bottom sticker area** where batch codes like `2024SA_20251227_39` appear, and reinforces the exact Agroverse QR code format patterns.
2. **Better model**: Switched to `"grok-4-1"` (standard) for the vision fallback, keeping the fast model only for the primary pipeline.

Want me to merge it, or would you like to review the diff first?

