from fastapi import APIRouter
from engine.boot_simulator import simulate_boot
from engine.simulation_report import format_report

router = APIRouter()

@router.post("/simulate")
def simulate(data: dict):
    sim = simulate_boot(data["iso"])

    return {
        "raw": sim,
        "report": format_report(sim)
    }
