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
Installation script for PyCharm Professional 2025

This script downloads the appropriate installer for PyCharm Professional
based on the operating system in use and (optionally after manual confirmation)
initiates the installation process.

Note: For automatic installation, administrator/root privileges or
OS-specific commands may be required.
"""

import argparse
import logging
import os
import platform
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path
from urllib.parse import urlparse

import requests

# Configuration
PYCHARM_VERSION = "2025.1"
PRODUCT = "pycharm-professional"  # For Professional Edition. For Community Edition => "pycharm-community"

# URLs are fictional and should be updated in 2025!
DOWNLOAD_URLS = {
    "Windows": f"https://download.jetbrains.com/python/{PRODUCT}-{PYCHARM_VERSION}.exe",
    "Linux": f"https://download.jetbrains.com/python/{PRODUCT}-{PYCHARM_VERSION}.tar.gz",
    "Darwin": f"https://download.jetbrains.com/python/{PRODUCT}-{PYCHARM_VERSION}.dmg",
}

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

def get_download_url(os_name: str) -> str:
    if os_name not in DOWNLOAD_URLS:
        raise ValueError(f"Unsupported operating system: {os_name}")
    return DOWNLOAD_URLS[os_name]

def download_file(url: str, dest_path: Path) -> None:
    logging.info(f"Starting download from {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    chunk_size = 1024 * 1024  # 1 MB

    with dest_path.open("wb") as file:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:  # filter out keep-alive chunks
                file.write(chunk)
                downloaded += len(chunk)
                logging.info(f"Downloaded: {downloaded / (1024*1024):.2f} MB / {total_size / (1024*1024):.2f} MB")
    logging.info(f"Download completed: {dest_path}")

def extract_archive(archive_path: Path, extract_to: Path) -> None:
    logging.info(f"Extracting {archive_path} to {extract_to}")
    if archive_path.suffixes[-2:] == [".tar", ".gz"] or archive_path.suffix == ".tgz":
        with tarfile.open(archive_path, "r:gz") as tar:
            tar.extractall(path=extract_to)
    elif archive_path.suffix == ".zip":
        with zipfile.ZipFile(archive_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
    else:
        raise ValueError("Unknown archive format.")
    logging.info("Extraction completed.")

def run_installer(installer_path: Path) -> None:
    os_name = platform.system()
    logging.info(f"Launching installer: {installer_path}")
    try:
        if os_name == "Windows":
            subprocess.run([str(installer_path)], check=True)
        elif os_name == "Darwin":
            # On macOS, mounting the DMG image and moving it to /Applications may be required
            subprocess.run(["open", str(installer_path)], check=True)
        elif os_name == "Linux":
            # On Linux, it's often recommended to extract and run manually
            logging.info("For Linux: Please extract the archive and follow the installation instructions.")
        else:
            raise ValueError(f"No installation step defined for {os_name}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while running installer: {e}")
        sys.exit(1)

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="PyCharm Professional 2025 Installer")
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.cwd() / "downloads",
        help="Directory where the installer will be downloaded."
    )
    parser.add_argument(
        "--no-run",
        action="store_true",
        help="Only download, do not automatically install."
    )
    args = parser.parse_args()

    dest_dir: Path = args.dest
    dest_dir.mkdir(parents=True, exist_ok=True)

    os_name = platform.system()
    try:
        download_url = get_download_url(os_name)
    except ValueError as e:
        logging.error(e)
        sys.exit(1)

    filename = os.path.basename(urlparse(download_url).path)
    dest_file = dest_dir / filename

    try:
        download_file(download_url, dest_file)
    except Exception as e:
        logging.error(f"Download failed: {e}")
        sys.exit(1)

    if os_name == "Linux" and dest_file.suffix in [".tar.gz", ".tgz"]:
        # On Linux, we extract the archive
        extract_to = dest_dir / f"{PRODUCT}-{PYCHARM_VERSION}"
        extract_to.mkdir(exist_ok=True)
        try:
            extract_archive(dest_file, extract_to)
        except Exception as e:
            logging.error(f"Extraction failed: {e}")
            sys.exit(1)
        logging.info(f"PyCharm was extracted to: {extract_to}")

    if not args.no_run:
        run_installer(dest_file)
    else:
        logging.info("Automatic installation was disabled.")

if __name__ == "__main__":
    main()
