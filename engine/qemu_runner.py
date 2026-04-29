import subprocess

def run_qemu(iso, mode="uefi"):

    cmd = [
        "qemu-system-x86_64",
        "-m", "2048",
        "-cdrom", iso,
        "-boot", "d"
    ]

    # UEFI support
    if mode == "uefi":
        cmd += [
            "-bios", "/usr/share/OVMF/OVMF_CODE.fd"
        ]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate(timeout=20)

    return {
        "exit_code": process.returncode,
        "log": stdout.decode() + stderr.decode()
    }
