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

:: ====================================================================
:: Configuration and Logging
:: ====================================================================
set "USERNAME=%USERNAME%"
set "PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe"
set "SCRIPT_INSTALL_RUSTUP=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run\rust\install-rustup.py"
set "LOGFILE=%TEMP%\rustup_install_log.txt"

(
    echo ========================================================
    echo [INFO] Starting Rustup installation script
    echo [INFO] User: %USERNAME%
    echo [INFO] Start time: %date% %time%
    echo ========================================================
) >> "%LOGFILE%"

:: ====================================================================
:: Check if Rustup is already installed
:: ====================================================================
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup is already installed.
    echo [INFO] Rustup already installed >> "%LOGFILE%"
    goto End
)

echo Rustup is not installed.
echo [INFO] Rustup not found >> "%LOGFILE%"

:: ====================================================================
:: User prompt to confirm installation
:: ====================================================================
set /p install_rustup="Would you like to install Rustup? [y/n]: "
if /i not "%install_rustup%"=="y" (
    echo Installation canceled. Please install Rustup manually: https://rustup.rs/
    echo [WARN] User canceled the installation >> "%LOGFILE%"
    goto End
)

:: ====================================================================
:: Function: Download file using PowerShell
:: ====================================================================
:DownloadFile
:: Parameter %1 = URL, %2 = Output file path
echo [INFO] Attempting to download: %1 >> "%LOGFILE%"
powershell -Command ^
   "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; " ^
   "Invoke-WebRequest -Uri '%~1' -OutFile '%~2'" 2>>"%LOGFILE%"
if exist "%~2" (
    echo [INFO] Download successful: %~2 >> "%LOGFILE%"
    exit /b 0
) else (
    echo [ERROR] Download failed: %~2 >> "%LOGFILE%"
    exit /b 2
)

:: ====================================================================
:: Attempt 1: Official installer from https://win.rustup.rs
:: ====================================================================
set "RUSTUP_URL=https://win.rustup.rs"
set "RUSTUP_INSTALLER=%TEMP%\rustup-init.exe"
echo [INFO] Attempt 1: Official installer >> "%LOGFILE%"
call :DownloadFile "%RUSTUP_URL%" "%RUSTUP_INSTALLER%"
if errorlevel 2 (
    echo [ERROR] Official download failed. Switching to alternative method.
    goto AlternativeDownload
)
echo [INFO] Running official installer >> "%LOGFILE%"
start /wait "%RUSTUP_INSTALLER%" -y
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed using the official installer!
    echo [INFO] Installation successful in Attempt 1 >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Official installer did not work.
    echo [ERROR] Attempt 1: Installer error >> "%LOGFILE%"
)

:: ====================================================================
:: Attempt 2: Retry official installer
:: ====================================================================
echo [INFO] Attempt 2: Retrying official installer >> "%LOGFILE%"
if exist "%RUSTUP_INSTALLER%" (
    del "%RUSTUP_INSTALLER%" >nul 2>&1
)
call :DownloadFile "%RUSTUP_URL%" "%RUSTUP_INSTALLER%"
if errorlevel 2 (
    echo [ERROR] Retry download failed. Switching to alternative method.
    goto AlternativeDownload
)
start /wait "%RUSTUP_INSTALLER%" -y
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed on the second attempt!
    echo [INFO] Installation successful in Attempt 2 >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Second attempt with official installer did not work.
    echo [ERROR] Attempt 2: Installer error >> "%LOGFILE%"
)

:: ====================================================================
:: Attempt 3: Alternative download method
:: ====================================================================
:AlternativeDownload
echo [INFO] Attempt 3: Alternative installer URL >> "%LOGFILE%"
set "RUSTUP_ALT_URL=https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe"
set "RUSTUP_INSTALLER=%TEMP%\rustup-alt.exe"
call :DownloadFile "%RUSTUP_ALT_URL%" "%RUSTUP_INSTALLER%"
if errorlevel 2 (
    echo [ERROR] Alternative download failed.
    goto PythonFallback
)
echo [INFO] Running alternative installer >> "%LOGFILE%"
start /wait "%RUSTUP_INSTALLER%" -y
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed using the alternative method!
    echo [INFO] Installation successful in Attempt 3 >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Alternative installation failed.
    echo [ERROR] Attempt 3: Alternative installer error >> "%LOGFILE%"
)

:: ====================================================================
:: Attempt 4: Fallback using Python installation script
:: ====================================================================
:PythonFallback
echo [INFO] Attempt 4: Python installation script fallback >> "%LOGFILE%"
if not exist "%SCRIPT_INSTALL_RUSTUP%" (
    echo ❌ Error: Python script not found: %SCRIPT_INSTALL_RUSTUP%
    echo [ERROR] Python script missing. >> "%LOGFILE%"
    echo Installation canceled. Please install Rustup manually: https://rustup.rs/
    goto End
)
echo [INFO] Running Python installation script >> "%LOGFILE%"
"%PYTHON_PATH%" "%SCRIPT_INSTALL_RUSTUP%"
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed using the Python script!
    echo [INFO] Installation successful via Python script >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Python script installation attempt failed.
    echo [ERROR] Python script did not work >> "%LOGFILE%"
    echo Installation canceled. Please install Rustup manually: https://rustup.rs/
    goto End
)

:: ====================================================================
:: Cleanup temporary files
:: ====================================================================
:Cleanup
echo [INFO] Cleaning up temporary files... >> "%LOGFILE%"
if exist "%RUSTUP_INSTALLER%" (
    del "%RUSTUP_INSTALLER%" >nul 2>&1
    echo [INFO] Temporary file %RUSTUP_INSTALLER% removed >> "%LOGFILE%"
)
echo [INFO] Installation script completed. >> "%LOGFILE%"

:: ====================================================================
:: End of script
:: ====================================================================
:End
echo [INFO] End of installation script.
echo [INFO] Logfile: %LOGFILE%
