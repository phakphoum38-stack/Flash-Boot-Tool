import os

os.system("pyinstaller --onefile engine/flash_engine.py")
os.system("makensis installer/FlashForge.nsi")
