import subprocess
import time

def run_qemu_boot(iso):

    cmd = [
        "qemu-system-x86_64",
        "-m", "1024",
        "-cdrom", iso,
        "-boot", "d",
        "-nographic",
        "-serial", "stdio",
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    start = time.time()
    output = []

    # อ่าน log 10 วินาที
    while True:
        line = process.stdout.readline()
        if not line:
            break

        output.append(line.strip())

        # timeout
        if time.time() - start > 10:
            process.kill()
            break

    return "\n".join(output)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate(timeout=20)

    return {
        "exit_code": process.returncode,
        "log": stdout.decode() + stderr.decode()
    }
