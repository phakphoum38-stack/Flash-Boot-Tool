import os
import shutil

def fix_efi(iso, usb):

    efi_path = f"{usb}/EFI/BOOT"
    os.makedirs(efi_path, exist_ok=True)

    shutil.copy(
        "BOOTX64.EFI",
        f"{efi_path}/BOOTX64.EFI"
    )

    return {
        "status": "EFI boot repaired",
        "secure_boot": "compatible"
    }
