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
