from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import json

from engine.flash_engine import flash_with_progress
from engine.verify_flash import smart_verify
from engine.safety import (
    verify_device_safe,
    verify_iso_safe,
    request_abort,
    reset_abort
)
from engine.qemu_runner import run_qemu_boot
from engine.boot_analyzer import analyze_boot
from engine.auto_fix_engine import suggest_fix, apply_fix

router = APIRouter()

class FlashRequest(BaseModel):
    iso: str
    device: str

@router.get("/")
def health():
    return {"status": "ok"}


# 🔥 FLASH + PROGRESS + VERIFY
@router.post("/flash")
def flash(data: FlashRequest):

    verify_device_safe(data.device)
    verify_iso_safe(data.iso)
    reset_abort()

    def gen():
        for update in flash_with_progress(data.iso, data.device):
            yield json.dumps(update) + "\n"

            if update.get("status") == "aborted":
                return

        # auto verify
        result = smart_verify(data.iso, data.device)
        yield json.dumps({"verify": result}) + "\n"

    return StreamingResponse(gen(), media_type="application/json")


# 🔴 KILL SWITCH
@router.post("/abort")
def abort():
    request_abort()
    return {"status": "aborting"}


# 📦 ISO SIZE
@router.get("/iso-size")
def iso_size(path: str):
    import os
    return {"size": os.path.getsize(path)}

@router.post("/boot-test")
def boot_test(data: dict):

    iso = data.get("iso")

    log = run_qemu_boot(iso)
    result = analyze_boot(log)

    return {
        "result": result,
        "log": log[:1000]  # ตัด log ไม่ให้ยาวเกิน
    }

@router.post("/auto-fix")
def auto_fix(data: dict):
    log = data.get("log")
    device = data.get("device")

    suggestion = suggest_fix(log)

    return {"suggestion": suggestion}


@router.post("/apply-fix")
def apply_fix_api(data: dict):
    log = data.get("log")
    device = data.get("device")

    result = apply_fix(log, device)

    return {"result": result}
