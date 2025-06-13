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

#!/usr/bin/env python3
"""
3D Slicer Installer Script

This script downloads and installs 3D Slicer on a Linux machine.
By default, version 5.8.1 is installed. It will ask the user whether
to install the 5.9 EAP version instead.

Usage: Run with root privileges (e.g. sudo python3 install_3dslicer.py)
Options:
  --install_dir, -d  Specify an installation directory (default: /opt/3dslicer)

Author: Your Name
Date: 2025-04-11
License: MIT License
"""

import os
import sys
import argparse
import tarfile
import urllib.request
import shutil
import tempfile

# Default parameters
DEFAULT_VERSION = "5.8.1"
EAP_VERSION = "5.9-EAP"  # Version string for the EAP version; adjust if needed.
DEFAULT_INSTALL_DIR = "/opt/3dslicer"
PLATFORM = "linux-amd64"  # Adjust if using a different platform.
SYMLINK_PATH = "/usr/local/bin/slicer"

def check_root():
    """Ensure the script is run as root."""
    if os.geteuid() != 0:
        print("Error: This script must be run as root. Please re-run using sudo or as root.")
        sys.exit(1)

def prompt_eap_choice():
    """Ask the user whether they want to install the 5.9 EAP version."""
    choice = input("Do you want to install the 5.9 EAP version instead of the default 5.8.1? [y/N]: ").strip().lower()
    return choice in ['y', 'yes']

def construct_download_url(version):
    """
    Construct the download URL for the selected version.
    The URL is based on the typical naming conventions for 3D Slicer.
    """
    return f"https://download.slicer.org/bitstream/3DSlicer-{version}-{PLATFORM}.tar.gz"

def download_file(url, dest_path):
    """Download file from the given URL and save it to dest_path."""
    try:
        print(f"Downloading 3D Slicer from {url} ...")
        with urllib.request.urlopen(url) as response, open(dest_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Download successful.")
    except Exception as e:
        print(f"Error while downloading 3D Slicer: {e}")
        sys.exit(1)

def extract_tar_with_strip(source_tar, target_dir, strip_components=1):
    """
    Extract a tar.gz archive to target_dir, stripping the first 'strip_components'
    parts from each file path.
    """
    try:
        with tarfile.open(source_tar, "r:gz") as tar:
            members = tar.getmembers()
            for member in members:
                # Split the original name by "/" and remove the first 'strip_components' parts
                path_parts = member.name.split('/')
                if len(path_parts) <= strip_components:
                    continue
                member.name = os.path.join(*path_parts[strip_components:])
                tar.extract(member, target_dir)
        print("Extraction completed successfully.")
    except Exception as e:
        print(f"Error during extraction: {e}")
        sys.exit(1)

def create_symlink(executable_path, link_path):
    """Create a symbolic link pointing to executable_path at link_path."""
    try:
        # Remove the symlink or file if it exists
        if os.path.islink(link_path) or os.path.exists(link_path):
            os.remove(link_path)
        os.symlink(executable_path, link_path)
        print(f"Symbolic link created at {link_path}.")
    except Exception as e:
        print(f"Error creating symbolic link: {e}")
        sys.exit(1)

def main():
    # Check if running as root
    check_root()

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="3D Slicer Installer Script")
    parser.add_argument("--install_dir", "-d", type=str, default=DEFAULT_INSTALL_DIR,
                        help=f"Installation directory (default: {DEFAULT_INSTALL_DIR})")
    args = parser.parse_args()
    install_dir = args.install_dir

    # Determine which version to install (default or EAP)
    version = DEFAULT_VERSION
    if prompt_eap_choice():
        version = EAP_VERSION

    print("--------------------------------------------------")
    print("3D Slicer Installer")
    print(f"Version to install: {version}")
    print(f"Installation directory: {install_dir}")
    print("--------------------------------------------------")

    # Construct the download URL based on version and platform
    download_url = construct_download_url(version)
    print(f"Download URL: {download_url}")

    # Create the installation directory if it does not exist
    if not os.path.isdir(install_dir):
        try:
            print(f"Creating installation directory at {install_dir} ...")
            os.makedirs(install_dir)
        except Exception as e:
            print(f"Error creating installation directory: {e}")
            sys.exit(1)

    # Download the tarball to a temporary file
    tmp_tar = os.path.join(tempfile.gettempdir(), "3dslicer.tar.gz")
    download_file(download_url, tmp_tar)

    # Extract the tarball (stripping the top directory)
    extract_tar_with_strip(tmp_tar, install_dir, strip_components=1)

    # Check for the Slicer executable within the installation directory
    slicer_executable = os.path.join(install_dir, "Slicer")
    if not os.path.isfile(slicer_executable):
        print(f"Error: 3D Slicer executable was not found at {slicer_executable}.")
        sys.exit(1)

    # Create a symbolic link at SYMLINK_PATH so that Slicer can be started from anywhere.
    create_symlink(slicer_executable, SYMLINK_PATH)

    # Clean up the temporary tarball
    try:
        os.remove(tmp_tar)
    except Exception as e:
        print(f"Warning: Could not remove temporary file: {e}")

    print("--------------------------------------------------")
    print("Installation completed successfully!")
    print("You can start 3D Slicer by running the command: 'slicer'")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
