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

import platform
import time
import json
import sys
import getpass
import os
import subprocess
import threading
import time
from dotenv import load_dotenv
import importlib.util
from dotenv import load_dotenv
from subprocess import run

print("")

required_packages = ["requests", "ollama", "transformers", "python-dotenv", "PyQt6", "PyQt6-sip", "keyboard"]

def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path, "bin", "activate")

    # Überprüfen, ob die virtuelle Umgebung existiert
    if not os.path.exists(activate_script):
        print(f"Error: The virtual environment could not be found at {venv_path}.")
        sys.exit(1)

    # Umgebungsvariable für die virtuelle Umgebung setzen
    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"Virtual environment {venv_path} enabled.")

def ensure_packages_installed(packages):
    """Stellt sicher, dass alle erforderlichen Pakete installiert sind."""
    for package in packages:
        if importlib.util.find_spec(package) is None:
            print(f"Installing {package}...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
                print(f"{package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"WARNING: Failed to install {package}. Please install it manually.")
        else:
            print(f"{package} is already installed.")

# Pfad zur bestehenden virtuellen Umgebung
venv_path = rf"C:\Users\{os.getlogin()}\PycharmProjects\MAVIS\.env"

# Aktivieren der virtuellen Umgebung
activate_virtualenv(venv_path)

# Sicherstellen, dass alle erforderlichen Pakete installiert sind
ensure_packages_installed(required_packages)

sys.stdout.reconfigure(encoding='utf-8')
user_name = getpass.getuser()

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

def run_help_script():
    """
    Führt das Hilfe-Skript aus, wenn der Benutzer 'help' eingibt.
    """
    help_script_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "install", "help-models.py")
    if os.path.exists(help_script_path):
        print(f"{cyan}Running help script...{reset}")
        subprocess.run(["python", help_script_path], check=True)
    else:
        print(f"{red}Help script not found at {help_script_path}. Please check the path.{reset}")

def check_ollama_update():
    """
    Prüft, ob eine neue Version von Ollama verfügbar ist, und bietet ein Update an.
    """
    try:
        result = subprocess.run(["ollama", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            local_version = result.stdout.strip()
            remote_version = subprocess.run(["curl", "-s", "https://api.ollama.ai/version"],
                                            stdout=subprocess.PIPE, text=True).stdout.strip()

            if local_version != remote_version:
                print(f"{yellow}New Ollama version available: {remote_version} (Current: {local_version}){reset}")
                while True:
                    user_input = input("Do you want to update Ollama? [y/n]:").strip().lower()
                    if user_input in ["y", "yes"]:
                        subprocess.run(["ollama", "update"], check=True)
                        print(f"{green}Ollama updated successfully! Please restart the script.{reset}")
                        exit()
                    elif user_input in ["n", "no"]:
                        print("Skipping update.")
                        break
                    else:
                        print(f"{red}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

    except Exception as e:
        print(f"{red}Error checking for updates: {e}{reset}")

def find_ollama_path():
    """
    Findet den Installationspfad von Ollama basierend auf dem Betriebssystem.
    """
    try:
        if platform.system() == "Windows":
            base_path = os.environ.get("LOCALAPPDATA", "C:\\Users\\Default\\AppData\\Local")
            return os.path.join(base_path, "Programs", "Ollama", "ollama app.exe")
        elif platform.system() == "Darwin":  # macOS
            return "/Applications/Ollama.app/Contents/MacOS/Ollama"
        else:
            raise EnvironmentError("Unsupported Operating System. Ollama is not supported on this platform.")
    except Exception as e:
        raise FileNotFoundError(f"Error finding Ollama path: {e}")

def start_ollama():
    """
    Startet Ollama, falls es noch nicht läuft.
    """
    try:
        # Überprüfen, ob Ollama bereits läuft
        result = subprocess.run(
            ["tasklist"] if platform.system() == "Windows" else ["ps", "aux"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if "ollama" not in result.stdout.lower():
            print(f"{blue}Ollama is not running. Starting Ollama...{reset}")

            # Pfad zu Ollama finden
            ollama_path = find_ollama_path()

            if not os.path.exists(ollama_path):
                raise FileNotFoundError(f"Ollama executable not found at: {ollama_path}")

            # Ollama starten
            subprocess.Popen([ollama_path], close_fds=True if platform.system() != "Windows" else False)
            time.sleep(5)  # Warten, bis Ollama gestartet ist
            print(f"{green}Ollama started successfully.{reset}\n")
        else:
            print(f"{green}Ollama is already running.{reset}\n")
    except Exception as e:
        print(f"{red}Error starting Ollama: {e}{reset}")

def check_command_installed(command):
    """
    Überprüft, ob ein Befehlszeilentool installiert ist (z. B. ollama).
    :param command: Zu prüfender Befehlsname.
    :return: True, wenn installiert, andernfalls False.
    """
    try:
        result = subprocess.run(["which" if os.name != "nt" else "where", command],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"{red}Error checking command {command}: {e}{reset}")
        return False

def check_model_with_ollama(model_name):
    """
    Überprüft, ob ein bestimmtes Modell in ollama verfügbar ist.
    :param model_name: Der Name des zu prüfenden Modells.
    :return: True, wenn verfügbar, andernfalls False.
    """
    try:
        result = subprocess.run(
            ["ollama", "show", model_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",  # Sicherstellen, dass UTF-8 für die Ausgabe verwendet wird
            errors="replace"  # Ersetzt ungültige Zeichen, anstatt eine Exception auszulösen
        )

        if result.returncode == 0:
            print(f"Model information for {blue}{model_name}{reset}:\n"
                  f"--------------------------------------\n{result.stdout}\n")
            return True
        else:
            print(f"{yellow}Model {model_name} is not available{reset}:\n"
                  f"-----------------------------------\n{result.stderr}\n")
            return False

    except Exception as e:
        print(f"{red}Error checking model {model_name} with ollama{reset}:\n"
              f"-----------------------------------\n{e}\n")
        return False

def install_model_with_ollama(model_name):
    """
    Installiert ein Modell mit ollama, sofern verfügbar.
    :param model_name: Der Name des zu installierenden Modells.
    """
    try:
        print(f"{blue}Attempting to install model {model_name} with ollama...{reset}")
        result = subprocess.run(["ollama", "run", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            print(f"{green}Model {model_name} installed successfully.{reset}")
        else:
            print(f"{red}Failed to install model {model_name}{reset}:\n-----------------------------------\n{result.stderr}\n")
    except Exception as e:
        print(f"{red}Error installing model {model_name}{reset}:\n-----------------------------------\n{e}\n")

def prompt_user_for_installation(model_name):
    """
    Fragt den Benutzer, ob das Modell installiert werden soll.
    :param model_name: Der Name des Modells.
    :return: True, wenn der Benutzer zustimmt, False ansonsten.
    """
    while True:
        user_input = input(f"Do you want to install the model {model_name}? [y/n]:").strip().lower()
        if user_input in ["y", "yes"]:
            return True
        elif user_input in ["n", "no"]:
            return False
        else:
            print(f"{yellow}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

def save_model_selection(models):
    """
    Speichert die ausgewählten Modelle in einer JSON-Datei.
    :param models: Ein Dictionary mit den ausgewählten Modellen.
    """
    file_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "model-mavis-4.json")
    mavis_data = {
        "mavis-4": models
    }

    try:
        with open(file_path, 'w') as f:
            json.dump(mavis_data, f, indent=4)
        print(f"{green}Model selection saved to {file_path}{reset}")
    except Exception as e:
        print(f"{red}Error saving model selection: {e}{reset}")

def run_help_script():
    """
    Führt das Hilfe-Skript aus, wenn der Benutzer 'help' eingibt.
    """
    help_script_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "install", "help-models.py")
    if os.path.exists(help_script_path):
        print(f"{blue}Running help script...{reset}")
        run([f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env\\Scripts\\python.exe",
             f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\install\\help-models.py"],
            shell=True)
    else:
        print(f"{red}Help script not found at {help_script_path}. Please check the path.{reset}")

def m_run_help_script():
    """
    Führt das Hilfe-Skript aus, wenn der Benutzer 'help' eingibt.
    """
    help_script_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "install", "help-models.py")
    if os.path.exists(help_script_path):
        print(f"{blue}Running help script...{reset}")
        run([f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env\\Scripts\\python.exe",
             f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\install\\m-help-models.py"],
            shell=True)
    else:
        print(f"{red}Help script not found at {help_script_path}. Please check the path.{reset}")

def load_existing_models():
    """
    Lädt die bestehenden Modelle aus der JSON-Datei.
    """
    file_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "model-mavis-4.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get("mavis-4", {})
    return {}


if __name__ == "__main__":
    print("\nOllama Information:")
    print("-------------------")

    ollama_installed = check_command_installed("ollama")
    if ollama_installed:
        print(f"{green}Ollama is installed.{reset}")
    else:
        print(f"{red}Ollama is not installed. Please install it to proceed.{reset}")

    start_ollama()
    check_ollama_update()

    existing_models = load_existing_models()
    print("Current models:")
    for key, value in existing_models.items():
        print(f"   {blue}{key}{reset}: {value}")

    choice = input("\nDo you want to change the models? [y/n]:").strip().lower()

    if choice in ["y", "yes"]:
        # Benutzer fragt nach den Modellnamen
        models = {}

        # Model 1: Beliebiges Modell
        while True:
            models["model1"] = input(f"\nPlease select Main model (Model 1)\n - this model is used for everything (e.g. gemma3:12b, deepseek-r1:14b, qwq, llama3.3, phi4, mistral etc.)\nor type 'help', 'models ls', 'm help' or 'm models ls' for assistance:").strip()
            if models["model1"].lower() == "help":
                run_help_script()
            elif models["model1"].lower() == "models ls":
                run_help_script()
            elif models["model1"].lower() == "m help":
                m_run_help_script()
            elif models["model1"].lower() == "m models ls":
                m_run_help_script()
            elif models["model1"].lower() == "exit":
                sys.exit(0)
            else:
                break

        # Model 2: Vision-Modell
        while True:
            models["model2"] = input(f"\nPlease select Vision Model (Model 2)\n - this model is used only for image analysis (This should be a vision model, e.g. llama3.2-vision:11b, gemma3:12b, granite3.2-vision, minicpm-v etc.)\nor type 'help', 'models ls', 'm help' or 'm models ls' for assistance:").strip()
            if models["model2"].lower() == "help":
                run_help_script()
            elif models["model2"].lower() == "models ls":
                run_help_script()
            elif models["model2"].lower() == "m help":
                m_run_help_script()
            elif models["model2"].lower() == "m models ls":
                m_run_help_script()
            elif models["model2"].lower() == "exit":
                sys.exit(0)
            else:
                break

        # Model 3: Kleineren Modell auswählen
        while True:
            models["model3"] = input(f"\nPlease select TTS Model (Model 3)\n - this model is only used for Voice A (This should be a smaller model, e.g. gemma3:1b, qwen2.5:1.5b, llama3.2:1b etc.)\nor type 'help', 'models ls', 'm help' or 'm models ls' for assistance:").strip()
            if models["model3"].lower() == "help":
                run_help_script()
            elif models["model3"].lower() == "models ls":
                run_help_script()
            elif models["model3"].lower() == "m help":
                m_run_help_script()
            elif models["model3"].lower() == "m models ls":
                m_run_help_script()
            elif models["model3"].lower() == "exit":
                sys.exit(0)
            else:
                break

        # Model 4: Sehr kleines Vision-Modell auswählen
        while True:
            models["model4"] = input(f"\nPlease select Solution Model (Model 4)\n - this model is only used for Solution (This should be a very small vision model, e.g. gemma3:1b, granite3.2-vision, moondream etc.)\nor type 'help', 'models ls', 'm help' or 'm models ls' for assistance:").strip()
            if models["model4"].lower() == "help":
                run_help_script()
            elif models["model4"].lower() == "models ls":
                run_help_script()
            elif models["model4"].lower() == "m help":
                m_run_help_script()
            elif models["model4"].lower() == "m models ls":
                m_run_help_script()
            elif models["model4"].lower() == "exit":
                sys.exit(0)
            else:
                break

        # Speichern der Auswahl
        save_model_selection(models)

    else:
        models = existing_models

    print(f"{blue}Final models{reset}:", models, "\n")

    models_to_check = [models["model1"], models["model2"], models["model3"], models["model4"]]

    for model in models_to_check:
        model_installed = check_model_with_ollama(model)
        if model_installed:
            print(f"{green}{model} is installed.{reset}\n")
        else:
            print(f"{yellow}{model} is not installed.{reset}\n")
            if ollama_installed and prompt_user_for_installation(model):
                install_model_with_ollama(model)
            else:
                print(f"{yellow}Skipping installation of {model}.{reset}\n")
