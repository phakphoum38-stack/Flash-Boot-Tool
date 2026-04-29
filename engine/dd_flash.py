import subprocess
from engine.safety import register_process

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
