from engine.qemu_runner import run_qemu

def emulate_boot(iso_path):

    result = run_qemu(iso_path)

    log = result["log"].lower()

    report = {
        "iso": iso_path,
        "boot_success": False,
        "mode": "unknown",
        "error": None
    }

    # วิเคราะห์ log แบบ heuristic (simple AI)
    if "booting from hard disk" in log or "welcome" in log:
        report["boot_success"] = True
        report["mode"] = "UEFI/BIOS OK"

    elif "no bootable device" in log:
        report["error"] = "Missing bootloader"

    elif "grub" in log:
        report["boot_success"] = True
        report["mode"] = "GRUB detected"

    else:
        report["error"] = "Unknown boot state"

    return report
