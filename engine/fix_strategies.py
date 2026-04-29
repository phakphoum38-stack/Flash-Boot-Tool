def map_fix_strategy(qemu_result):

    error = (qemu_result.get("error") or "").lower()
    log = (qemu_result.get("log") or "").lower()

    strategies = []

    if "no bootable device" in error or "no bootable device" in log:
        strategies.append("rebuild_mbr")
        strategies.append("install_bootloader")

    if "missing bootloader" in error:
        strategies.append("install_efi")

    if "grub rescue" in log:
        strategies.append("rebuild_grub")

    if "wim" in log or "install.wim" in log:
        strategies.append("split_wim")

    if not strategies:
        strategies.append("full_reset")

    return strategies
