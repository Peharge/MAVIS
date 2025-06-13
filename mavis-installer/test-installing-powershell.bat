@echo off

REM Englisch Peharge: This source code is released under the MIT License.
REM
REM Usage Rights:
REM The source code may be copied, modified, and adapted to individual requirements.
REM Users are permitted to use this code in their own projects, both for private and commercial purposes.
REM However, it is recommended to modify the code only if you have sufficient programming knowledge,
REM as changes could cause unintended errors or security risks.
REM
REM Dependencies and Additional Frameworks:
REM The code relies on the use of various frameworks and executes additional files.
REM Some of these files may automatically install further dependencies required for functionality.
REM It is strongly recommended to perform installation and configuration in an isolated environment
REM (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
REM
REM Disclaimer:
REM Use of the code is entirely at your own risk.
REM Peharge assumes no liability for damages, data loss, system errors, or other issues
REM that may arise directly or indirectly from the use, modification, or redistribution of the code.
REM
REM Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

REM Deutsch Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
REM
REM Nutzungsrechte:
REM Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
REM Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
REM Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
REM da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
REM
REM Abhängigkeiten und zusätzliche Frameworks:
REM Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
REM Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
REM Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
REM um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
REM
REM Haftungsausschluss:
REM Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
REM Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
REM die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
REM
REM Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

REM Français Peharge: Ce code source est publié sous la licence MIT.
REM
REM Droits d'utilisation:
REM Le code source peut être copié, édité et adapté aux besoins individuels.
REM Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
REM Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
REM car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
REM
REM Dépendances et frameworks supplémentaires:
REM Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
REM Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
REM Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
REM pour éviter d'éventuels conflits avec les installations de logiciels existantes.
REM
REM Clause de non-responsabilité:
REM L'utilisation du code est entièrement à vos propres risques.
REM Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
REM pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
REM
REM Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

setlocal EnableExtensions EnableDelayedExpansion

REM ============================================================
REM Secure batch script to install PowerShell 7
REM Installs PowerShell in C:\Users\%USERNAME%\PycharmProjects\MAVIS\
REM ============================================================

REM Set target path
set "INSTALL_DIR=C:\Users\%USERNAME%\PycharmProjects\MAVIS\PowerShell"
set "ZIP_FILE=C:\Users\%USERNAME%\PycharmProjects\MAVIS\PowerShell.zip"

REM Check if the installation directory exists
if exist "%INSTALL_DIR%" (
    echo ✅ PowerShell directory already exists: %INSTALL_DIR%
) else (
    echo ❌ PowerShell directory not found. Creating PowerShell directory...
    mkdir "%INSTALL_DIR%"
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ Error creating PowerShell directory. Script will terminate.
        exit /b 1
    )
    echo ✅ PowerShell directory successfully created: %INSTALL_DIR%
)

REM Check if the ZIP file exists
if exist "%ZIP_FILE%" (
    echo ✅ PowerShell.zip found. Skipping download.
) else (
    echo ❌ PowerShell.zip not found. Starting download...

    REM Check processor architecture
    reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" >nul && set OS=32BIT || set OS=64BIT

    REM Download the appropriate version of PowerShell
    if "%OS%"=="32BIT" (
        echo ❌ Downloading 32-bit version of PowerShell...
        c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command ^
        "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; `
        $release = Invoke-RestMethod -Uri 'https://api.github.com/repos/PowerShell/PowerShell/releases/latest'; `
        $url = ($release.assets | Where-Object { $_.name -like '*win-x86.zip' }).browser_download_url; `
        Invoke-WebRequest -Uri $url -OutFile '%ZIP_FILE%'"
    )
    if "%OS%"=="64BIT" (
        echo ❌ Downloading 64-bit version of PowerShell...
        c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command ^
        "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; `
        $release = Invoke-RestMethod -Uri 'https://api.github.com/repos/PowerShell/PowerShell/releases/latest'; `
        $url = ($release.assets | Where-Object { $_.name -like '*win-x64.zip' }).browser_download_url; `
        Invoke-WebRequest -Uri $url -OutFile '%ZIP_FILE%'"
    )
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ Error downloading PowerShell.zip. Script will terminate.
        exit /b 1
    )
    echo ✅ PowerShell.zip successfully downloaded: %ZIP_FILE%
)

REM Check if PowerShell has already been extracted
if exist "%INSTALL_DIR%\pwsh.exe" (
    echo ✅ PowerShell already extracted: %INSTALL_DIR%
) else (
    echo ❌ Starting extraction of PowerShell.zip to %INSTALL_DIR%...

    REM Extract contents of PowerShell.zip
    c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command ^
    "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; `
    Add-Type -AssemblyName System.IO.Compression.FileSystem; `
    [System.IO.Compression.ZipFile]::ExtractToDirectory('%ZIP_FILE%', '%INSTALL_DIR%')"
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ Error extracting PowerShell.zip. Script will terminate.
        exit /b 1
    )
    echo ✅ PowerShell.zip successfully extracted to %INSTALL_DIR%.
)

REM Installation complete
echo ✅ PowerShell setup completed. Installed at: %INSTALL_DIR%
exit /b 0
