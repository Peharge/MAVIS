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
import json
import subprocess
from datetime import datetime

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

# Lokale JSON-Datei, in der das Datum gespeichert wird
DATA_FILE = os.path.join(os.path.dirname(__file__), "last_update.json")
# Pfad zum Batch-Skript
image_dir = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "update")
batch_file = os.path.join(image_dir, "update-mavis-repository.bat")
python_file = os.path.join(image_dir, "m-git.py")
python_env = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", ".env", "Scripts", "python.exe")

def read_last_update():
    """Liest das letzte gespeicherte Datum aus der JSON-Datei."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("last_update")
    return None


def write_last_update():
    """Speichert das aktuelle Datum in die JSON-Datei."""
    current_date = datetime.now().strftime("%d.%m.%Y")
    data = {"last_update": current_date}
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)
    return current_date


def prompt_for_update():
    """Fragt den Benutzer, ob ein Update durchgeführt werden soll."""
    while True:
        choice = input(f"Would you like to perform an update? For more information, type 'm help' or 'm git' [y/n]:").strip().lower()
        if choice in {"y", "yes"}:
            return True
        elif choice in {"n", "no"}:
            return False
        if choice == "m help":
            subprocess.run(f'"{python_env}" {python_file}', shell=True)
        elif choice == "m git":
            subprocess.run(f'"{python_env}" {python_file}', shell=True)
        else:
            print(f"{yellow}Invalid input. Please enter 'y', 'n' or 'help'.{reset}")


def perform_update():
    """Führt das Update durch, indem das Batch-Skript ausgeführt wird."""
    if os.path.exists(batch_file):
        print(f"{green}Start update...{reset}")
        subprocess.run(batch_file, shell=True)  # Führt das Skript aus
        print(f"{green}Update completed.{reset}")
        write_last_update()  # Aktualisiert das Datum auf heute
    else:
        print(f"{red}Batch file not found{reset}: {batch_file}")


def get_unpulled_commits():
    """Gibt die Anzahl der Commits zurück, die noch nicht gepullt wurden."""
    try:
        result = subprocess.run(
            ["git", "fetch", "--dry-run"],
            capture_output=True,
            text=True,
            cwd=image_dir
        )
        output = result.stdout
        if "From" in output:
            return output.count("commit")
        return 0
    except Exception as e:
        print(f"{red}Error checking for unpulled commits: {e}{reset}")
        return -1


def main():
    print("\nMAVIS Repository Update (experimental):")
    print("---------------------------------------")
    print("Please note that this update function is not yet 100% reliable and errors may occur. \nTherefore, we recommend using the git pull https://github.com/Peharge/MAVIS.git command instead. \nHowever, if this is not possible...\n")

    last_update = read_last_update()
    if last_update:
        print(f"{blue}MAVIS - Last update{reset}: {last_update}")
    else:
        print(f"{yellow}MAVIS - No update date found.{reset}")

    unpulled_commits = get_unpulled_commits()
    if unpulled_commits > 0:
        print(f"{magenta}There are {unpulled_commits} commits that have not been pulled yet.{reset}")
    elif unpulled_commits == 0:
        print(f"{green}Your local repository is up-to-date.{reset}")

    if prompt_for_update():
        perform_update()
    else:
        print(f"{blue}Update aborted.{reset}")

if __name__ == "__main__":
    main()
