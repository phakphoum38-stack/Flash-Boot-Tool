from fastapi import FastAPI
from cloud.database import conn, cur
from cloud.ranking import rank_fixes

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
