import json
import os
from datetime import datetime

DB_PATH = "engine/ai_memory_db.json"

def _load():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)

def _save(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_record(signature, strategies, success):
    db = _load()
    db.append({
        "signature": signature,
        "strategies": strategies,
        "success": success,
        "ts": datetime.utcnow().isoformat()
    })
    _save(db)

def find_best(signature):
    db = _load()
    candidates = [r for r in db if r["signature"] == signature and r["success"]]

    # ให้ความสำคัญ record ล่าสุด
    candidates.sort(key=lambda x: x["ts"], reverse=True)

    if candidates:
        return candidates[0]["strategies"]

    return None
