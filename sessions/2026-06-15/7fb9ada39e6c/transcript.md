# Autopilot Session — 2026-06-15

**Session**: `7fb9ada39e6c`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=5100] I noticed alot of the previous blog entries are not listed 

https://truesight.me/blog/index.html


### 🤖 Autopilot

Let me check the blog page to see what's there and what might be missing.


### 🤖 Autopilot

Let me also check what blog post files actually exist in the repo.


### 🤖 Autopilot

Let me see the full index.html to compare what's listed vs what's in the posts directory.


### 🤖 Autopilot

Let me get the full content to see all blog cards listed.


### 🤖 Autopilot

Let me get the rest to see all blog cards.


### 🤖 Autopilot

Let me check what blog post files actually exist in the repo to compare.


### 🤖 Autopilot

Now I can see the full picture. Let me compare what's in the `blog/posts/` directory vs what's listed on the `index.html` page.

**Blog posts directory** has **46 files** (including some duplicates with slightly different filenames).

**Blog index page** currently lists only these posts (from what I can see in the HTML):

1. Agentic AI and the Common Law Tradition (Jun 13, 2026)
2. The Joy Was the Point (Jun 13, 2026)
3. The Darwinian Agent (Jun 10, 2026)
4. The scripture is not the point (Jun 7, 2026)
5. Should an AI Agent Get Voting Rights? (Jun 4, 2026)
6. Signal Brief 01 — Experience Economy (May 30, 2026)
7. Where 道 Integrates with DAO (May 28, 2026)
8. The shared memory is the moat (May 25, 2026)
9. The far end is the human end (May 22, 2026)
10. The system that broke is the system that proposes the fix (May 19, 2026)
11. Three times is when you name it (May 16, 2026)
12. What the angels couldn't name (May 13, 2026)
13. The chain holds (May 10, 2026)
14. The checklist that lets you do nothing (May 7, 2026)
15. The most tracked thing in the room is a cup of cacao (May 4, 2026)
16. We let an AI run our DAO (May 1, 2026)

That's **16 posts** on the index page vs **46 files** in the posts directory. The missing ~30 posts are older ones that were published before the recent redesign.

You're right — a lot of the earlier blog entries aren't listed on the index page anymore. The older posts include things like:

- Agroverse Guild partners with CEPOTX and CooperCabruca
- Cooperative profit sharing
- DAO evolution post-LLM research findings
- DApp digital signature / email onboarding protocol
- Digital infrastructure AWS incident
- Discovered protocols
- Expanding regenerative cacao network
- From integrity to trustlessness
- From Singapore catalogs to Brazil containers
- Voting influence / governance policies
- Oracle feedback loop
- Plug-and-play architecture
- Regeneration after winter downturns
- Rest / Play / Do Nothing Society
- TDG tokens paired with SOL on Raydium
- The Do Nothing Society (original)
- The Mycelial Economy
- Troubleshooting governance tokens in Phantom
- Truesight DAO at Davos 2025
- Operational framework / supply chain cadence
- Security breach incident report
- Understanding AUM
- Daily buy-back budget
- Warehousing mystery inventory
- Why TrueSight keeps WhatsApp in the loop

Looks like the blog index was rebuilt at some point (probably when the site was redesigned) and only the most recent 16 posts were included. The older posts still exist at their URLs — they just aren't linked from the index.

Want me to add them back to the index page? I could add a "Previous Posts" section below the current grid, or integrate them chronologically.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=5100] Yeah, please add them back in and then promote production. [System note: the user sent this as a VOICE message via the Telegram bot. Your text reply is automatically synthesized into a voice note and sent back, so answer naturally for speech and keep it concise. The user is on Telegram, NOT the DApp web chat -- do not claim otherwise. URLs are delivered separately as text, so do not read URLs aloud.]


### 🤖 Autopilot

Let me first get the full list of all blog posts and their dates so I can build a complete chronological index.


### 🤖 Autopilot

I have the dates from the existing posts. Now let me extract dates from the older posts that are missing from the index. Let me check a batch of them.


### 🤖 Autopilot

Good — I now have the dates for the 16 posts already on the index. Now I need to extract dates from the older posts. Let me batch-read the remaining ones to get their published dates.


### 🤖 Autopilot

I now have enough data to build the complete index. Let me also grab the remaining posts' dates quickly.


### 🤖 Autopilot

I now have all the dates I need. Let me also grab the remaining few posts' dates.


### 🤖 Autopilot

Now I have all the data. Let me build the complete index.html with all posts chronologically. I'll work on the truesight_me_beta repo first (beta-first flow), then promote to prod.


### 🤖 Autopilot

Good — the beta repo has the same content. Now let me build the complete index with all 46 posts in chronological order. I'll create the full HTML and push it to the beta repo.


### 🤖 Autopilot

I have all the data I need. Now let me build the complete blog index with all posts. I'll push to the beta repo first.


### 🤖 Autopilot

The PR is up on the beta repo. Let me check it's ready and then promote to prod since you said to go ahead.

The PR is at https://github.com/TrueSightDAO/truesight_me_beta/pull/238 — it adds all 46 blog posts to the index, sorted newest-first. The older posts from 2024-2025 that were missing are now included.

Since you said "add them back in and then promote production" — I'll go ahead and sync beta to prod now.


### 🤖 Autopilot

There's a merge conflict when syncing beta to prod — the histories have diverged, which is expected since prod and beta have different CNAME configurations. This needs a human to reconcile.

Here's what happened:

1. **PR opened on beta**: https://github.com/TrueSightDAO/truesight_me_beta/pull/238 — adds all 46 blog posts to the index
2. **Prod sync blocked**: The beta→prod sync hit a merge conflict (expected — prod and beta intentionally have different CNAMEs)

**What I need from you**: Can you merge the beta PR (#238) and then I'll try the prod sync again? Or if you'd prefer, I can apply the same change directly to prod's `main` branch since it's a single file change.

