import hashlib

def sha256_file(path, block_size=1024*1024):
    sha = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            sha.update(data)

    return sha.hexdigest()
