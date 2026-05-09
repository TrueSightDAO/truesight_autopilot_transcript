# Autopilot Session — 2026-05-09

**Session**: `e742542d4ca5`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

Which model are out running on now?


### 🤖 Autopilot

Based on the workspace context, the main AI model currently running is **DeepSeek-V3** as part of the **truesight_autopilot** service.

Here's what's active:

## **truesight_autopilot** (Primary AI Service)
- **Model**: DeepSeek-V3
- **Purpose**: Unified AI service for TrueSight DAO - handles governor chat + autonomous SRE + developer tasks
- **Deployment**: Running on dedicated EC2 instance (`i-02c699d3d7efbdc82` in `us-east-1d`)
- **Capabilities**: 
  - Governor chat via DApp interface
  - Autonomous diagnostics and fix PR creation
  - Background monitoring (Gmail, AWS, GitHub Actions)
  - Tool calls for reading context/repos and opening PRs

## Other AI Models in Use (Supporting Services)
- **Grok**: Used by `market_research` for photo review and contact enrichment
- **Qwen**: Available via `jarvis` local LLM service
- **Whisper/YOLO**: Used by `video_editor` for video processing

The **DeepSeek-V3** in `truesight_autopilot` is the primary model you're interacting with now - it's about 30× cheaper than Claude/Kimi alternatives and was chosen as the main workhorse after dropping Kimi and Claude.


### 🧑 Governor

Don’t you have access to big model?


### 🧑 Governor

Don’t you have access to big model?


### 🤖 Autopilot

Based on the context and my available tools, I have access to **DeepSeek-V3** as my primary model through the `truesight_autopilot` service.

The system documentation shows that:

- **DeepSeek-V3** is the main model I'm running on
- It was chosen because it's about 30× cheaper than Claude/Kimi alternatives
- The team dropped Kimi and Claude in favor of DeepSeek-V3

I don't have access to other "big models" like GPT-4, Claude 3 Opus, or similar large language models through my available tools. My capabilities are focused on:

- Reading and analyzing the DAO's codebase and documentation
- Opening fix PRs for issues
- Managing QR codes and inventory
- Submitting contributions to Edgar
- Autonomous monitoring and diagnostics

If you need access to more powerful models for specific tasks, you would need to use other services in the ecosystem like:
- **Grok** (for photo review and contact enrichment via market_research)
- **Qwen** (via the jarvis local LLM service)

But for my core autopilot functions, DeepSeek-V3 is the model I'm operating on.

