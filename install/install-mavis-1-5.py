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
import requests
from typing import List
import re
import time
from typing import Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

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
        response = input(f"{message} [y/n]:").strip().lower()
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

import locale

def get_package_version(package: str) -> str:
    """Holt sich die aktuell installierte Version des Pakets."""
    try:
        output = subprocess.check_output([sys.executable, "-m", "pip", "show", package], stderr=subprocess.DEVNULL)
        encoding = locale.getpreferredencoding()  # Lokale Standardkodierung ermitteln
        for line in output.decode(encoding).splitlines():
            if line.startswith("Version:"):
                return line.split(":")[1].strip()
    except subprocess.CalledProcessError:
        return None

def get_latest_package_version(package: str, timeout: int = 10, retries: int = 3, backoff_factor: float = 0.5) -> str:
    """
    Achtung Deutsch

    Holt die neueste Version eines Pakets von PyPI mit verbessertem Fehler- und Retry-Handling.

    Args:
        package (str): Der Name des Pakets.
        timeout (int): Timeout für die Netzwerkverbindung (Standard: 10 Sekunden).
        retries (int): Anzahl der automatischen Wiederholungsversuche bei Fehlern.
        backoff_factor (float): Faktor für exponentielles Backoff bei Wiederholungen.

    Returns:
        str: Die neueste Paketversion.

    Raises:
        ValueError: Ungültiger Paketname oder fehlende Versionsinformationen.
        ConnectionError: Netzwerkprobleme beim Zugriff auf PyPI.
        RuntimeError: Allgemeine Fehler beim Verarbeiten der Antwort.
    """
    # Paketname validieren
    if not re.match(r"^[a-zA-Z0-9_\-\.]+$", package):
        raise ValueError(f"Ungültiger Paketname: '{package}'.")

    url = f"https://pypi.org/pypi/{package}/json"

    # Session mit Retry-Strategie erstellen
    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],  # Fehler, bei denen Retry sinnvoll ist
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()  # HTTP-Fehler auslösen

        # JSON validieren
        try:
            package_info = response.json()
        except ValueError:
            raise RuntimeError(f"Ungültiges JSON-Format von PyPI für '{package}'.")

        # Version extrahieren
        version: Optional[str] = package_info.get("info", {}).get("version")
        if not version:
            raise ValueError(f"Keine Versionsinformationen für '{package}' gefunden.")

        return version

    except requests.exceptions.HTTPError as http_err:
        # Handling von Rate Limits (HTTP 429)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Rate-Limit erreicht. Neuer Versuch in {retry_after} Sekunden...")
            time.sleep(retry_after)
            return get_latest_package_version(package, timeout, retries - 1, backoff_factor)
        raise ConnectionError(f"HTTP-Fehler bei '{package}': {http_err}")

    except requests.exceptions.ConnectionError as conn_err:
        raise ConnectionError(f"Verbindungsfehler zu PyPI für '{package}': {conn_err}")

    except requests.exceptions.Timeout:
        raise TimeoutError(f"Timeout nach {timeout} Sekunden beim Abrufen von '{package}'.")

    except requests.exceptions.RequestException as req_err:
        raise ConnectionError(f"Allgemeiner Netzwerkfehler bei '{package}': {req_err}")

    except ValueError as json_err:
        raise RuntimeError(f"Ungültige JSON-Antwort für '{package}': {json_err}")

    except Exception as e:
        raise RuntimeError(f"Unerwarteter Fehler bei '{package}': {e}")

def install_or_update_package(package: str):
    """Installiert oder aktualisiert ein Paket basierend auf der Version."""
    if not is_package_installed(package):
        print(f"{package} is not installed. Installing now.")
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
        print(f"{package} has been installed.")
    else:
        current_version = get_package_version(package)
        latest_version = get_latest_package_version(package)

        if current_version != latest_version:
            print(f"{blue}{package} is installed, but an update is available.{reset}")
            print(f"   {blue}Current version{reset}: {current_version}\n   {blue}Latest version{reset}: {latest_version}.")
            print(f"{blue}Updating {package} to the latest version...{reset}")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package], check=True)
            print(f"{green}{package} has been upgraded to version {latest_version}.{reset}")
        else:
            print(f"{green}{package} is already up-to-date (version {current_version}).{reset}")

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
            install_or_update_package(package)
        else:
            install_package(package)

print(f"\nAll frameworks for {blue}MAVIS versions 1.2, 1.3, 1.4, and 1.5{reset} are currently being installed and updated.")

# Paketlisten
packages = [
    "Flask", "ollama", "jupyter", "jupyterlab", "Werkzeug", "markdown", "matplotlib", "plotly",
    "dash", "seaborn", "numpy", "sympy", "pandas", "geopandas", "scipy", "torch",
    "torchvision", "torchaudio", "tensorflow", "scikit-learn", "transformers",
    "altair", "vega_datasets", "altair_viewer", "ipython", "altair-saver", "kaleido",
    "vl-convert-python", "py-cpuinfo", "GPUtil", "requests", "astropy", "QuantLib",
    "openmdao", "pybullet", "monai", "fenics", "pydy", "pycalculix", "solidpython",
    "pyomo", "gekko", "casadi", "control", "pybullet", "h2o", "pint", "coolprop",
    "pythermo", "biopython", "opencv-python", "SimpleITK", "nilearn", "deepchem",
    "pymedtermino", "lifelines", "rdkit", "ase", "chempy", "shapely", "fiona",
    "cartopy", "statsmodels", "yfinance", "PySpice", "networkx", "schematics",
    "schemdraw", "ipywidgets", "pybullet", "vtk", "diagrams", "graphviz", '"pix2tex[gui]"',
    "pillow",
]

process_packages(packages)

if platform.system().lower() == "windows":
    print("\nSkipping uvloop installation: uvloop is not supported on Windows.")
else:
    uvloop_packages = ["uvloop"]
    process_packages(uvloop_packages)

print(f"\n{blue}To serve vllm, use the following commands{reset}:")
print("vllm serve 'Qwen/Qwen2-VL-7B-Instruct'")
print("or")
print("vllm serve 'Qwen/Qwen2-VL-7B-Instruct' --no-uvloop\n")
