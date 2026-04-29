import json
from datetime import datetime

def log_action(action, detail):
    with open("audit.log", "a") as f:
        f.write(json.dumps({
            "time": datetime.utcnow().isoformat(),
            "action": action,
            "detail": detail
        }) + "\n")
