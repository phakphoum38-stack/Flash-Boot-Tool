def generate_menu(isos):
    menu = "set timeout=5\n"

    for iso in isos:
        menu += f"""
menuentry "{iso}" {{
    loopback loop /ISO/{iso}
    chainloader (loop)
}}
"""

    return menu
