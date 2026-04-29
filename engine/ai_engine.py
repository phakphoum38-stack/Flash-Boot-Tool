from engine.ai_signature import build_signature
from engine.ai_recommender import recommend
from engine.auto_fix_engine import auto_fix
from engine.qemu_boot_emulator import emulate_boot
from engine.ai_trainer import train


def detect_best_mode(iso_name):
    iso_name = iso_name.lower()

    if "windows" in iso_name:
        return {
            "mode": "windows_smart",
            "fs": "NTFS",
            "boot": "uefi+legacy",
            "fix": "wim_split_required"
        }

    if "ubuntu" in iso_name:
        return {
            "mode": "linux",
            "fs": "FAT32",
            "boot": "uefi",
            "fix": None
        }

    return {
        "mode": "dd_raw",
        "fs": "raw",
        "boot": "auto",
        "fix": None
    }

def smart_auto_fix(iso, usb):

    # 1. emulate boot
    qemu_result = emulate_boot(iso)

    # 2. build signature
    signature = build_signature(qemu_result)

    # 3. ask AI memory
    rec = recommend(signature)

    if rec["strategies"]:
        # ใช้ strategy ที่เคยสำเร็จ
        result = auto_fix(
            {"error": "", "log": ""},
            iso,
            usb
        )
        result["ai_source"] = "memory"

    else:
        # fallback heuristic
        result = auto_fix(qemu_result, iso, usb)
        result["ai_source"] = "heuristic"

    # 4. re-test
    recheck = emulate_boot(iso)

    success = recheck.get("boot_success", False)

    # 5. train memory
    train(signature, result.get("strategies", []), success)

    return {
        "signature": signature,
        "ai_source": result["ai_source"],
        "fix": result,
        "recheck": recheck
    }
