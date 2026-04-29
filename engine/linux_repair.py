import os

def fix_linux(iso, usb):

    os.makedirs(f"{usb}/boot/grub", exist_ok=True)

    grub_cfg = """
set timeout=5
menuentry "Boot Linux ISO" {
    loopback loop /ISO/linux.iso
    linux (loop)/casper/vmlinuz boot=casper
    initrd (loop)/casper/initrd
}
"""

    with open(f"{usb}/boot/grub/grub.cfg", "w") as f:
        f.write(grub_cfg)

    return {
        "status": "linux boot repaired",
        "bootloader": "GRUB2"
    }
