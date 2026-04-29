# engine/verify_flash.py

import os
import hashlib
import random
from concurrent.futures import ThreadPoolExecutor

SAMPLE_SIZE = 1024 * 1024  # 1MB ต่อ sample
NUM_SAMPLES = 20           # จำนวน sample

def read_block(path, offset, size):
    with open(path, "rb") as f:
        f.seek(offset)
        return f.read(size)

def hash_block(data):
    return hashlib.sha256(data).hexdigest()

def get_offsets(size):
    offsets = [0, size // 2, size - SAMPLE_SIZE]  # จุดสำคัญ
    for _ in range(NUM_SAMPLES):
        offsets.append(random.randint(0, size - SAMPLE_SIZE))
    return offsets

def fast_verify(iso, device):

    size = os.path.getsize(iso)

    offsets = get_offsets(size)

    def check_offset(offset):
        iso_block = read_block(iso, offset, SAMPLE_SIZE)
        usb_block = read_block(device, offset, SAMPLE_SIZE)

        return hash_block(iso_block) == hash_block(usb_block)

    # 🔥 parallel
    with ThreadPoolExecutor(max_workers=8) as exe:
        results = list(exe.map(check_offset, offsets))

    match_ratio = sum(results) / len(results)

    return {
        "method": "fast_verify",
        "samples": len(offsets),
        "match_ratio": match_ratio,
        "match": match_ratio > 0.95
    }
