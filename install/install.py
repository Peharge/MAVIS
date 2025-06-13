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
import sys
import platform
from typing import List

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

def confirm_action(message: str) -> bool:
    """Fordert den Benutzer zur Bestätigung auf."""
    while True:
        response = input(f"{message} [y/n]: ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def is_package_installed(package: str) -> bool:
    """Prüft, ob ein Paket installiert ist."""
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "show", package], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_or_update_package(package: str, upgrade: bool = False):
    """Installiert oder aktualisiert ein Paket basierend auf Benutzerbestätigung."""
    if upgrade:
        print(f"{package} is installed, checking for updates.")
        if confirm_action(f"Do you want to upgrade {package}?"):
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package], check=True)
            print(f"{green}{package} has been upgraded.{reset}")
        else:
            print(f"{yellow}Skipping upgrade for {package}.{reset}")
    else:
        print(f"{green}{package} is already installed and up-to-date.{reset}")

def install_package(package: str):
    """Installiert ein Paket basierend auf Benutzerbestätigung."""
    print(f"{red}{package} is not installed.{reset}")
    if confirm_action(f"Do you want to install {package}?"):
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
        print(f"{green}{package} has been installed.{reset}")
    else:
        print(f"{yellow}Skipping installation for {package}.{reset}")

def process_packages(packages: List[str], upgrade: bool = False):
    """Überprüft, installiert oder aktualisiert eine Liste von Paketen."""
    for idx, package in enumerate(packages, start=1):
        print(f"\n[{idx}/{len(packages)}] Checking package: {blue}{package}{reset}")
        if is_package_installed(package):
            install_or_update_package(package, upgrade=upgrade)
        else:
            install_package(package)

print(f"\nAll frameworks for {blue}MAVIS versions 1.2, 1.3 and 1.4{reset} are currently being installed and updated.")

# Paketlisten
packages = [
    "Flask", "ollama", "Werkzeug", "markdown", "matplotlib", "plotly",
    "dash", "seaborn", "numpy", "sympy", "pandas", "scipy", "torch", "torchvision",
    "torchaudio", "tensorflow", "scikit-learn", "transformers", "geopandas",
    "altair", "vega_datasets", "altair_viewer", "ipython", "altair-saver", "kaleido",
    "vl-convert-python", "py-cpuinfo", "GPUtil", "requests"
]

process_packages(packages, upgrade=False)

print("All frameworks for Mavis versions 1.3 and 1.4 are currently being installed and updated.")

specific_packages = [
    "qwen-vl-utils", "accelerate"
]

process_packages(specific_packages, upgrade=False)

print("All frameworks for Mavis versions 1.4 are currently being installed and updated.")

vllm_packages = ["vllm"]
process_packages(vllm_packages, upgrade=False)

if platform.system().lower() == "windows":
    print("\nSkipping uvloop installation: uvloop is not supported on Windows.")
else:
    uvloop_packages = ["uvloop"]
    process_packages(uvloop_packages, upgrade=False)

print("\nTo serve vllm, use the following commands:")
print("vllm serve 'Qwen/Qwen2-VL-7B-Instruct'")
print("or")
print("vllm serve 'Qwen/Qwen2-VL-7B-Instruct' --no-uvloop\n")
