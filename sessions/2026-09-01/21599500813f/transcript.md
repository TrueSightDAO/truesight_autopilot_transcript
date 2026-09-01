# Autopilot Session — 2026-09-01

**Session**: `21599500813f`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=18800] help me check the status of the two pipeline the RSA signed event pipeline as well as the media archive pipeline


### 🤖 Autopilot

Found both. Let me read the two runbooks to understand what "status" means for each.


### 🤖 Autopilot

I've got the runbooks for both. Now let me check live status of each pipeline. Starting with a parallel sweep — Edgar API health, keypair presence on the box, the media manifests, and any running media jobs.


### 🤖 Autopilot

Both runbooks are in hand. Now checking live state — Edgar service health, the media daemon, cleide manifest, and any known issues.


### 🤖 Autopilot

SSH key to dao_protocol host isn't authorized from here — no problem, I'll check Edgar over HTTP instead. The daemon is running locally, so let me query it directly.


### 🤖 Autopilot

Edgar's endpoint is alive (405 on GET = expects POST; 404 on /health just means no such route). The daemon is running and actively uploading. Let me dig into queue state, sidecar health, photos, and Edgar's actual POST behavior.


### 🤖 Autopilot

Edgar endpoint is confirmed live. Now let me find the daemon's actual inbox path, its current state, and check photo uploads in farm-media-raw.


### 🤖 Autopilot

Both pipelines are coming into focus. Let me get the precise queue state, photo counts, the real daemon config, and run a local RSA self-test on the keypair.


### 🤖 Autopilot

Now I have a full picture. The queue CLI reported zero because it was pointed at the wrong default path — the daemon's real inbox is `/home/ubuntu/media_archive_inbox/`. Let me count the tree listing precisely to get definitive photo/video counts and verify YouTube live status of a sample.


### 🤖 Autopilot

All sidecars now have yt_ids — the queue looks drained. Let me confirm the daemon's current state, verify a sample of YouTube uploads are actually LIVE (not just captured IDs — the runbook warns about stale IDs), and count photos per farm in farm-media-raw.


### 🤖 Autopilot

Both pipelines checked end-to-end. Here's the status report:

## 1. RSA-Signed Event Pipeline (Edgar submit_contribution) — ✅ HEALTHY

| Check | Result |
|---|---|
| Edgar API `POST /dao/submit_contribution` | **200 OK** — returns `{"status":"ok","signature_verification":...}` (empty-body probe expectedly said `no_signature_format`; endpoint is live and accepting payloads) |
| Autopilot keypair in `.env` | `PUBLIC_KEY` / `PRIVATE_KEY` / `EMAIL` all present (`admin+sophia@truesight.me`) |
| RSA-2048 self-test | **Sign + verify roundtrip OK** with stored keypair (PKCS1v15 + SHA-256, exactly the format the runbook specifies) |

Nothing blocking submissions — the signing machinery and the endpoint are both live.

## 2. Media Archive Pipeline (MAP / farm-media) — ✅ RUNNING, QUEUE DRAINED

**Daemon:** `farm-media-daemon.service` **active (running)** on this box.

**Queue (sidecar coverage — all uploaded, zero pending/error):**

| Inbox | sidecars | yt_id | pending | error |
|---|---|---|---|---|
| cleide | 71 | 71 | 0 | 0 |
| paulo-la-do-sitio | 2 | 2 | 0 | 0 |
| jedielcio | 4 | 4 | 0 | 0 |
| santa-anna-fazenda | 8 | 8 | 0 | 0 |

Last upload batch: cleide `IMG_4924.MOV → vBPBZ6oUlfc` at **10:49 UTC** — daemon then went quiet because there's nothing left in the inboxes (expected idle, not stuck).

**YouTube LIVE verification (not just captured IDs):** sampled 5 cleide IDs (`NGQ9BP97_t4`, `sM9C5ipPKfA`, `vBPBZ6oUlfc`, `XxIwutVtbsw`, `qmONEO7gjkM`) → all **public + processed**, live on the channel. No stale/dead IDs.

**Photos in farm-media-raw:** 113 total — cleide 14, la-do-sitio 52, rancho-maranta 15, santa-anna-fazenda-para 32.

**Manifests committed:** all 4 farms in `FARM_MEDIA_MANIFESTS/` (index.json updated 2026-08-31 / cleide 2026-09-01), cleide manifest lists 71 MOV all with yt_id — matches sidecars.

## Small finding (tooling nit, not a pipeline fault)
The `farm_media_queue.py` CLI defaults to `/home/ubuntu/farm_media_inbox/{farm}` which doesn't exist — the daemon's real inbox is `/home/ubuntu/media_archive_inbox/farm-media/{farm}`. Querying via `--farm cleide` alone returns all-zeros and looks alarming; you must pass `--inbox <path>`. Worth a one-line fix so `--farm` uses the right default. Want me to open that PR (truesight_autopilot or farm-media-daemon)?

Also noting: real daemon config has `daily_budget: 500` (ceiling test per its own comment) — that's a deliberate config, but worth remembering the YouTube unverified-project hidden cap can still bind.

Bottom line: **both pipelines are healthy; nothing needs intervention.**

———
**✅ Done this turn — actions taken:**
• `ssh run` ×11 → echo "=== .env keypair presence ==="; grep -oE '^(PUBLIC_KEY|PRIVATE_KEY|EMAIL)=' /opt/truesight_autopilot/.env | sed 's/=$/= <set>/'; echo;; echo "=== edgar / dao_protocol service ==="; systemctl is-active dao_protocol 2>/dev/null; systemctl status dao_protocol --no-pager -n 5 2>/; echo "=== cleide_work contents ==="; find /home/ubuntu/cleide_work -maxdepth 2 -type d | head -20; echo; echo "=== cleide counts ==="; find ; …(+8 more)

