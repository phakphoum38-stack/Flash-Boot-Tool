def parse_log(log):
    log = log.lower()

    if "efi" in log:
        return "UEFI boot detected"

    if "grub" in log:
        return "Linux GRUB boot"

    if "windows" in log:
        return "Windows bootloader detected"

    if "error" in log:
        return "BOOT ERROR"

    return "UNKNOWN STATE"
