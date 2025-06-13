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

# Farbcodes definieren (kleingeschrieben)
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

# Logging-Funktion für Fehler
def log_error(message):
    """Protokolliert Fehler in eine Datei."""
    try:
        with open("error_log.txt", "a") as log_file:
            log_file.write(message + "\n")
    except Exception as e:
        print(f"{red}Error while writing to log file: {e}{reset}")

def run_shell_file(shell_name):
    """Führt die Shell-Datei aus, überprüft, ob sie existiert, und gibt eine passende Fehlermeldung aus."""
    file_name = os.path.join(
        os.path.expanduser("~"),
        "PycharmProjects",
        "MAVIS",
        f"run-{shell_name}.sh"  # Die Dateiendung von .bat auf .sh geändert
    )

    # Prüft, ob die Datei existiert
    if not os.path.exists(file_name):
        error_message = f"{red}Error: The file '{file_name}' does not exist.{reset}"
        print(error_message)
        log_error(f"File not found: {file_name}")
        return

    # Versucht, die Shell-Datei auszuführen
    try:
        print(f"Executing file: {file_name}")
        os.system(f"bash {file_name}")  # Benutze 'bash' zum Ausführen der .sh Datei
        print(f"{green}The shell file '{file_name}' was executed successfully.{reset}")
    except Exception as e:
        error_message = f"{red}Error executing file '{file_name}': {e}{reset}"
        print(error_message)
        log_error(f"Execution failed for {file_name}: {e}")

def display_versions():
    """Zeigt alle Versionen und zugehörigen Shell-Dateien ohne 'run-' und '.sh'."""
    print(f"All MAVIS versions are available here:\n")

    versions = {
        "mavis-1-2-main": "MAVIS 1.2",
        "mavis-1-2-code": "MAVIS 1.2",
        "mavis-1-2-code-pro": "MAVIS 1.2",
        "mavis-1-2-math": "MAVIS 1.2",
        "mavis-1-2-math-pro": "MAVIS 1.2",
        "mavis-1-2-mini": "MAVIS 1.2",
        "mavis-1-2-mini-mini": "MAVIS 1.2",
        "mavis-1-2-3-main": "MAVIS 1.2-3",
        "mavis-1-2-3-math": "MAVIS 1.2-3",
        "mavis-1-2-3-math-pro": "MAVIS 1.2-3",
        "mavis-1-2-3-math-ultra": "MAVIS 1.2-3",
        "mavis-1-3-main": "MAVIS 1.3 EAP",
        "mavis-1-3_code": "MAVIS 1.3 EAP",
        "mavis-1-3_code-pro": "MAVIS 1.3 EAP",
        "mavis-1-3-math": "MAVIS 1.3 EAP",
        "mavis-1-3-math-pro": "MAVIS 1.3 EAP",
        "mavis-1-4-math": "MAVIS 1.4 EAP",
        "mavis-1-5-main": "MAVIS 1.5 EAP",
        "mavis-1-5-code": "MAVIS 1.5 EAP",
        "mavis-1-5-code-pro": "MAVIS 1.5 EAP",
        "mavis-1-5-math": "MAVIS 1.5 EAP",
        "mavis-1-5-math-pro": "MAVIS 1.5 EAP",
        "mavis-1-5-mini": "MAVIS 1.5 EAP",
        "mavis-1-5-mini-mini": "MAVIS 1.5 EAP"
    }

    # Gruppieren der Versionen für eine saubere Anzeige
    grouped_versions = {}
    for shell_name, version in versions.items():
        if version not in grouped_versions:
            grouped_versions[version] = []
        grouped_versions[version].append(shell_name)

    # Ausgabe der gruppierten Versionen
    for i, (version, shell_files) in enumerate(grouped_versions.items(), 1):
        print(f"{i}. {version}:")
        for j, shell_file in enumerate(shell_files, 1):
            print(f"   {j}. {shell_file}")
        print()

    return versions

def get_user_input(versions):
    """Fragt den Benutzer nach der gewünschten MAVIS-Shell-Datei und validiert die Eingabe."""
    while True:
        user_input = input(f"Enter a MAVIS shell file (e.g. 'mavis-1-2-main'): ").strip()

        # Validiert, ob die Eingabe korrekt ist
        if user_input in versions:
            run_shell_file(user_input)
            break
        else:
            print(f"{red}Error: '{user_input}' is not a valid option. Please try again.{reset}")

if __name__ == "__main__":
    try:
        versions = display_versions()
        get_user_input(versions)
    except Exception as e:
        print(f"{red}An unexpected error occurred: {e}{reset}")
        log_error(f"Unexpected error: {e}")
        sys.exit(1)
