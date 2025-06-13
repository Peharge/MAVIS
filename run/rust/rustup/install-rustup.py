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
import subprocess
import sys
import shutil
import urllib.request
from pathlib import Path

RUSTUP_URL = "https://sh.rustup.rs"
INSTALLER_PATH = Path("/tmp/rustup-init.sh")
LOGFILE = Path("/tmp/rustup_install.log")
GPG_KEY_ID = "108F52B48DB57BB0"

def log(message):
    full_msg = f"[INFO] {message}"
    print(full_msg)
    with open(LOGFILE, "a") as f:
        f.write(full_msg + "\n")

def error(message):
    full_msg = f"[ERROR] {message}"
    print(full_msg, file=sys.stderr)
    with open(LOGFILE, "a") as f:
        f.write(full_msg + "\n")
    sys.exit(1)

def check_dependencies():
    for cmd in ["curl", "gpg", "sh"]:
        if shutil.which(cmd) is None:
            error(f"'{cmd}' is required but not found in PATH.")

def download_installer():
    log("Downloading rustup installer...")
    try:
        with urllib.request.urlopen(RUSTUP_URL) as response:
            with open(INSTALLER_PATH, 'wb') as out_file:
                out_file.write(response.read())
        os.chmod(INSTALLER_PATH, 0o755)
    except Exception as e:
        error(f"Failed to download installer: {e}")

def verify_installer():
    sig_url = f"{RUSTUP_URL}.asc"
    sig_path = INSTALLER_PATH.with_suffix(".asc")

    try:
        urllib.request.urlretrieve(sig_url, sig_path)
    except Exception:
        log("No signature file found. Skipping GPG verification.")
        return

    try:
        subprocess.run(["gpg", "--keyserver", "hkps://keys.openpgp.org", "--recv-keys", GPG_KEY_ID], check=True)
        subprocess.run(["gpg", "--verify", str(sig_path), str(INSTALLER_PATH)], check=True)
        log("GPG verification successful.")
    except subprocess.CalledProcessError:
        error("GPG verification failed.")

def run_installer():
    log("Running rustup installer (non-interactive)...")
    try:
        subprocess.run([str(INSTALLER_PATH), "-y"], check=True)
    except subprocess.CalledProcessError as e:
        error(f"Installer failed with exit code {e.returncode}")

def setup_path():
    cargo_path = Path.home() / ".cargo" / "bin"
    bashrc = Path.home() / ".bashrc"

    if str(cargo_path) not in os.environ.get("PATH", ""):
        log("Adding ~/.cargo/bin to PATH in .bashrc")
        with open(bashrc, "a") as f:
            f.write(f'\nexport PATH="{cargo_path}:$PATH"\n')

def verify_installation():
    rustc = shutil.which("rustc")
    cargo = shutil.which("cargo")
    if rustc and cargo:
        log("Rust installed successfully!")
        subprocess.run(["rustc", "--version"], check=True)
        subprocess.run(["cargo", "--version"], check=True)
    else:
        error("Rust installation failed. rustc or cargo not found.")

def main():
    log("==== Starting Rustup Installation via Python ====")
    check_dependencies()
    download_installer()
    verify_installer()
    run_installer()
    setup_path()
    verify_installation()
    log("==== Rustup Installation Completed Successfully ====")

if __name__ == "__main__":
    main()
