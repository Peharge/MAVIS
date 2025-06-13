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
import importlib.util

required_packages = ["requests", "Flask", "numpy", "pandas", "python-dotenv", "pipdeptree", "urllib3", "PyQt6", "pipdeptree", "jupyter_server_terminals"]

def ensure_packages_installed(packages):
    """Stellt sicher, dass alle erforderlichen Pakete installiert sind."""
    for package in packages:
        if importlib.util.find_spec(package) is None:
            print(f"Installing {package}...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"{package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"WARNING: Failed to install {package}. Please install it manually.")
        else:
            print(f"{package} is already installed.")

# Stellen Sie sicher, dass alle erforderlichen Pakete installiert sind
ensure_packages_installed(required_packages)

import requests
import re
import time
from typing import Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import locale
from typing import List, Dict
import subprocess
import requests
import re
import time
from typing import Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import importlib.metadata

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
        print("Invalid input. Please enter 'y/yes' or 'n/no'.")

def is_package_installed(package: str) -> bool:
    """Prüft, ob ein Paket installiert ist."""
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "show", package], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

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
        raise ValueError(f"Invalid package name: '{package}'.")

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
            raise RuntimeError(f"Invalid JSON format from PyPI for '{package}'.")

        # Version extrahieren
        version: Optional[str] = package_info.get("info", {}).get("version")
        if not version:
            raise ValueError(f"No version information found for '{package}'.")

        return version

    except requests.exceptions.HTTPError as http_err:
        # Handling von Rate Limits (HTTP 429)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Rate limit reached. Retry in {retry_after} seconds...")
            time.sleep(retry_after)
            return get_latest_package_version(package, timeout, retries - 1, backoff_factor)
        raise ConnectionError(f"HTTP error at '{package}': {http_err}")

    except requests.exceptions.ConnectionError as conn_err:
        raise ConnectionError(f"Connection error to PyPI for '{package}': {conn_err}")

    except requests.exceptions.Timeout:
        raise TimeoutError(f"Timeout after {timeout} seconds while retrieving '{package}'.")

    except requests.exceptions.RequestException as req_err:
        raise ConnectionError(f"General network error at '{package}': {req_err}")

    except ValueError as json_err:
        raise RuntimeError(f"Invalid JSON response for '{package}': {json_err}")

    except Exception as e:
        raise RuntimeError(f"Unexpected error in '{package}': {e}")


