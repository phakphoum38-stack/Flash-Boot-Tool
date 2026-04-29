from fastapi import APIRouter
from engine.verify_flash import smart_verify

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/verify")
def verify(data: dict):
    iso = data.get("iso")
    device = data.get("device")

    if not iso or not device:
        return {"error": "iso/device required"}

    return smart_verify(iso, device)
