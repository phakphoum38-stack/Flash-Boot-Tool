import subprocess

def format_disk(device, fs):
    if fs == "NTFS":
        subprocess.run(["mkfs.ntfs", device])
    elif fs == "FAT32":
        subprocess.run(["mkfs.vfat", device])
    else:
        subprocess.run(["dd", "if=/dev/zero", f"of={device}"])
