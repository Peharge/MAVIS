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

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\%USERNAME%\PycharmProjects\MAVIS\info\info-start-mavis-3-3-main.py
set SCRIPT_PATH_account=C:\Users\%USERNAME%\PycharmProjects\MAVIS\account\account.py
set SCRIPT_PATH_3=C:\Users\%USERNAME%\PycharmProjects\MAVIS\install\install-ollama-mavis-3-3-main.py
set PYTHON_SCRIPT_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run-browser\run-browser-one.py
set run_jup=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run-jup\run-jup.py
set run_grafana=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run-grafana\run-grafana.py
set run_solution=C:\Users\%USERNAME%\PycharmProjects\MAVIS\solution\run-solution-3.py
set SCRIPT_PATH_5=C:\Users\%USERNAME%\PycharmProjects\MAVIS\mavis-3-3-main-main.py

if not exist "%PYTHON_PATH%" (
    echo Error: Python interpreter not found: %PYTHON_PATH%
    exit /B 1
)

if not exist "%SCRIPT_PATH_1%" (
    echo Error: Script not found: %SCRIPT_PATH_1%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_1%"

if not exist "%SCRIPT_PATH_account%" (
    echo Error: Script not found: %SCRIPT_PATH_account%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_account%"

if not exist "%SCRIPT_PATH_3%" (
    echo Error: Script not found: %SCRIPT_PATH_3%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_3%"

if not exist "%PYTHON_SCRIPT_PATH%" (
    echo Error: Python script not found: %PYTHON_SCRIPT_PATH%
    exit /B 1
)

"%PYTHON_PATH%" "%PYTHON_SCRIPT_PATH%"

if not exist "%run_jup%" (
    echo Error: Python script not found: %run_jup%
    exit /B 1
)

REM Run the `run-jup.py` script in the background
start "" "%PYTHON_PATH%" "%run_jup%"

REM Wait for 5 seconds before continuing
timeout /t 5 /nobreak

if not exist "%run_grafana%" (
    echo Error: Python script not found: %run_grafana%
    exit /B 1
)

REM Run the `run-grafana.py` script in the background
start "" "%PYTHON_PATH%" "%run_grafana%"

REM Wait for 5 seconds before continuing
timeout /t 5 /nobreak

if not exist "%run_solution%" (
    echo Error: Python script not found: %run_solution%
    exit /B 1
)

REM Run the `run-solution.py` script in the background
start "" "%PYTHON_PATH%" "%run_solution%"

REM Wait for 5 seconds before continuing
timeout /t 5 /nobreak

if not exist "%SCRIPT_PATH_5%" (
    echo Error: Script not found: %SCRIPT_PATH_5%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_5%"

echo.
echo The scripts have been executed, Ollama has been started, and the browser has been opened.
echo Press any key to exit.
pause