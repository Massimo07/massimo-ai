from fastapi import Request, HTTPException

def check_human(req: Request):
    user_agent = req.headers.get("user-agent", "")
    if "bot" in user_agent.lower() or "curl" in user_agent.lower():
        raise HTTPException(status_code=403, detail="Bot non ammesso")
    # Collega qui captcha/fingerprint se vuoi essere ULTRA TOP!
    return True
