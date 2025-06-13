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
import re
import sys
import time
import hashlib
import psutil
import subprocess
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

# Kritische Sicherheitsvariablen
CRITICAL_VARS = [
    'SECRET_KEY',         # Geheimschlüssel für Sessions, JWT und andere Sicherheitsmechanismen
    'DB_PASSWORD',        # Passwort für die Datenbankverbindung
    'API_KEY',            # Schlüssel für externe APIs, um auf Dienste zuzugreifen
    'JWT_SECRET',         # Geheimschlüssel für JWT Token-Generierung
    'EMAIL_PASSWORD',     # Passwort für den E-Mail-Server
    'DEBUG',              # Gibt an, ob die Anwendung im Debug-Modus läuft (sollte in Produktion auf False gesetzt werden)
    'ALLOWED_HOSTS',      # Hosts, die für die Anwendung zugelassen sind (z. B. Domainnamen)
    'DATABASE_URL',       # URL zur Verbindung zur Datenbank (z. B. PostgreSQL)
    'REDIS_URL',          # URL für die Verbindung zu einem Redis-Server (falls verwendet)
    'CELERY_BROKER_URL',  # URL für den Broker (z. B. RabbitMQ oder Redis) für asynchrone Tasks
    'LOG_LEVEL',          # Definiert das Logging-Level (z. B. DEBUG, INFO, WARNING, ERROR)
    'SSL_CERT_PATH',      # Pfad zum SSL-Zertifikat (falls HTTPS erforderlich ist)
    'SSL_KEY_PATH',       # Pfad zum SSL-Schlüssel (falls HTTPS erforderlich ist)
    'OAUTH_CLIENT_ID',    # OAuth-Client-ID für externe Authentifizierung (z. B. Google oder GitHub)
    'OAUTH_CLIENT_SECRET',# Geheimschlüssel für OAuth-Authentifizierung
    'S3_BUCKET_NAME',     # Name des S3-Buckets für Dateispeicherung (falls AWS S3 verwendet wird)
    'S3_ACCESS_KEY',      # Access Key für S3
    'S3_SECRET_KEY',      # Secret Key für S3
    'SENDGRID_API_KEY',   # API-Schlüssel für SendGrid, wenn E-Mail-Versand erforderlich ist
    'GITHUB_TOKEN',       # GitHub Access Token, falls mit GitHub integriert wird
    'TWITTER_API_KEY',    # API-Schlüssel für Twitter-Integration
    'TWITTER_API_SECRET', # API-Geheimnis für Twitter-Integration
]

# Schwache Muster
WEAK_PATTERNS = [
    r'1234', r'password', r'test', r'admin', r'secret', r'abc123',
    r'letmein', r'12345', r'123456', r'qwerty', r'password1',
    r'1q2w3e4r', r'welcome', r'123123', r'root', r'admin123',
    r'football', r'iloveyou', r'123qwe', r'changeme', r'welcome1',
    r'123321', r'password123', r'1password', r'password1', r'1234abcd',
    r'111111', r'123', r'123abc', r'letmein1', r'newpassword',
    r'passw0rd', r'guest', r'password1234', r'987654321', r'1qaz2wsx'
]

'''
def loading_bar(duration=10, message=f"{blue}Running Security Check{reset}:"):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        progress = min(int((elapsed_time / duration) * 100), 100)
        bar_length = 43
        bar_progress = int(bar_length * progress / 100)
        bar = "█" * bar_progress + "-" * (bar_length - bar_progress)
        sys.stdout.write(f"\r{blue}{message}{reset} [{bar}] {progress}%")
        sys.stdout.flush()
        if progress >= 100:
            break
        time.sleep(0.1)
    sys.stdout.write("\n")
'''

def load_env():
    env_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", ".env")
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
        print(f"{green}INFO{reset}: .env file loaded successfully.")
    else:
        print(f"{red}WARNING{reset}: No .env file found.")
    return env_path

class EnvFileMonitor(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".env"):
            print(f"{red}WARNING{reset}: .env file has been modified!")

def start_env_monitor():
    observer = Observer()
    observer.schedule(EnvFileMonitor(), path=".", recursive=False)
    observer.start()

def check_env_security():
    print(f"\n{blue}.env security variables{reset}:")
    for var in CRITICAL_VARS:
        value = os.getenv(var)
        if not value:
            print(f"   {red}ERROR{reset}: {var} is not set!")
        elif any(re.search(pattern, value, re.IGNORECASE) for pattern in WEAK_PATTERNS):
            print(f"   {yellow}WARNING{reset}: {var} uses a weak pattern!")

def check_env_integrity(path):
    print(f"\n{blue}.env security CHECK{reset}:")
    if not os.path.exists(path):
        print(f"   {red}ERROR{reset}: .env file not found!")
        return None
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        print(f"   {red}ERROR{reset}: Failed to read .env - {e}")
        return None

def check_outdated_packages():
    print(f"\n{blue}OUTDATED PACKAGES CHECK{reset}:")
    result = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True, timeout=60)
    print(result.stdout if result.stdout else f"   {green}SUCCESS{reset}: All packages are up to date!")

def check_network_connections():
    print(f"\n{blue}NETWORK SECURITY CHECK{reset}:")
    for conn in psutil.net_connections(kind="inet"):
        if conn.raddr:
            print(f"   Connection from {conn.laddr.ip}:{conn.laddr.port} to {conn.raddr.ip}:{conn.raddr.port}")

def run_bandit_scan():
    print(f"\n{blue}CODE SECURITY CHECK (Bandit){reset}:")
    result = subprocess.run(["bandit", "-r", "."], capture_output=True, text=True)
    print(result.stdout if result.stdout else f"   {green}SUCCESS{reset}: No security issues found.")

def run_dotenv_linter():
    print(f"\n{blue}.env FORMAT CHECK{reset}:")
    result = subprocess.run(["dotenv-linter", ".env"], capture_output=True, text=True)
    print(result.stdout if result.stdout else f"   {green}SUCCESS{reset}: No issues found with .env format.")

def main():
    env_path = load_env()
    if env_path:
        start_env_monitor()
        # loading_bar()
        check_env_security()
        reference_hash = check_env_integrity(env_path)
        if reference_hash:
            check_outdated_packages()
            check_network_connections()
            run_bandit_scan()
            run_dotenv_linter()
            print(f"\n{green}SUCCESS{reset}: Security check complete!")

if __name__ == '__main__':
    main()
