from engine.ai_boot_analyzer import analyze_iso
from engine.windows_repair import fix_windows
from engine.linux_repair import fix_linux
from engine.efi_repair import fix_efi
from engine.fallback_repair import fallback_fix

def auto_repair_boot(iso, usb):
    plan = analyze_iso(iso)

    os_type = plan["os"]

    if os_type == "windows":
        return fix_windows(iso, usb)

    if os_type == "linux":
        return fix_linux(iso, usb)

    if os_type == "macos":
        return fix_efi(iso, usb)

    return fallback_fix(usb)
