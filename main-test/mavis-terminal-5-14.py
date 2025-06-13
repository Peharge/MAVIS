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
import logging
import os
import getpass
import subprocess
import logging
import shutil
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

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

{white} ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ███████╗{reset}
{white} ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██╔════╝{reset}
{white}    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ███████╗{reset}
{white}    ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ╚════██║{reset}
{white}    ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗    ███████║{reset}
{white}    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚══════╝{reset}
""")
    print(f"""A warm welcome, {blue}{user_name}{reset}, to MAVIS (MAth Visual Intelligent System) Terminal 5
Developed by Peharge and JK (Peharge Projects 2025)
Thank you so much for using MAVIS. We truly appreciate your support ❤️""")

    print(f"""
{blue}MAVIS Version{reset}: 4
{blue}MAVIS Launcher Version{reset}: 4
{blue}MAVIS Terminal Version{reset}: 5
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
        "env install": "install\\install-info-mavis-4.py",
        "install env": "install\\install-info-mavis-4.py",
        "install mavis3": "install\\install-info-mavis-4.py", # new
        "install mavis3.3": "install\\install-info-mavis-4.py", # new
        "install mavis4": "install\\install-info-mavis-4.py", # new
        "install mavis4.3": "install\\install-info-mavis-4.py", # new
        "mavis env install": "install\\install-info-mavis-4.py",
        "install mavis env": "install\\install-info-mavis-4.py",
        "env update": "install\\install-info-mavis-4.py",
        "update env": "install\\install-info-mavis-4.py",
        "mavis env update": "install\\install-info-mavis-4.py",
        "update mavis env": "install\\install-info-mavis-4.py",
        "update": "update\\update-repository-windows.py",
        "mavis update": "update\\update-repository-windows.py",
        "update mavis": "update\\update-repository-windows.py",
        "security": "security\\security_check-mavis-4.py",
        "mavis security": "security\\security_check-mavis-4.py",
        "securitycheck": "security\\security_check-mavis-4.py",
        "info": "mavis-terminal\\info.py",
        "mavis info": "mavis-terminal\\info.py",
        "info mavis": "mavis-terminal\\info.py",
        "neofetch": "mavis-terminal\\neofetch.py",
        "fastfetch": "mavis-terminal\\neofetch.py", # new
        "screenfetch": "mavis-terminal\\neofetch.py", # new
        "jupyter": "run-jup\\run-jup.py",
        "run jupyter": "run-jup\\run-jup.py",
        "run ju": "run-jup\\run-jup.py", # new
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
        "run mavis-4-3": "mavis-4-main.py",  # new
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
        "run ollama mavis-4": "install\\install-ollama-mavis-4.py",  # new
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
        "change models mavis-4": "install\\install-ollama-mavis-4.py",  # new
        "change models": "install\\install-ollama-mavis-4.py",  # new
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
        "run qwen-2-5-omni:7b": "mavis-terminal\\qwen-2-5-omni-7b.py",  # new
        "run qvq:72b": "mavis-terminal\\qvq-72b.py",  # new
        "run qwen-2-5-vl:32b": "mavis-terminal\\qwen-2-5-vl-32b.py",  # new
        "run qwen-2-5-vl:72b": "mavis-terminal\\qwen-2-5-vl-72b.py",  # new
        "run llama-4-maverick:17b": "mavis-terminal\\llama-4-maverick-17b.py",  # new
        "run llama-4-scout:17b": "mavis-terminal\\llama-4-scout-17b.py",  # new
        "run deepcoder:1.5b": "mavis-terminal\\deepcoder-1-5b.py",  # new
        "run deepcoder:14b": "mavis-terminal\\deepcoder-14b.py", # new
        "run mistral-small3.1": "mavis-terminal\\mistral-small-3-1.py",  # new
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
        "install qwen-2-5-omni:7b": "mavis-terminal\\qwen-2-5-omni-7b.py",  # new
        "install qvq:72b": "mavis-terminal\\qvq-72b.py",  # new
        "install qwen-2-5-vl:32b": "mavis-terminal\\qwen-2-5-vl-32b.py",  # new
        "install qwen-2-5-vl:72b": "mavis-terminal\\qwen-2-5-vl-72b.py",  # new
        "install llama-4-maverick:17b": "mavis-terminal\\llama-4-maverick-17b.py",  # new
        "install llama-4-scout:17b": "mavis-terminal\\llama-4-scout-17b.py",  # new
        "install deepcoder:1.5b": "mavis-terminal\\deepcoder-1-5b.py",  # new
        "install deepcoder:14b": "mavis-terminal\\deepcoder-14b.py",  # new
        "install mistral-small3.1": "mavis-terminal\\mistral-small-3-1.py",  # new
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
        "m kali.com": "mavis-terminal\\m-kali.py",  # new
        "m mint.com": "mavis-terminal\\m-mint.py",  # new
        "m monai.com": "mavis-terminal\\m-monai.py",  # new
        "m monai-github.com": "mavis-terminal\\m-monai-git.py",  # new
        "m python.com": "mavis-terminal\\m-python.py",  # new
        "m pytorch.com": "mavis-terminal\\m-pytorch.py",  # new
        "m pytorch-github.com": "mavis-terminal\\m-pytorch-git.py",  # new
        "m ubuntu.com": "mavis-terminal\\m-ubuntu.py",  # new
        "m 3dslicer-github.com": "mavis-terminal\\m-3dslicer-git.py",  # new
        "m 3dslicer.com": "mavis-terminal\\m-3dslicer-web.py",  # new
        "m arch.com": "mavis-terminal\\m-arch.py",  # new
        "m debian.com": "mavis-terminal\\m-debian.py",  # new
        "m google.com": "mavis-terminal\\m-google.py",  # new
        "m ollama.com": "mavis-terminal\\m-ollama.py",  # new
        "m huggingface.com": "mavis-terminal\\m-huggingface.py",  # new
        "m mavis": "mavis-terminal\\m-mavis-git.py",  # new
        "m mavis.com": "mavis-terminal\\m-mavis.py",  # new
        "m simon": "mavis-terminal\\m-simon.py",  # new
        "m simon.com": "mavis-terminal\\m-simon-git.py", # new
        "install 3d-slicer": "run\\simon\\3d-slicer\\install-3d-slicer.py", # new
        "run 3d-slicer": "run\\simon\\3d-slicer\\run-3d-slicer.py",  # new
        "install simon": "run\\simon\\install-simon-1.py",  # new
        "run simon": "run-jup\\run-jup.py",  # new
        "jupyter --version": "mavis-terminal\\jupyter-version.py", # new
        "grafana --version": "mavis-terminal\\grafana-version.py",  # new
        "3d-slicer --version": "mavis-terminal\\3d-slicer-version.py",  # new
        "doctor": "mavis-terminal\\doctor.py" # new
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
    commands = ["cd", "cls", "clear", "dir", "ls", "mkdir", "rmdir", "del", "rm", "echo", "type", "cat", "exit", "lx", "m", "mp",
                "ubuntu", "debian", "kali", "hack", "arch", "etc."]
    readline.set_completer(lambda text, state: [cmd for cmd in commands if cmd.startswith(text)][state] if state < len(
        [cmd for cmd in commands if cmd.startswith(text)]) else None)
    readline.parse_and_bind("tab: complete")

