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
Installation script for the mavis-c-compiler environment.
Automatically sets up a build system for C projects using Visual Studio's cl.exe.
"""

import os
import sys
import subprocess
import traceback
import getpass
import platform
import shutil
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


def find_vcvarsall():
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
                logger.info("Found: vcvarsall.bat -> %s", path_found)
                return path_found
    return None


def write_logfile(target_dir, vcvarsall_path):
    try:
        with open(os.path.join(target_dir, "c_compiler_ready.txt"), "w", encoding="utf-8") as f:
            f.write("Visual Studio C Build Tools ready.\n")
            f.write(f"vcvarsall.bat path: {vcvarsall_path}\n")
        logger.info("Log file successfully written.")
    except Exception as e:
        logger.warning("Error writing log file: %s", e)


def verify_c_compiler(vcvarsall_path, temp_dir):
    logger.info("Performing C compiler test run...")
    test_c = os.path.join(temp_dir, "test.c")
    exe_output = os.path.join(temp_dir, "test.exe")

    try:
        with open(test_c, "w", encoding="utf-8") as f:
            f.write('#include <stdio.h>\nint main() { printf("Hello from cl.exe (C)!\\n"); return 0; }')
    except Exception as e:
        logger.error("Error creating test file: %s", e)
        return False

    bat_script = os.path.join(temp_dir, "compile_test_c.bat")
    try:
        with open(bat_script, "w", encoding="utf-8") as f:
            f.write(f'call "{vcvarsall_path}" x64 && cl.exe /TC "{test_c}" /Fe"{exe_output}"\n')
    except Exception as e:
        logger.error("Error creating batch script: %s", e)
        return False

    try:
        result = subprocess.run(
            ['cmd', '/c', bat_script],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='cp850',
            errors='replace',
            check=False
        )
        logger.info("Compiler output:\n%s", result.stdout)
    except Exception as e:
        logger.error("Error executing batch script: %s", e)
        return False

    if os.path.exists(exe_output):
        logger.info("C compilation successful. cl.exe is working.")
        return True
    else:
        logger.error("Compilation failed. Is Visual Studio installed and configured correctly?")
        return False


def create_c_compiler_folder(target_dir, vcvarsall_path):
    os.makedirs(target_dir, exist_ok=True)
    batch_file = os.path.join(target_dir, "build_mavis_c.bat")
    try:
        with open(batch_file, "w", encoding="utf-8") as f:
            f.write("@echo off\n")
            f.write(f'call "{vcvarsall_path}" x64\n')
            f.write("echo Visual Studio C compiler environment activated.\n")
            f.write('cd /d "%~dp0\\..\\..\\MAVIS_C"\n')
            f.write("echo Starting C compilation...\n")
            f.write('cl.exe /TC main.c /Fe:mavis_c.exe\n')
            f.write("pause\n")
        logger.info("Batch file for C compiler created: %s", batch_file)
    except Exception as e:
        logger.error("Error creating batch file: %s", e)


def main():
    try:
        if platform.system() != "Windows":
            raise EnvironmentError("This script is intended for Windows only (requires Visual Studio cl.exe).")

        username = getpass.getuser()
        project_root = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
        compiler_dir = os.path.join(project_root, "mavis-c-compiler")
        os.makedirs(compiler_dir, exist_ok=True)
        temp_dir = os.path.join(project_root, "vs_test_c")
        os.makedirs(temp_dir, exist_ok=True)

        logger.info("Project directory: %s", project_root)

        vcvarsall_path = find_vcvarsall()
        if not vcvarsall_path:
            raise FileNotFoundError("vcvarsall.bat not found. Make sure Visual Studio is properly installed.")

        if verify_c_compiler(vcvarsall_path, temp_dir):
            write_logfile(compiler_dir, vcvarsall_path)
            create_c_compiler_folder(compiler_dir, vcvarsall_path)
            logger.info("mavis-c-compiler successfully set up.")
        else:
            raise Exception("C compilation test failed.")

        shutil.rmtree(temp_dir, ignore_errors=True)
        logger.info("Temporary files removed.")

    except Exception as e:
        logger.error("An error occurred during setup:")
        logger.error(str(e))
        logger.error("Stacktrace:\n%s", traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
