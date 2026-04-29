import os

def create_virtual_usb_image(iso_path, img_path="virtual_usb.img"):
    size = 4 * 1024 * 1024 * 1024  # 4GB

    os.system(f"qemu-img create -f raw {img_path} {size}")

    return img_path
