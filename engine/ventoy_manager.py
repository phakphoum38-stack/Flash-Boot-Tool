import os
import shutil

def install_ventoy(device):
    os.system(f"ventoy -i {device}")

def add_iso(device, iso_path):
    iso_folder = f"{device}/ISO"
    os.makedirs(iso_folder, exist_ok=True)

    shutil.copy(iso_path, iso_folder)

def list_isos(device):
    return os.listdir(f"{device}/ISO")
