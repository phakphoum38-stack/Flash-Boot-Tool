DANGEROUS_DISKS = ["/dev/sda", "/dev/nvme0n1"]

def validate_device(device):
    if device in DANGEROUS_DISKS:
        raise Exception("🚫 SYSTEM DISK BLOCKED")

    return True
