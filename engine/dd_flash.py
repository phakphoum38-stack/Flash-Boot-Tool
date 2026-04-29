import subprocess
from engine.safety import register_process
from engine.validator import verify_device, verify_iso

def flash_dd(iso, device):

    cmd = [
        "dd",
        f"if={iso}",
        f"of={device}",
        "bs=4M",
        "status=progress"
    ]

    proc = subprocess.Popen(cmd)

    # 🔥 register process เพื่อ kill ได้
    register_process(proc)

    proc.wait()

    return {"status": "done"}

def flash_dd(iso, device):

    # 🔥 VERIFY ก่อน
    verify_iso(iso)
    verify_device(device)

    cmd = [
        "dd",
        f"if={iso}",
        f"of={device}",
        "bs=4M",
        "status=progress"
    ]

    proc = subprocess.Popen(cmd)
    register_process(proc)

    proc.wait()

    return {"status": "done"}
