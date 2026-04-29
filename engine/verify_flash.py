import subprocess
import os
from engine.checksum import sha256_file

def verify_flash(iso, device):

    tmp_dump = "/tmp/usb_dump.img"

    # 🔥 อ่าน USB กลับมา (ขนาดเท่า ISO)
    size = os.path.getsize(iso)

    cmd = [
        "dd",
        f"if={device}",
        f"of={tmp_dump}",
        "bs=4M",
        f"count={size // (4*1024*1024) + 1}"
    ]

    subprocess.run(cmd)

    print("🔍 Calculating ISO hash...")
    iso_hash = sha256_file(iso)

    print("🔍 Calculating USB hash...")
    usb_hash = sha256_file(tmp_dump)

    os.remove(tmp_dump)

    return {
        "iso_hash": iso_hash,
        "usb_hash": usb_hash,
        "match": iso_hash == usb_hash
    }
