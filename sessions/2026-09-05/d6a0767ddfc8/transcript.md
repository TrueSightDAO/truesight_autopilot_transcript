# Autopilot Session — 2026-09-05

**Session**: `d6a0767ddfc8`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=21005] https://github.com/TrueSightDAO/agentic_ai_context/blob/main/AGROVERSE_SUNMINT_FARM_LISTING.md


### 🤖 Autopilot

Read and understood — `AGROVERSE_SUNMINT_FARM_LISTING.md` is the consolidated end-to-end SOP for onboarding new partner farms (raw media → live Agroverse profile + SunMint plot + FSVP records), built from the Sítio Raimundo & Geniza (RG-P1) post-mortem.

Key points I'm holding in context:

- **Step 0 identity/attribution gate** — check registry overlap in `sunmint/plots/index.geojson` + SunMint Plots tab *before* any registration; never attribute ownership or invent names without your confirmation.
- **GPS intake** — only Document/Drive/scp uploads carry GPS (Telegram photo recompression strips it); MOV GPS under `Keys:GPSCoordinates`; S/W negative; sha256-dedupe first.
- **Plot registration** — convex hull → SunMint Plots row → geojson/farms index push (sunmint is api-only, Contents API) → on-chain geo event.
- **Media archive** — daemon inbox needs `.mp4` **+ sidecar** together; new farm = config yaml append + daemon restart.
- **Farm page** — clone `rancho-maranta-para` template, mandatory post-clone token grep (names/CEPOTX/header jpgs), canonical slug without double region suffix, UTF-8 literal media.json.
- **Impact map** — data-driven off `index.geojson`, popup link works when `farm_id == page slug`; prod-link only live after prod sync.
- **FSVP** — entity profile + site codes recorded as reported, never decoded/derived from guesses.
- **Deploy gate** — beta verify → `sync_beta_to_prod` only on your explicit go.

What would you like to do with this — a new farm onboarding run, a status check against a current listing, or something else? If it's a new farm, send the media batch and I'll start at Step 0 (identity + registry-overlap gate).

