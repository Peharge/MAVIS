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
import sys
import subprocess
import psutil
import socket
import logging
import logging.handlers  # Wichtig: expliziter Import von logging.handlers
import hashlib
import json
from datetime import datetime
from pathlib import Path
import time
from dotenv import load_dotenv
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration / Constants
CRITICAL_VARS = [
    'SECRET_KEY', 'DB_PASSWORD', 'API_KEY', 'JWT_SECRET', 'EMAIL_PASSWORD', 'DEBUG',
    'ALLOWED_HOSTS', 'DATABASE_URL', 'REDIS_URL', 'CELERY_BROKER_URL', 'LOG_LEVEL',
    'SSL_CERT_PATH', 'SSL_KEY_PATH', 'OAUTH_CLIENT_ID', 'OAUTH_CLIENT_SECRET',
    'S3_BUCKET_NAME', 'S3_ACCESS_KEY', 'S3_SECRET_KEY', 'SENDGRID_API_KEY',
    'GITHUB_TOKEN', 'TWITTER_API_KEY', 'TWITTER_API_SECRET'
]

# Color codes for console output
COLORS = {
    'red': "\033[91m",
    'green': "\033[92m",
    'yellow': "\033[93m",
    'blue': "\033[94m",
    'magenta': "\033[95m",
    'cyan': "\033[96m",
    'white': "\033[97m",
    'reset': "\033[0m",
    'bold': "\033[1m"
}

# Known file hashes for integrity checking.
KNOWN_FILE_HASHES_PATH = Path("known_hashes.json")
KNOWN_HASHES = {
    "sample_file.txt": "d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2"
}

# Network and system parameters
KNOWN_MALICIOUS_IPS = {"192.168.1.100", "203.0.113.5"}
SUSPICIOUS_PORTS = {22, 23, 25, 3306, 3389}
MAX_CONNECTIONS_FROM_SAME_IP = 10
SUSPICIOUS_CPU_THRESHOLD = 70  # in percent
SUSPICIOUS_MEMORY_THRESHOLD = 1_000_000_000  # in bytes (1GB)

# Project base directory: scan the entire folder
DEFAULT_PROJECT_DIR = Path(rf"C:\Users\{os.getlogin()}\PycharmProjects\MAVIS")
HASH_CACHE_FILE = Path("hash_cache.json")  # Cache file for file modification tracking

# Logging Configuration
def setup_logging():
    logger = logging.getLogger("SecurityScanner")
    logger.setLevel(logging.INFO)

    # Rotating file handler
    file_handler = logging.handlers.RotatingFileHandler("security_scan.log", maxBytes=5*1024*1024, backupCount=2)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    # Console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)

    return logger

logger = setup_logging()

# Load Environment Variables
def load_env() -> Path:
    try:
        user = os.getlogin() if hasattr(os, 'getlogin') else os.environ.get("USERNAME", "default")
    except Exception:
        user = os.environ.get("USERNAME", "default")
    env_path = Path(f"C:/Users/{user}/PycharmProjects/MAVIS/.env")
    if env_path.exists():
        load_dotenv(dotenv_path=str(env_path))
        print(f"{COLORS['blue']}INFO{COLORS['reset']}: .env file loaded successfully.")
        logger.info("Loaded .env file successfully from %s.", env_path)
    else:
        print(f"{COLORS['yellow']}WARNING{COLORS['reset']}: No .env file found at {env_path}.")
        logger.warning("No .env file found at %s.", env_path)
    return env_path

