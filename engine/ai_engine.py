def detect_best_mode(iso_name):
    iso_name = iso_name.lower()

    if "windows" in iso_name:
        return {
            "mode": "windows_smart",
            "fs": "NTFS",
            "boot": "uefi+legacy",
            "fix": "wim_split_required"
        }

    if "ubuntu" in iso_name:
        return {
            "mode": "linux",
            "fs": "FAT32",
            "boot": "uefi",
            "fix": None
        }

    return {
        "mode": "dd_raw",
        "fs": "raw",
        "boot": "auto",
        "fix": None
    }
