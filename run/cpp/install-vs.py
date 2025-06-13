# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

# -*- coding: utf-8 -*-
"""
Installationsskript für die Visual Studio C++ Build Tools Umgebung.
Dieses Skript ermittelt das Projektverzeichnis (basierend auf dem aktuellen Benutzer) und
erstellt darin den Ordner "mavis-cpp-compier". In diesem Ordner wird nach erfolgreichem
Test der Visual Studio Umgebung (über vcvarsall.bat und cl.exe) ein Batch-Skript abgelegt,
das die Umgebung initialisiert und ein Beispiel-Kompilierungskommando ausführt.
"""

import os
import sys
import subprocess
import traceback
import getpass
import platform
import shutil
import logging

# Logging-Konfiguration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


def find_vcvarsall():
    """
    Sucht rekursiv nach der Datei 'vcvarsall.bat', die zur Initialisierung der Visual Studio
    Entwicklungsumgebung benötigt wird.

    Returns:
        str: Vollständiger Pfad zu 'vcvarsall.bat' oder None, wenn nicht gefunden.
    """
    possible_paths = [
        os.environ.get("VSINSTALLDIR", ""),
        os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Microsoft Visual Studio"),
        os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft Visual Studio"),
    ]
    for base in possible_paths:
        if not base or not os.path.exists(base):
            continue
        for root, dirs, files in os.walk(base):
            if "vcvarsall.bat" in files:
                path_found = os.path.join(root, "vcvarsall.bat")
                logger.info("Found vcvarsall.bat: %s", path_found)
                return path_found
    return None


def write_logfile(target_dir, vcvarsall_path):
    """
    Schreibt eine Log-Datei mit Informationen zur gefundenen Visual Studio Umgebung.

    Args:
        target_dir (str): Zielverzeichnis, in dem die Log-Datei abgelegt werden soll.
        vcvarsall_path (str): Pfad zur Datei 'vcvarsall.bat'.
    """
    log_file = os.path.join(target_dir, "compiler_installed.txt")
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("Visual Studio C++ Build Tools detected and ready.\n")
            f.write(f"vcvarsall.bat path: {vcvarsall_path}\n")
        logger.info("Installation status logged in: %s", log_file)
    except Exception as e:
        logger.warning("Log file could not be written: %s", e)


def verify_compiler(vcvarsall_path, temp_dir):
    """
    Erstellt eine temporäre Test-C++-Datei und kompiliert sie mit cl.exe, um sicherzustellen,
    dass die Visual Studio-Umgebung korrekt eingerichtet ist.

    Args:
        vcvarsall_path (str): Pfad zur Initialisierungsdatei der Visual Studio Umgebung.
        temp_dir (str): Temporäres Verzeichnis für den Kompilierungstest.

    Returns:
        bool: True, wenn der Test erfolgreich war, sonst False.
    """
    logger.info("Test compiler availability...")
    test_cpp = os.path.join(temp_dir, "test.cpp")
    exe_output = os.path.join(temp_dir, "test.exe")

    # Erstelle Test-CPP-Datei
    try:
        with open(test_cpp, "w", encoding="utf-8") as f:
            f.write("#include <iostream>\nint main() { std::cout << \"Hello from cl.exe!\" << std::endl; return 0; }")
    except Exception as e:
        logger.error("Error creating test file: %s", e)
        return False

    # Erstelle ein Batch-Skript zur Initialisierung der Umgebung und Kompilierung der Testdatei.
    bat_script = os.path.join(temp_dir, "compile_test.bat")
    try:
        with open(bat_script, "w", encoding="utf-8") as f:
            # "x64" ist hier als Ziel gesetzt; bei Bedarf anpassen (z.B. x86)
            f.write(f'"{vcvarsall_path}" x64 && cl.exe /EHsc "{test_cpp}" /Fe"{exe_output}"\n')
    except Exception as e:
        logger.error("Error creating batch script: %s", e)
        return False

    try:
        result = subprocess.run(
            ['cmd', '/c', bat_script],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='cp850',  # Windows-Konsolen-Encoding
            errors='replace',
            check=False
        )
        logger.info("Output of the compilation test:\n%s", result.stdout)
    except Exception as e:
        logger.error("Error running compilation test: %s", e)
        return False

    if os.path.exists(exe_output):
        logger.info("Compilation successful. cl.exe works perfectly.")
        return True
    else:
        logger.error(
            "Compilation failed. Please ensure that Visual Studio C++ Build Tools are correctly installed.")
        return False


