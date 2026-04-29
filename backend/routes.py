from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import json
import traceback
import os

from engine.flash_engine import flash_with_progress
from engine.verify_flash import smart_verify
from engine.safety import (
    verify_device_safe,
    verify_iso_safe,
    request_abort,
    reset_abort
)

router = APIRouter()


# =========================
# 📦 Request Model
# =========================
class FlashRequest(BaseModel):
    iso: str
    device: str


# =========================
# ❤️ HEALTH CHECK
# =========================
@router.get("/")
def health():
    return {"status": "ok"}


# =========================
# 🔥 FLASH STREAM (FIXED + SAFE)
# =========================
@router.post("/flash")
def flash(data: FlashRequest):

    try:
        verify_device_safe(data.device)
        verify_iso_safe(data.iso)
        reset_abort()

        def gen():
            try:
                # 🚀 flash progress stream
                for update in flash_with_progress(data.iso, data.device):

                    # กัน crash ถ้า engine ส่งไม่ใช่ dict
                    if not isinstance(update, dict):
                        update = {"raw": str(update)}

                    yield json.dumps({
                        "type": "progress",
                        "data": update
                    }) + "\n"

                    if update.get("status") == "aborted":
                        yield json.dumps({"type": "aborted"}) + "\n"
                        return

                # 🔍 auto verify
                result = smart_verify(data.iso, data.device)

                yield json.dumps({
                    "type": "verify",
                    "data": result
                }) + "\n"

            except Exception as e:
                traceback.print_exc()
                yield json.dumps({
                    "type": "error",
                    "message": str(e)
                }) + "\n"

        return StreamingResponse(
            gen(),
            media_type="application/x-ndjson"
        )

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}


# =========================
# 🛑 ABORT
# =========================
@router.post("/abort")
def abort():
    request_abort()
    return {"status": "aborting"}


# =========================
# 💾 ISO SIZE (FIXED SAFE)
# =========================
@router.get("/iso-size")
def iso_size(path: str):

    try:
        return {"size": os.path.getsize(path)}
    except Exception as e:
        return {"error": str(e)}
