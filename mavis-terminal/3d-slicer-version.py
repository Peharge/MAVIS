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
import shutil
import subprocess
import logging
import string
from ctypes import windll


def get_all_drives():
    """
    Returns a list of all drives on the system.
    """
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ":\\")
        bitmask >>= 1
    return drives


def search_entire_pc(filename):
    """
    Searches the entire PC for a specific file.
    """
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
    """
    Finds the 3D Slicer executable on the system.
    """
    # 1. Check the default installation path:
    try:
        username = os.getlogin()
    except Exception as e:
        logging.error(f"Unable to determine the username: {e}")
        return None

    default_path = rf"C:\Users\{username}\AppData\Local\slicer.org\Slicer 5.6.2\Slicer.exe"
    if os.path.isfile(default_path):
        logging.info(f"Found 3D Slicer at default location: {default_path}")
        return default_path

    # 2. Check if Slicer.exe is in the PATH.
    slicer_path = shutil.which("Slicer.exe")
    if slicer_path is None:
        slicer_path = shutil.which("slicer")
    if slicer_path:
        logging.info(f"Found 3D Slicer via PATH: {slicer_path}")
        return slicer_path

    # 3. Perform full PC search.
    logging.info("3D Slicer not found in default location or PATH. Starting full PC search. This may take a while...")
    slicer_path = search_entire_pc("Slicer.exe")
    return slicer_path


def get_slicer_version(slicer_executable):
    """
    Runs the Slicer executable to get the version and other details.
    """
    command = [slicer_executable, "--version"]
    logging.info(f"Executing command to get version: {command}")

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version_info = result.stdout.strip()
        print(f"3D Slicer Version Details:\n{version_info}")
    except subprocess.CalledProcessError as error:
        logging.error(f"Failed to get version details. Error: {error}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")


def main():
    """
    Main function to locate and display 3D Slicer version details.
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Ensure the script is executed on Windows
    if os.name != "nt":
        logging.error("This script is intended to run on Windows.")
        return

    # Locate the 3D Slicer executable
    slicer_executable = find_slicer_executable()
    if not slicer_executable:
        logging.error("Error: 3D Slicer executable (Slicer.exe) not found on your system.")
        logging.error("Please ensure that 3D Slicer is installed.")
        return

    logging.info(f"Using 3D Slicer executable at: {slicer_executable}")

    # Get 3D Slicer version details
    get_slicer_version(slicer_executable)


if __name__ == '__main__':
    main()