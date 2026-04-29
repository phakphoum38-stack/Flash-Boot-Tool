from engine.qemu_boot_emulator import emulate_boot

@router.post("/emulate")
def emulate(data: dict):
    result = emulate_boot(data["iso"])

    return {
        "result": result,
        "status": "simulation complete"
    }
