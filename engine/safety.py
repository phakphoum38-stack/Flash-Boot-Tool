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
