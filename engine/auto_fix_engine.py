from engine.fix_strategies import map_fix_strategy
from engine.fix_executor import (
    rebuild_mbr,
    install_efi,
    rebuild_grub,
    split_wim,
    full_reset
)

def auto_fix(qemu_result, iso_path, usb):

    strategies = map_fix_strategy(qemu_result)

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
