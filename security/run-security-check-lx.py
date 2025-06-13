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

"""
Advanced Security Scanner for Linux (Arch Linux optimized)
"""
import os
import sys
import subprocess
import logging
from logging.handlers import RotatingFileHandler
import hashlib
import json
from datetime import datetime
from pathlib import Path
import time
import socket
import platform
import psutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

# Configuration
CRITICAL_ENV_VARS = [
    'SECRET_KEY', 'DB_PASSWORD', 'API_KEY', 'JWT_SECRET', 'EMAIL_PASSWORD',
    'DEBUG', 'ALLOWED_HOSTS', 'DATABASE_URL', 'REDIS_URL', 'CELERY_BROKER_URL',
    'LOG_LEVEL', 'SSL_CERT_PATH', 'SSL_KEY_PATH', 'OAUTH_CLIENT_ID',
    'OAUTH_CLIENT_SECRET', 'S3_BUCKET_NAME', 'S3_ACCESS_KEY', 'S3_SECRET_KEY',
    'SENDGRID_API_KEY', 'GITHUB_TOKEN', 'TWITTER_API_KEY', 'TWITTER_API_SECRET'
]

# Console color codes
COLORS = {
    'reset': '\033[0m', 'bold': '\033[1m',
    'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
    'blue': '\033[94m', 'magenta': '\033[95m', 'cyan': '\033[96m', 'white': '\033[97m'
}

# File integrity
KNOWN_HASHES_FILE = Path("known_hashes.json")
DEFAULT_HASHES = {}
HASH_CACHE_FILE = Path("hash_cache.json")

# Network thresholds
MALICIOUS_IPS = {"203.0.113.5", "198.51.100.7"}
SUSPICIOUS_PORTS = {22, 23, 25, 3306, 3389}
MAX_CONN_PER_IP = 10
CPU_THRESHOLD = 70
MEM_THRESHOLD = 1_000_000_000  # 1GB

# Project directory (home)
HOME_DIR = Path.home()
PROJECT_DIR = HOME_DIR / 'projects' / 'MAVIS'


# Logging Setup
def setup_logging() -> logging.Logger:
    logger = logging.getLogger('ArchSecurityScanner')
    level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logger.setLevel(level)

    log_file = Path.cwd() / 'security_scan.log'
    handler = RotatingFileHandler(log_file, maxBytes=5*1024**2, backupCount=3)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger

logger = setup_logging()


# Environment Loader
def load_environment() -> None:
    env_file = PROJECT_DIR / '.env'
    if env_file.exists():
        load_dotenv(dotenv_path=env_file)
        logger.info(f"Loaded environment from {env_file}")
    else:
        logger.warning(f"No .env file at {env_file}")


# Hash Utilities
def compute_sha256(path: Path) -> str:
    hash_obj = hashlib.sha256()
    try:
        with path.open('rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_obj.update(chunk)
    except Exception as e:
        logger.error(f"Failed hashing {path}: {e}")
        return ''
    return hash_obj.hexdigest()


def load_known_hashes() -> dict:
    if KNOWN_HASHES_FILE.exists():
        try:
            return json.loads(KNOWN_HASHES_FILE.read_text())
        except Exception as e:
            logger.error(f"Error loading known hashes: {e}")
    return DEFAULT_HASHES.copy()

KNOWN_HASHES = load_known_hashes()


# File Scanning
def scan_files(directory: Path) -> int:
    count = 0
    for root, _, files in os.walk(directory, followlinks=False):
        for fname in files:
            count += 1
    logger.info(f"Files scanned in {directory}: {count}")
    return count


# ClamAV Scan
def scan_with_clamav(target: Path) -> int:
    logger.info(f"Running ClamAV scan on {target}")
    try:
        subprocess.run(['sudo', 'freshclam'], check=True, stdout=subprocess.DEVNULL)
        result = subprocess.run(['clamscan', '-r', '--bell', str(target)], capture_output=True, text=True)
        print(result.stdout)
        return scan_files(target)
    except subprocess.CalledProcessError as e:
        logger.error(f"ClamAV error: {e}")
        return 0


# Firewall Status
def check_firewall():
    logger.info("Checking firewall (ufw) status")
    try:
        status = subprocess.check_output(['sudo', 'ufw', 'status'], text=True)
        if 'active' in status.lower():
            print(f"{COLORS['green']}Firewall active{COLORS['reset']}")
        else:
            print(f"{COLORS['red']}Firewall inactive{COLORS['reset']}")
    except Exception as e:
        logger.error(f"Firewall check failed: {e}")


# Processes Check
def check_processes() -> None:
    logger.info("Checking processes")
    suspicious = {'wget', 'curl', 'nmap', 'netcat'}
    for proc in psutil.process_iter(['pid','name','cpu_percent','memory_info','cmdline']):
        try:
            name = proc.info['name'] or ''
            if any(s in name for s in suspicious):
                cpu = proc.info['cpu_percent']
                mem = proc.info['memory_info'].rss
                if cpu > CPU_THRESHOLD or mem > MEM_THRESHOLD:
                    print(f"{COLORS['red']}High-resource suspicious process: {name} (PID {proc.pid}){COLORS['reset']}")
                else:
                    print(f"{COLORS['yellow']}Suspicious process: {name} (PID {proc.pid}){COLORS['reset']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


# Network Check
def check_network():
    logger.info("Checking network connections")
    conns = psutil.net_connections(kind='inet')
    counts = {}
    for c in conns:
        if c.status=='ESTABLISHED' and c.raddr:
            ip = c.raddr.ip
            counts[ip] = counts.get(ip,0) + 1
            if counts[ip] > MAX_CONN_PER_IP:
                print(f"{COLORS['red']}Possible DDoS: {ip} ({counts[ip]}){COLORS['reset']}")
            if ip in MALICIOUS_IPS:
                print(f"{COLORS['red']}Malicious IP: {ip}{COLORS['reset']}")
            if c.laddr.port in SUSPICIOUS_PORTS:
                print(f"{COLORS['yellow']}Suspicious local port: {c.laddr.port}{COLORS['reset']}")


# OS Updates
def check_updates():
    logger.info("Checking Arch Linux updates")
    try:
        out = subprocess.check_output(['sudo', 'pacman', '-Qu'], text=True)
        if out.strip():
            print(f"Available updates:\n{out}")
        else:
            print(f"{COLORS['green']}System is up-to-date{COLORS['reset']}")
    except Exception as e:
        logger.error(f"Update check failed: {e}")


# Main scanner
def main():
    logger.info("Starting full security scan")
    load_environment()

    with ThreadPoolExecutor(max_workers=8) as exec:
        futures = {
            exec.submit(scan_with_clamav, PROJECT_DIR): 'clamav',
            exec.submit(check_firewall): 'firewall',
            exec.submit(check_processes): 'processes',
            exec.submit(check_network): 'network',
            exec.submit(check_updates): 'updates'
        }
        for future in as_completed(futures):
            name = futures[future]
            try:
                future.result()
            except Exception as e:
                logger.error(f"Task {name} failed: {e}")

    logger.info("Security scan complete")


if __name__ == '__main__':
    main()
