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

