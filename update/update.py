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

import subprocess
import requests
import sys
import os

# Farbcodes definieren
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"

# Die URL des GitHub-Repositories
repo_url = "https://github.com/Peharge/MAVIS.git"
repo_name = "MAVIS"


# Funktion, um die neuesten Commits von GitHub zu holen
def get_latest_commits():
    try:
        github_api_url = f"https://api.github.com/repos/Peharge/MAVIS/commits"
        response = requests.get(github_api_url)
        response.raise_for_status()  # Überprüft auf HTTP-Fehler

        commits = response.json()
        print(f"\n{cyan}Latest commits on GitHub: {reset}")
        for commit in commits[:5]:  # Zeige die letzten 5 Commits an
            print(
                f"{blue}Commit {commit['sha'][:7]}:{reset} {commit['commit']['message']} ({magenta}Autor: {commit['commit']['author']['name']}{reset})")
    except requests.exceptions.RequestException as e:
        print(f"{red}Error retrieving commits from GitHub: {e}{reset}")


# Funktion, um ein Git-Repository zu aktualisieren
def update_repo():
    try:
        print(f"\n{yellow}Start pull process...{reset}")
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"{green}Repository has been successfully updated!{reset}")
        else:
            print(f"{red}Error updating repository: {reset}")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"{red}Error running git pull: {e}{reset}")
    except Exception as e:
        print(f"{red}Unknown error updating repository: {e}{reset}")


# Funktion, um zu überprüfen, ob das Verzeichnis ein Git-Repository ist
def is_git_repo():
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        if "fatal: not a git repository" in result.stderr:
            return False
        return True
    except subprocess.CalledProcessError:
        return False


# Hauptprogramm
def main():
    print("\nRepository Information:\n-----------------------")
    # Sicherstellen, dass das Skript im richtigen Verzeichnis ausgeführt wird
    if not is_git_repo():
        print(f"{red}The current directory is not a Git repository!{reset}")
        sys.exit(1)

    # Überprüfen, ob ein Update verfügbar ist
    try:
        result = subprocess.run(["git", "fetch"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"{red}Error retrieving changes!{reset}")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"{red}Error running git fetch: {e}{reset}")
        sys.exit(1)

    # Überprüfen, ob Updates verfügbar sind
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "Your branch is up to date" in result.stdout:
        print(f"{green}The repository is already up to date.{reset}")
        sys.exit(0)

    # Frage, ob der Benutzer die neuesten Commits auf GitHub sehen möchte
    show_commits = input(f"\n{blue}Want to see the latest commits on GitHub? [y/n]: {reset}").strip().lower()
    if show_commits in ['y', 'yes']:
        get_latest_commits()

    # Frage, ob der Benutzer das Repository aktualisieren möchte
    update = input(f"\n{cyan}Do you want to update the repository now? [y/n]: {reset}").strip().lower()
    if update in ['y', 'yes']:
        update_repo()
    else:
        print(f"{yellow}Update canceled!{reset}")


if __name__ == "__main__":
    main()