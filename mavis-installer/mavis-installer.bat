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

setlocal enabledelayedexpansion

:: Funktionen für die Installation
:install_git
where git >nul 2>nul
if %errorlevel%==0 (
    echo ✅ Git is already installed.
) else (
    echo 🔄 Installing Git...
    winget install --id Git.Git -e --source winget || (
        echo ❌ Git installation failed. Visit https://git-scm.com.
        exit /b 1
    )
)

:install_python
where python >nul 2>nul
if %errorlevel%==0 (
    echo ✅ Python is already installed.
) else (
    echo 🔄 Installing Python...
    winget install --id Python.Python.3 -e --source winget || (
        echo ❌ Python installation failed. Visit https://www.python.org.
        exit /b 1
    )
)

:install_ollama
where ollama >nul 2>nul
if %errorlevel%==0 (
    echo ✅ Ollama is already installed.
) else (
    echo 🔄 Installing Ollama...
    start https://ollama.com/download || (
        echo ❌ Ollama installation failed. Visit https://ollama.com/download.
        exit /b 1
    )
)

:create_folder
set folder=%USERPROFILE%\PycharmProjects
if not exist "%folder%" (
    mkdir "%folder%"
    echo ✅ Folder created: %folder%
) else (
    echo ℹ️ Folder already exists: %folder%
)

:clone_repository
set repo_url=https://github.com/Peharge/MAVIS
set target_path=%USERPROFILE%\PycharmProjects\MAVIS
if exist "%target_path%" (
    echo ℹ️ Repository has already been cloned.
) else (
    echo 🔄 Cloning repository...
    git clone %repo_url% %target_path% || (
        echo ❌ Repository could not be cloned.
        exit /b 1
    )
)

:create_virtual_environment
set env_path=%USERPROFILE%\PycharmProjects\MAVIS\env
if exist "%env_path%" (
    echo ℹ️ Virtual environment already exists.
) else (
    echo 🔄 Creating virtual environment...
    python -m venv "%env_path%" || (
        echo ❌ Virtual environment could not be created.
        exit /b 1
    )
)

:start_ui
set script_path=%USERPROFILE%\PycharmProjects\MAVIS\run-mavis-all.bat
if exist "%script_path%" (
    echo 🚀 Starting User Interface...
    call "%script_path%"
) else (
    echo ❌ User interface script not found.
    exit /b 1
)

:menu
cls
echo MAVIS Installer
echo =================
echo 1. Install prerequisites (Git, Python, Ollama)
echo 2. Create folder
echo 3. Clone repository
echo 4. Create virtual environment
echo 5. Start user interface
echo 6. Finish
echo =================
set /p choice=Select an option:
if "%choice%"=="1" call :install_git & call :install_python & call :install_ollama
if "%choice%"=="2" call :create_folder
if "%choice%"=="3" call :clone_repository
if "%choice%"=="4" call :create_virtual_environment
if "%choice%"=="5" call :start_ui
if "%choice%"=="6" exit /b 0
goto menu
