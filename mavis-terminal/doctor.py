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
Doctor Script for a Comprehensive Full-Stack Project Checker.
This modern diagnostic tool runs entirely in the terminal and is engineered for maximum performance,
safety, and stability. It continuously scans the project for a wide range of issues and,
importantly, listens for user input—if "q" is pressed at any time, the scan is immediately aborted and
all identified issues (up to that point) are printed to the terminal.

Features:
- Validates the environment file (.env) with auto-backup and re-encoding.
- Checks system tool versions (Python, Git, WMIC, WSL, PowerShell, Docker).
- Recursively scans project files for:
    • Path sanitization.
    • Python syntax verification using ast.parse.
    • Bytecode compilation tests using compileall and py_compile.
    • File encoding verification with robust UTF-8 handling.
    • Permission checks (read, write, execute).
    • File size and last modification analysis to flag large or outdated files.
- Validates essential environment variables against a predefined schema.
- Performs dependency checks for Python (pip check) and Node.js (npm ci --dry-run).
- Executes language-specific checks for Python, C++, Java, JavaScript/TypeScript, .NET, Rust, and Go.
- Checks Docker configurations.
- Optionally monitors system resources (CPU and memory) if psutil is installed.
- Uses multithreading for concurrent scanning.
- Monitors for user input: pressing "q" immediately aborts the scan and outputs all findings so far.
"""

import os
import sys
import subprocess
import getpass
import argparse
import logging
import ast
import compileall
import py_compile
import shutil
import datetime
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Callable, Optional

# Try to import psutil for system resource monitoring.
try:
    import psutil
    SYSTEM_MONITORING_ENABLED = True
except ImportError:
    SYSTEM_MONITORING_ENABLED = False

import threading
import logging
import sys

stop_event = threading.Event()

def monitor_keyboard():
    while not stop_event.is_set():
        user_input = input("Press 'q' to quit:\n")
        if user_input.lower() == 'q':
            print("Quitting...")
            stop_event.set()
            sys.exit()  # <-- Beendet das Programm sofort

# ANSI Color Codes for terminal output.
class C:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

# Constants for scanning.
DEFAULT_THREADS = 8
LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"
FILE_SIZE_THRESHOLD = 10 * 1024 * 1024  # 10 MB
OUTDATED_THRESHOLD_DAYS = 365  # 1 year

def monitor_quit() -> None:
    """
    Listens for user input continuously; when "q" is entered,
    sets the stop_event to abort the scan.
    """
    try:
        while not stop_event.is_set():
            # Informiere den Benutzer, dass er mit 'q' abbrechen kann.
            user_input = input()
            if user_input.strip().lower() == "q":
                logging.info("User requested abort ('q' pressed).")
                stop_event.set()
                break
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt detected in monitor_quit.")
        stop_event.set()

# Start the quit monitor thread
monitor_thread = threading.Thread(target=monitor_quit, daemon=True)
monitor_thread.start()

# Utility Functions
def run_cmd(cmd: List[str], cwd: Optional[str] = None, timeout: int = 60) -> (int, str, str):
    """
    Executes a command and returns its (return code, stdout, stderr).
    """
    try:
        result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, timeout=timeout)
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as ex:
        return -1, "", str(ex)

def detect_project_path(custom: Optional[Path] = None) -> Path:
    """
    Determines the project path: uses a custom path if provided,
    or a default user-specific path; falls back to the current directory.
    """
    if custom:
        return custom.resolve()
    user = getpass.getuser()
    default = Path("C:/Users") / user / "PycharmProjects" / "MAVIS"
    return default if default.exists() else Path.cwd()

def sanitize_path(p: str) -> str:
    """
    Converts Windows style path backslashes to forward slashes.
    """
    if p.startswith(("C:\\", "D:\\", "E:\\")):
        return p.replace("\\\\", "/").replace("\\", "/")
    return p

def safe_read_text(file: Path) -> str:
    """
    Reads a file using UTF-8 encoding, replacing invalid characters.
    """
    content = file.read_text(encoding="utf-8", errors="replace")
    if "�" in content:
        logging.warning(f"Replaced invalid characters in: {file}")
    return content

# Additional File Checks
def check_file_size(file: Path, report) -> None:
    """
    Checks for unusually large files or outdated files based on modification time.
    """
    if stop_event.is_set():
        return
    try:
        size = file.stat().st_size
        mtime = datetime.datetime.fromtimestamp(file.stat().st_mtime)
        now = datetime.datetime.now()
        if size > FILE_SIZE_THRESHOLD:
            report.add_issue(f"Large file detected ({size} bytes): {file}")
        else:
            report.add_pass(f"File size OK ({size} bytes): {file}")
        if (now - mtime).days > OUTDATED_THRESHOLD_DAYS:
            report.add_issue(f"Outdated file (last modified: {mtime.date()}): {file}")
        else:
            report.add_pass(f"File modification date OK: {file}")
    except Exception as ex:
        report.add_issue(f"Error checking file {file}: {ex}")

def check_system_resources(report) -> None:
    """
    Monitors and reports on CPU and memory usage.
    """
    if stop_event.is_set():
        return
    if SYSTEM_MONITORING_ENABLED:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        report.add_pass(f"System resources: CPU {cpu}% / Memory {mem.percent}%")
    else:
        report.add_issue("psutil is not installed; system resource checks skipped.")

# Core Diagnostic Checks
def check_python_syntax(root: Path, report) -> None:
    """
    Performs syntax checks on all Python files using ast.parse and triggers bytecode compilation test.
    """
    for py_file in root.rglob("*.py"):
        if stop_event.is_set():
            report.add_issue("Scan aborted during Python syntax check.")
            return
        try:
            source = safe_read_text(py_file)
            ast.parse(source)
            report.add_pass(f"Python syntax OK: {py_file}")
        except SyntaxError as e:
            report.add_issue(f"Syntax error in {py_file}: {e}")
    compileall.compile_dir(str(root), force=True, quiet=1)

def check_pycompile(root: Path, report) -> None:
    """
    Performs bytecode compilation test on Python files using py_compile.
    """
    for py_file in root.rglob("*.py"):
        if stop_event.is_set():
            report.add_issue("Scan aborted during bytecode check.")
            return
        try:
            py_compile.compile(str(py_file), doraise=True)
            report.add_pass(f"Bytecode compile OK: {py_file}")
        except py_compile.PyCompileError as e:
            report.add_issue(f"Bytecode compile error in {py_file}: {e.msg}")

def check_encoding(file: Path, report) -> None:
    """
    Checks file encoding using a safe read.
    """
    if stop_event.is_set():
        return
    try:
        _ = safe_read_text(file)
        report.add_pass(f"UTF-8 encoding OK: {file}")
    except Exception as e:
        report.add_issue(f"Encoding error in {file}: {e}")

def check_permissions(file: Path, report) -> None:
    """
    Checks if the file has read, write, and execute permissions.
    """
    if stop_event.is_set():
        return
    perms = []
    if os.access(file, os.R_OK):
        perms.append("read")
    if os.access(file, os.W_OK):
        perms.append("write")
    if os.access(file, os.X_OK):
        perms.append("exec")
    if not perms:
        report.add_issue(f"Insufficient permissions for {file}")
    else:
        report.add_pass(f"Permissions OK ({', '.join(perms)}): {file}")

def check_env_vars(required: List[str], report, env_path: Path) -> None:
    """
    Validates that required environment variables are defined in the .env file.
    """
    if stop_event.is_set():
        return
    try:
        from dotenv import dotenv_values
    except ImportError:
        report.add_issue("python-dotenv required but not installed; skipping .env validation.")
        return

    if not env_path.exists():
        report.add_issue(f".env file missing: {env_path}")
        return

    env = dotenv_values(env_path)
    for key in required:
        if key not in env:
            report.add_issue(f"Missing environment variable: {key}")
        else:
            report.add_pass(f"Environment variable '{key}' is present.")

def check_dependencies(report, project_path: Path) -> None:
    """
    Checks dependency integrity for Python (pip check) and Node.js (npm ci --dry-run).
    """
    if stop_event.is_set():
        return
    if (project_path / "requirements.txt").exists() or (project_path / "pyproject.toml").exists():
        code, _, _ = run_cmd(["pip", "check"])
        if code != 0:
            report.add_issue("pip dependency check failed")
        else:
            report.add_pass("pip dependencies OK")
    if (project_path / "package.json").exists():
        code, _, _ = run_cmd(["npm", "ci", "--dry-run"], cwd=str(project_path))
        if code != 0:
            report.add_issue("npm dependency check failed")
        else:
            report.add_pass("npm dependencies OK")

def advanced_checks(proj: Path, report) -> None:
    """
    Executes advanced checks over the project directory including file encoding, permissions,
    syntax validation, dependency checks, and system resource monitoring.
    """
    for py_file in proj.rglob("*.py"):
        if stop_event.is_set():
            report.add_issue("Scan aborted during advanced Python checks.")
            return
        check_encoding(py_file, report)
        check_permissions(py_file, report)
        check_file_size(py_file, report)
        sanitized = sanitize_path(str(py_file))
        report.add_pass(f"Sanitized path: {sanitized}")
    check_python_syntax(proj, report)
    check_pycompile(proj, report)
    env_path = proj / ".env"
    check_env_vars(["DB_HOST", "DB_USER", "DB_PASS"], report, env_path)
    check_dependencies(report, proj)
    check_system_resources(report)

# Auto-fix Feature for .env File
def backup_and_fix_env(env_path: Path, report) -> None:
    """
    Creates a backup of .env and re-encodes the contents to UTF-8.
    """
    if not env_path.exists():
        report.add_issue(f".env file not found; cannot fix: {env_path}")
        return
    try:
        content = env_path.read_text(encoding="ISO-8859-1", errors="replace")
        backup_path = env_path.with_suffix(".env.backup")
        shutil.copy(env_path, backup_path)
        report.add_pass(f"Backup for .env created at: {backup_path}")
        env_path.write_text(content, encoding="utf-8", errors="replace")
        report.add_pass(f".env re-encoded to UTF-8: {env_path}")
    except Exception as ex:
        report.add_issue(f"Failed to fix .env file: {ex}")

# Report Class for Terminal Output
class Report:
    def __init__(self, fmt: str = "text") -> None:
        self.issues: List[str] = []
        self.passes: List[str] = []
        self.fmt = fmt

    def add_issue(self, msg: str) -> None:
        logging.warning(msg)
        self.issues.append(msg)

    def add_pass(self, msg: str) -> None:
        logging.info(msg)
        self.passes.append(msg)

    def summary(self) -> None:
        print(f"\n{C.BOLD}Doctor Script Summary{C.RESET}")
        print(f"{C.BLUE}{'-'*60}{C.RESET}")
        if self.issues:
            print(f"{C.RED}Issues Detected:{C.RESET}")
            for idx, message in enumerate(self.issues, 1):
                print(f"  {idx}. {message}")
        else:
            print(f"{C.GREEN}No issues detected!{C.RESET}")
        print(f"{C.BLUE}{'-'*60}{C.RESET}")
        print(f"{C.BLUE}Passed Checks:{C.RESET}")
        for idx, message in enumerate(self.passes, 1):
            print(f"  {idx}. {message}")
        print(f"{C.BLUE}{'-'*60}{C.RESET}")

# File and Tool Check Functions
def check_file(path: Path, report: Report) -> bool:
    """
    Verifies that the file exists and is readable.
    """
    if not path.exists():
        report.add_issue(f"File not found: {path}")
        return False
    if not os.access(path, os.R_OK):
        report.add_issue(f"File not readable: {path}")
        return False
    report.add_pass(f"File exists and is readable: {path}")
    return True

def check_tool(name: str, cmd: List[str], report,
               parser_func: Callable[[str], str] = lambda out: out.splitlines()[0]) -> bool:
    """
    Checks for a system tool and logs its version information.
    """
    if stop_event.is_set():
        return False
    logging.info(f"Checking {name}...")
    code, out, err = run_cmd(cmd)
    if code == 0 and (out or err):
        version = parser_func(out or err)
        report.add_pass(f"{name} available: {version}")
        return True
    report.add_issue(f"{name} missing or version check failed.")
    return False

# Language-Specific Checks
def python_checks(proj: Path, report: Report) -> None:
    """
    Runs Python-specific diagnostics (linting, type checking, tests).
    """
    if stop_event.is_set():
        return
    if (proj / "requirements.txt").exists() or (proj / "pyproject.toml").exists():
        for tool, args in [
            ("flake8", [sys.executable, "-m", "flake8", str(proj)]),
            ("mypy", [sys.executable, "-m", "mypy", str(proj)]),
            ("pytest", [sys.executable, "-m", "pytest", str(proj)])
        ]:
            check_tool(tool, args, report=report)
    else:
        report.add_pass("No Python configuration found; skipping Python checks.")

def cpp_checks(proj: Path, report: Report) -> None:
    """
    Runs C++ diagnostics using CMake.
    """
    if stop_event.is_set():
        return
    if (proj / "CMakeLists.txt").exists():
        build_dir = proj / "_build"
        build_dir.mkdir(exist_ok=True)
        check_tool("cmake-configure", ["cmake", str(proj)], report=report)
        check_tool("cmake-build", ["cmake", "--build", str(build_dir)], report=report)
    else:
        report.add_pass("No CMake project found; skipping C++ checks.")

def java_checks(proj: Path, report: Report) -> None:
    """
    Runs diagnostics for Java projects using Maven or Gradle.
    """
    if stop_event.is_set():
        return
    if (proj / "pom.xml").exists():
        check_tool("maven-compile", ["mvn", "-f", str(proj / "pom.xml"), "compile"], report=report)
    elif (proj / "build.gradle").exists():
        check_tool("gradle-build", ["gradle", "build", "-p", str(proj)], report=report)
    else:
        report.add_pass("No Java project found; skipping Java checks.")

def js_checks(proj: Path, report: Report) -> None:
    """
    Runs JavaScript/TypeScript checks (linting, tests).
    """
    if stop_event.is_set():
        return
    if (proj / "package.json").exists():
        check_tool("npm-install", ["npm", "install"], report=report)
        check_tool("npm-lint", ["npm", "run", "lint", "--prefix", str(proj)], report=report)
        check_tool("npm-test", ["npm", "test", "--prefix", str(proj)], report=report)
    else:
        report.add_pass("No package.json found; skipping JS/TS checks.")

def dotnet_checks(proj: Path, report: Report) -> None:
    """
    Runs .NET diagnostics for available solution files.
    """
    if stop_event.is_set():
        return
    sln_files = list(proj.glob("*.sln"))
    if sln_files:
        for sln in sln_files:
            check_tool("dotnet-build", ["dotnet", "build", str(sln)], report=report)
            check_tool("dotnet-test", ["dotnet", "test", str(sln)], report=report)
    else:
        report.add_pass("No .NET solution found; skipping .NET checks.")

def rust_checks(proj: Path, report: Report) -> None:
    """
    Runs Rust diagnostics using Cargo.
    """
    if stop_event.is_set():
        return
    if (proj / "Cargo.toml").exists():
        check_tool("cargo-check", ["cargo", "check", "--manifest-path", str(proj / "Cargo.toml")], report=report)
        check_tool("cargo-test", ["cargo", "test", "--manifest-path", str(proj / "Cargo.toml")], report=report)
    else:
        report.add_pass("No Cargo.toml found; skipping Rust checks.")

def go_checks(proj: Path, report: Report) -> None:
    """
    Runs diagnostics for Go projects.
    """
    if stop_event.is_set():
        return
    if (proj / "go.mod").exists():
        check_tool("go-build", ["go", "build", "./..."], report=report)
        check_tool("go-test", ["go", "test", "./..."], report=report)
    else:
        report.add_pass("No go.mod found; skipping Go checks.")

def docker_checks(proj: Path, report: Report) -> None:
    """
    Runs Docker diagnostics including Dockerfile and docker-compose checks.
    """
    if stop_event.is_set():
        return
    if (proj / "Dockerfile").exists():
        check_tool("docker-build", ["docker", "build", "-t", "mavis_project", str(proj)], report=report)
    if (proj / "docker-compose.yml").exists():
        check_tool("docker-compose-config", ["docker-compose", "-f", str(proj / "docker-compose.yml"), "config"], report=report)
    check_tool("docker-version", ["docker", "--version"], report=report)

# Main Execution
def main() -> None:
    parser = argparse.ArgumentParser("Doctor Script: Comprehensive Full-Stack Project Checker")
    parser.add_argument("-p", "--path", type=Path, help="Project path")
    parser.add_argument("-t", "--threads", type=int, default=DEFAULT_THREADS, help="Number of parallel threads")
    parser.add_argument("-o", "--output", choices=["text", "json"], default="text", help="Output format (terminal only)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--fix-env", action="store_true", help="Backup and fix .env encoding issues automatically")
    args = parser.parse_args()

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format=LOG_FORMAT, handlers=[logging.StreamHandler(sys.stdout)])
    logging.info("Starting Doctor Script...")

    project_path = detect_project_path(args.path)
    print(f"{C.BOLD}Scanning project at: {project_path.resolve()}{C.RESET}")

    report = Report(fmt=args.output)

    # Step 1: Check .env file and apply auto-fix if requested.
    env_file = project_path / ".env"
    if check_file(env_file, report):
        if args.fix_env:
            backup_and_fix_env(env_file, report)

    # Step 2: Check system tools.
    system_tools = [
        ("python", [sys.executable, "--version"]),
        ("git", ["git", "--version"]),
        ("wmic", ["wmic", "os", "get", "Caption"]),
        ("wsl", ["wsl", "--version"]),
        ("powershell", ["powershell", "-Command", "$PSVersionTable.PSVersion"]),
        ("docker", ["docker", "--version"])
    ]
    for name, cmd in system_tools:
        if stop_event.is_set():
            break
        check_tool(name, cmd, report=report)

    # Step 3: Run language-specific diagnostics in parallel.
    tasks: List[Callable[[Path, Report], None]] = [
        python_checks,
        cpp_checks,
        java_checks,
        js_checks,
        dotnet_checks,
        rust_checks,
        go_checks,
        docker_checks
    ]
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(func, project_path, report) for func in tasks]
        for f in as_completed(futures):
            if stop_event.is_set():
                break

    # Step 4: Execute advanced project-wide checks.
    advanced_checks(project_path, report)

    # Step 5: Check miscellaneous files (non-Python, non-.env) for size and modification.
    for file in project_path.rglob("*"):
        if stop_event.is_set():
            break
        if file.is_file() and file.suffix not in [".py", ".env"]:
            check_file_size(file, report)

    # Final Summary Output.
    report.summary()
    logging.info("Doctor Script completed successfully.")

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=monitor_keyboard, daemon=True)
    monitor_thread.start()

    try:
        main()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        stop_event.set()
        if monitor_thread.is_alive():
            monitor_thread.join()
