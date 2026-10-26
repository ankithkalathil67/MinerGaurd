# ACM AI Bot (name pending vote)

An AI-powered Discord bot built by the ACM AI group at Missouri S&T.

**Main goal:** protect S&T student organization Discord servers from scam and spam accounts, and get other S&T orgs using it.

## What it does

**Server guard**
- New-account check when someone joins
- Raid detection (lots of joins at once)
- AI scam check on suspicious messages
- Scam-link detection
- Suspicious accounts get quarantined and officers are pinged. A human makes the final call.

**Campus info**
- Rolla weather (done)
- St. Pat's countdown
- Campus events
- Dining hours

**CS club**
- Contest and hackathon reminders
- `/explain`: paste an error, get it explained

**Ask it anything:** @mention the bot and it answers using an AI agent with tools.

## Setup (to run the bot yourself)

1. Install Python 3.10 or newer
2. Install the packages:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to a new file named `.env` and paste in the bot token
   (ask an officer for a test token). **Never commit `.env`.**
4. Sign in to Ollama for the AI model: `ollama signin`
5. Run it:
   ```
   python bot.py
   ```

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Team

Built by the ACM AI group at Missouri S&T, Fall 2026.
<!-- Add your name here in your first pull request! -->
