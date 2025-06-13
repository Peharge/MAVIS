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
WSL Information Utility
-----------------------
This professional script gathers comprehensive information about the Windows Subsystem for Linux (WSL)
and the installed Linux distributions. It utilizes native WSL commands to retrieve details about the system
status and available distributions, while ensuring that any errors encountered during execution are handled appropriately.

Prerequisites:
    - Windows 10/11 with WSL installed.
    - The "wsl" command must be accessible in the system's PATH.
"""

import subprocess
import sys


def run_command(cmd: list[str]) -> tuple[str, str]:
    """
    Executes a system command and returns its output.

    Args:
        cmd (list[str]): The command to execute, specified as a list of strings.

    Returns:
        tuple[str, str]: A tuple (stdout, stderr). In case of an error, stderr contains the error message.
    """
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip(), ""
    except subprocess.CalledProcessError as e:
        return "", f"Error executing {' '.join(cmd)}: {e.stderr.strip()}"
    except FileNotFoundError:
        return "", f"Command not found: {cmd[0]}"


def get_wsl_status() -> str:
    """
    Retrieves the current WSL status.

    Returns:
        str: The output string from the command "wsl --status" or an error message if the command fails.
    """
    status, error = run_command(["wsl", "--status"])
    if error:
        return f"Error retrieving WSL status:\n{error}"
    return status


def get_installed_distros() -> str:
    """
    Retrieves the list of installed WSL Linux distributions in detailed mode.

    Returns:
        str: The output from the command "wsl --list --verbose" or an error message if the command fails.
    """
    distros, error = run_command(["wsl", "--list", "--verbose"])
    if error:
        return f"Error retrieving installed distributions:\n{error}"
    return distros


def print_section(title: str, content: str) -> None:
    """
    Prints a formatted section title along with the associated content.

    Args:
        title (str): The section title.
        content (str): The content to display under the title.
    """
    print(f"{title}\n{'-' * len(title)}")
    print(content)
    print()


def main() -> None:
    """
    Main function that prints the WSL status and the installed Linux distributions.
    """
    print_section("WSL Status", get_wsl_status())
    print_section("Installed Linux Distributions", get_installed_distros())


if __name__ == "__main__":
    main()
