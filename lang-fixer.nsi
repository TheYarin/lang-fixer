InstallDir "$PROGRAMFILES\lang-fixer"
Name "lang-fixer"

; Read version
FileOpen $VersionFile "version.txt" r
FileRead $VersionFile $VERSION ; Read until the end of line (including carriage return and new line) and save it to $VERSION
FileClose $VersionFile ; and close the file

outFile "lang-fixer-installer_v${VERSION}.exe"

Page directory
Page instfiles

Section "install"
    setOutPath $INSTDIR

    file -oname "lang-fixer.exe" ".\dist\lang-fixer.exe"
    file "settings.json"
    file "layout1.txt"
    file "layout2.txt"
    
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Run" "lang-fixer" "$INSTDIR\lang-fixer.exe"

    writeUninstaller "$INSTDIR\uninstall.exe"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "DisplayName" "lang-fixer"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "DisplayVersion" "$VERSION"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "InstallLocation" "$INSTDIR"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "Publisher" "TheYarin"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "HelpLink" "https://github.com/TheYarin/lang-fixer"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "Readme" "https://github.com/TheYarin/lang-fixer"
    writeRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "NoModify" 1
    writeRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "NoRepair" 1

     ${GetSize} "$INSTDIR" "/S=0K" $0 $1 $2
    IntFmt $0 "0x%08X" $0
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer" "EstimatedSize" "$0"
    
SectionEnd

function un.onInit
	SetShellVarContext all
 
	#Verify the uninstaller - last chance to back out
	MessageBox MB_OKCANCEL "Permanently remove lang-fixer?" IDOK next
		Abort
	next:
	!insertmacro VerifyUserIsAdmin
functionEnd

section "uninstall"
    Delete "$INSTDIR\lang-fixer.exe"

    MessageBox MB_YESNO "Would you like to delete even the settings and the keyboard layouts configured?" /SD IDYES lbl_delete_configs IDNO lbl_skip
    
    lbl_delete_configs:
    Delete $INSTDIR\settings.json
    Delete $INSTDIR\layout1.txt
    Delete $INSTDIR\layout2.txt

    lbl_skip:

    Delete $INSTDIR\uninstall.exe

    rmdir $INSTDIR

    DeleteRegValue HKLM "Software\Microsoft\Windows\CurrentVersion\Run" "lang-fixer"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\lang-fixer"
sectionEnd