def create_compiler_folder(target_dir, vcvarsall_path):
    """
    Erstellt im angegebenen Zielverzeichnis ('mavis-cpp-compier') eine Batch-Datei, die
    die Visual Studio Umgebung initialisiert und ein Beispiel-Kompilierungskommando ausführt.

    Args:
        target_dir (str): Das Verzeichnis, in dem der "Compiler" abgelegt werden soll.
        vcvarsall_path (str): Pfad zur Datei 'vcvarsall.bat'.
    """
    # Erstelle den Ordner falls nicht existent (target_dir sollte z. B. "mavis-cpp-compier" sein)
    os.makedirs(target_dir, exist_ok=True)

    batch_file = os.path.join(target_dir, "build_mavis.bat")
    try:
        with open(batch_file, "w", encoding="utf-8") as f:
            f.write("@echo off\n")
            f.write(f'call "{vcvarsall_path}" x64\n')
            f.write("echo Visual Studio Compiler Environment enabled.\n")
            # Beispiel: Wechsle in das Projektverzeichnis und kompiliere ein bestimmtes Quellfile.
            f.write('cd /d "%~dp0\\..\\..\\MAVIS"\n')
            f.write("echo Start compiling the MAVIS project...\n")
            # Platzhalter: Passe den cl.exe Aufruf an deine Projektstruktur an
            f.write('cl.exe /EHsc main.cpp /Fe:mavis_project.exe\n')
            f.write("pause\n")
        logger.info("Batch file created for the compiler: %s", batch_file)
    except Exception as e:
        logger.error("Error creating compiler batch file: %s", e)


def main():
    """
    Hauptfunktion, die den Ablauf steuert:
      - Ermitteln des Projektverzeichnisses.
      - Suchen der Visual Studio Umgebung.
      - Testen des Compilers.
      - Erstellen des speziellen Ordners 'mavis-cpp-compier' mit einer Batch-Datei,
        die zum Kompilieren des MAVIS-Projektes verwendet werden kann.
      - Schreiben einer Log-Datei im Zielordner.
    """
    try:
        if platform.system() != "Windows":
            raise EnvironmentError("This installation script is intended for Windows only.")

        username = getpass.getuser()
        project_root = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
        # Der Zielordner für den "Compiler" wird hier angelegt:
        compiler_dir = os.path.join(project_root, "mavis-cpp-compier")
        os.makedirs(compiler_dir, exist_ok=True)
        logger.info("Project directory: %s", project_root)

        # Temporäres Verzeichnis für den Kompilierungstest
        temp_dir = os.path.join(project_root, "vs_test")
        os.makedirs(temp_dir, exist_ok=True)

        logger.info("Search for the Visual Studio C++ development environment...")
        vcvarsall_path = find_vcvarsall()
        if not vcvarsall_path:
            raise FileNotFoundError("Visual Studio environment could not be found."
                                    "Please make sure that Visual Studio with the C++ Build Tools is installed.")

        # Teste den Compiler (cl.exe)
        if verify_compiler(vcvarsall_path, temp_dir):
            write_logfile(compiler_dir, vcvarsall_path)
            create_compiler_folder(compiler_dir, vcvarsall_path)
            logger.info("Visual Studio C++ Build Tools successfully detected and tested.")
        else:
            raise Exception("The compilation test failed.")

        # Aufräumen: Entferne das temporäre Verzeichnis
        shutil.rmtree(temp_dir, ignore_errors=True)
        logger.info("Temporary files have been removed.")

    except Exception as e:
        logger.error("An error occurred during installation:")
        logger.error(str(e))
        logger.error("Stacktrace:\n%s", traceback.format_exc())
        logger.error("Please make sure that Visual Studio is installed with the required C++ components.")
        sys.exit(1)


if __name__ == "__main__":
    main()
