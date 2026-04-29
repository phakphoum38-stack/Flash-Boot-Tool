from engine.fix_strategies import map_fix_strategy
from engine.fix_executor import (
    rebuild_mbr,
    install_efi,
    rebuild_grub,
    split_wim,
    full_reset
)
from engine.security_policy import filter_strategies
from engine.fix_strategies import FIX_DB
from engine.fix_executor import FIX_MAP


def auto_fix(qemu_result, iso_path, usb):

    strategies = map_fix_strategy(qemu_result)
    strategies = filter_strategies(strategies)

    applied = []

    for s in strategies:

        if s == "rebuild_mbr":
            rebuild_mbr(usb)
            applied.append("MBR rebuilt")

        elif s == "install_bootloader" or s == "install_efi":
            install_efi(usb)
            applied.append("EFI installed")

        elif s == "rebuild_grub":
            rebuild_grub(usb)
            applied.append("GRUB rebuilt")

        elif s == "split_wim":
            wim = f"/tmp/extract/sources/install.wim"
            split_wim(wim, usb)
            applied.append("WIM split")

        elif s == "full_reset":
            full_reset(usb)
            applied.append("USB reset")

    return {
        "status": "fix applied",
        "strategies": strategies,
        "actions": applied
    }

def detect_issue(log):
    log = log.lower()

    for key in FIX_DB:
        if key in log:
            return key

    return None


def suggest_fix(log):
    issue = detect_issue(log)

    if not issue:
        return {"status": "unknown", "message": "No known issue"}

    data = FIX_DB[issue]

    return {
        "status": "detected",
        "issue": issue,
        "fix": data["fix"],
        "description": data["desc"]
    }


def apply_fix(log, device):
    issue = detect_issue(log)

    if not issue:
        return {"status": "no_fix"}

    fix_name = FIX_DB[issue]["fix"]
    func = FIX_MAP.get(fix_name)

    if func:
        try:
            result = func(device)
            return {"status": "applied", "fix": fix_name, "result": str(result)}
        except Exception as e:
            return {"status": "error", "error": str(e)}

    return {"status": "not_found"}
