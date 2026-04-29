import os

def scan_iso(iso_path):
    return {
        "name": os.path.basename(iso_path),
        "size": os.path.getsize(iso_path),
        "type": detect_type(iso_path)
    }

def detect_type(path):
    name = path.lower()

    if "windows" in name:
        return "windows"
    if "ubuntu" in name or "linux" in name:
        return "linux"
    if "mac" in name:
        return "macos"

    return "unknown"
