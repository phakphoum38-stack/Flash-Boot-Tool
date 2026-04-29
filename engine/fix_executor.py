import subprocess
import os

def rebuild_mbr(device):
    subprocess.run(["parted", device, "mklabel", "msdos"])

def install_efi(usb):
    os.makedirs(f"{usb}/EFI/BOOT", exist_ok=True)
    subprocess.run([
        "cp",
        "BOOTX64.EFI",
        f"{usb}/EFI/BOOT/BOOTX64.EFI"
    ])

def rebuild_grub(usb):
    os.makedirs(f"{usb}/boot/grub", exist_ok=True)

    grub_cfg = """
set timeout=5
menuentry "Auto Fix Boot" {
    insmod part_gpt
    insmod fat
    chainloader /EFI/BOOT/BOOTX64.EFI
}
"""
    with open(f"{usb}/boot/grub/grub.cfg", "w") as f:
        f.write(grub_cfg)

def split_wim(wim_path, usb):
    subprocess.run([
        "wimlib-imagex",
        "split",
        wim_path,
        f"{usb}/sources/install.swm",
        "3800"
    ])

def full_reset(device):
    subprocess.run(["mkfs.vfat", device])


def rebuild_partition_table(device):
    subprocess.run(["parted", device, "mklabel", "msdos"])

def repair_grub(device):
    subprocess.run(["grub-install", device])

def rewrite_mbr(device):
    subprocess.run(["dd", "if=/usr/lib/syslinux/mbr/mbr.bin", f"of={device}"])

def windows_boot_fix(device):
    return "Use Windows recovery (bootrec /fixmbr)"

def safe_mode_boot(device):
    return "Try boot with safe mode kernel"

FIX_MAP = {
    "rebuild_partition_table": rebuild_partition_table,
    "repair_grub": repair_grub,
    "rewrite_mbr": rewrite_mbr,
    "windows_boot_fix": windows_boot_fix,
    "safe_mode_boot": safe_mode_boot,
}
