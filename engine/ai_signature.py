def build_signature(qemu_result: dict):
    log = (qemu_result.get("log") or "").lower()
    err = (qemu_result.get("error") or "").lower()

    sig = []

    if "no bootable device" in log or "no bootable device" in err:
        sig.append("NO_BOOT")

    if "grub rescue" in log:
        sig.append("GRUB_RESCUE")

    if "efi" in log:
        sig.append("EFI_ISSUE")

    if "wim" in log or "install.wim" in log:
        sig.append("WIM_LARGE")

    if not sig:
        sig.append("UNKNOWN")

    return "|".join(sorted(sig))
