# engine/validator.py

import os

def verify_device(device):
    if not device.startswith("/dev/"):
        raise Exception("❌ Invalid device path")

    if "sda" in device or "nvme0n1" in device:
        raise Exception("🚫 Blocked system disk")

def verify_iso(iso):
    if not iso.endswith(".iso"):
        raise Exception("❌ Not an ISO file")

    if not os.path.exists(iso):
        raise Exception("❌ ISO not found")
