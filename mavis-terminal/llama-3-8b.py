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

import sys
import os
import subprocess
import time
import platform
import importlib.util
from dotenv import load_dotenv
import select

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

def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path, "bin", "activate")

    if not os.path.exists(activate_script):
        print(f"Error: The virtual environment could not be found at {venv_path}.")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"Virtual environment {venv_path} enabled.")

def ensure_packages_installed(packages):
    """Stellt sicher, dass alle erforderlichen Pakete installiert sind."""
    for package in packages:
        if importlib.util.find_spec(package) is None:
            print(f"Installing {package}...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
                print(f"{package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"WARNING: Failed to install {package}. Please install it manually.")
        else:
            print(f"{package} is already installed.")

def find_ollama_path():
    """Findet den Installationspfad von Ollama basierend auf dem Betriebssystem."""
    if platform.system() == "Windows":
        base_path = os.environ.get("LOCALAPPDATA", "C:\\Users\\Default\\AppData\\Local")
        return os.path.join(base_path, "Programs", "Ollama", "ollama app.exe")
    elif platform.system() == "Darwin":  # macOS
        return "/Applications/Ollama.app/Contents/MacOS/Ollama"
    else:
        raise EnvironmentError("Unsupported Operating System. Ollama is not supported on this platform.")

def start_ollama():
    """Startet Ollama, falls es noch nicht läuft."""
    try:
        result = subprocess.run(
            ["tasklist"] if platform.system() == "Windows" else ["ps", "aux"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Textmodus aktivieren
            encoding="utf-8",  # Explizite Angabe der Codierung
            errors="replace"  # Ersetze ungültige Zeichen
        )

        if "ollama" not in result.stdout.lower():
            print(f"{blue}Ollama is not running. Starting Ollama...{reset}")
            ollama_path = find_ollama_path()

            if not os.path.exists(ollama_path):
                raise FileNotFoundError(f"Ollama executable not found at: {ollama_path}")

            subprocess.Popen([ollama_path], close_fds=True if platform.system() != "Windows" else False)
            time.sleep(5)
            print(f"{green}Ollama started successfully.{reset}\n")
        else:
            print(f"{green}Ollama is already running.{reset}\n")
    except Exception as e:
        print(f"{red}Error starting Ollama: {e}{reset}")

def check_command_installed(command):
    """Überprüft, ob ein Befehlszeilentool installiert ist."""
    try:
        result = subprocess.run(["which" if os.name != "nt" else "where", command],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"{red}Error checking command {command}{reset}: {e}")
        return False

def check_model_with_ollama(model_name):
    """Überprüft, ob ein Modell in Ollama verfügbar ist."""
    try:
        result = subprocess.run(["ollama", "show", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                encoding="utf-8",  # Hier wird auch explizite UTF-8-Codierung gesetzt
                                errors="replace")  # Fehlerhafte Zeichen werden ersetzt
        if result.returncode == 0:
            print(f"Model information for {blue}{model_name}{reset}:\n{result.stdout}")
            return True
        else:
            print(f"{yellow}Model {model_name} is not available{reset}:\n{result.stderr}")
            return False
    except Exception as e:
        print(f"{red}Error checking model {model_name} with ollama{reset}: {e}")
        return False

def install_model_with_ollama(model_name):
    """Installiert ein Modell mit Ollama."""
    try:
        print(f"{blue}Attempting to install model {model_name} with Ollama...{reset}")
        result = subprocess.run(["ollama", "run", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                encoding="utf-8",  # Hier wird auch explizite UTF-8-Codierung gesetzt
                                errors="replace")  # Fehlerhafte Zeichen werden ersetzt
        if result.returncode == 0:
            print(f"{green}Model {model_name} installed successfully.{reset}")
        else:
            print(f"{red}Failed to install model {model_name}{reset}:\n{result.stderr}")
    except Exception as e:
        print(f"{red}Error installing model {model_name}{reset}: {e}")

def prompt_user_for_installation(model_name):
    """Fragt den Benutzer, ob das Modell installiert werden soll."""
    while True:
        user_input = input_with_timeout(f"Do you want to install the model {model_name}? [y/n]:", 10)
        if user_input is None:
            print(f"{yellow}Timeout reached. No input received. Defaulting to 'no'.{reset}")
            return False
        elif user_input in ["y", "yes"]:
            return True
        elif user_input in ["n", "no"]:
            return False
        else:
            print(f"{yellow}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

def get_response_from_ollama(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="llama3:8b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"ERROR: {e}"

def input_with_timeout(prompt, timeout=10):
    """Fragt den Benutzer nach einer Eingabe mit Timeout."""
    print(prompt, end=": ", flush=True)
    i, _, _ = select.select([sys.stdin], [], [], timeout)
    if i:
        return sys.stdin.readline().strip()
    else:
        return None  # Timeout erreicht

def type_out_text(text, delay=0.05):
    """Tippt den Text langsam aus."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    """Hauptfunktion."""
    if check_command_installed("ollama"):
        print(f"{green}Ollama is installed.{reset}")

        import ollama  # Ollama nur importieren, wenn es installiert ist

        start_ollama()

        models_to_check = ["llama3:8b"]
        for model in models_to_check:
            if check_model_with_ollama(model):
                print(f"{green}{model} is installed.{reset}\n")
            else:
                print(f"{yellow}{model} is not installed.{reset}\n")
                if prompt_user_for_installation(model):
                    install_model_with_ollama(model)

        while True:
            user_input = input("\nEnter a prompt (or 'exit' to exit):")

            if user_input.lower() == "exit":
                print("Exit the program...")
                break

            response = get_response_from_ollama(user_input, ollama)

            print("Response from the model:", end=" ")
            type_out_text(response)

    else:
        print(f"{red}Ollama is not installed. Please install it to proceed.{reset}")
        sys.exit(1)

if __name__ == "__main__":
    main()
