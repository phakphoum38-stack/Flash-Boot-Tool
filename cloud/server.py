from fastapi import FastAPI
from cloud.database import conn, cur
from cloud.ranking import rank_fixes
from fastapi import Header, HTTPException
import time

API_KEY = "flashforge-secure"

last_call = {}

app = FastAPI()

@app.post("/submit")
def submit(data: dict):
    cur.execute(
        "INSERT INTO fixes (signature, strategies, success) VALUES (?, ?, ?)",
        (data["signature"], str(data["strategies"]), data["success"])
    )
    conn.commit()
    return {"status": "stored"}

@app.get("/get/{signature}")
def get(signature: str):
    cur.execute(
        "SELECT strategies, success, uses FROM fixes WHERE signature=?",
        (signature,)
    )
    rows = cur.fetchall()

    ranked = rank_fixes(rows)

    if ranked:
        return {"strategies": ranked}

    return {"strategies": []}

@app.post("/submit")
def submit(data: dict, x_api_key: str = Header(None)):
    check_auth(x_api_key)

def check_auth(key):
    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

def rate_limit(ip):
    now = time.time()
    if ip in last_call and now - last_call[ip] < 1:
        raise HTTPException(status_code=429, detail="Too many requests")
    last_call[ip] = now


