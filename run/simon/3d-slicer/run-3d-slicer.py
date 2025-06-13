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

import os
import sys
import shutil
import subprocess
import logging
import argparse
import string
from ctypes import windll


def get_all_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ":\\")
        bitmask >>= 1
    return drives


def search_entire_pc(filename):
    drives = get_all_drives()
    logging.info(f"Searching for {filename} on all drives: {drives}")
    for drive in drives:
        for root, dirs, files in os.walk(drive, topdown=True):
            if filename in files:
                found_path = os.path.join(root, filename)
                logging.info(f"Found {filename} at {found_path}")
                return found_path
    return None


def find_slicer_executable():
    # 1. Check the default installation path:
    try:
        username = os.getlogin()
    except Exception as e:
        logging.error(f"Unable to determine the username: {e}")
        sys.exit(1)

    default_path = rf"C:\Users\{username}\AppData\Local\slicer.org\Slicer 5.6.2\Slicer.exe"
    if os.path.isfile(default_path):
        logging.info(f"Found 3D Slicer at default location: {default_path}")
        return default_path

    # 2. Check if Slicer.exe is in the PATH.
    slicer_path = shutil.which("slicer.exe")
    if slicer_path is None:
        slicer_path = shutil.which("slicer")
    if slicer_path:
        logging.info(f"Found 3D Slicer via PATH: {slicer_path}")
        return slicer_path

    # 3. Perform full PC search.
    logging.info("3D Slicer not found in default location or PATH. Starting full PC search. This may take a while...")
    slicer_path = search_entire_pc("Slicer.exe")
    return slicer_path


def launch_slicer(slicer_executable, slicer_args):
    command = [slicer_executable] + slicer_args
    logging.info(f"Launching 3D Slicer with command: {command}")

    try:
        subprocess.run(command, check=True)
    except subprocess.TimeoutExpired:
        logging.error("Error: 3D Slicer launch timed out.")
        sys.exit(1)
    except subprocess.CalledProcessError as error:
        logging.error(f"Error: 3D Slicer exited with an error.\nDetails: {error}")
        sys.exit(1)
    except KeyboardInterrupt:
        logging.info("Execution interrupted by the user.")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        sys.exit(1)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Launcher script for 3D Slicer on Windows. "
                    "Attempts to run Slicer from the default location first, then searches the entire PC if not found."
    )
    parser.add_argument(
        "slicer_args",
        nargs=argparse.REMAINDER,
        help="Optional arguments to pass directly to 3D Slicer."
    )
    return parser.parse_args()


def main():
    # Configure logging with timestamped messages.
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Ensure the script is executed on Windows.
    if os.name != "nt":
        logging.error("This launcher script is intended to run on Windows.")
        sys.exit(1)

    # Parse command-line arguments.
    args = parse_arguments()

    # Locate the 3D Slicer executable.
    slicer_executable = find_slicer_executable()
    if not slicer_executable:
        logging.error("Error: 3D Slicer executable (Slicer.exe) not found on your system.")
        logging.error("Please ensure that 3D Slicer is installed.")
        sys.exit(1)

    logging.info(f"Using 3D Slicer executable at: {slicer_executable}")

    # Launch 3D Slicer with any provided additional arguments.
    launch_slicer(slicer_executable, args.slicer_args)


if __name__ == '__main__':
    main()