# File Integrity Check Functions
def compute_sha256(file_path: Path) -> str:
    """Compute the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
    except Exception as e:
        logger.error("Error computing hash for %s: %s", file_path, e)
        return ""
    return sha256_hash.hexdigest()

def load_known_hashes() -> dict:
    """Load known file hashes from a JSON file, if available."""
    if KNOWN_FILE_HASHES_PATH.exists():
        try:
            with KNOWN_FILE_HASHES_PATH.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error("Error loading known hashes: %s", e)
    return KNOWN_HASHES.copy()

KNOWN_HASHES = load_known_hashes()

def is_safe(file_path: Path) -> bool:
    """
    Check if a file is considered safe based on hash comparisons.
    If no known hash is available, the integrity check is skipped.
    """
    if not file_path.is_file():
        return True
    current_hash = compute_sha256(file_path)
    known_hash = KNOWN_HASHES.get(str(file_path)) or KNOWN_HASHES.get(file_path.name)
    if known_hash:
        if current_hash == known_hash:
            return True
        else:
            logger.warning("Hash mismatch for %s. Expected: %s, Found: %s", file_path, known_hash, current_hash)
            return False
    else:
        logger.info("No known hash for %s. Skipping integrity check.", file_path)
        return True

# Optimized File Iteration (Scans every file)
def safe_iter_files(directory: Path):
    """
    Recursively iterate over files in a directory using os.scandir with error handling.
    Every file found is yielded.
    """
    try:
        with os.scandir(directory) as it:
            for entry in it:
                path_entry = Path(entry.path)
                if entry.is_file(follow_symlinks=False):
                    yield path_entry
                elif entry.is_dir(follow_symlinks=False):
                    yield from safe_iter_files(path_entry)
    except Exception as e:
        logger.error("Error scanning directory %s: %s", directory, e)

def list_files_for_scan(directory: Path) -> int:
    """
    List all files in a directory (recursively) and return the count.
    """
    file_count = 0
    print(f"\n{COLORS['blue']}Files in scan area:{COLORS['reset']}")
    for file_path in safe_iter_files(directory):
        print(f"   - {file_path}")
        file_count += 1
    return file_count

# Windows Defender Scan (Improved Handling)
def scan_with_defender(target: Path) -> int:
    """
    Run a Windows Defender scan on the given target with error and timeout handling.
    Uses a reduced timeout per scan to avoid hangs.
    """
    print(f"\n{COLORS['blue']}Starting Windows Defender scan on:{COLORS['reset']} {target}")
    if not target.exists():
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: The specified path does not exist: {target}")
        logger.error("Invalid scan path: %s", target)
        return 0
    try:
        total_files = list_files_for_scan(target)
        ps_command = [
            "powershell", "-Command",
            "Start-MpScan", "-ScanType", "CustomScan", "-ScanPath", str(target)
        ]
        result = subprocess.run(ps_command,
                                  capture_output=True,
                                  text=True,
                                  timeout=180,
                                  encoding="cp1252",
                                  errors="ignore")
        if result.stdout.strip():
            print(result.stdout)
            logger.info("Windows Defender scan result for %s: %s", target, result.stdout)
        else:
            print(f"{COLORS['green']}No threats detected on {target}.{COLORS['reset']}")
            logger.info("No issues found during scan on %s", target)
        return total_files
    except subprocess.TimeoutExpired:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Scan timed out on {target}. Skipping this target.")
        logger.error("Scan timeout for %s", target)
        return 0
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Scan failed on {target} – {e}")
        logger.error("Scan failed for %s: %s", target, e)
        return 0

# Extract Paths from Environment Variables
def extract_paths_from_env() -> list:
    """
    Extract local paths or URLs from critical environment variables.
    """
    paths = []
    for var in CRITICAL_VARS:
        value = os.getenv(var)
        if value:
            candidate = Path(value)
            if candidate.exists():
                paths.append(candidate)
                logger.info("Local path from %s: %s", var, value)
            elif value.startswith("http"):
                print(f"{COLORS['blue']}URL found{COLORS['reset']}: {var} -> {value}")
                logger.info("URL found: %s -> %s", var, value)
    return paths

# Check Firewall Status (Cross-Platform)
def check_firewall_status():
    print(f"\n{COLORS['blue']}Checking firewall status...{COLORS['reset']}")
    try:
        system_platform = platform.system()
        if system_platform == "Windows":
            result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"],
                                      capture_output=True, text=True, timeout=60)
            if "State" in result.stdout:
                print(f"{COLORS['green']}Firewall is enabled.{COLORS['reset']}")
                logger.info("Windows Firewall is enabled.")
            else:
                print(f"{COLORS['red']}Firewall is not enabled.{COLORS['reset']}")
                logger.warning("Windows Firewall is not enabled.")
        elif system_platform in ["Linux", "Darwin"]:
            result = subprocess.run(["sudo", "ufw", "status"],
                                      capture_output=True, text=True, timeout=30)
            if "active" in result.stdout.lower():
                print(f"{COLORS['green']}Firewall is active.{COLORS['reset']}")
                logger.info("Firewall is active on %s.", system_platform)
            else:
                print(f"{COLORS['red']}Firewall is not active.{COLORS['reset']}")
                logger.warning("Firewall is not active on %s.", system_platform)
        else:
            print(f"{COLORS['yellow']}No firewall check implemented for this platform.{COLORS['reset']}")
            logger.warning("Unknown platform for firewall check: %s", system_platform)
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Error checking firewall status – {e}")
        logger.error("Error in firewall check: %s", e)

# Check Suspicious Processes
def check_suspicious_processes():
    print(f"\n{COLORS['blue']}Checking for suspicious processes...{COLORS['reset']}")
    suspicious_names = {
        "cmd.exe", "powershell.exe", "netstat.exe", "whois.exe",
        "python.exe", "java.exe", "wget.exe", "curl.exe", "nc.exe", "nmap.exe"
    }
    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'cpu_percent', 'memory_info', 'create_time', 'username']):
        try:
            proc_name = (proc.info.get('name') or "").lower()
            if proc_name in suspicious_names:
                cpu_usage = proc.info.get('cpu_percent', 0)
                mem_info = proc.info.get('memory_info')
                memory_usage = getattr(mem_info, 'rss', 0) if mem_info else 0
                create_time = datetime.fromtimestamp(proc.info.get('create_time', time.time())).strftime("%Y-%m-%d %H:%M:%S")
                username = proc.info.get('username', 'Unknown')
                cmdline = " ".join(proc.info.get('cmdline', []))
                if cpu_usage > SUSPICIOUS_CPU_THRESHOLD or memory_usage > SUSPICIOUS_MEMORY_THRESHOLD:
                    print(f"{COLORS['red']}Suspicious process with high resource usage{COLORS['reset']}: {proc.info.get('name')} (PID: {proc.info.get('pid')})")
                    print(f"   CPU: {cpu_usage}% | Memory: {memory_usage / (1024*1024):.2f} MB")
                    print(f"   Started: {create_time} by {username}")
                    print(f"   Command: {cmdline}")
                    logger.warning("High resource usage process: %s (PID: %s)", proc.info.get('name'), proc.info.get('pid'))
                else:
                    print(f"{COLORS['yellow']}Suspicious process (normal usage){COLORS['reset']}: {proc.info.get('name')} (PID: {proc.info.get('pid')})")
                    print(f"   Started: {create_time} by {username}")
                    print(f"   Command: {cmdline}")
                    logger.info("Suspicious process detected: %s (PID: %s)", proc.info.get('name'), proc.info.get('pid'))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
        except Exception as e:
            logger.error("Error checking process: %s", e)
    print(f"{COLORS['green']}Process check complete.{COLORS['reset']}")

# Check Active Network Connections
def check_network_connections():
    print(f"\n{COLORS['blue']}Checking active network connections...{COLORS['reset']}")
    try:
        net_connections = psutil.net_connections(kind='inet')
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Could not retrieve network connections – {e}")
        logger.error("Network connection error: %s", e)
        return
    ip_connection_count = {}
    for conn in net_connections:
        try:
            if conn.status == 'ESTABLISHED' and conn.raddr:
                local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}"
                remote_ip = conn.raddr.ip
                ip_connection_count[remote_ip] = ip_connection_count.get(remote_ip, 0) + 1
                if ip_connection_count[remote_ip] > MAX_CONNECTIONS_FROM_SAME_IP:
                    print(f"{COLORS['red']}Potential DDoS attack detected{COLORS['reset']}: {remote_ip} has {ip_connection_count[remote_ip]} connections!")
                    logger.warning("Potential DDoS: %s (%s connections).", remote_ip, ip_connection_count[remote_ip])
                    continue
                print(f"{COLORS['cyan']}Active connection found{COLORS['reset']}: {local_addr} -> {remote_addr}")
                logger.info("Network connection: %s -> %s", local_addr, remote_addr)
                if remote_ip in KNOWN_MALICIOUS_IPS:
                    print(f"{COLORS['red']}WARNING: Connection to known malicious IP detected{COLORS['reset']}: {remote_ip}")
                    logger.warning("Connection to known malicious IP: %s", remote_ip)
                if conn.laddr and conn.laddr.port in SUSPICIOUS_PORTS:
                    print(f"{COLORS['yellow']}Suspicious local port detected{COLORS['reset']}: {conn.laddr.port}")
                    logger.warning("Suspicious local port: %s", conn.laddr.port)
                if conn.raddr and conn.raddr.port in SUSPICIOUS_PORTS:
                    print(f"{COLORS['yellow']}Suspicious remote port detected{COLORS['reset']}: {conn.raddr.port}")
                    logger.warning("Suspicious remote port: %s", conn.raddr.port)
                if conn.raddr and conn.raddr.port == 443:
                    try:
                        with socket.create_connection((remote_ip, 443), timeout=5) as s:
                            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                            response = s.recv(1024)
                        if b"200 OK" in response:
                            print(f"{COLORS['green']}Stable HTTPS connection established{COLORS['reset']}: {remote_ip}:443")
                            logger.info("Stable HTTPS connection: %s:443", remote_ip)
                        else:
                            print(f"{COLORS['red']}Unusual HTTPS response{COLORS['reset']}: {remote_ip}:443")
                            logger.warning("Unclear HTTPS response: %s:443", remote_ip)
                    except Exception as e:
                        print(f"{COLORS['red']}Error during SSL/TLS check{COLORS['reset']}: {e}")
                        logger.error("SSL/TLS check error for %s:443 – %s", remote_ip, e)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print(f"{COLORS['green']}Network connection check complete.{COLORS['reset']}")

# Check Security-Related System Logs
def check_security_logs():
    print(f"\n{COLORS['blue']}Checking security-related system logs...{COLORS['reset']}")
    log_file = Path("/var/log/auth.log")
    if log_file.exists():
        try:
            with log_file.open("r", encoding="utf-8", errors="ignore") as f:
                logs = f.readlines()[-50:]
                for line in logs:
                    if "failed" in line.lower() or "error" in line.lower():
                        print(f"{COLORS['red']}Security issue detected in logs{COLORS['reset']}: {line.strip()}")
                        logger.warning("Security log entry: %s", line.strip())
        except Exception as e:
            print(f"{COLORS['red']}ERROR{COLORS['reset']}: Error reading log file – {e}")
            logger.error("Error reading %s: %s", log_file, e)
    else:
        print(f"{COLORS['yellow']}Log file {log_file} not found.{COLORS['reset']}")
        logger.warning("Log file %s not found.", log_file)

# Check System Permissions and User Accounts
def check_system_permissions():
    print(f"\n{COLORS['blue']}Checking system users and file permissions...{COLORS['reset']}")
    try:
        for user in psutil.users():
            print(f"{COLORS['blue']}User detected:{COLORS['reset']} {user.name}, {user.host}")
            logger.info("User detected: %s, %s", user.name, user.host)
    except Exception as e:
        logger.error("Error retrieving user list: %s", e)
    print(f"\n{COLORS['blue']}Checking file permissions...{COLORS['reset']}")
    base_dir = DEFAULT_PROJECT_DIR
    for file_path in safe_iter_files(base_dir):
        try:
            permissions = oct(os.stat(file_path).st_mode & 0o777)[2:]
            if int(permissions, 8) > 0o755:
                print(f"{COLORS['yellow']}Warning: Overly permissive permissions for {file_path}: {permissions}{COLORS['reset']}")
                logger.warning("Overly permissive permissions for %s: %s", file_path, permissions)
            else:
                logger.info("Permissions for %s: %s", file_path, permissions)
        except Exception as e:
            logger.error("Error checking permissions for %s: %s", file_path, e)

# Extra Feature: Check for OS Updates
def check_os_updates():
    print(f"\n{COLORS['blue']}Checking for operating system updates...{COLORS['reset']}")
    system_platform = platform.system()
    try:
        if system_platform == "Windows":
            result = subprocess.run(["wmic", "qfe", "list"], capture_output=True, text=True, timeout=30)
            print(f"{COLORS['blue']}Windows Update Info:{COLORS['reset']}\n{result.stdout}")
            logger.info("Windows update info: %s", result.stdout)
        elif system_platform == "Linux":
            result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, timeout=30)
            print(f"{COLORS['blue']}Linux updates available:{COLORS['reset']}\n{result.stdout}")
            logger.info("Linux update info: %s", result.stdout)
        else:
            print(f"{COLORS['yellow']}OS update check not implemented for {system_platform}.{COLORS['reset']}")
            logger.warning("OS update check not implemented for %s", system_platform)
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Error checking OS updates – {e}")
        logger.error("Error checking OS updates: %s", e)

# Extra Feature: Check YARA Malware Signatures (Optional)
def check_yara_signatures():
    print(f"\n{COLORS['blue']}Checking files against YARA rules...{COLORS['reset']}")
    try:
        import yara
    except ImportError:
        print(f"{COLORS['yellow']}YARA module not installed. Skipping YARA scan.{COLORS['reset']}")
        logger.warning("YARA module not installed.")
        return
    rule_source = '''
    rule DummyRule {
        strings:
            $a = "malicious" nocase
        condition:
            $a
    }
    '''
    try:
        rules = yara.compile(source=rule_source)
    except Exception as e:
        logger.error("Error compiling YARA rules: %s", e)
        return
    for file_path in safe_iter_files(DEFAULT_PROJECT_DIR):
        try:
            matches = rules.match(str(file_path))
            if matches:
                print(f"{COLORS['red']}YARA match found in {file_path}:{COLORS['reset']} {matches}")
                logger.warning("YARA match in %s: %s", file_path, matches)
        except Exception as e:
            logger.error("Error scanning %s with YARA: %s", file_path, e)
    print(f"{COLORS['green']}YARA scan complete.{COLORS['reset']}")

# Extra Feature: Check for Rootkit Signatures (Stub Function)
def check_rootkit_signatures():
    print(f"\n{COLORS['blue']}Performing rootkit signature check...{COLORS['reset']}")
    print(f"{COLORS['yellow']}Rootkit check not fully implemented. Consider integrating a dedicated tool.{COLORS['reset']}")
    logger.info("Rootkit check stub executed.")

# Extra Feature: File Modification Tracking Using a Hash Cache
def load_hash_cache() -> dict:
    if HASH_CACHE_FILE.exists():
        try:
            with HASH_CACHE_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error("Error loading hash cache: %s", e)
    return {}

def update_hash_cache(new_cache: dict):
    try:
        with HASH_CACHE_FILE.open("w", encoding="utf-8") as f:
            json.dump(new_cache, f, indent=4)
        logger.info("Hash cache updated successfully.")
    except Exception as e:
        logger.error("Error updating hash cache: %s", e)

def check_file_modifications_with_cache():
    """
    Compare current file hashes with the cached state.
    Report if any file modifications are detected.
    """
    print(f"\n{COLORS['blue']}Performing file modification tracking...{COLORS['reset']}")
    previous_hashes = load_hash_cache()
    current_hashes = {}
    modifications_detected = False
    for file_path in safe_iter_files(DEFAULT_PROJECT_DIR):
        if file_path.is_file():
            current_hash = compute_sha256(file_path)
            current_hashes[str(file_path)] = current_hash
            if str(file_path) in previous_hashes:
                if previous_hashes[str(file_path)] != current_hash:
                    print(f"{COLORS['red']}Modification detected:{COLORS['reset']} {file_path}")
                    logger.warning("File modification detected for %s", file_path)
                    modifications_detected = True
            else:
                logger.info("New file detected (added to cache): %s", file_path)
    if not modifications_detected:
        print(f"{COLORS['green']}No unauthorized file modifications detected.{COLORS['reset']}")
    update_hash_cache(current_hashes)

# Full Security Scan (Parallelized)
def scan_all_files():
    env_path = load_env()
    total_scanned_files = 0

    # Preliminary: Check system permissions and user accounts
    check_system_permissions()

    if env_path:
        base_directory = env_path.parent
        # Combine base directory and environment variable paths
        paths_to_scan = [base_directory] + extract_paths_from_env()

        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_path = {executor.submit(scan_with_defender, path): path for path in paths_to_scan}
            for future in as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    scanned_count = future.result()
                    total_scanned_files += scanned_count
                except Exception as exc:
                    logger.error("Scan exception for %s: %s", path, exc)

        # Integrity check for each path
        for path in paths_to_scan:
            if path.exists():
                if is_safe(path):
                    print(f"{COLORS['green']}Integrity check passed:{COLORS['reset']} {path}")
                    logger.info("File safe: %s", path)
                else:
                    print(f"{COLORS['red']}Warning: Integrity issue with {path}{COLORS['reset']}")
                    logger.warning("File not safe: %s", path)

        print(f"\n{COLORS['green']}Security scan complete!{COLORS['reset']}")
        print(f"{COLORS['blue']}Total files scanned:{COLORS['reset']} {total_scanned_files}")
    else:
        print(f"{COLORS['red']}Critical error: Could not determine project environment.{COLORS['reset']}")
        logger.critical("No .env file loaded; project environment unknown.")

    # Additional checks
    check_firewall_status()
    check_suspicious_processes()
    check_network_connections()
    check_security_logs()

    # Extra security features
    check_os_updates()
    check_yara_signatures()
    check_rootkit_signatures()
    check_file_modifications_with_cache()

# Main Program
if __name__ == '__main__':
    try:
        scan_all_files()
    except Exception as e:
        print(f"{COLORS['red']}Critical error during security scan: {e}{COLORS['reset']}")
        logger.critical("Critical error in security scan: %s", e)
