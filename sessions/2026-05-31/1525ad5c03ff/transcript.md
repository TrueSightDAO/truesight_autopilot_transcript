# Autopilot Session — 2026-05-31

**Session**: `1525ad5c03ff`

**Governor**: Gary Teh


---


### 🧑 Governor

 You are speaking with Gary Teh. When they say 'I', 'me', or 'my', they mean Gary Teh.]

I noticed that this https://dapp.truesight.me/governor_contributor_admin.html after I registered the email address of a new contributor did not send out a welcome email to 

https://dapp.truesight.me/create_signature.html

Can you find out why?


### 🤖 Autopilot

Let me investigate this. First, I'll look at the relevant code in the dapp repos to understand how the registration and email flow works.


### 🤖 Autopilot

Now I can see the issue. Let me look at the flow more carefully. The `governor_contributor_admin.html` page submits a `[CONTRIBUTOR ADD EVENT]` to Edgar — it does NOT send any welcome email. The email flow is on `create_signature.html`, where the contributor self-registers.

Let me check what happens on the Edgar/backend side when a `[CONTRIBUTOR ADD EVENT]` is submitted — does it trigger any email?


### 🤖 Autopilot

Let me look at the Edgar backend to understand what happens when a `[CONTRIBUTOR ADD EVENT]` is submitted — specifically whether it triggers any email sending.


### 🤖 Autopilot

The `dao_client` repo seems to have moved. Let me check what repos exist and find the right one.


### 🤖 Autopilot

I see — `dao_client` is no longer listed. Let me check the `dapp_prod` repo (which is the production DApp) and look at the Edgar backend in the tokenomics repo.


### 🤖 Autopilot

Now let me look at the Edgar backend to understand the email flow. Let me check the tokenomics repo for the GAS scripts that handle email registration.


### 🤖 Autopilot

Let me look at the Edgar backend directly — the Rails app that processes these events.


### 🤖 Autopilot

Now I see the architecture clearly. Let me look at the actual GAS script that sends the verification email to understand the full flow.


### 🤖 Autopilot

Now I see — Edgar is the Rails app in `sentiment_importer`. Let me look at how it handles the `[CONTRIBUTOR ADD EVENT]` and whether it sends any email.


### 🤖 Autopilot

Now I can see the full picture. Let me look at the `DaoEmailRegistrationService` to understand the email sending flow:


### 🤖 Autopilot

Now I have the full picture. Let me check the key piece — the `[CONTRIBUTOR ADD EVENT]` handler. Looking at the `trigger_immediate_processing` method in the controller, I can see:

```ruby
elsif text.include?('[CONTRIBUTOR ADD EVENT]')
  contributor_add_webhook_url = Rails.application.config.contributor_add_processing_webhook_url
  if contributor_add_webhook_url.present?
    webhooks_to_trigger << { ... }
  else
    Rails.logger.warn('contributor_add_processing_webhook_url not set in config/application.rb - contributor adds will only be processed by manual runs')
  end
```

Let me check what the `contributor_add_processing_webhook_url` config looks like:


### 🤖 Autopilot

Now I have the complete picture. Let me also check the GAS side — the `ContributorAddHandler.js`:


### 🤖 Autopilot

Let me check the clasp_mirrors README to find the right script ID:


### 🤖 Autopilot

Now I have a thorough understanding of the architecture. Let me summarize the answer for you.

---

Here's the full analysis of why **no welcome email** is sent when you register a new contributor via `governor_contributor_admin.html`:

## The Two Separate Flows

There are **two distinct flows** in the system, and they are intentionally decoupled:

### Flow 1: Governor Adds Contributor (`governor_contributor_admin.html`)
- You submit a `[CONTRIBUTOR ADD EVENT]` with name + email
- Edgar logs it to **Telegram Chat Logs** (Google Sheet)
- Edgar fires a **webhook** to the GAS `tdg_identity_management` project (`?action=processContributorAddsFromTelegramChatLogs`)
- That GAS handler appends the name + email to **"Contributors contact information"** on the Main Ledger
- **No email is sent** at this stage — by design

### Flow 2: Contributor Self-Registers (`create_signature.html`)
- The contributor visits `create_signature.html`, enters their email, generates a keypair
- The browser submits an `[EMAIL REGISTERED EVENT]` to Edgar
- Edgar calls `DaoEmailRegistrationService` → `trigger_verification_email()`
- That fires a **separate GAS webhook** (`email_verification_gas_webhook_url`) with `?action=sendEmailVerification`
- The GAS handler calls `GmailApp.sendEmail()` to send the verification link
- The contributor clicks the link → `[EMAIL VERIFICATION EVENT]` → key is activated

## Why No Welcome Email

The `governor_contributor_admin.html` page **does not trigger any email**. The page's own description says it clearly:

> *"The new contributor will later self-register their first device public key via the email-verification flow; you do not need to enter a public key here."*

The design intent is:
1. **You** (governor) add the contributor's name + email to the ledger (Flow 1)
2. **The contributor** goes to `create_signature.html`, enters their email, and the system sends them a verification link (Flow 2)

The contributor doesn't get a "welcome" email from your action — they only get the verification email when **they** initiate the registration on `create_signature.html`.

## What's Missing (if you want a welcome email)

If you want the system to send a welcome/onboarding email when a governor adds a contributor, that would be a **new feature** — the `ContributorAddHandler.js` GAS script would need to be extended to call `GmailApp.sendEmail()` after appending the row. Currently it only appends to the sheet.

Would you like me to open a fix PR to add a welcome email feature to the contributor add flow?

