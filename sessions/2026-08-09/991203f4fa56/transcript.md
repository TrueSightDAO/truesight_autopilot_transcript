# Autopilot Session — 2026-08-09

**Session**: `991203f4fa56`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=10635] [Handoff context — this Telegram topic (thread 10635) may be an execution handoff. If the governor gives a go-signal ("go for it", "go", "proceed") or references a plan/mission, find this thread in agentic_ai_context/handoffs/HANDOFF_MANIFEST.md via read_context_file, open the referenced `*_PLAN.md`, and resume from its RESUME HERE. Do NOT reply that you lack context without checking the registry first.]

Hey, currently I'm thinking that in China we have a problem right because telegram is kind of blocked So block of the users over here in China and right users, especially the I know I'm talking about the internal team So the way that we operate at least like you and me in the face is via telegram Channel and like we've been each the channel. There's like individual topics. I wonder if we could have like say Android app Define and then in the Android app itself Having individual team and within the team itself, right different topics like what we have right now for telegram Can you spend some time do some proper research and come up with a full-fledged implementation plan execution roadmap and roadmap checklist? Yeah, do it as an MD file and once you're done come back to me [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me check for any existing DAO context on a China team, and dig deeper into white-labeling options for the top candidates.


### 🤖 Autopilot

I have the DAO context now (China operation: Dongguan, GACC, Aora events, Jerri/Ling). Let me verify a few Zulip-specific details before writing the plan.


### 🤖 Autopilot

I've got solid research. Let me grab the mission doc for a proper tie-in, then write the plan.


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

