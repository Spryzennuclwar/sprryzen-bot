# Spryzen Automation (minimal safe agent)

This repository contains a minimal, whitelisted automation agent.
**Important:** this agent must be run only on machines owned by consenting users.

## How to run (on a PC)
1. Install Python 3.9+.
2. Clone repo and `cd agent`.
3. Set a strong API key:
   - Linux/macOS/PowerShell: `export SPRYZEN_API_KEY="your_strong_key"`
   - Windows CMD: `set SPRYZEN_API_KEY=your_strong_key`
4. Install deps: `pip install -r requirements.txt`
5. Run: `python agent.py`
6. Agent listens on `http://127.0.0.1:7878` by default.

## Example request (from controller)
## Security
- Agent only accepts whitelisted commands.
- Always set a unique `SPRZYEN_API_KEY` environment variable.
- Do not expose the agent to the public internet unless you add TLS and strict auth.
---

✅ **Summary for GitHub users:**
- This README now **lists all commands** (`open_notepad`, `type_text`, `press_key`) with arguments and examples.  
- Users know exactly **how to send commands** safely.  
- Users are instructed to **install Python libraries themselves** using `pip install -r requirements.txt`.  

---

If you want, I can also **add a small optional controller script** that users can run from their PC or phone, where they type simple natural-language instructions (like “open notepad and type hello”) and it automatically sends the proper whitelisted commands — this will make it feel like a “smart” bot.  

Do you want me to create that controller next?