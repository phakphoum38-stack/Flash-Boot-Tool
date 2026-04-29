import os
import os, hashlib, random
from concurrent.futures import ThreadPoolExecutor

SAMPLE_SIZE = 1024 * 1024
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

    def check(o):
        return hash_block(read_block(iso, o, SAMPLE_SIZE)) == \
               hash_block(read_block(device, o, SAMPLE_SIZE))

    with ThreadPoolExecutor(max_workers=8) as exe:
        results = list(exe.map(check, offsets))

    ratio = sum(results)/len(results)

    return {"match": ratio > 0.95, "match_ratio": ratio}

def smart_verify(iso, device):
    return {"fast": fast_verify(iso, device)}
