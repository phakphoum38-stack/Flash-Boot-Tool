from fastapi import APIRouter
from engine.boot_simulator import simulate_boot
from engine.simulation_report import format_report
from engine.auto_fix_engine import auto_fix
from engine.ai_engine import smart_auto_fix
from engine.safety import kill_switch
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import json
from engine.dd_flash import flash_dd_with_progress

router = APIRouter()

@router.post("/simulate")
def simulate(data: dict):
    sim = simulate_boot(data["iso"])

    return {
        "raw": sim,
        "report": format_report(sim)
    }

@router.post("/auto-fix")
def auto_fix_api(data: dict):
    result = auto_fix(
        data["qemu_result"],
        data["iso"],
        data["usb"]
    )

    return result

@router.post("/ai-auto-fix")
def ai_fix(data: dict):
    return smart_auto_fix(
        data["iso"],
        data["usb"]
    )

@router.post("/abort")
def abort():
    return kill_switch()

@router.get("/flash-progress")
def flash_progress(iso: str, device: str):

    def event_stream():
        for update in flash_dd_with_progress(iso, device):
            yield f"data: {json.dumps(update)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
