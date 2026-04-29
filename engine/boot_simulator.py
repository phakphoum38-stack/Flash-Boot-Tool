from engine.iso_scanner import scan_iso
from engine.boot_validator import validate_windows, validate_linux

def simulate_boot(iso_path):

    iso = scan_iso(iso_path)

    result = {
        "iso": iso["name"],
        "type": iso["type"],
        "bootable": False,
        "risk": "unknown",
        "issues": [],
        "fix_suggestion": []
    }

    # WINDOWS
    if iso["type"] == "windows":
        issues = validate_windows(iso_path)

        result["issues"] = issues

        if len(issues) == 0:
            result["bootable"] = True
            result["risk"] = "low"
        else:
            result["bootable"] = True
            result["risk"] = "medium"
            result["fix_suggestion"].append("Enable WIM split + EFI fix")

    # LINUX
    elif iso["type"] == "linux":
        issues = validate_linux(iso_path)

        result["bootable"] = True
        result["risk"] = "low"
        result["issues"] = issues

    # UNKNOWN
    else:
        result["bootable"] = False
        result["risk"] = "high"
        result["fix_suggestion"].append("Use DD raw mode")

    return result
