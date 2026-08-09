# Autopilot Session — 2026-08-09

**Session**: `991203f4fa56`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=10635] [Handoff context — this Telegram topic (thread 10635) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/handoffs/HANDOFF_MANIFEST.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

Hey, currently I'm thinking that in China we have a problem right because telegram is kind of blocked So block of the users over here in China and right users, especially the I know I'm talking about the internal team So the way that we operate at least like you and me in the face is via telegram Channel and like we've been each the channel. There's like individual topics. I wonder if we could have like say Android app Define and then in the Android app itself Having individual team and within the team itself, right different topics like what we have right now for telegram Can you spend some time do some proper research and come up with a full-fledged implementation plan execution roadmap and roadmap checklist? Yeah, do it as an MD file and once you're done come back to me [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

[3 tool result(s) compacted: read_context_file, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

[3 tool result(s) compacted: web_search, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

[4 tool result(s) compacted: web_search, web_search, aws_query, aws_query — detail in artifacts]


### 🤖 Autopilot

Let me check for any existing DAO context on a China team, and dig deeper into white-labeling options for the top candidates.
[4 tool result(s) compacted: search_context, search_context, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

[3 tool result(s) compacted: read_tool_result, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

[2 tool result(s) compacted: read_repo_file, search_context — detail in artifacts]


### 🤖 Autopilot

I have the DAO context now (China operation: Dongguan, GACC, Aora events, Jerri/Ling). Let me verify a few Zulip-specific details before writing the plan.
[3 tool result(s) compacted: web_search, web_search, web_search — detail in artifacts]


### 🤖 Autopilot

I've got solid research. Let me grab the mission doc for a proper tie-in, then write the plan.
[1 tool result(s) compacted: read_context_file — detail in artifacts]


### 🤖 Autopilot

I have everything I need — DAO China context (Dongguan, Jerri/Ling, Aora events, GACC), the research, and the mission north star. Writing the full plan now.


### 🤖 Autopilot

The call formatting failed — retrying with the parameters passed directly.


### 🤖 Autopilot

Done, Gary. The full plan is written and up as **PR #742** in agentic_ai_context — `CHINA_TEAM_COMMS_PLATFORM_PLAN.md` (link delivered separately as text).

Quick summary of what's in it:

**The recommendation — self-hosted Zulip with a white-labeled Android app.** Zulip is the only mainstream open-source self-hosted platform where *topics* are the core unit — its "streams + topics" maps 1:1 to your Telegram channel + topic forums. Teams become streams (or separate realms), topics stay topics. Free, Apache license, we own the data.

**Research covered three paths:**
- Chinese SaaS (Feishu/Lark, DingTalk, WeCom) — zero build, but someone else's platform; kept as fallback
- Self-hosted open source (Zulip vs Rocket.Chat vs Mattermost) — Zulip wins on the topics model
- Building from scratch — rejected

**Infra:** AWS Hong Kong (ap-east-1) — no ICP filing needed, 20–40ms latency to mainland, ~$30–60/month. Mainland hosting would need a Chinese entity + ICP — too heavy for an internal tool.

**The hard part — push notifications.** FCM is blocked in China. Plan ships MVP with WebSocket + polling + email fallback, then escalates to UnifiedPush or vendor SDKs (Huawei/Xiaomi) only if the pilot says it's needed. APK distribution is direct download + QR code, with a Chinese-language install guide for the different phone ROMs.

**Roadmap:** 6 phases with checkboxes — Phase 0 decisions (your sign-off), infra, server deploy, pilot with Jerri/Ling, Android app build, then migration & rollout. MVP ~2 weeks, full rollout ~6–8 weeks.

There's an "Open Questions" section for you — biggest ones: self-host vs Feishu, single shared workspace vs separate China realm, and whether OS-level push is a launch must-have.

Want me to walk through any section in more detail, or shall we start Phase 0 decisions?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=10635] Also, regarding this Android interface where we expose it for our internal teams, we need to be able to assign that. Some team members only have read view, others have editing and read view. So I think I came up with the specifications before, but for the telegram experience. So dig into that and give some thoughts to it. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me dig for your earlier Telegram permissions specs before I give thoughts.


### 🤖 Autopilot

Let me search a few more angles for that Telegram spec you mentioned.


### 🤖 Autopilot

That plan is about the autopilot Telegram interface — not the team-permission spec. Let me search more precisely for your earlier Telegram permissions spec.


### 🤖 Autopilot

I dug into it — and I have to be straight with you: **I couldn't find a written permissions spec anywhere.** I searched the whole context repo (every file, terms like "read only", "permissions", "viewer", "restricted", "spectator"), past session transcripts for the last 90 days, and the org's code — nothing matches a Telegram team-permissions spec. The only permission docs that exist are the DAO's DApp governor-permission flow, which is unrelated. So either it lives somewhere I can't see, or it was a verbal spec. If you re-share it or point me to it, I'll match it exactly.

That said, the requirement itself — some team members read-only, others read + edit — is very doable, so here are my thoughts on how it maps onto the Zulip platform from the plan:

**1. The permission model maps cleanly onto Zulip roles:**
- **Owner** — you + Sophia (full control)
- **Admin** — team leads (manage members, streams, settings)
- **Editor** — can post + edit/delete their own messages (Zulip's "member" role)
- **Viewer** — read-only

**2. Read-only is enforced at the stream (team) level, not the topic level.** This is the key design point: Zulip lets you set who can *post* in a stream — options like "admins only" or "only a specific group can post." So a read-only team member = someone subscribed to the team's stream, with the stream's posting policy locked to editors/admins only. They see everything, can react maybe, but can't post.

**3. Topic-level restrictions don't exist natively** — permissions in Zulip live on the stream, not per-topic. So if you need *some topics read-only and others editable inside the same team*, the clean pattern is to split sensitive topics into their own stream with tighter posting policy. I'd recommend we design streams as "permission boundaries": e.g. `China Ops — view` vs `China Ops — edit`.

**4. Zulip also has a "guest" role** — users limited to only the streams they're invited into, which is perfect for external people (e.g. partners, contractors) who should see only specific teams and nothing else.

**5. One nuance on "editing":** in a chat app, editing usually means editing/deleting your own messages within a window, plus admins editing anything. If you actually meant document-style editing — like someone can edit a shared spec or plan — that's a different capability (Zulip has docs for that too, but weaker than Google Docs). Worth telling me which you mean.

**6. Telegram comparison:** Telegram can only do this crudely — mute a user, or make a channel admins-only-post. Zulip's model is strictly better: real roles, per-stream posting policy, guest scoping, and an audit log of admin actions.

Want me to fold this into the plan doc as a proper permissions section — I can update the PR — and also, can you point me to that earlier spec if it exists?


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=10635] Are you calling me that Zoolib actually works in China if I've been blocked? [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Great question — let me be precise, because I don't want you thinking it's magic.

The difference isn't Zulip vs Telegram. It's *self-hosted vs blocked-by-name*.

Telegram is blocked because the GFW has Telegram's servers, IP ranges, and protocol signature on its blocklist — it detects MTProto traffic and kills it, no matter which phone or app you use. There's a specific "thing" to block.

Zulip is just software. There's no "Zulip server" out there to block — we run it ourselves, on our own server in Hong Kong, behind our own domain. To the firewall, traffic to it looks like ordinary, boring HTTPS to a normal business website — the same as visiting any company's site. The GFW has no list entry for our little server, and no reason to flag an internal team chat.

That's genuinely how a lot of companies operate in China — self-hosted GitLab, Jira, Slack alternatives, all on ordinary HTTPS, all working fine.

But — honesty here — I can't guarantee 100% from a desk in the US that it'll be smooth from every ISP in Dongguan. Cross-border HTTPS can occasionally get throttled, and nothing is ever truly guaranteed with the GFW. That's exactly why the plan bakes in a smoke test early: in Phase 2, before we build the app, we have Jerri and Ling test the server from their phones in Dongguan for a few days. If it's solid, we build on it. If it's flaky, we fall back to Feishu/Lark, which is the zero-risk Chinese option.

One more thing that helps: the Android app we'd fork talks only to our own server — no Google or Firebase calls in the path — so there are no blocked dependencies hiding inside the app either.

So short answer: no, I'm not claiming Zulip has some China pass. I'm claiming *our own server on our own domain* is a fundamentally different situation from Telegram — and we'll verify it from the ground in Dongguan before committing.

