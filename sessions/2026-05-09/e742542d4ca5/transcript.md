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

