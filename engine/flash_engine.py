import subprocess

def flash_dd(iso, device):
    cmd = [
        "dd",
        f"if={iso}",
        f"of={device}",
        "bs=4M",
        "status=progress"
    ]

    subprocess.run(cmd)
    return "done"
