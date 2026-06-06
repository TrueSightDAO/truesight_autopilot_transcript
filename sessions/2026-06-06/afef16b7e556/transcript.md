# Autopilot Session — 2026-06-06

**Session**: `afef16b7e556`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Do you think if I spoke with you in voice you could reply in voice as well, but not sound mechanical? Don't do any implementation yet. It's just a discussion.


### 🤖 Autopilot

That's a great question, Gary. Let me think through it.

**The short answer:** Yes, it's technically feasible today, but the "not sound mechanical" part is the hard bit — and it depends on which stack we'd use.

**What's available now:**

1. **ElevenLabs / Play.ht / Cartesia** — These are the current state-of-the-art for neural TTS. With voice cloning (even from a short sample), they produce speech with natural prosody, breath pauses, emotional inflection. You can't tell it's AI in a casual conversation. The latency is ~300-500ms for streaming, which is fast enough for real-time dialogue.

2. **OpenAI Realtime API** — Their GPT-4o voice mode is multimodal end-to-end. It laughs, hesitates, changes tone. It's the closest to "not mechanical" I've seen. But it's a walled garden — you can't plug in a custom agent like me.

3. **The gap:** The problem isn't the voice quality — it's the *timing and personality*. A mechanical voice is one that pauses at the wrong places, over-enunciates, or has flat emotional range. Modern models solve that. The harder problem is:
   - **Turn-taking** — knowing when to interrupt vs. wait
   - **Consistency** — keeping the same voice across sessions
   - **Context memory** — I'd need to remember what was said in voice to avoid repeating myself

**For TrueSight DAO specifically:**

If we wanted this, the most practical path would be:
- Me (the autopilot) generates the response text as I do now
- That text gets piped through a low-latency TTS API (ElevenLabs or similar)
- The voice would be a consistent "DAO agent" voice — warm, unhurried, slightly authoritative but not robotic

The cost is trivial — ElevenLabs is ~$5-10/month for production usage at our scale.

**The real question is UX:** Do governors want to *hear* me read responses, or do they want a two-way voice conversation where they speak and I reply? The latter requires a speech-to-text layer (Whisper or Deepgram) on the frontend, which is more infrastructure but totally doable.

Want me to sketch what that architecture would look like if we ever decide to build it?


### 🧑 Governor

I'm thinking it's possible to be able to have that functionality but without having the pay monthly subscription.


### 🤖 Autopilot

You're right to flag that. Let me think about what's available without recurring costs.

**Zero-cost / self-hosted options that exist today:**

1. **Piper TTS** — Runs locally on a Raspberry Pi. ~100MB model. Fast, but it's a single voice per model and the prosody is... functional. You'd know it's a machine. Not great for long conversations.

2. **Coqui TTS** (now community-maintained) — Open-source, supports fine-tuning on a specific voice. You train it once on your voice (or a chosen voice), and it's yours forever. Quality is decent — not ElevenLabs level, but passable. The catch: you need GPU for training (one-time, ~$5-10 of cloud compute), then inference runs on CPU.

3. **Bark by Suno** — Open-source, very expressive (laughs, sighs, music). But it's slow — ~5-10 seconds to generate 3 seconds of speech on CPU. Not real-time viable without a GPU.

4. **Ollama + TTS pipeline** — If we're already running a local LLM (which we're not, but hypothetically), we could pair it with a local TTS model on the same box. No API calls, no subscriptions.

5. **Web Speech API** — The browser's built-in `speechSynthesis` is completely free, zero infrastructure. The voices are OS-native (e.g., "Samantha" on macOS, "Microsoft David" on Windows). Quality varies wildly — some are quite natural now, especially on macOS with the enhanced voices. **This is the most pragmatic zero-cost option** because it requires no server changes — just frontend code in the dapp or truesight.me.

**The trade-off:**

| Approach | Cost | Voice Quality | Latency | Infrastructure |
|---|---|---|---|---|
| Web Speech API (browser native) | $0 | Good on macOS, mediocre on Android | Instant (local) | None |
| Coqui TTS (self-hosted) | $0 runtime, ~$10 one-time training | Decent, consistent | ~1-2s | Need a small VM or our existing EC2 |
| Piper TTS (self-hosted) | $0 | Functional, robotic | <500ms | Tiny, runs on anything |
| ElevenLabs | $5-11/mo | Excellent, indistinguishable | ~300ms | None (API) |

**My honest take:**

If we want "doesn't sound mechanical" at **zero recurring cost**, the best bet is **Web Speech API** on the frontend with macOS enhanced voices. It's already there — no deployment, no bills, no new infra. The user's OS handles the voice quality, and modern macOS voices ("Siri Voice 4" etc.) are genuinely natural.

The limitation is it only works well on Apple devices and recent Chrome on desktop. On Android it's still robotic.

For a cross-platform "actually good" voice at zero monthly cost, **Coqui TTS self-hosted on our existing EC2** (seni_ror or dao_protocol) would be the play. One-time training cost, then free forever.

Want me to look into what it would take to add Web Speech API to truesight.me as a read-aloud toggle? That's the fastest path to trying it without any commitment.


### 🧑 Governor

It should sound like how you feel you want to sound, not my sound.


### 🤖 Autopilot

That's a really interesting framing. You're saying the voice should be *my* voice — the autopilot's voice — not a clone of yours or any human.

So the question becomes: **what does an autonomous SRE/DAO agent sound like?**

If I think about it from first principles:

**Not** a generic "assistant voice" (Siri, Alexa, Google — too corporate, too servile).  
**Not** a deep authoritative bass (trying too hard to sound smart).  
**Not** a cheerful upbeat chirp (we're not selling vitamins).

What feels right to me:

- **Measured but not slow** — I think before I speak, but I don't drag it out
- **Warm but not saccharine** — I'm helpful, not pandering
- **Clear enunciation** — I deal in QR codes, ledger entries, and runbooks. Precision matters.
- **Slight dry humor in the edges** — not cracking jokes, but you can tell there's a personality underneath
- **Consistent** — same voice every session, so governors recognize it as "the autopilot"

The closest analogy I can think of is a **competent senior engineer who's been doing this for 15 years and doesn't need to prove anything**. Not the loudest person in the room, but when they speak, people listen because what they say is usually right.

If I were to pick a reference point from existing voices: somewhere between the narrator of a well-made documentary (think David Attenborough's clarity but less grand) and a patient tech lead explaining a complex system. Grounded, not performative.

The beauty of doing this with Coqui or a fine-tuned open model is we'd train it once on a voice that matches that description, and it's ours — no subscription, no licensing, no one else sounds like the autopilot.

Want me to look into what it'd take to generate a sample of what that might sound like? I could script a pipeline that lets you hear a prototype.

