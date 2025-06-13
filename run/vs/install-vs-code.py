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

"""
Professional VS Code Installer Script (2025 Edition)

This script automatically downloads the appropriate installer for Visual Studio Code
based on the detected operating system and attempts to run the installer.
It supports Windows, macOS, and Linux (via a deb/rpm download extraction method).

Requirements:
- Python 3.8+
- The 'requests' module (install with pip install requests)
- Administrator/Root privileges might be needed for an unattended install.

Note: For Linux, the script downloads the .deb or .rpm package based on the distro.
For macOS, it downloads the .dmg file and opens it.
For Windows, it downloads the system installer (.exe) and launches it.
"""

import argparse
import logging
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests

# Configuration for VS Code version 2025.1. Adjust base URLs as necessary.
VSCODE_VERSION = "2025.1"
DOWNLOAD_URLS = {
    "Windows": f"https://update.code.visualstudio.com/{VSCODE_VERSION}/win32-x64/stable",
    "Darwin": f"https://update.code.visualstudio.com/{VSCODE_VERSION}/darwin/stable",
    # For Linux we decide based on distro later; here's the .deb file as default.
    "Linux_deb": f"https://update.code.visualstudio.com/{VSCODE_VERSION}/linux-deb-x64/stable",
    "Linux_rpm": f"https://update.code.visualstudio.com/{VSCODE_VERSION}/linux-rpm-x64/stable",
}

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def get_download_url() -> (str, str):
    os_name = platform.system()
    if os_name == "Windows":
        return DOWNLOAD_URLS["Windows"], ".exe"
    elif os_name == "Darwin":
        return DOWNLOAD_URLS["Darwin"], ".dmg"
    elif os_name == "Linux":
        # For Linux, detect package manager if possible.
        # You might want to improve detection for specific distributions.
        if shutil.which("dpkg"):
            return DOWNLOAD_URLS["Linux_deb"], ".deb"
        elif shutil.which("rpm"):
            return DOWNLOAD_URLS["Linux_rpm"], ".rpm"
        else:
            logging.error("Unsupported Linux package system. Ensure dpkg or rpm is installed.")
            sys.exit(1)
    else:
        logging.error(f"Unsupported operating system: {os_name}")
        sys.exit(1)

def download_file(url: str, dest_path: Path):
    logging.info(f"Starting download from {url} ...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    chunk_size = 1024 * 1024  # 1 MB chunks

    with dest_path.open("wb") as file:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                downloaded += len(chunk)
                percent = downloaded / total_size * 100 if total_size else 0
                logging.info(f"Downloaded {downloaded / (1024*1024):.2f} MB of {total_size / (1024*1024):.2f} MB ({percent:.1f}%)")
    logging.info(f"Download completed: {dest_path}")

def run_installer(installer_path: Path):
    os_name = platform.system()
    logging.info(f"Launching installer: {installer_path}")
    try:
        if os_name == "Windows":
            # For Windows, use os.startfile if available
            os.startfile(str(installer_path))
        elif os_name == "Darwin":
            # On macOS, open the DMG file, user must then drag VS Code to Applications.
            subprocess.run(["open", str(installer_path)], check=True)
        elif os_name == "Linux":
            # For Linux, use appropriate package manager commands.
            # This assumes the user has privileges to install packages.
            if installer_path.suffix == ".deb":
                subprocess.run(["sudo", "dpkg", "-i", str(installer_path)], check=True)
            elif installer_path.suffix == ".rpm":
                subprocess.run(["sudo", "rpm", "-i", str(installer_path)], check=True)
            else:
                logging.error("Unknown installer format for Linux.")
                sys.exit(1)
        else:
            logging.error("Installation method not defined for this OS.")
            sys.exit(1)
    except subprocess.CalledProcessError as err:
        logging.error(f"Error during installation: {err}")
        sys.exit(1)

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="VS Code Installer 2025")
    parser.add_argument("--dest", type=Path, default=Path.cwd() / "vscode_downloads",
                        help="Directory to download the VS Code installer")
    parser.add_argument("--no-run", action="store_true",
                        help="Download the installer only without executing it")
    args = parser.parse_args()

    dest_dir = args.dest
    dest_dir.mkdir(parents=True, exist_ok=True)

    download_url, file_ext = get_download_url()
    filename = f"vscode-{VSCODE_VERSION}{file_ext}"
    dest_file = dest_dir / filename

    try:
        download_file(download_url, dest_file)
    except Exception as e:
        logging.error(f"Failed to download file: {e}")
        sys.exit(1)

    if args.no_run:
        logging.info("Installer execution was disabled by the user (--no-run).")
    else:
        run_installer(dest_file)

if __name__ == "__main__":
    main()