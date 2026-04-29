Name "FlashForge Pro"
OutFile "FlashForgeProSetup.exe"
InstallDir "$PROGRAMFILES\FlashForge"

Section
  SetOutPath "$INSTDIR"
  File /r "..\dist\*"

  CreateShortcut "$DESKTOP\FlashForge.lnk" "$INSTDIR\FlashForge.exe"
SectionEnd
