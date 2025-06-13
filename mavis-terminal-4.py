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
import getpass
import subprocess
import threading
import time
import importlib.util
import os

required_packages = [
    "requests", "ollama", "transformers", "numpy", "pandas", "python-dotenv",
    "PyQt6", "PyQt6-sip", "PyQt6-Charts", "PyQt6-WebEngine", "keyboard"
]


def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path,
                                                                                                          "bin",
                                                                                                          "activate")

    if not os.path.exists(activate_script):
        print(f"Error: Virtual environment not found at {venv_path}.")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"Virtual environment {venv_path} activated.")


def ensure_packages_installed(packages):
    """Installiert fehlende Pakete effizient."""
    to_install = [pkg for pkg in packages if importlib.util.find_spec(pkg) is None]

    if to_install:
        print(f"Installing missing packages: {', '.join(to_install)}...")
        subprocess.run([sys.executable, "-m", "pip", "install"] + to_install, check=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        print("All missing packages installed.")
    else:
        print("All required packages are already installed.")


# Virtuelle Umgebung aktivieren und Pakete sicherstellen
venv_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
activate_virtualenv(venv_path)
ensure_packages_installed(required_packages)

from cgitb import strong
from dotenv import load_dotenv
from subprocess import run

import readline
import ctypes
import shlex

user_name = getpass.getuser()

sys.stdout.reconfigure(encoding='utf-8')

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

def print_banner():

    print(f"""
{blue}      ██╗     █╗      {reset}
{blue}     ████╗   ███╗     {reset}   {white}███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗{reset}
{blue}    ██████╗  ████╗    {reset}   {white}████╗ ████║██╔══██╗██║   ██║██║██╔════╝{reset}
{blue}   ████████╗  ████╗   {reset}   {white}██╔████╔██║███████║██║   ██║██║███████╗{reset}
{blue}  ████╔█████╗  ████╗  {reset}   {white}██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║{reset}
{blue} ████╔╝ █████╗  ████╗ {reset}   {white}██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║{reset}
{blue} ╚═══╝   ███╔╝  ╚═══╝ {reset}   {white}╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝{reset}
{blue}          █╔╝         {reset}
{blue}          ╚╝          {reset}

{white} ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ██╗  ██╗{reset}
{white} ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██║  ██║{reset}
{white}    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ███████║{reset}
{white}    ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ╚════██║{reset}
{white}    ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗         ██║{reset}
{white}    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝         ╚═╝{reset}
""")
    print(f"""A warm welcome, {blue}{user_name}{reset}, to MAVIS (MAth Visual Intelligent System) Terminal 4
Developed by Peharge and JK (Peharge Projects 2025)
Thank you so much for using MAVIS. We truly appreciate your support ❤️""")

    print(f"""
{blue}MAVIS Version{reset}: 4
{blue}MAVIS Launcher Version{reset}: 4
{blue}MAVIS Terminal Version{reset}: 4
{blue}MAVIS License{reset}: MIT
    """)

    # Funktion zur Anzeige der 16 Farbpaletten ohne Abstände und Zahlen
    def show_color_palette():
        for i in range(8):
            print(f"\033[48;5;{i}m  \033[0m", end="")  # Farben ohne Zahlen und ohne Abstände

        print()  # Zeilenumbruch nach der ersten Reihe

        # Anzeige der helleren Farben (8-15) ohne Abstände und Zahlen
        for i in range(8, 16):
            print(f"\033[48;5;{i}m  \033[0m", end="")

        print()  # Noch ein Zeilenumbruch am Ende

    # Aufruf der Funktion, um die Farbpalette zu zeigen
    show_color_palette()

    print("")

def set_python_path():
    python_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env\\Scripts\\python.exe"
    os.environ["PYTHON_PATH"] = python_path


def run_command(command, shell=False):
    python_path = os.environ.get("PYTHON_PATH")

    if isinstance(command, str):
        command = shlex.split(command)

    if "pip" in command:
        command = [python_path, "-m", "pip"] + command[1:]

    """
    elif "python" in command:
        command = [python_path] + command[1:]
    """

    process = subprocess.Popen(command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) # encoding='utf-8'

    def read_stream(stream, output_list):
        for line in iter(stream.readline, ''):
            output_list.append(line)
        stream.close()

    stdout_lines = []
    stderr_lines = []
    stdout_thread = threading.Thread(target=read_stream, args=(process.stdout, stdout_lines), daemon=True)
    stderr_thread = threading.Thread(target=read_stream, args=(process.stderr, stderr_lines), daemon=True)
    stdout_thread.start()
    stderr_thread.start()

    while process.poll() is None or stdout_lines or stderr_lines:
        while stdout_lines:
            print(stdout_lines.pop(0), end='', flush=True)
        while stderr_lines:
            print(stderr_lines.pop(0), end='', flush=True, file=sys.stderr)
        time.sleep(1 / 24)

    stdout_thread.join()
    stderr_thread.join()

    while stdout_lines:
        print(stdout_lines.pop(0), end='', flush=True)
    while stderr_lines:
        print(stderr_lines.pop(0), end='', flush=True, file=sys.stderr)


def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory not found: {path}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)


