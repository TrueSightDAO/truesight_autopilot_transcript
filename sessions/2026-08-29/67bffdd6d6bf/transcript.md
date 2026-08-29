# Autopilot Session — 2026-08-29

**Session**: `67bffdd6d6bf`

**Governor**: Gary Teh


---


### 🧑 Governor

[observed, not directed at you — Nobody Will not DM you]: Can you help explain why I am getting for this call

https://edgar.truesight.me/dao/contributors?public_key=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPRTAO1crTPepPB0kFl1POCqyRJk1yxVm0vQZBHZmLyFrnD%2FmxVvHu7fW4qLgjMC%2BbXZ7O1Vt1rfK08oZMSuWWGhnQuBwVUWYX0gkmHB5ajXieBzfnXbnyCdIYjNR8lIlig02T%2FX7U2Jg6vdNF%2FqpX6000F9cdeqeE%2FsLyJ87sazaBHR4tjW9phoKHliNH0D%2BJFcebHLn0StK5qLlhoCtJTPekCBqCEdpftf17Mh069RTAXZj10EsRI2%2BG9ygku2seZZI22JNAcUe0T0g%2F5gOvCXFFj0%2BzX2PGf%2BtT4apUStuv5PugAdznKZbnnt7g0X4wbRXJhvps2t1wyY%2FBxCTQIDAQAB

the response
{
detail: "Not Found"
}

---

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

[Telegram context: chat_id=-1003919341801, thread_id=16210] @truesight_autopilot_bot thoughts on this?

---

[observed, not directed at you — Nobody Will not DM you]: When i grabbed the value from my browser this is the value

MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPRTAO1crTPepPB0kFl1POCqyRJk1yxVm0vQZBHZmLyFrnD/mxVvHu7fW4qLgjMC+bXZ7O1Vt1rfK08oZMSuWWGhnQuBwVUWYX0gkmHB5ajXieBzfnXbnyCdIYjNR8lIlig02T/X7U2Jg6vdNF/qpX6000F9cdeqeE/sLyJ87sazaBHR4tjW9phoKHliNH0D+JFcebHLn0StK5qLlhoCtJTPekCBqCEdpftf17Mh069RTAXZj10EsRI2+G9ygku2seZZI22JNAcUe0T0g/5gOvCXFFj0+zX2PGf+tT4apUStuv5PugAdznKZbnnt7g0X4wbRXJhvps2t1wyY/BxCTQIDAQAB

but in the URL it is https://edgar.truesight.me/dao/contributors?public_key=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPRTAO1crTPepPB0kFl1POCqyRJk1yxVm0vQZBHZmLyFrnD/mxVvHu7fW4qLgjMC+bXZ7O1Vt1rfK08oZMSuWWGhnQuBwVUWYX0gkmHB5ajXieBzfnXbnyCdIYjNR8lIlig02T/X7U2Jg6vdNF/qpX6000F9cdeqeE/sLyJ87sazaBHR4tjW9phoKHliNH0D+JFcebHLn0StK5qLlhoCtJTPekCBqCEdpftf17Mh069RTAXZj10EsRI2+G9ygku2seZZI22JNAcUe0T0g/5gOvCXFFj0+zX2PGf+tT4apUStuv5PugAdznKZbnnt7g0X4wbRXJhvps2t1wyY/BxCTQIDAQAB

And I am getting {
detail: "Not Found"
}

---

[Telegram context: chat_id=-1003919341801, thread_id=16210]


### 🤖 Autopilot

SSH to dao_protocol denied (publickey), so I'll inspect the API surface via the repos. Let me check how the client calls this endpoint and what the server actually exposes.


### 🤖 Autopilot

The Integration Guide is revealing. Let me confirm the actual route names in the dao_protocol FastAPI app.


### 🤖 Autopilot

The Integration Guide documents `check_digital_signature`, not `contributors`. Let me check what routes the live API actually exposes and whether the DApp calls something different.


### 🤖 Autopilot

The live API has a Swagger UI. Let me pull the OpenAPI spec to see the exact route list.


### 🤖 Autopilot

I have the full route picture. Let me confirm there's no `/dao/contributors` anywhere in the spec, and test the correct endpoint with the governor's key to prove the fix.


### 🤖 Autopilot

I've confirmed the root cause. Let me do one quick check for where the broken `/dao/contributors` URL might be coming from (DApp or docs), since that would be a fixable bug.


### 🤖 Autopilot

## Answer — why you get `{"detail": "Not Found"}`

**There is no `/dao/contributors` route on Edgar.** The path you're hitting simply doesn't exist in the API — FastAPI returns `{"detail":"Not Found"}` (404) for any route it doesn't define. The public key is irrelevant; the server never even looks at it for that URL.

I verified this three ways:

1. **Live OpenAPI spec** — I fetched `https://edgar.truesight.me/openapi.json` (version `17018c3`). The full route list under `/dao/` is:
   - `/dao/verify-signature` (POST)
   - `/dao/check_digital_signature` (GET — `?signature=<SPKI base64>`)
   - `/dao/submit_contribution` (POST)
   - `/dao/submit_contribution_review` (POST)
   - `/dao/transactions`, `/dao/qr-codes`, `/dao/inventory-movements`, `/dao/review_queue` (GET queries)
   
   **No `/dao/contributors` anywhere.** I also confirmed via the Swagger UI at `/docs`.

2. **Integration guide** — `dao_protocol/INTEGRATION_GUIDE.md` documents the signature-status lookup as `GET /dao/check_digital_signature?signature=<base64 SPKI public key>`, not `/contributors`.

3. **Org-wide code search** — nothing in any TrueSightDAO repo references `/dao/contributors` or `contributors?public_key`, so it's not a stale link living in our code; it looks hand-typed or from an outdated external reference.

**The correct endpoint works with your exact key** — I just called it and got a 200:



**Fix:** use this URL instead —

```
https://edgar.truesight.me/dao/check_digital_signature?signature=<your SPKI public key>
```

Notes on your two URL variants:
- Both your browser copy and the URL version work fine — `+` vs `%2B` and `/` vs `%2F` are just URL-encoding of the same base64; the server decodes both identically.
- The one gotcha: if you paste the raw key (with `+` and `/`) into a browser address bar, some browsers may mangle it — URL-encoding (`%2B`, `%2F`) is the safe form. But that's not why you got 404; the 404 is purely the wrong path.

If this came from a specific page/tool that generated that URL, tell me where you saw it and I can track down whether there's a docs page or client that should be fixed to point at `check_digital_signature`.

———
**✅ Done this turn — actions taken:**
• `ssh run` → cd /opt/dao_protocol 2>/dev/null || cd ~/dao_protocol 2>/dev/null; pwd; ls; find . -maxdepth 2 -name "*.py" | head -50

