import subprocess
import time
import re
from engine.safety import should_abort

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

def flash_with_progress(iso, device):

    cmd = [
        "dd",
        f"if={iso}",
        f"of={device}",
        "bs=4M",
        "status=progress",
        "oflag=sync"
    ]

    process = subprocess.Popen(
        cmd,
        stderr=subprocess.PIPE,
        text=True
    )

    start = time.time()
    total_bytes = 0

    for line in process.stderr:
        if should_abort():
            process.kill()
            yield {"status": "aborted"}
            return

        match = re.search(r'(\d+) bytes', line)
        if match:
            total_bytes = int(match.group(1))

            elapsed = time.time() - start
            speed = total_bytes / elapsed if elapsed > 0 else 0

            yield {
                "bytes": total_bytes,
                "speed": speed / (1024*1024)
            }

    process.wait()

    yield {"status": "done"}
