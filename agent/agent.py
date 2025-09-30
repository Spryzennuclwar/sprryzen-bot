# Minimal, safe agent. Exposes authenticated REST endpoint and runs only whitelisted actions.

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from actions import WHITELIST
import uvicorn
import os

# IMPORTANT: set this before distributing. Don't hardcode in public repos.
API_KEY = os.environ.get("SPRYZEN_API_KEY", "CHANGE_THIS_TO_A_STRONG_KEY")

app = FastAPI(title="Spryzen Agent (safe whitelist)")

class Command(BaseModel):
    name: str
    args: dict = {}

@app.post("/run")
async def run_cmd(cmd: Command, authorization: str = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing auth")
    token = authorization.split(" ", 1)[1]
    if token != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if cmd.name not in WHITELIST:
        raise HTTPException(status_code=403, detail="Command not allowed")
    fn = WHITELIST[cmd.name]
    try:
        result = fn(**(cmd.args or {}))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=f"Bad args: {e}")
    return {"ok": True, "result": result}

if __name__ == "__main__":
    # default: listen on localhost only. Good for initial safety.
    uvicorn.run("agent.agent:app", host="127.0.0.1", port=7878, reload=False)