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
This script installs Debian for WSL on Windows.
It performs the following steps:
  1. Checks if the script is running on Windows and with administrator privileges.
  2. Enables the necessary Windows features:
       - Microsoft-Windows-Subsystem-Linux
       - VirtualMachinePlatform
  3. Sets WSL 2 as the default version.
  4. Downloads the Debian Rootfs (as a tarball) if not already present and imports it into WSL.

Important:
  - The script MUST be run as Administrator.
  - A system restart may be required for all changes to take effect.
  - After installation, you can start Debian with "wsl -d Debian".
"""

import os
import sys
import subprocess
import logging
import traceback
import platform
import ctypes
import urllib.request


def is_admin():
    """
    Checks if the script was started with administrator privileges.

    Returns:
        bool: True if administrator privileges are present.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        logging.error("Error checking administrator privileges: %s", e)
        return False


def run_command(command, shell=False):
    """
    Executes a command and returns the output.

    Args:
        command (list or str): The command to execute.
        shell (bool): If True, the command is run via the shell.

    Returns:
        subprocess.CompletedProcess: The result of the command execution.

    Raises:
        subprocess.CalledProcessError: If the command fails.
    """
    cmd_str = " ".join(command) if isinstance(command, list) else command
    logging.info("Executing: %s", cmd_str)
    try:
        result = subprocess.run(
            command,
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        if result.stdout:
            logging.info("Output:\n%s", result.stdout)
        if result.stderr:
            logging.error("Error message:\n%s", result.stderr)
        return result
    except subprocess.CalledProcessError as e:
        logging.error("Command failed: %s", cmd_str)
        logging.error("Error output:\n%s", e.stderr)
        raise


def enable_wsl_features():
    """
    Enables the Windows features for WSL and VirtualMachinePlatform.
    """
    commands = [
        ["dism.exe", "/online", "/enable-feature", "/featurename:Microsoft-Windows-Subsystem-Linux", "/all",
         "/norestart"],
        ["dism.exe", "/online", "/enable-feature", "/featurename:VirtualMachinePlatform", "/all", "/norestart"],
        # Optional: If Hyper-V is needed, the following line can be enabled:
        # ["dism.exe", "/online", "/enable-feature", "/featurename:Microsoft-Hyper-V", "/all", "/norestart"],
    ]
    for cmd in commands:
        run_command(cmd)


def set_default_wsl_version():
    """
    Sets WSL 2 as the default version.
    """
    run_command(["wsl", "--set-default-version", "2"])


def download_file(url, dest):
    """
    Downloads a file from the specified URL and saves it to the destination path.

    Args:
        url (str): The URL of the file.
        dest (str): The path where the file should be saved.
    """
    logging.info("Downloading %s to %s", url, dest)
    try:
        urllib.request.urlretrieve(url, dest)
        logging.info("Download completed.")
    except Exception as e:
        logging.error("Error during download: %s", e)
        raise


def install_debian():
    """
    Installs Debian in WSL.

    Procedure:
      1. Checks if the Debian tarball already exists. If not, it will be downloaded.
      2. Sets the installation directory.
      3. Imports Debian into WSL using "wsl --import".
    """
    # URL of the Debian Rootfs tarball (placeholder – please adjust if needed)
    tarball_url = "https://github.com/mbb1987/wsl-debian/releases/latest/download/Debian.tar"
    tarball_file = os.path.join(os.getcwd(), "Debian.tar")

    # Download if the file doesn't already exist
    if not os.path.exists(tarball_file):
        download_file(tarball_url, tarball_file)
    else:
        logging.info("Tarball already exists: %s", tarball_file)

    # Set the installation directory (default: %LOCALAPPDATA%\Packages\Debian)
    install_dir = os.path.join(os.environ["LOCALAPPDATA"], "Packages", "Debian")
    os.makedirs(install_dir, exist_ok=True)

    # Import Debian into WSL
    run_command(["wsl", "--import", "Debian", install_dir, tarball_file, "--version", "2"])


def main():
    # Logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Starting Debian installation for WSL...")

    # Check if the operating system is Windows
    if platform.system() != "Windows":
        logging.error("This script is intended only for Windows.")
        sys.exit(1)

    # Check if administrator privileges are available
    if not is_admin():
        logging.error("The script must be run as Administrator. Please run with elevated privileges.")
        sys.exit(1)

    try:
        # Enable the required Windows features (WSL, VirtualMachinePlatform)
        enable_wsl_features()

        # Set WSL 2 as the default version
        set_default_wsl_version()

        # Start the installation of Debian
        install_debian()

        logging.info(
            "The Debian installation has started. A restart may be required for all changes to take effect.")
        logging.info("Start Debian in the future with 'wsl -d Debian'.")
    except Exception as e:
        logging.error("An error occurred during the installation:")
        logging.error(str(e))
        logging.error(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
