from engine.validator import verify_device, verify_iso

def safe_flash(func, iso, device):

    verify_iso(iso)
    verify_device(device)

    return func(iso, device)
