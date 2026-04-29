import os

def validate_windows(iso):
    issues = []

    # fake check (จริงจะ mount ISO)
    if "windows" in iso.lower():
        issues.append("Check install.wim size")

    return issues


def validate_linux(iso):
    issues = []

    if "ubuntu" in iso.lower():
        issues.append("GRUB OK expected")

    return issues