def handle_special_commands(user_input):
    user_input = user_input.strip()

    # Lade die .env-Datei
    load_dotenv(dotenv_path=f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env")

    # Der Pfad zum Python-Interpreter in der .env
    python_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env\\Scripts\\python.exe"

    commands = {
        "env install": "mavis-terminal\\install-mavis-3.py",
        "install env": "mavis-terminal\\install-mavis-3.py",
        "mavis env install": "mavis-terminal\\install-mavis-3.py",
        "install mavis env": "mavis-terminal\\install-mavis-3.py",
        "env update": "mavis-terminal\\install-mavis-3.py",
        "update env": "mavis-terminal\\install-mavis-3.py",
        "mavis env update": "mavis-terminal\\install-mavis-3.py",
        "update mavis env": "mavis-terminal\\install-mavis-3.py",
        "update": "mavis-terminal\\update-repository-windows.py",
        "mavis update": "mavis-terminal\\update-repository-windows.py",
        "update mavis": "mavis-terminal\\update-repository-windows.py",
        "security": "mavis-terminal\\security-check-mavis-4.py",
        "mavis security": "mavis-terminal\\security-check-mavis-4.py",
        "securitycheck": "mavis-terminal\\security-check-mavis-4.py",
        "info": "mavis-terminal\\info.py",
        "mavis info": "mavis-terminal\\info.py",
        "info mavis": "mavis-terminal\\info.py",
        "neofetch": "mavis-terminal\\neofetch.py",
        "fastfetch": "mavis-terminal\\neofetch.py", # new
        "screenfetch": "mavis-terminal\\neofetch.py", # new
        "jupyter": "mavis-terminal\\run-jup.py",
        "run jupyter": "mavis-terminal\\run-jup.py",
        "run mavis-1-5-main": "mavis-1-5-main-main.py",
        "run mavis-1-5-math": "mavis-1-5-math-math.py",
        "run mavis-1-5-math-pro": "mavis-1-5-math-math-pro.py",
        "run mavis-1-5-math-ultra": "mavis-1-5-math-math-ultra.py",
        "run mavis-1-5-math-mini": "mavis-1-5-math-math-mini.py",
        "run mavis-1-5-math-mini-mini": "mavis-1-5-math-math-mini-mini.py",
        "run mavis-1-5-code": "mavis-1-5-main-code.py",
        "run mavis-1-5-code-pro": "mavis-1-5-main-code-pro.py",
        "run mavis-1-5-code-mini": "mavis-1-5-main-code-mini.py",
        "run mavis-1-5-code-mini-mini": "mavis-1-5-main-code-mini-mini.py",
        "run mavis-1-5-3-math-mini-mini": "mavis-1-5-3-main-math-mini-mini.py",
        "run mavis-1-2-main": "main-old\\mavis-1-2-main-main.py",
        "run mavis-1-2-math": "main-old\\mavis-1-2-main-math.py",
        "run mavis-1-2-math pro": "main-old\\mavis-1-2-main-math-pro.py",
        "run mavis-1-2-code": "main-old\\mavis-1-2-main-code.py",
        "run mavis-1-2-code pro": "main-old\\mavis-1-2-main-code-pro.py",
        "run mavis-1-2-main-mini": "main-old\\mavis-1-2-main-main-mini.py",
        "run mavis-1-2-main-mini-mini": "main-old\\mavis-1-2-main-main-mini-mini.py",
        "run mavis-1-2-3-main": "main-old\\mavis-1-2-3-main-main.py",
        "run mavis-1-2-3-math": "main-old\\mavis-1-2-3-main-math.py",
        "run mavis-1-2-3-math-pro": "main-old\\mavis-1-2-3-main-math-pro.py",
        "run mavis-1-2-3-math-ultra": "main-old\\mavis-1-2-3-main-math-ultra.py",
        "run mavis-1-4-math": "main-old\\mavis-1-4-main-math.py",
        "run mavis-3-main": "mavis-3-main-main.py",  # new
        "run mavis-3-main-mini": "mavis-3-main-main-mini.py",  # new
        "run mavis-3-math": "mavis-3-main-math.py",  # new
        "run mavis-3-math-pro": "mavis-3-main-math-pro.py",  # new
        "run mavis-3-math-ultra": "mavis-3-main-math-ultra.py",  # new
        "run mavis-3-math-mini": "mavis-3-main-math-mini.py",  # new
        "run mavis-3-math-mini-mini": "mavis-3-main-math-mini-mini.py",  # new
        "run mavis-3-code": "mavis-3-main-code.py",  # new
        "run mavis-3-code-pro": "mavis-3-main-code-pro.py",  # new
        "run mavis-3-code-mini": "mavis-3-main-code-mini.py",  # new
        "run mavis-3-code-mini-mini": "mavis-3-main-code-mini-mini.py",  # new
        "run mavis-3-3-main": "mavis-3-3-main-main.py",  # new
        "run mavis-3-3-main-pro": "mavis-3-3-main-main-pro.py",  # new
        "run mavis-3-3-main-mini": "mavis-3-3-main-main-mini.py",  # new
        "run mavis-3-3-main-mini-mini": "mavis-3-3-main-main-mini-mini.py",  # new
        "run mavis-3-3-math": "mavis-3-3-main-math.py",  # new
        "run mavis-3-3-math-mini": "mavis-3-3-main-math-pro.py",  # new
        "run mavis-4": "mavis-4-main.py",  # new
        "run ollama mavis-3-main": "install\\install-ollama-mavis-3-main.py",  # new
        "run ollama mavis-3-main-mini": "install\\install-ollama-mavis-3-main-mini.py",  # new
        "run ollama mavis-3-math": "install\\install-ollama-mavis-3-math.py",  # new
        "run ollama mavis-3-math-pro": "install\\install-ollama-mavis-3-math.py",  # new
        "run ollama mavis-3-math-ultra": "install\\install-ollama-mavis-3-math.py",  # new
        "run ollama mavis-3-math-mini": "install\\install-ollama-mavis-3-math.py",  # new
        "run ollama mavis-3-math-mini-mini": "install\\install-ollama-mavis-3-math.py",  # new
        "run ollama mavis-3-code": "install\\install-ollama-mavis-3-code.py",  # new
        "run ollama mavis-3-code-pro": "install\\install-ollama-mavis-3-code.py",  # new
        "run ollama mavis-3-code-mini": "install\\install-ollama-mavis-3-code.py",  # new
        "run ollama mavis-3-code-mini-mini": "install\\install-ollama-mavis-3-code.py",  # new
        "run ollama mavis-3-3-main": "install\\install-ollama-mavis-3-3-main.py",  # new
        "run ollama mavis-3-3-main-pro": "install\\install-ollama-mavis-3-3-main-pro.py",  # new
        "run ollama mavis-3-3-main-mini": "install\\install-ollama-mavis-3-3-main-mini.py",  # new
        "run ollama mavis-3-3-main-mini-mini": "install\\install-ollama-mavis-3-3-main-mini-mini.py",  # new
        "run ollama mavis-3-3-math": "install\\install-ollama-mavis-3-3-math.py",  # new
        "run ollama mavis-3-3-math-mini": "install\\install-ollama-mavis-3-3-math-mini.py",  # new
        "install ollama mavis-1-5-main": "install\\install-ollama-mavis-1-5-main.py",
        "install ollama mavis-1-5-math": "install\\install-ollama-mavis-1-5-math.py",
        "install ollama mavis-1-5-math-pro": "install\\install-ollama-mavis-1-5-math-pro.py",
        "install ollama mavis-1-5-math-ultra": "install\\install-ollama-mavis-1-5-math-ultra.py",
        "install ollama mavis-1-5-math-mini": "install\\install-ollama-mavis-1-5-math-mini.py",
        "install ollama mavis-1-5-math-mini-mini": "install\\install-ollama-mavis-1-5-math-mini-mini.py",
        "install ollama mavis-1-5-code": "install\\install-ollama-mavis-1-5-code.py",
        "install ollama mavis-1-5-code-pro": "install\\install-ollama-mavis-1-5-code-pro.py",
        "install ollama mavis-1-5-code-mini": "install\\install-ollama-mavis-1-5-code-mini.py",
        "install ollama mavis-1-5-code-mini-mini": "install\\install-ollama-mavis-1-5-code-mini-mini.py",
        "install ollama mavis-1-5-3-math-mini-mini": "install\\install-ollama-mavis-1-5-3-math-mini-mini.py",
        "install ollama mavis-3-main": "install\\install-ollama-mavis-3-main.py", # new
        "install ollama mavis-3-main-mini": "install\\install-ollama-mavis-3-main-mini.py", # new
        "install ollama mavis-3-math": "install\\install-ollama-mavis-3-math.py", # new
        "install ollama mavis-3-math-pro": "install\\install-ollama-mavis-3-math.py", # new
        "install ollama mavis-3-math-ultra": "install\\install-ollama-mavis-3-math.py", # new
        "install ollama mavis-3-math-mini": "install\\install-ollama-mavis-3-math.py", # new
        "install ollama mavis-3-math-mini-mini": "install\\install-ollama-mavis-3-math.py", # new
        "install ollama mavis-3-code": "install\\install-ollama-mavis-3-code.py", # new
        "install ollama mavis-3-code-pro": "install\\install-ollama-mavis-3-code.py", # new
        "install ollama mavis-3-code-mini": "install\\install-ollama-mavis-3-code.py", # new
        "install ollama mavis-3-code-mini-mini": "install\\install-ollama-mavis-3-code.py", # new
        "install ollama mavis-3-3-main": "install\\install-ollama-mavis-3-3-main.py", # new
        "install ollama mavis-3-3-main-pro": "install\\install-ollama-mavis-3-3-main-pro.py", # new
        "install ollama mavis-3-3-main-mini": "install\\install-ollama-mavis-3-3-main-mini.py", # new
        "install ollama mavis-3-3-main-mini-mini": "install\\install-ollama-mavis-3-3-main-mini-mini.py", # new
        "install ollama mavis-3-3-math": "install\\install-ollama-mavis-3-3-math.py", # new
        "install ollama mavis-3-3-math-mini": "install\\install-ollama-mavis-3-3-math-mini.py", # new
        "install ollama mavis-4": "install\\install-ollama-mavis-4.py",  # new
        "install mavis-4": "install\\install-ollama-mavis-4.py",  # new
        "grafana": "run-grafana\\run-grafana.py",
        "run grafana": "run-grafana\\run-grafana.py",
        "install grafana": "run-grafana\\run-grafana.py",
        "account": "account\\account.py",
        "run deepseek-r1:1.5b": "mavis-terminal\\deepseek-r1-1-5b.py",
        "run deepseek-r1:7b": "mavis-terminal\\deepseek-r1-7b.py",
        "run deepseek-r1:8b": "mavis-terminal\\deepseek-r1-8b.py",
        "run deepseek-r1:14b": "mavis-terminal\\deepseek-r1-14b.py",
        "run deepseek-r1:32b": "mavis-terminal\\deepseek-r1-32b.py",
        "run deepseek-r1:70b": "mavis-terminal\\deepseek-r1-70b.py",
        "run deepseek-r1:671b": "mavis-terminal\\deepseek-r1-671b.py",
        "run deepscaler": "mavis-terminal\\deepscaler.py",
        "run llama3.1:8b": "mavis-terminal\\llama-3-1-8b.py",
        "run llama3.1:70b": "mavis-terminal\\llama-3-1-70b.py",
        "run llama3.1:405": "mavis-terminal\\llama-3-1-405b.py",
        "run llama3.2:1b": "mavis-terminal\\llama-3-2-1b.py",
        "run llama3.2:3b": "mavis-terminal\\llama-3-2-3b.py",
        "run llama3.3": "mavis-terminal\\llama-3-3.py",
        "run llama3:8b": "mavis-terminal\\llama-3-8b.py",
        "run llama3:70b": "mavis-terminal\\llama-3-70b.py",
        "run mistral": "mavis-terminal\\mistral.py",
        "run mistral-large": "mavis-terminal\\mistral-large.py", #new
        "run mistral-nemo": "mavis-terminal\\mistral-nemo.py", #new
        "run mistral-openorca": "mavis-terminal\\mistral-openorca.py", #new
        "run mistral-small:22b": "mavis-terminal\\mistral-small-22b.py", #new
        "run mistral-small:24b": "mavis-terminal\\mistral-small-24b.py", #new
        "run phi4": "mavis-terminal\\phi-4.py",
        "run qwen2.5:0.5b": "mavis-terminal\\qwen-2-5-0.5b.py",
        "run qwen2.5:1.5b": "mavis-terminal\\qwen-2-5-1.5b.py",
        "run qwen2.5:3b": "mavis-terminal\\qwen-2-5-3b.py",
        "run qwen2.5:7b": "mavis-terminal\\qwen-2-5-7b.py",
        "run qwen2.5:14b": "mavis-terminal\\qwen-2-5-14b.py",
        "run qwen2.5:32b": "mavis-terminal\\qwen-2-5-32b.py",
        "run qwen2.5:72b": "mavis-terminal\\qwen-2-5-72b.py",
        "run qwen2.5-coder:0.5b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:1.5b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:3b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:7b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:14b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:32b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "run gemma3:1b": "mavis-terminal\\gemma-3-1b.py", # new
        "run gemma3:4b": "mavis-terminal\\gemma-3-4b.py", # new
        "run gemma3:12b": "mavis-terminal\\gemma-3-12b.py", # new
        "run gemma3:27b": "mavis-terminal\\gemma-3-27b.py", # new
        "run qwq": "mavis-terminal\\qwq.py", # new
        "run command-a": "mavis-terminal\\command-a.py", #new
        "run phi4-mini": "mavis-terminal\\phi-4-mini.py", #new
        "run granite3.2:8b": "mavis-terminal\\granite-3-2-8b.py", # new
        "run granite3.2:2b": "mavis-terminal\\granite-3-2-2b.py", # new
        "run granite3.2-vision:2b": "mavis-terminal\\granite-3-2-2b-vision.py", # new
        "run qwen-2-5-omni-7b": "mavis-terminal\\qwen-2-5-omni-7b.py",  # new
        "run qvq-72b": "mavis-terminal\\qvq-72b.py",  # new
        "run qwen-2-5-vl-32b": "mavis-terminal\\qwen-2-5-vl-32b.py",  # new
        "run qwen-2-5-vl-72b": "mavis-terminal\\qwen-2-5-vl-72b.py",  # new
        "install deepseek-r1:1.5b": "mavis-terminal\\deepseek-r1-1-5b.py",
        "install deepseek-r1:7b": "mavis-terminal\\deepseek-r1-7b.py",
        "install deepseek-r1:8b": "mavis-terminal\\deepseek-r1-8b.py",
        "install deepseek-r1:14b": "mavis-terminal\\deepseek-r1-14b.py",
        "install deepseek-r1:32b": "mavis-terminal\\deepseek-r1-32b.py",
        "install deepseek-r1:70b": "mavis-terminal\\deepseek-r1-70b.py",
        "install deepseek-r1:671b": "mavis-terminal\\deepseek-r1-671b.py",
        "install deepscaler": "mavis-terminal\\deepscaler.py",
        "install llama3.1:8b": "mavis-terminal\\llama-3-1-8b.py",
        "install llama3.1:70b": "mavis-terminal\\llama-3-1-70b.py",
        "install llama3.1:405": "mavis-terminal\\llama-3-1-405b.py",
        "install llama3.2:1b": "mavis-terminal\\llama-3-2-1b.py",
        "install llama3.2:3b": "mavis-terminal\\llama-3-2-3b.py",
        "install llama3.3": "mavis-terminal\\llama-3-3.py",
        "install llama3:8b": "mavis-terminal\\llama-3-8b.py",
        "install llama3:70b": "mavis-terminal\\llama-3-70b.py",
        "install mistral": "mavis-terminal\\mistral.py",
        "install mistral-large": "mavis-terminal\\mistral-large.py", #new
        "install mistral-nemo": "mavis-terminal\\mistral-nemo.py", #new
        "install mistral-openorca": "mavis-terminal\\mistral-openorca.py", #new
        "install mistral-small:22b": "mavis-terminal\\mistral-small-22b.py", #new
        "install mistral-small:24b": "mavis-terminal\\mistral-small-24b.py", #new
        "install phi4": "mavis-terminal\\phi-4.py",
        "install qwen2.5:0.5b": "mavis-terminal\\qwen-2-5-0.5b.py",
        "install qwen2.5:1.5b": "mavis-terminal\\qwen-2-5-1.5b.py",
        "install qwen2.5:3b": "mavis-terminal\\qwen-2-5-3b.py",
        "install qwen2.5:7b": "mavis-terminal\\qwen-2-5-7b.py",
        "install qwen2.5:14b": "mavis-terminal\\qwen-2-5-14b.py",
        "install qwen2.5:32b": "mavis-terminal\\qwen-2-5-32b.py",
        "install qwen2.5:72b": "mavis-terminal\\qwen-2-5-72b.py",
        "install qwen2.5-coder:0.5b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:1.5b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:3b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:7b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:14b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:32b": "mavis-terminal\\qwen-2-5-coder-0.5b.py",
        "install gemma3:1b": "mavis-terminal\\gemma-3-1b.py", # new
        "install gemma3:4b": "mavis-terminal\\gemma-3-4b.py", # new
        "install gemma3:12b": "mavis-terminal\\gemma-3-12b.py", # new
        "install gemma3:27b": "mavis-terminal\\gemma-3-27b.py", # new
        "install qwq": "mavis-terminal\\qwq.py", # new
        "install command-a": "mavis-terminal\\command-a.py", # new
        "install phi4-mini": "mavis-terminal\\phi-4-mini.py", # new
        "install granite3.2:8b": "mavis-terminal\\granite-3-2-8b.py", # new
        "install granite3.2:2b": "mavis-terminal\\granite-3-2-2b.py", # new
        "install granite3.2-vision:2b": "mavis-terminal\\granite-3-2-2b-vision.py", # new
        "help": "mavis-terminal\\help.py",
        "image generation": "mavis-terminal\\stable-diffusion-3-5-large-turbo.py",
        "video generation": "mavis-terminal\\wan-2-1-t2v-14b.py",
        "run mavis": "mavis-installer-3-main-windows.py",
        "m run all": "mavis-terminal\\m-run-all.py", # new
        "m htop": "mavis-terminal\\m-htop.py", # new
        "m run gemma3": "mavis-terminal\\m-gemma-3.py", # new
        "m run deepseek-r1": "mavis-terminal\\m-deepseek-r1.py", # new
        "m run qwen2.5": "mavis-terminal\\m-qwen-2-5.py", # new
        "m run qwen2.5-coder": "mavis-terminal\\m-qwen-2-5-coder.py", # new
        "m python frameworks": "mavis-terminal\\m-python-frameworks.py", # new
        "m pip list": "mavis-terminal\\m-python-frameworks.py", # new
        "m pip ls": "mavis-terminal\\m-python-frameworks.py",  # new
        "m git ls": "mavis-terminal\\m-git.py", # new
        "m git": "mavis-terminal\\m-git.py",  # new
        "m ls": "mavis-terminal\\m-ls.py", # new
        "models ls": "mavis-terminal\\models-ls.py",  # new
        "m models ls": "mavis-terminal\\m-models-ls.py",  # new
        "m github mavis": "mavis-terminal\\m-github-mavis.py",  # new
        "m github commits": "mavis-terminal\\m-github-commits.py",  # new
        "m github issues": "mavis-terminal\\m-github-issues.py",  # new
        "m github peharge": "mavis-terminal\\m-github-peharge.py",  # new
        "m github pulls": "mavis-terminal\\m-github-pulls.py",  # new
        "m github readme": "mavis-terminal\\m-github-readme.py",  # new
        "m github releases": "mavis-terminal\\m-github-releases.py",  # new
        "m github": "mavis-terminal\\m-github.py",  # new
        "m search": "mavis-terminal\\m-search.py",  # new
        "m google": "mavis-terminal\\m-google.py",  # new
        "m ollama": "mavis-terminal\\m-ollama.py",  # new
        "m huggingface": "mavis-terminal\\m-huggingface.py",  # new
        "m github.com": "mavis-terminal\\m-github.py",  # new
        "m google.com": "mavis-terminal\\m-google.py",  # new
        "m ollama.com": "mavis-terminal\\m-ollama.py",  # new
        "m huggingface.com": "mavis-terminal\\m-huggingface.py",  # new
        "m mavis.com": "mavis-terminal\\m-mavis.py"  # new
    }

    if user_input in commands:
        script_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\{commands[user_input]}"

        # Prüfen, ob es eine Python-Datei oder eine Batch-Datei ist
        if not user_input.endswith(".bat"):
            # Führe das Skript mit dem Python-Interpreter aus der .env-Umgebung aus
            run([python_path, script_path], shell=True)
        else:
            # Wenn es eine Batch-Datei ist, führe sie direkt aus
            run([script_path], shell=True)

        return True

    if user_input.startswith("cd "):
        path = user_input[3:].strip()
        change_directory(path)
        return True
    elif user_input.lower() in ["cls", "clear"]:
        os.system("cls" if os.name == "nt" else "clear")
        return True
    elif user_input.lower() in ["dir", "ls"]:
        run_command("dir" if os.name == "nt" else "ls -la", shell=True)
        return True
    elif user_input.startswith("mkdir "):
        os.makedirs(user_input[6:].strip(), exist_ok=True)
        return True
    elif user_input.startswith("rmdir "):
        try:
            os.rmdir(user_input[6:].strip())
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
        return True
    elif user_input.startswith("del ") or user_input.startswith("rm "):
        try:
            os.remove(user_input.split(maxsplit=1)[1].strip())
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
        return True
    elif user_input.startswith("echo "):
        print(user_input[5:].strip())
        return True
    elif "=" in user_input:
        var, value = map(str.strip, user_input.split("=", 1))
        os.environ[var] = value
        return True
    elif user_input.startswith("type ") or user_input.startswith("cat "):
        try:
            with open(user_input.split(maxsplit=1)[1].strip(), "r", encoding="utf-8") as file:
                print(file.read())
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
        return True
    elif user_input.lower() == "exit":
        sys.exit(0)
    return False


def is_tool_installed(tool_name):
    """Check if a tool is installed."""
    result = subprocess.run(["which", tool_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0


def setup_autocomplete():
    commands = ["cd", "cls", "clear", "dir", "ls", "mkdir", "rmdir", "del", "rm", "echo", "type", "cat", "exit",
                "ubuntu"]
    readline.set_completer(lambda text, state: [cmd for cmd in commands if cmd.startswith(text)][state] if state < len(
        [cmd for cmd in commands if cmd.startswith(text)]) else None)
    readline.parse_and_bind("tab: complete")


def run_command_with_admin_privileges(command):
    if sys.platform == "win32":
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            powershell_command = f"Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command \"{command}\"' -Verb RunAs"
            subprocess.run(["powershell", "-Command", powershell_command], shell=True)
        else:
            subprocess.run(command, shell=True)
    else:
        subprocess.run(['sudo', '-S', command], input="password", text=True, shell=True)

def is_wsl_installed():
    """Check if WSL is installed by attempting to run a basic wsl command."""
    try:
        # Try running 'wsl --list' which lists installed WSL distributions
        subprocess.check_call(["wsl", "--list"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        # WSL executable not found, meaning WSL is not installed
        print("Error: WSL is not installed or not found on the system.")
        return False
    except subprocess.CalledProcessError:
        # WSL is found, but something went wrong while running the command
        print("Error: WSL is installed, but an error occurred while executing the command.")
        return False
    except Exception as e:
        # Catch any unexpected exceptions
        print(f"Unexpected error occurred while checking if WSL is installed: {e}")
        return False

def run_linux_command(command):
    if isinstance(command, str):
        command = f"wsl -e {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def run_ubuntu_command(command):
    if isinstance(command, str):
        command = f"wsl -d ubuntu {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def run_debian_command(command):
    if isinstance(command, str):
        command = f"wsl -d debian {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def run_kali_command(command):
    if isinstance(command, str):
        command = f"wsl -d kali-linux {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def run_arch_command(command):
    if isinstance(command, str):
        command = f"wsl -d arch-linux {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def run_scoop_command(command):
    if isinstance(command, str):
        command = f"scoop {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def run_choco_command(command):
    if isinstance(command, str):
        command = f"choco {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def run_winget_command(command):
    if isinstance(command, str):
        command = f"winget {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


def main():
    print_banner()
    set_python_path()
    setup_autocomplete()

    while True:
        try:
            current_dir = os.getcwd()
            prompt = f"\n{green}┌──({reset}{blue}{getpass.getuser()}㉿MAVIS{reset}{green})-[{reset}{current_dir}{green}]{reset}\n{green}└─{reset}{blue}#{reset}"

            print(prompt, end='')
            user_input = input().strip()

            if handle_special_commands(user_input):
                continue
            elif user_input.startswith("mp "):
                user_input = user_input[3:]
                run_command_with_admin_privileges(user_input)
            elif user_input.startswith("powershell "):
                run_command(user_input, shell=True)

            elif user_input.startswith("lx "):
                user_input = user_input[3:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("linux "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("ubuntu "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_command(user_input)

            elif user_input.startswith("debian "):
                user_input = user_input[7:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Debian: {user_input}")
                    run_debian_command(user_input)

            elif user_input.startswith("kali "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("hack "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("arch "):
                user_input = user_input[5:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Arch: {user_input}")
                    run_arch_command(user_input)

            elif user_input.startswith("openSUSE "):
                user_input = user_input[9:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    try:
                        print(f"Executing the following command on openSUSE: {user_input}")
                        result = run_command(f"wsl -d openSUSE-Leap {user_input}", shell=True)
                        if result is None:
                            print("The command could not be executed successfully.")
                        else:
                            print("Command output:")
                            print(result)
                    except Exception as e:
                        print(f"An error occurred while executing the command: {e}")

            elif user_input.startswith("mint "):
                user_input = user_input[5:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    try:
                        print(f"Executing the following command on Linux Mint: {user_input}")
                        result = run_command(f"wsl -d LinuxMint {user_input}", shell=True)
                        if result is None:
                            print("The command could not be executed successfully.")
                        else:
                            print("Command output:")
                            print(result)
                    except Exception as e:
                        print(f"An error occurred while executing the command: {e}")

            elif user_input.startswith("fedora "):
                user_input = user_input[7:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    try:
                        print(f"Executing the following command on Fedora: {user_input}")
                        result = run_command(f"wsl -d Fedora-Remix {user_input}", shell=True)
                        if result is None:
                            print("The command could not be executed successfully.")
                        else:
                            print("Command output:")
                            print(result)
                    except Exception as e:
                        print(f"An error occurred while executing the command: {e}")

            elif user_input.startswith("redhat "):
                user_input = user_input[7:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    try:
                        print(f"Executing the following command on Red Hat: {user_input}")
                        result = run_command(f"wsl -d RedHat {user_input}", shell=True)
                        if result is None:
                            print("The command could not be executed successfully.")
                        else:
                            print("Command output:")
                            print(result)
                    except Exception as e:
                        print(f"An error occurred while executing the command: {e}")

            elif user_input.startswith("sc "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command with scoop: {user_input}")
                    run_scoop_command(user_input)

            elif user_input.startswith("cho "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command with choco: {user_input}")
                    run_choco_command(user_input)

            elif user_input.startswith("winget "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command with winget : {user_input}")
                    run_winget_command(user_input)

            else:
                run_command(user_input, shell=True)

            sys.stdout.flush()
            sys.stderr.flush()

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)


if __name__ == "__main__":
    main()
