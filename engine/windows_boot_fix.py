import subprocess
import os

def fix_windows_boot(usb):
    os.makedirs(f"{usb}/EFI/BOOT", exist_ok=True)

    subprocess.run([
        "cp",
        "bootx64.efi",
        f"{usb}/EFI/BOOT/BOOTX64.EFI"
    ])

    return "Windows UEFI fixed"
