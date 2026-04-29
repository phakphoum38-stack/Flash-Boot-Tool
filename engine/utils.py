import os

def sanitize_path(path):
    if ".." in path or path.startswith("/etc"):
        raise Exception("Invalid path")
    return os.path.abspath(path)

def get_file_size(path):
    return os.path.getsize(path)
