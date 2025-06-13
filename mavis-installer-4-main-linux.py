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
import platform
import subprocess
import time
import sys
import shutil

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

def find_ollama_executable():
    """
    Attempts to find the path to the Ollama executable.
    Searches PATH first, then common directories.
    """
    # Check system PATH
    ollama_path = shutil.which("ollama")
    if ollama_path and os.path.isfile(ollama_path):
        return ollama_path

    # Try common install locations
    possible_paths = [
        "/usr/local/bin/ollama",
        "/usr/bin/ollama",
        "/opt/ollama/ollama",
        os.path.expanduser("~/.ollama/bin/ollama"),
    ]

    for path in possible_paths:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path

    raise FileNotFoundError("Could not find 'ollama'. Please ensure it's installed and in your PATH.")

def check_ollama_update():
    """
    Checks if an update is available for Ollama by prompting the user directly,
    since no CLI command currently provides the local version.
    """
    try:
        ollama_path = find_ollama_executable()

        remote_version = subprocess.run(
            ["curl", "-s", "https://api.ollama.ai/version"],
            stdout=subprocess.PIPE, text=True
        ).stdout.strip()

        print(f"{yellow}Latest available Ollama version: {remote_version}{reset}")
        print(f"{blue}Note: The current installed version could not be determined automatically.{reset}")

        while True:
            user_input = input("Would you like to run 'ollama update' to upgrade? [y/n]:").strip().lower()
            if user_input in ["y", "yes"]:
                subprocess.run([ollama_path, "update"], check=True)
                print(f"{green}Ollama was updated successfully. Please restart the script.{reset}")
                exit()
            elif user_input in ["n", "no"]:
                print("Skipping update.")
                break
            else:
                print(f"{red}Invalid input. Please enter 'y' or 'n'.{reset}")

    except Exception as e:
        print(f"{red}Error checking for updates: {e}{reset}")

def check_installed_model(model_name):
    """
    Checks if a specific model is installed in Ollama.
    :param model_name: Name of the model to check (e.g. "phi4").
    :return: True if installed, False otherwise.
    """
    try:
        ollama_path = find_ollama_executable()
        result = subprocess.run([ollama_path, "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"{red}Error fetching model list: {result.stderr}{reset}")
            return False

        return model_name.lower() in result.stdout.lower()

    except Exception as e:
        print(f"{red}Error checking model: {e}{reset}")
        return False

def start_ollama():
    """
    Starts Ollama if it is not already running.
    """
    try:
        # Check if Ollama is already running using pgrep
        result = subprocess.run(["pgrep", "-f", "ollama"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"{green}Ollama is already running.{reset}\n")
            return

        print(f"{blue}Ollama is not running. Starting Ollama...{reset}")
        ollama_path = find_ollama_executable()

        subprocess.Popen([ollama_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
        time.sleep(5)
        print(f"{green}Ollama started successfully.{reset}\n")

    except Exception as e:
        print(f"{red}Error starting Ollama: {e}{reset}")

def check_command_installed(command):
    """
    Überprüft, ob ein Befehlszeilentool installiert ist (z. B. ollama).
    :param command: Zu prüfender Befehlsname.
    :return: True, wenn installiert, andernfalls False.
    """
    try:
        result = subprocess.run(["which", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"{red}Error checking command {command}: {e}{reset}")
        return False

def run_shell_script(script_name):
    """Führt die angegebene Shell-Skript-Datei aus."""
    file_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", f"run-{script_name}.sh")

    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        return

    try:
        print(f"Start: {file_path}")
        exit_code = os.system(f"bash {file_path}")
        if exit_code == 0:
            print(f" '{file_path}' executed successfully.")
        else:
            print(f"Error executing '{file_path}' with exit code {exit_code}.")
    except Exception as e:
        print(f"Execution errors: {e}")

def display_versions():
    """Zeigt verfügbare MAVIS-Versionen und Shell-Skripte an."""
    versions = {
        "mavis-4": ("MAVIS 4 EAP", "NEW - Development of MAVIS 4 has begun – featuring new Vision Models, a more powerful and faster MAVIS Terminal, and access to over 200 models.", ""),
        "mavis-terminal-4-arch": ("MAVIS Terminal 4 EAP", "The MAVIS Terminal is always available for you!!!", ""),
        "mavis-terminal-4-debian": ("MAVIS Terminal 4 EAP", "The MAVIS Terminal is always available for you!!!", ""),
        "mavis-4-3": ("MAVIS 4 EAP",
                    "NEW - Development of MAVIS 4 has begun – featuring new Vision Models, a more powerful and faster MAVIS Terminal, and access to over 200 models.",
                    "")
    }

    print(f"All MAVIS versions are available here:\n\n{green}█{reset} Required LLM model for this MAVIS version is already installed\n{orange}█{reset} Required LLM model for this MAVIS version is not yet installed\n{blue}█{reset} LLM model is available for you - you have all the permissions\n{red}█{reset} LLM model is not available for you - you do not have permission to install the model")
    categories = {}
    for script_name, (version, description, model_name) in versions.items():
        categories.setdefault(version, []).append((script_name, description, model_name))

    for i, (version, script_files) in enumerate(categories.items(), 1):
        print(f"\n{i}. {version}:")
        for script_name, description, model_name in script_files:
            # Check if model for the version is installed
            if check_installed_model(model_name):  # Check for the specific model
                print(f"   - {green}{script_name}{reset}: {description} ({blue}{model_name}{reset} Installed)")
            else:
                print(f"   - {orange}{script_name}{reset}: {description} ({blue}{model_name}{reset} Not Installed)")

    return versions

def get_user_input(versions):
    """Fragt nach einer MAVIS-Shell-Skript-Datei und führt sie aus."""
    while True:
        user_input = input("\nEnter a MAVIS shell script (e.g. 'mavis-4', 'mavis-4-3' or 'mavis-terminal-4-arch'):").strip()
        if user_input in versions:
            run_shell_script(user_input)
            break
        else:
            print("Invalid input. Please try again.")

def main():
    ollama_installed = check_command_installed("ollama")
    if ollama_installed:
        print(f"{green}Ollama is installed.{reset}")
    else:
        print(f"{red}Ollama is not installed. Please install it to proceed.{reset}")

    start_ollama()
    check_ollama_update()

    try:
        versions = display_versions()
        get_user_input(versions)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
