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

setlocal EnableDelayedExpansion

:: Variablen definieren
set PYTHON_VERSION=3.12.10
set PYTHON_EXECUTABLE=py -3.12
set PYTHON_INSTALLER_PATH=%USERPROFILE%\Downloads
set INSTALLER_NAME=python-!PYTHON_VERSION!-amd64.exe
set INSTALLER_URL=https://www.python.org/ftp/python/!PYTHON_VERSION!/!INSTALLER_NAME!
set LOG_DIR=%USERPROFILE%\Desktop\Python_Install_Logs
set LOG_FILE=!LOG_DIR!\python_install_!PYTHON_VERSION!.log

:: Icons für visuelles Feedback
set CHECK_MARK=✅
set CROSS_MARK=❌

:: Überprüfen, ob Python 3.12 bereits installiert ist
%PYTHON_EXECUTABLE% -c "import sys; version = sys.version.split()[0]; assert version.startswith('%PYTHON_VERSION%')" >nul 2>&1
if not errorlevel 1 (
    echo !CHECK_MARK! Python !PYTHON_VERSION! ist bereits auf Ihrem System installiert.
    pause
    goto end
)

:: Benutzer zur Installation auffordern
:prompt_user
set /p USER_INPUT=Möchten Sie Python !PYTHON_VERSION! installieren? [y/n]:
if /i "!USER_INPUT!"=="Y" goto proceed_installation
if /i "!USER_INPUT!"=="N" goto end
echo Ungültige Eingabe. Bitte geben Sie Y oder N ein.
goto prompt_user

:: Installation ausführen
:proceed_installation

:: Sicherstellen, dass das Log-Verzeichnis existiert
if not exist "!LOG_DIR!" (
    echo Erstelle Log-Verzeichnis...
    mkdir "!LOG_DIR!"
    if errorlevel 1 (
        echo !CROSS_MARK! Fehler: Log-Verzeichnis "!LOG_DIR!" konnte nicht erstellt werden. Überprüfen Sie Ihre Berechtigungen.
        pause
        goto end
    )
)

:: Ausgabe in Konsole und Log-Datei
echo %DATE% %TIME%: Beginne mit dem Download von Python !PYTHON_VERSION! >> "!LOG_FILE!"
echo Starte Download von Python !PYTHON_VERSION!...

:: Python-Installer mit PowerShell herunterladen
powershell -Command "Invoke-WebRequest -Uri '!INSTALLER_URL!' -OutFile '!PYTHON_INSTALLER_PATH!\!INSTALLER_NAME!'" >> "!LOG_FILE!" 2>&1
if errorlevel 1 (
    echo !CROSS_MARK! Download fehlgeschlagen. Details finden Sie im Log unter "!LOG_FILE!".
    pause
    goto end
)

:: Installation starten
echo %DATE% %TIME%: Starte Installation von Python !PYTHON_VERSION! >> "!LOG_FILE!"
echo Starte Installation von Python !PYTHON_VERSION!...

"!PYTHON_INSTALLER_PATH!\!INSTALLER_NAME!" /passive InstallAllUsers=1 PrependPath=1 Include_test=0 >> "!LOG_FILE!" 2>&1
if errorlevel 1 (
    echo !CROSS_MARK! Installation fehlgeschlagen. Details finden Sie im Log unter "!LOG_FILE!".
    pause
    goto end
)

:: Python-Installation verifizieren
echo Überprüfe Python-Installation...
%PYTHON_EXECUTABLE% -c "import sys; print('Python version:', sys.version)" >> "!LOG_FILE!" 2>&1
if errorlevel 1 (
    echo !CROSS_MARK! Verifikation fehlgeschlagen. Python !PYTHON_VERSION! wurde möglicherweise nicht korrekt installiert.
    pause
    goto end
)

:: Installationsdateien aufräumen
echo Bereinige Installationsdateien...
del /f /q "!PYTHON_INSTALLER_PATH!\!INSTALLER_NAME!" >> "!LOG_FILE!" 2>&1

:: Abschließende Meldung
echo !CHECK_MARK! Python !PYTHON_VERSION! wurde erfolgreich installiert und verifiziert.
echo %DATE% %TIME%: Python !PYTHON_VERSION! wurde erfolgreich installiert und verifiziert. >> "!LOG_FILE!"
echo Installation abgeschlossen. Drücken Sie eine beliebige Taste zum Beenden.
pause

:end
endlocal
