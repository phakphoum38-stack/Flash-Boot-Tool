import requests

CLOUD_URL = "http://localhost:9000"

def upload_fix(signature, strategies, success):
    requests.post(f"{CLOUD_URL}/submit", json={
        "signature": signature,
        "strategies": strategies,
        "success": success
    })

def get_fix(signature):
    res = requests.get(f"{CLOUD_URL}/get/{signature}")
    return res.json().get("strategies", [])