def search_websites(command):
    """Searches for websites related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': command}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")

def find_vcvarsall():
    """
    Sucht nach der Visual Studio-Initialisierungsdatei (vcvarsall.bat).
    """
    path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if os.path.isfile(path):
        return path
    raise FileNotFoundError("vcvarsall.bat not found. Please make sure Visual Studio is installed.")

def find_vcvarsall_c():
    """
    Sucht nach der Visual Studio Entwicklungsumgebung (vcvarsall.bat).
    """
    # Visual Studio Installationspfad (Standardort für VS 2022)
    vs_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if not os.path.isfile(vs_path):
        logging.error("Visual Studio vcvarsall.bat file not found.")
        raise FileNotFoundError("vcvarsall.bat not found. Please ensure Visual Studio is installed.")
    return vs_path

# --- mp command---

def get_project_paths_mp():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    mp_cpp_file = os.path.join(terminal_dir, "run_mp_command.cpp")
    mp_exe_file = os.path.join(terminal_dir, "run_mp_command.exe")
    return mp_cpp_file, mp_exe_file, terminal_dir

def compile_mp_cpp_with_vs(mp_cpp_file, mp_exe_file):
    """
    Kompiliert run_mp_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_mp_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{mp_cpp_file}" /Fe:"{mp_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_command_with_admin_privileges(command):
    """
    Führt einen Powershell interaktiv über den C++-Wrapper aus.

    Falls run_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mp_cpp_file, mp_exe_file, _ = get_project_paths_mp()

    if not os.path.isfile(mp_exe_file):
        if not compile_mp_cpp_with_vs(mp_cpp_file, mp_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [mp_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- mp-c command---

def get_project_paths_mp_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    mp_c_file = os.path.join(terminal_dir, "run_mp_command.c")
    mp_c_exe_file = os.path.join(terminal_dir, "run_mp_c_command.exe")
    return mp_c_file, mp_c_exe_file, terminal_dir

def compile_mp_c_with_vs(mp_c_file, mp_c_exe_file):
    """
    Kompiliert run_mp_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_mp_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{mp_c_file}" /Fe:"{mp_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_command_with_admin_c_privileges(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_mp_c_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mp_c_file, mp_c_exe_file, _ = get_project_paths_mp_c()

    if not os.path.isfile(mp_c_exe_file):
        if not compile_mp_c_with_vs(mp_c_file, mp_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [mp_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- mp-p command---

def run_command_with_admin_python_privileges(command):
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

# --- lx command---

def get_project_paths_lx():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    lx_cpp_file = os.path.join(terminal_dir, "run_lx_command.cpp")
    lx_exe_file = os.path.join(terminal_dir, "run_lx_command.exe")
    return lx_cpp_file, lx_exe_file, terminal_dir

def compile_lx_cpp_with_vs(lx_cpp_file, lx_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_lx_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{lx_cpp_file}" /Fe:"{lx_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_linux_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    lx_cpp_file, lx_exe_file, _ = get_project_paths_lx()

    if not os.path.isfile(lx_exe_file):
        if not compile_lx_cpp_with_vs(lx_cpp_file, lx_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [lx_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- lx-c command---

def get_project_paths_lx_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    lx_c_file = os.path.join(terminal_dir, "run_lx_command.c")
    lx_c_exe_file = os.path.join(terminal_dir, "run_lx_c_command.exe")
    return lx_c_file, lx_c_exe_file, terminal_dir

def compile_lx_c_with_vs(lx_c_file, lx_c_exe_file):
    """
    Kompiliert run_lx_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_lx_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{lx_c_file}" /Fe:"{lx_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_linux_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    lx_c_file, lx_c_exe_file, _ = get_project_paths_lx_c()

    if not os.path.isfile(lx_c_exe_file):
        if not compile_lx_c_with_vs(lx_c_file, lx_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [lx_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- lx-p command---

def run_linux_python_command(command):
    if isinstance(command, str):
        command = f"wsl -e {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- ubuntu command---

def get_project_paths_ubuntu():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    ubuntu_cpp_file = os.path.join(terminal_dir, "run_ubuntu_command.cpp")
    ubuntu_exe_file = os.path.join(terminal_dir, "run_ubuntu_command.exe")
    return ubuntu_cpp_file, ubuntu_exe_file, terminal_dir

def compile_ubuntu_cpp_with_vs(ubuntu_cpp_file, ubuntu_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_ubuntu_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{ubuntu_cpp_file}" /Fe:"{ubuntu_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_ubuntu_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_ubuntu_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    ubuntu_cpp_file, ubuntu_exe_file, _ = get_project_paths_ubuntu()

    if not os.path.isfile(ubuntu_exe_file):
        if not compile_ubuntu_cpp_with_vs(ubuntu_cpp_file, ubuntu_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [ubuntu_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- ubuntu-c command---

def get_project_paths_ubuntu_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    ubuntu_c_file = os.path.join(terminal_dir, "run_ubuntu_command.c")
    ubuntu_c_exe_file = os.path.join(terminal_dir, "run_ubuntu_c_command.exe")
    return ubuntu_c_file, ubuntu_c_exe_file, terminal_dir

def compile_ubuntu_c_with_vs(ubuntu_c_file, ubuntu_c_exe_file):
    """
    Kompiliert run_ubuntu_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_ubuntu_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{ubuntu_c_file}" /Fe:"{ubuntu_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_ubuntu_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_ubuntu_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    ubuntu_c_file, ubuntu_c_exe_file, _ = get_project_paths_ubuntu_c()

    if not os.path.isfile(ubuntu_c_exe_file):
        if not compile_ubuntu_c_with_vs(ubuntu_c_file, ubuntu_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [ubuntu_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- ubuntu-p command---

def run_ubuntu_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d ubuntu {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- debian command---

def get_project_paths_debian():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    debian_cpp_file = os.path.join(terminal_dir, "run_debian_command.cpp")
    debian_exe_file = os.path.join(terminal_dir, "run_debian_command.exe")
    return debian_cpp_file, debian_exe_file, terminal_dir

def compile_debian_cpp_with_vs(debian_cpp_file, debian_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_debian_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{debian_cpp_file}" /Fe:"{debian_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_debian_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_debian_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    debian_cpp_file, debian_exe_file, _ = get_project_paths_debian()

    if not os.path.isfile(debian_exe_file):
        if not compile_debian_cpp_with_vs(debian_cpp_file, debian_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [debian_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- debian-c command---

def get_project_paths_debian_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    debian_c_file = os.path.join(terminal_dir, "run_debian_command.c")
    debian_c_exe_file = os.path.join(terminal_dir, "run_debian_c_command.exe")
    return debian_c_file, debian_c_exe_file, terminal_dir

def compile_debian_c_with_vs(debian_c_file, debian_c_exe_file):
    """
    Kompiliert run_debian_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_debian_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{debian_c_file}" /Fe:"{debian_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_debian_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_debian_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    debian_c_file, debian_c_exe_file, _ = get_project_paths_debian_c()

    if not os.path.isfile(debian_c_exe_file):
        if not compile_debian_c_with_vs(debian_c_file, debian_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [debian_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- debian-p command---

def run_debian_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d debian {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- kali command---

def get_project_paths_kali():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    kali_cpp_file = os.path.join(terminal_dir, "run_kali_command.cpp")
    kali_exe_file = os.path.join(terminal_dir, "run_kali_command.exe")
    return kali_cpp_file, kali_exe_file, terminal_dir

def compile_kali_cpp_with_vs(kali_cpp_file, kali_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_kali_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{kali_cpp_file}" /Fe:"{kali_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_kali_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_kali_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    kali_cpp_file, kali_exe_file, _ = get_project_paths_kali()

    if not os.path.isfile(kali_exe_file):
        if not compile_kali_cpp_with_vs(kali_cpp_file, kali_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [kali_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- kali-c command---

def get_project_paths_kali_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    kali_c_file = os.path.join(terminal_dir, "run_kali_command.c")
    kali_c_exe_file = os.path.join(terminal_dir, "run_kali_c_command.exe")
    return kali_c_file, kali_c_exe_file, terminal_dir

def compile_kali_c_with_vs(kali_c_file, kali_c_exe_file):
    """
    Kompiliert run_kali_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_kali_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{kali_c_file}" /Fe:"{kali_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_kali_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    kali_c_file, kali_c_exe_file, _ = get_project_paths_kali_c()

    if not os.path.isfile(kali_c_exe_file):
        if not compile_kali_c_with_vs(kali_c_file, kali_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [kali_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- kali-p command---

def run_kali_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d kali-linux {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- arch command---

def get_project_paths_arch():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    arch_cpp_file = os.path.join(terminal_dir, "run_arch_command.cpp")
    arch_exe_file = os.path.join(terminal_dir, "run_arch_command.exe")
    return arch_cpp_file, arch_exe_file, terminal_dir

def compile_arch_cpp_with_vs(arch_cpp_file, arch_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_arch_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{arch_cpp_file}" /Fe:"{arch_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_arch_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    arch_cpp_file, arch_exe_file, _ = get_project_paths_arch()

    if not os.path.isfile(arch_exe_file):
        if not compile_arch_cpp_with_vs(arch_cpp_file, arch_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [arch_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- arch-c command---

def get_project_paths_arch_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    arch_c_file = os.path.join(terminal_dir, "run_arch_command.c")
    arch_c_exe_file = os.path.join(terminal_dir, "run_arch_c_command.exe")
    return arch_c_file, arch_c_exe_file, terminal_dir

def compile_arch_c_with_vs(arch_c_file, arch_c_exe_file):
    """
    Kompiliert run_arch_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_arch_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{arch_c_file}" /Fe:"{arch_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_arch_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_larch_c_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    arch_c_file, arch_c_exe_file, _ = get_project_paths_arch_c()

    if not os.path.isfile(arch_c_exe_file):
        if not compile_arch_c_with_vs(arch_c_file, arch_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [arch_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- arch-p command---

def run_arch_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d Arch {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- opensuse command---

def get_project_paths_opensuse():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    opensuse_cpp_file = os.path.join(terminal_dir, "run_opensuse_command.cpp")
    opensuse_exe_file = os.path.join(terminal_dir, "run_opensuse_command.exe")
    return opensuse_cpp_file, opensuse_exe_file, terminal_dir

def compile_opensuse_cpp_with_vs(opensuse_cpp_file, opensuse_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_opensuse_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{opensuse_cpp_file}" /Fe:"{opensuse_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_opensuse_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    opensuse_cpp_file, opensuse_exe_file, _ = get_project_paths_opensuse()

    if not os.path.isfile(opensuse_exe_file):
        if not compile_opensuse_cpp_with_vs(opensuse_cpp_file, opensuse_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [opensuse_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- opensuse-c command---

def get_project_paths_opensuse_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    opensuse_c_file = os.path.join(terminal_dir, "run_opensuse_command.c")
    opensuse_c_exe_file = os.path.join(terminal_dir, "run_opensuse_c_command.exe")
    return opensuse_c_file, opensuse_c_exe_file, terminal_dir

def compile_opensuse_c_with_vs(opensuse_c_file, opensuse_c_exe_file):
    """
    Kompiliert run_opensuse_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_opensuse_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{opensuse_c_file}" /Fe:"{opensuse_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_opensuse_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_opensuse_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    opensuse_c_file, opensuse_c_exe_file, _ = get_project_paths_opensuse_c()

    if not os.path.isfile(opensuse_c_exe_file):
        if not compile_opensuse_c_with_vs(opensuse_c_file, opensuse_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [opensuse_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- opensuse-p command---

def run_opensuse_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d openSUSE-Leap {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- mint command---

def get_project_paths_mint():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    mint_cpp_file = os.path.join(terminal_dir, "run_mint_command.cpp")
    mint_exe_file = os.path.join(terminal_dir, "run_mint_command.exe")
    return mint_cpp_file, mint_exe_file, terminal_dir

def compile_mint_cpp_with_vs(mint_cpp_file, mint_exe_file):
    """
    Kompiliert run_mint_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_mint_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{mint_cpp_file}" /Fe:"{mint_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_mint_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mint_cpp_file, mint_exe_file, _ = get_project_paths_mint()

    if not os.path.isfile(mint_exe_file):
        if not compile_mint_cpp_with_vs(mint_cpp_file, mint_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [mint_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- mint-c command---

def get_project_paths_mint_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    mint_c_file = os.path.join(terminal_dir, "run_mint_command.c")
    mint_c_exe_file = os.path.join(terminal_dir, "run_mint_c_command.exe")
    return mint_c_file, mint_c_exe_file, terminal_dir

def compile_mint_c_with_vs(mint_c_file, mint_c_exe_file):
    """
    Kompiliert run_mint_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_mint_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{mint_c_file}" /Fe:"{mint_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_mint_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_mint_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mint_c_file, mint_c_exe_file, _ = get_project_paths_mint_c()

    if not os.path.isfile(mint_c_exe_file):
        if not compile_mint_c_with_vs(mint_c_file, mint_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [mint_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- mint-p command---

def run_mint_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d mint {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- fedora command---

def get_project_paths_fedora():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    fedora_cpp_file = os.path.join(terminal_dir, "run_fedora_command.cpp")
    fedora_exe_file = os.path.join(terminal_dir, "run_fedora_command.exe")
    return fedora_cpp_file, fedora_exe_file, terminal_dir

def compile_fedora_cpp_with_vs(fedora_cpp_file, fedora_exe_file):
    """
    Kompiliert run_fedora_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_fedora_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{fedora_cpp_file}" /Fe:"{fedora_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_fedora_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    fedora_cpp_file, fedora_exe_file, _ = get_project_paths_fedora()

    if not os.path.isfile(fedora_exe_file):
        if not compile_fedora_cpp_with_vs(fedora_cpp_file, fedora_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [fedora_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- fedora-c command---

def get_project_paths_fedora_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    fedora_c_file = os.path.join(terminal_dir, "run_fedora_command.c")
    fedora_c_exe_file = os.path.join(terminal_dir, "run_fedora_c_command.exe")
    return fedora_c_file, fedora_c_exe_file, terminal_dir

def compile_fedora_c_with_vs(fedora_c_file, fedora_c_exe_file):
    """
    Kompiliert run_fedora_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_fedora_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{fedora_c_file}" /Fe:"{fedora_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_fedora_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_fedora_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    fedora_c_file, fedora_c_exe_file, _ = get_project_paths_fedora_c()

    if not os.path.isfile(fedora_c_exe_file):
        if not compile_fedora_c_with_vs(fedora_c_file, fedora_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [fedora_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- fedora-p command---

def run_fedora_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d -d Fedora-Remix {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- redhat command---

def get_project_paths_redhat():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    redhat_cpp_file = os.path.join(terminal_dir, "run_redhat_command.cpp")
    redhat_exe_file = os.path.join(terminal_dir, "run_redhat_command.exe")
    return redhat_cpp_file, redhat_exe_file, terminal_dir

def compile_redhat_cpp_with_vs(redhat_cpp_file, redhat_exe_file):
    """
    Kompiliert run_redhat_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_redhat_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{redhat_cpp_file}" /Fe:"{redhat_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_redhat_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_redhat_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    redhat_cpp_file, redhat_exe_file, _ = get_project_paths_redhat()

    if not os.path.isfile(redhat_exe_file):
        if not compile_redhat_cpp_with_vs(redhat_cpp_file, redhat_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [redhat_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- redhat-c command---

def get_project_paths_redhat_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    redhat_c_file = os.path.join(terminal_dir, "run_redhat_command.c")
    redhat_c_exe_file = os.path.join(terminal_dir, "run_redhat_c_command.exe")
    return redhat_c_file, redhat_c_exe_file, terminal_dir

def compile_redhat_c_with_vs(redhat_c_file, redhat_c_exe_file):
    """
    Kompiliert run_redhat_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_redhat_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{redhat_c_file}" /Fe:"{redhat_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_redhat_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_redhat_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    redhat_c_file, redhat_c_exe_file, _ = get_project_paths_redhat_c()

    if not os.path.isfile(redhat_c_exe_file):
        if not compile_redhat_c_with_vs(redhat_c_file, redhat_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [redhat_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- redhat-p command---

def run_redhat_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d RedHat {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- sles command---

def get_project_paths_sles():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    sles_cpp_file = os.path.join(terminal_dir, "run_sles_command.cpp")
    sles_exe_file = os.path.join(terminal_dir, "run_sles_command.exe")
    return sles_cpp_file, sles_exe_file, terminal_dir

def compile_sles_cpp_with_vs(sles_cpp_file, sles_exe_file):
    """
    Kompiliert run_sles_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_sles_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{sles_cpp_file}" /Fe:"{sles_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_sles_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_sles_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    sles_cpp_file, sles_exe_file, _ = get_project_paths_sles()

    if not os.path.isfile(sles_exe_file):
        if not compile_sles_cpp_with_vs(sles_cpp_file, sles_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [sles_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- sles-c command---

def get_project_paths_sles_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    sles_c_file = os.path.join(terminal_dir, "run_sles_command.c")
    sles_c_exe_file = os.path.join(terminal_dir, "run_sles_c_command.exe")
    return sles_c_file, sles_c_exe_file, terminal_dir

def compile_sles_c_with_vs(sles_c_file, sles_c_exe_file):
    """
    Kompiliert run_sles_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_sles_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{sles_c_file}" /Fe:"{sles_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_sles_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_sles_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    sles_c_file, sles_c_exe_file, _ = get_project_paths_sles_c()

    if not os.path.isfile(sles_c_exe_file):
        if not compile_sles_c_with_vs(sles_c_file, sles_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [sles_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- sles-p command---

def run_sles_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d SLES {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- pengwin command---

def get_project_paths_pengwin():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    pengwin_cpp_file = os.path.join(terminal_dir, "run_pengwin_command.cpp")
    pengwin_exe_file = os.path.join(terminal_dir, "run_pengwin_command.exe")
    return pengwin_cpp_file, pengwin_exe_file, terminal_dir

def compile_pengwin_cpp_with_vs(pengwin_cpp_file, pengwin_exe_file):
    """
    Kompiliert run_pengwin_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_pengwin_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{pengwin_cpp_file}" /Fe:"{pengwin_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_pengwin_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_pengwin_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    pengwin_cpp_file, pengwin_exe_file, _ = get_project_paths_pengwin()

    if not os.path.isfile(pengwin_exe_file):
        if not compile_pengwin_cpp_with_vs(pengwin_cpp_file, pengwin_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [pengwin_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- pengwin-c command---

def get_project_paths_pengwin_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    pengwin_c_file = os.path.join(terminal_dir, "run_pengwin_command.c")
    pengwin_c_exe_file = os.path.join(terminal_dir, "run_pengwin_c_command.exe")
    return pengwin_c_file, pengwin_c_exe_file, terminal_dir

def compile_pengwin_c_with_vs(pengwin_c_file, pengwin_c_exe_file):
    """
    Kompiliert run_pengwin_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_pengwin_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{pengwin_c_file}" /Fe:"{pengwin_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_pengwin_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_pengwin_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    pengwin_c_file, pengwin_c_exe_file, _ = get_project_paths_pengwin_c()

    if not os.path.isfile(pengwin_c_exe_file):
        if not compile_pengwin_c_with_vs(pengwin_c_file, pengwin_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [pengwin_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- pengwin-p command---

def run_pengwin_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d Pengwin {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- oracle command---

def get_project_paths_oracle():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    oracle_cpp_file = os.path.join(terminal_dir, "run_oracle_command.cpp")
    oracle_exe_file = os.path.join(terminal_dir, "run_oracle_command.exe")
    return oracle_cpp_file, oracle_exe_file, terminal_dir

def compile_oracle_cpp_with_vs(oracle_cpp_file, oracle_exe_file):
    """
    Kompiliert run_oracle_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_oracle_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{oracle_cpp_file}" /Fe:"{oracle_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_oracle_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_oracle_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    oracle_cpp_file, oracle_exe_file, _ = get_project_paths_oracle()

    if not os.path.isfile(oracle_exe_file):
        if not compile_oracle_cpp_with_vs(oracle_cpp_file, oracle_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [oracle_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- oracle-c command---

def get_project_paths_oracle_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    oracle_c_file = os.path.join(terminal_dir, "run_oracle_command.c")
    oracle_c_exe_file = os.path.join(terminal_dir, "run_oracle_c_command.exe")
    return oracle_c_file, oracle_c_exe_file, terminal_dir

def compile_oracle_c_with_vs(oracle_c_file, oracle_c_exe_file):
    """
    Kompiliert run_oracle_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_oracle_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{oracle_c_file}" /Fe:"{oracle_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_oracle_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_oracle_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    oracle_c_file, oracle_c_exe_file, _ = get_project_paths_oracle_c()

    if not os.path.isfile(oracle_c_exe_file):
        if not compile_oracle_c_with_vs(oracle_c_file, oracle_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [oracle_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- oracle-p command---

def run_oracle_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d OracleLinux {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- alpine command---

def get_project_paths_alpine():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    alpine_cpp_file = os.path.join(terminal_dir, "run_alpine_command.cpp")
    alpine_exe_file = os.path.join(terminal_dir, "run_alpine_command.exe")
    return alpine_cpp_file, alpine_exe_file, terminal_dir

def compile_alpine_cpp_with_vs(alpine_cpp_file, alpine_exe_file):
    """
    Kompiliert run_alpine_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_alpine_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{alpine_cpp_file}" /Fe:"{alpine_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_alpine_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_alpine_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    alpine_cpp_file, alpine_exe_file, _ = get_project_paths_alpine()

    if not os.path.isfile(alpine_exe_file):
        if not compile_alpine_cpp_with_vs(alpine_cpp_file, alpine_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [alpine_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- alpine-c command---

def get_project_paths_alpine_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    alpine_c_file = os.path.join(terminal_dir, "run_alpine_command.c")
    alpine_c_exe_file = os.path.join(terminal_dir, "run_alpine_c_command.exe")
    return alpine_c_file, alpine_c_exe_file, terminal_dir

def compile_alpine_c_with_vs(alpine_c_file, alpine_c_exe_file):
    """
    Kompiliert run_alpine_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_alpine_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{alpine_c_file}" /Fe:"{alpine_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_alpine_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_alpine_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    alpine_c_file, alpine_c_exe_file, _ = get_project_paths_alpine_c()

    if not os.path.isfile(alpine_c_exe_file):
        if not compile_alpine_c_with_vs(alpine_c_file, alpine_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [alpine_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- alpine-p command---

def run_alpine_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d Alpine {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# --- clear command---

def get_project_paths_clear():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    clear_cpp_file = os.path.join(terminal_dir, "run_clear_command.cpp")
    clear_exe_file = os.path.join(terminal_dir, "run_clear_command.exe")
    return clear_cpp_file, clear_exe_file, terminal_dir

def compile_clear_cpp_with_vs(clear_cpp_file, clear_exe_file):
    """
    Kompiliert run_clear_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_clear_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{clear_cpp_file}" /Fe:"{clear_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True

def run_clear_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_clear_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    clear_cpp_file, clear_exe_file, _ = get_project_paths_clear()

    if not os.path.isfile(clear_exe_file):
        if not compile_clear_cpp_with_vs(clear_cpp_file, clear_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [clear_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- clear-c command---

def get_project_paths_clear_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis, den Ordner 'mavis-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    terminal_dir = os.path.join(base_dir, "mavis-terminal")
    clear_c_file = os.path.join(terminal_dir, "run_clear_command.c")
    clear_c_exe_file = os.path.join(terminal_dir, "run_clear_c_command.exe")
    return clear_c_file, clear_c_exe_file, terminal_dir

def compile_clear_c_with_vs(clear_c_file, clear_c_exe_file):
    """
    Kompiliert run_clear_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_clear_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{clear_c_file}" /Fe:"{clear_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_clear_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_clear_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    clear_c_file, clear_c_exe_file, _ = get_project_paths_clear_c()

    if not os.path.isfile(clear_c_exe_file):
        if not compile_clear_c_with_vs(clear_c_file, clear_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [clear_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- clear-p command---

def run_clear_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d ClearLinux {command}"

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
            # Prüfen, ob eine .env-Datei existiert und geladen ist
            env_active = os.getenv('VIRTUAL_ENV') or os.path.exists('.env')

            # .env-Indikator
            env_indicator = f"{green}[{reset}.\\MAVIS\\.env{green}]{reset}" if env_active else f"{green}[{reset}{red}.\\MAVIS\\.env{reset}{green}]{reset}"

            # Prompt-Design
            prompt = (
                f"\n{green}┌──({reset}{blue}{getpass.getuser()}㉿MAVIS{reset}{green})-[{reset}{current_dir}{green}]-{reset}{env_indicator}"
                f"\n{green}└─{reset}{blue}#{reset}"
            )

            print(prompt, end='')
            user_input = input().strip()

            if handle_special_commands(user_input):
                continue
            elif user_input.startswith("mp "):
                user_input = user_input[3:]

                run_command_with_admin_privileges(user_input)
            elif user_input.startswith("mp-c "):
                user_input = user_input[5:]

                run_command_with_admin_c_privileges(user_input)
            elif user_input.startswith("mp-p "):
                user_input = user_input[5:]

                run_command_with_admin_python_privileges(user_input)
            elif user_input.startswith("powershell "):
                run_command(user_input, shell=True)

            elif user_input.startswith("ms "):
                user_input = user_input[3:].strip()
                search_websites(user_input)

            elif user_input.startswith("lx "):
                user_input = user_input[3:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-cpp "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-c "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_c_command(user_input)

            elif user_input.startswith("lx-p "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_python_command(user_input)

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

            elif user_input.startswith("ubuntu-c "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_c_command(user_input)

            elif user_input.startswith("ubuntu-p "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_python_command(user_input)

            elif user_input.startswith("debian "):
                user_input = user_input[7:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Debian: {user_input}")
                    run_debian_command(user_input)

            elif user_input.startswith("debian-c "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Debian: {user_input}")
                    run_debian_c_command(user_input)

            elif user_input.startswith("debian-p "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Debian: {user_input}")
                    run_debian_python_command(user_input)

            elif user_input.startswith("kali "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("kali-c "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_c_command(user_input)

            elif user_input.startswith("kali-p "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_python_command(user_input)

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

            elif user_input.startswith("arch-c "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Arch: {user_input}")
                    run_arch_c_command(user_input)

            elif user_input.startswith("arch-p "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Arch: {user_input}")
                    run_arch_python_command(user_input)

            elif user_input.startswith("openSUSE "):
                user_input = user_input[9:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_opensuse_command(user_input)

            elif user_input.startswith("openSUSE-c "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_opensuse_c_command(user_input)

            elif user_input.startswith("openSUSE-p "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_opensuse_python_command(user_input)

            elif user_input.startswith("mint "):
                user_input = user_input[5:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_mint_command(user_input)

            elif user_input.startswith("mint-c "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_mint_c_command(user_input)

            elif user_input.startswith("mint-p "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_mint_python_command(user_input)

            elif user_input.startswith("fedora "):
                user_input = user_input[7:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Fedora: {user_input}")
                    run_fedora_command(user_input)

            elif user_input.startswith("fedora-c "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Fedora: {user_input}")
                    run_fedora_c_command(user_input)

            elif user_input.startswith("fedora-p "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Fedora: {user_input}")
                    run_fedora_python_command(user_input)

            elif user_input.startswith("redhat "):
                user_input = user_input[7:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on RedHat: {user_input}")
                    run_redhat_command(user_input)

            elif user_input.startswith("redhat-c "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on RedHat: {user_input}")
                    run_redhat_c_command(user_input)

            elif user_input.startswith("redhat-p "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on RedHat: {user_input}")
                    run_redhat_python_command(user_input)

            elif user_input.startswith("sles "):
                user_input = user_input[7:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on SLES: {user_input}")
                    run_sles_command(user_input)

            elif user_input.startswith("sles-c "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on SLES: {user_input}")
                    run_sles_c_command(user_input)

            elif user_input.startswith("sles-p "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on SLES: {user_input}")
                    run_sles_python_command(user_input)

            elif user_input.startswith("pengwin "):
                user_input = user_input[7:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Pengwin: {user_input}")
                    run_pengwin_command(user_input)

            elif user_input.startswith("pengwin-c "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Pengwin: {user_input}")
                    run_pengwin_c_command(user_input)

            elif user_input.startswith("pengwin-p "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Pengwin: {user_input}")
                    run_pengwin_python_command(user_input)

            elif user_input.startswith("oracle "):
                user_input = user_input[7:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Oracle: {user_input}")
                    run_oracle_command(user_input)

            elif user_input.startswith("oracle-c "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Oracle: {user_input}")
                    run_oracle_c_command(user_input)

            elif user_input.startswith("oracle-p "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Oracle: {user_input}")
                    run_oracle_python_command(user_input)

            elif user_input.startswith("alpine "):
                user_input = user_input[7:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Alpine: {user_input}")
                    run_alpine_command(user_input)

            elif user_input.startswith("alpine-c "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Alpine: {user_input}")
                    run_alpine_c_command(user_input)

            elif user_input.startswith("alpine-p "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Alpine: {user_input}")
                    run_alpine_python_command(user_input)

            elif user_input.startswith("clear "):
                user_input = user_input[7:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Clear: {user_input}")
                    run_clear_command(user_input)

            elif user_input.startswith("clear-c "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Clear: {user_input}")
                    run_clear_c_command(user_input)

            elif user_input.startswith("clear-p "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Clear: {user_input}")
                    run_clear_python_command(user_input)

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