def get_latest_version(package):
    # Verwende pip, um die neueste Version des Pakets zu finden
    result = subprocess.run(['pip', 'index', 'versions', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)

    if result.returncode == 0:
        # Extrahiere die neueste Version aus dem Output
        latest_version_line = [line for line in result.stdout.splitlines() if 'Available versions' in line]
        if latest_version_line:
            latest_version = latest_version_line[0].split(":")[-1].strip().split(',')[-1].strip()
            return latest_version
        else:
            print(f"Fehler: Konnte die neueste Version von {package} nicht ermitteln.")
            return None
    else:
        print(f"Fehler beim Abrufen der neuesten Version von {package}: {result.stderr}")
        return None


def check_package_compatibility(package):
    # Hole die neueste verfügbare Version des Pakets
    current_version = get_package_version(package)
    latest_version = get_latest_package_version(package)

    if not latest_version:
        return

    installed_packages = {pkg.metadata['Name'].lower(): pkg.version for pkg in importlib.metadata.distributions()}

    print(f"{blue}{package} is outdated ({current_version} -> {latest_version}).{reset}")

    # Überprüfen Sie, ob das Paket bereits installiert ist und welche Version

    # Prüfe Inkompatibilitäten mit installierten Paketen
    print(f"\nCheck for incompatibilities with installed packages...")

    # Verwenden Sie pipdeptree, um alle Pakete und deren Abhängigkeiten zu überprüfen
    pipdeptree_result = subprocess.run([sys.executable, "-m", 'pipdeptree', '-r', '-p', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if pipdeptree_result.returncode == 0:
        # Pipdeptree liefert alle installierten Pakete und deren Abhängigkeiten
        # print(pipdeptree_result.stdout)

        incompatible_packages = pipdeptree_result.stdout.splitlines()
        for line in incompatible_packages:
            if package in line:
                # Extrahiere das Paket, das eine inkompatible Version benötigt
                print(f"{red}Incompatibility found with{reset}: {line}")
                # Optional: Wenn du mehr Details zu den Abhängigkeiten sehen möchtest, kannst du nach dem Paket suchen,
                # das eine inkompatible Version benötigt.
                package_dependency = line.split('==')[0]  # Extrahiere den Namen des Pakets
                print(f"{red}{package_dependency} requires an incompatible version of {package}{reset}")
    else:
        print(f"Error retrieving package dependencies: {pipdeptree_result.stderr}")

"""
# Funktion, um die Kompatibilität eines Pakets zu prüfen
def check_package_compatibility(package):
    # Hole die neueste Version des Pakets
    latest_version = get_latest_package_version(package)
    if not latest_version:
        return  # Abbrechen, wenn keine neueste Version ermittelt werden konnte

    print(f"Neueste Version von {package}: {latest_version}")

    # Alle aktuell installierten Pakete abrufen
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

    # Prüfe Kompatibilität der neuesten Version mit installierten Paketen
    print(f"\nPrüfe Inkompatibilitäten mit installierten Paketen...")
    incompatible_packages = []

    # Führe pip check aus, um Kompatibilitätsprobleme zu finden
    result = subprocess.run(['pip', 'check'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        # Fehlerbehandlung bei inkompatiblen Paketen
        output_lines = result.stderr.splitlines()
        for line in output_lines:
            if package in line:  # Prüfe auf Zeilen, die das Zielpaket betreffen
                incompatible_packages.append(line.strip())

    if incompatible_packages:
        print(f"Inkompatibilitäten gefunden:")
        for pkg in incompatible_packages:
            print(f"  - {pkg}")
    else:
        print(f"✅ Keine Inkompatibilitäten gefunden!")
"""

def install_or_update_package(package: str):
    """Fragt nach Bestätigung für Updates und zeigt Inkompatibilitäten an."""
    # installed_packages = {pkg: get_package_version(pkg) for pkg in packages}  # Alle installierten Pakete holen

    if not is_package_installed(package):
        if confirm_action(f"{package} is not installed. Do you want to install it?"):
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            print(f"{green}{package} has been installed.{reset}")
        else:
            print(f"{yellow}{package} will not be installed.{reset}")
    else:
        current_version = get_package_version(package)
        latest_version = get_latest_package_version(package)

        try:
            # Wenn aktuelle und neueste Versionen vorhanden sind und sie nicht übereinstimmen, wird die Inkompatibilitätsprüfung durchgeführt
            if current_version and latest_version and current_version != latest_version:
                # Überprüfe Inkompatibilitäten vor der Anzeige der veralteten Version

                """
                incompatibilities = check_dependency_compatibility(package, latest_version, installed_packages)

                if incompatibilities:
                    print(f"{red}Warning{reset}: The new version of {package} may cause incompatibilities!")
                    for issue in incompatibilities:
                        print(f"  {yellow}{issue}{reset}")

                """
                # Wenn keine Inkompatibilitäten gefunden wurden, fahren wir fort und zeigen die veraltete Version an
                check_package_compatibility(package)
                if confirm_action(f"\nDo you want to update {package} to {latest_version}?"):
                    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package], check=True)
                    print(f"{green}{package} was updated to version {latest_version}.{reset}")
                    print(f"\nCheck again for incompatibilities after installation...")
                    pipdeptree_result = subprocess.run([sys.executable, "-m", 'pipdeptree', '-r', '-p', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                    if pipdeptree_result.returncode == 0:
                        print("Packages installed after installation:")
                        print(pipdeptree_result.stdout)

                        incompatible_packages = pipdeptree_result.stdout.splitlines()
                        for line in incompatible_packages:
                            if package in line:
                                print(f"Incompatibility found after update with: {line}")
                    else:
                        print(
                            f"Error retrieving package dependencies after update: {pipdeptree_result.stderr}")
                else:
                    print(f"{yellow}{package} remains at {current_version}.{reset}")

        except Exception as e:
            # Falls bei der Prüfung ein Fehler auftritt, geben wir diesen aus
            print(f"{red}Error while checking dependencies for {package}: {str(e)}{reset}")
            return  # Funktion vorzeitig verlassen, wenn ein Fehler auftritt

        # Wenn das Paket auf dem neuesten Stand ist, wird dies ebenfalls angezeigt
        if current_version and latest_version and current_version == latest_version:
            print(f"{green}{package} is up to date (Version {current_version}).{reset}")


def install_package(package: str):
    """Installiert ein Paket basierend auf Benutzerbestätigung."""
    print(f"{red}{package} is not installed.{reset}")
    if confirm_action(f"Do you want to install {package}?"):
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
        print(f"{green}{package} has been installed.{reset}")
    else:
        print(f"{yellow}Skipping installation for {package}.{reset}")

"""
def get_package_dependencies(package: str) -> List[str]:
    # Holt die Abhängigkeiten eines Pakets von 'pip show'.
    try:
        output = subprocess.check_output([sys.executable, "-m", "pip", "show", package], stderr=subprocess.DEVNULL).decode()
        dependencies = []

        for line in output.splitlines():
            if line.startswith("Requires:"):
                dependencies = line.split(":")[1].strip().split(", ")

        return dependencies
    except subprocess.CalledProcessError as e:
        print(f"Error while retrieving package info for {package}: {e}")
        return []

def check_dependency_compatibility(package: str, new_version: str, installed_packages: Dict[str, str]) -> List[str]:
    # Überprüft, welche anderen installierten Pakete möglicherweise inkompatibel mit der neuen Version sind.
    incompatibilities = []

    # Holen Sie die Abhängigkeiten des Pakets
    dependencies = get_package_dependencies(package)
    if not dependencies:
        print(f"No dependencies found for {package}.")
        return incompatibilities

    # Dictionary für neueste Versionen der Abhängigkeiten
    latest_versions = {}

    # Überprüfe jede Abhängigkeit
    for dep in dependencies:
        dep = dep.strip()

        # Überspringe leere oder ungültige Paketnamen
        if not dep:
            continue

        # Wenn die neueste Version der Abhängigkeit noch nicht abgefragt wurde, hole sie
        if dep not in latest_versions:
            try:
                latest_versions[dep] = get_latest_package_version(dep)
            except Exception as e:
                print(f"Error while getting latest version for {dep}: {e}")
                incompatibilities.append(f"Failed to check latest version for {dep}")
                continue

        installed_version = installed_packages.get(dep, None)
        latest_version = latest_versions.get(dep)

        # Prüfe auf inkompatible Versionen
        if installed_version and latest_version and installed_version != latest_version:
            incompatibilities.append(
                f"{dep} (installed: {installed_version}, latest: {latest_version}) may conflict with {package} {new_version}")

    # Indirekte Abhängigkeiten prüfen (rekursiv)
    for dep in dependencies:
        dep = dep.strip()
        if not dep:
            continue

        try:
            indirect_incompatibilities = check_dependency_compatibility(dep, new_version, installed_packages)
            incompatibilities.extend(indirect_incompatibilities)
        except Exception as e:
            print(f"Error while checking indirect dependencies for {dep}: {e}")

    # Wenn keine Inkompatibilitäten gefunden wurden
    if not incompatibilities:
        print(f"{package} {new_version} is compatible with all dependencies.")

    return incompatibilities

def check_all_installed_packages_compatibility(packages: List[str]) -> None:
    # Prüft alle installierten Pakete und ihre Abhängigkeiten auf mögliche Inkompatibilitäten.
    installed_packages = {pkg: get_package_version(pkg) for pkg in packages}

    for package in packages:
        print(f"Checking compatibility for {package}...")
        current_version = installed_packages.get(package)
        if current_version:
            print(f"Installed version of {package}: {current_version}")
            latest_version = get_latest_package_version(package)
            if latest_version != current_version:
                print(f"New version available: {latest_version}")
                incompatibilities = check_dependency_compatibility(package, latest_version, installed_packages)
                if incompatibilities:
                    print(f"Incompatibilities detected for {package} {latest_version}:")
                    for issue in incompatibilities:
                        print(f"  {issue}")
                else:
                    print(f"{package} is compatible with all other installed packages.")
            else:
                print(f"{package} is up to date.")
        else:
            print(f"{package} is not installed.")
"""

def process_packages(packages: List[str]):
    """Überprüft und installiert oder aktualisiert eine Liste von Paketen."""
    for idx, package in enumerate(packages, start=1):
        print(f"\n[{idx}/{len(packages)}] Checking package: {blue}{package}{reset}")
        install_or_update_package(package)

print(f"\nAll frameworks for {blue}MAVIS versions 4{reset} are currently being installed and updated.")

# Paketlisten
packages = [
    "Flask", "ollama", "jupyter", "jupyterlab", "Werkzeug", "markdown", "setuptools-rust",
    "matplotlib", "plotly", "dash", "seaborn", "numpy", "sympy", "pandas", "bokeh",
    "mayavi", "configobj", "manim", "geopandas", "scipy", "requests", "python-dotenv",
    "PyQt6", "PyQt6-sip", "PyQt6-Charts", "keyboard", "keyboard",
    "torch", "torchvision", "torchaudio", "tensorflow", "scikit-learn", "transformers",
    "altair", "vega_datasets", "altair_viewer", "ipython", "altair-saver", "kaleido",
    "vl-convert-python", "py-cpuinfo", "GPUtil", "requests", "astropy", "QuantLib",
    "openmdao", "pybullet", "monai", "fenics", "pydy", "pycalculix", "solidpython",
    "pyomo", "gekko", "casadi", "control", "h2o", "pint", "coolprop", "pythermo",
    "biopython", "opencv-python", "SimpleITK", "nilearn", "deepchem", "pymedtermino",
    "lifelines", "rdkit", "ase", "chempy", "shapely", "fiona", "cartopy", "statsmodels",
    "yfinance", "PySpice", "networkx", "schematics", "schemdraw", "ipywidgets", "vtk",
    "diagrams", "graphviz", "pix2tex[gui]", "pillow", "bcrypt", "watchdog", "bandit",
    "dotenv-linter", "psutil", "dotenv", "PyPDF2", "python-docx", "openai-whisper",
    "coqui-tts", "sounddevice", "pygame", "python-dotenv", "pyaudio", "webrtcvad",
    "ipydrawio[all]", "jupyter_server_terminals"
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
