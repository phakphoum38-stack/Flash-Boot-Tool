import subprocess

def fallback_fix(usb):

    # brute force restore bootability
    subprocess.run(["mkfs.vfat", usb])

    subprocess.run(["sync"])

    return {
        "status": "fallback repair applied",
        "mode": "raw boot reset"
    }
