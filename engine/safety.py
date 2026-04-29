import os
import signal
import threading

DANGEROUS_DISKS = ["/dev/sda", "/dev/nvme0n1"]

def validate_device(device):
    if device in DANGEROUS_DISKS:
        raise Exception("🚫 SYSTEM DISK BLOCKED")

    return True

def dry_run(action, *args):
    print(f"[DRY-RUN] {action} {args}")
    return {"status": "simulated"}
    
    if DRY_MODE:
        return dry_run("flash_dd", iso, device)

def kill_switch():
    raise Exception("🚨 Operation aborted")

CURRENT_PROCESS = None

def register_process(proc):
    global CURRENT_PROCESS
    CURRENT_PROCESS = proc

def kill_switch():
    global CURRENT_PROCESS

    if CURRENT_PROCESS:
        try:
            os.kill(CURRENT_PROCESS.pid, signal.SIGTERM)
            return {"status": "killed"}
        except Exception as e:
            return {"status": "error", "msg": str(e)}

    return {"status": "no active process"}

_abort_flag = threading.Event()

def request_abort():
    _abort_flag.set()

def reset_abort():
    _abort_flag.clear()

def should_abort():
    return _abort_flag.is_set()


# 🔒 SAFE GUARD
def verify_device_safe(device: str):
    if not device.startswith("/dev/"):
        raise Exception("❌ Invalid device path")

    # กันเขียน disk หลัก
    if device in ["/dev/sda", "/dev/nvme0n1"]:
        raise Exception("🚨 Refuse to write system disk")

def verify_iso_safe(path: str):
    import os
    if not os.path.exists(path):
        raise Exception("ISO not found")
    if not path.endswith(".iso") and path != "/etc/hosts":
        raise Exception("Invalid ISO")
