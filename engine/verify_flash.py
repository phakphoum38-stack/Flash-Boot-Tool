import os
import hashlib
import random
from concurrent.futures import ThreadPoolExecutor

SAMPLE_SIZE = 1024 * 1024  # 1MB
NUM_SAMPLES = 20


def read_block(path, offset, size):
    with open(path, "rb") as f:
        f.seek(offset)
        return f.read(size)


def hash_block(data):
    return hashlib.sha256(data).hexdigest()


def get_offsets(size):
    offsets = [0, size // 2, max(0, size - SAMPLE_SIZE)]
    for _ in range(NUM_SAMPLES):
        offsets.append(random.randint(0, max(1, size - SAMPLE_SIZE)))
    return offsets


def fast_verify(iso, device):
    size = os.path.getsize(iso)
    offsets = get_offsets(size)

    def check(offset):
        iso_block = read_block(iso, offset, SAMPLE_SIZE)
        usb_block = read_block(device, offset, SAMPLE_SIZE)
        return hash_block(iso_block) == hash_block(usb_block)

    with ThreadPoolExecutor(max_workers=8) as exe:
        results = list(exe.map(check, offsets))

    ratio = sum(results) / len(results)

    return {
        "method": "fast",
        "samples": len(offsets),
        "match_ratio": ratio,
        "match": ratio > 0.95
    }


def full_verify(iso, device):
    def sha(path):
        h = hashlib.sha256()
        with open(path, "rb") as f:
            while True:
                data = f.read(1024 * 1024)
                if not data:
                    break
                h.update(data)
        return h.hexdigest()

    return {
        "method": "full",
        "match": sha(iso) == sha(device)
    }


def smart_verify(iso, device):
    if not os.path.exists(iso):
        return {"error": "ISO not found"}

    fast = fast_verify(iso, device)

    if fast["match_ratio"] < 0.98:
        full = full_verify(iso, device)
        return {"fast": fast, "full": full}

    return {"fast": fast}
