# engine/dd_flash.py

import subprocess
import re
import time
from engine.safety import register_process

def flash_dd_with_progress(iso, device):

    cmd = [
        "dd",
        f"if={iso}",
        f"of={device}",
        "bs=4M",
        "status=progress"
    ]

    proc = subprocess.Popen(
        cmd,
        stderr=subprocess.PIPE,
        text=True
    )

    register_process(proc)

    start_time = time.time()

    for line in proc.stderr:
        # ตัวอย่าง:
        # 12345678 bytes (12 MB, ...) copied, 0.5 s, 24 MB/s

        match = re.search(r"(\d+) bytes.*?, ([0-9.]+) s, ([0-9.]+) MB/s", line)

        if match:
            bytes_written = int(match.group(1))
            seconds = float(match.group(2))
            speed = float(match.group(3))

            yield {
                "bytes": bytes_written,
                "time": seconds,
                "speed": speed
            }

    proc.wait()

    yield {"status": "done"}
