# Autopilot Session — 2026-07-26

**Session**: `ee5f466f5379`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=9634] Does gitee support feature like github pages


### 🤖 Autopilot

**Yes.** Gitee (gitee.com) has a feature called **Gitee Pages** that's their equivalent of GitHub Pages — a free static site hosting service directly from a repository.

## Comparison: Gitee Pages vs GitHub Pages

| Feature | Gitee Pages | GitHub Pages |
|---|---|---|
| **Free tier** | ✅ Yes (public repos) | ✅ Yes (public repos free; private on paid plans) |
| **Static site generators** | Jekyll, Hugo, Hexo | Jekyll, Hugo, Hexo (via Actions) |
| **Custom domain** | ✅ Yes | ✅ Yes |
| **Custom domain HTTPS** | 🔒 Gitee Pages Pro (paid) only | ✅ Free (auto via Let's Encrypt) |
| **Auto-deploy** | 🔒 Pro only | ✅ Free (on push to branch) |
| **CI/CD build** | Manual button click (free) / auto (Pro) | GitHub Actions |
| **Region advantage** | Fast in China, no ICP filing needed | Fast globally, but can be slow from China |
| **Storage / bandwidth** | 1GB / 100GB (Pro) | 1GB / 100GB (free) |

## How it works
1. Create a repo on gitee.com
2. Push your static files (HTML/CSS/JS or a Jekyll/Hugo/Hexo project)
3. Go to **Services → Gitee Pages** in the repo settings
4. Select the branch and deploy — your site is live at `username.gitee.io/repo-name`

**Catch:** On the free tier you manually hit "Deploy" to update — there's no auto-deploy-on-push unless you pay for Gitee Pages Pro. Also, no built-in free HTTPS for custom domains (Pro only).

**Verdict:** It's a solid option if your audience is primarily in China and you want fast local access without domain filing. If you need automatic deploys and free HTTPS on custom domains, GitHub Pages or other alternatives (Netlify, Cloudflare Pages) are better.


### 🧑 Governor

[Telegram context: chat_id=-1003919341801, thread_id=9634] Is GitHub accessible behind the Chinese firewall


### 🤖 Autopilot

**Not reliably.** GitHub has an inconsistent relationship with the Great Firewall of China (GFW):

## Current status (2025–2026)

| Service | Accessibility in China |
|---|---|
| **github.com (core)** | Generally accessible, but with **intermittent slowdowns and outages** |
| **Git clone/push (SSH/HTTPS)** | Mostly works, but can be slow or drop intermittently |
| **GitHub Pages** | Often **very slow or times out** — some ISPs throttle it |
| **raw.githubusercontent.com** | Frequently **blocked** by many Chinese ISPs |
| **Large binary downloads / releases** | Often throttled or fail |
| **Port 443** | Saw an **unconditional block event** on Aug 20, 2025 (1.5 hr outage) |
| **April 2025** | A config change by GitHub itself blocked Chinese connections for ~15 hours (mitigated) |

## The practical picture

- **No full blanket block**, but also **no reliable guarantee** — the GFW applies selective throttling and occasional RST injection.
- Many developers in China use **workarounds**: VPNs, or mirrors like `gitclone.com`, or Gitee which mirrors popular GitHub repos.
- For a **project relying on GitHub** (like TrueSight DAO's repos, CI/CD, or GitHub Pages hosting), users inside China would likely need:
  - A VPN/proxy for reliable access
  - Or a **mirror on Gitee** as a fallback
  - For static site hosting specifically, **Gitee Pages** would be more reliable for Chinese users than GitHub Pages

**Bottom line:** GitHub can be reached from China but it's unreliable day-to-day — expect random slowdowns, partial blocks, and the occasional total outage. If you have users or collaborators in China, plan for it (mirrors, Gitee, or a CDN with mainland China PoPs).

