from fastapi import APIRouter
from engine.boot_simulator import simulate_boot
from engine.simulation_report import format_report
from engine.auto_fix_engine import auto_fix

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
