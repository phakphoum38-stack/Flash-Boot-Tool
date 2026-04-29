import requests

def download_iso(url, path):
    r = requests.get(url, stream=True)

    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            f.write(chunk)

    return path
