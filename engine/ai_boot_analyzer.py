import os

def analyze_iso(path):
    name = path.lower()

    result = {
        "os": "unknown",
        "boot": "legacy+uefi",
        "fs": "FAT32",
        "strategy": "dd"
    }

    if "windows" in name:
        result.update({
            "os": "windows",
            "strategy": "windows_smart",
            "fs": "NTFS/FAT32_SPLIT",
            "boot": "uefi+legacy"
        })

    elif "ubuntu" in name or "linux" in name:
        result.update({
            "os": "linux",
            "strategy": "grub_uefi",
            "fs": "FAT32",
            "boot": "uefi"
        })

    elif "mac" in name or "macos" in name:
        result.update({
            "os": "macos",
            "strategy": "apple_efi_patch",
            "fs": "APFS/FAT32",
            "boot": "uefi"
        })

    return result

def analyze_boot(log):

    log = log.lower()

    if "no bootable device" in log:
        return {"status": "fail", "reason": "No bootable device"}

    if "booting from cd" in log or "isolinux" in log:
        return {"status": "ok", "reason": "Boot loader detected"}

    if "error" in log:
        return {"status": "fail", "reason": "Generic boot error"}

    return {"status": "unknown", "reason": "Unclear"}
