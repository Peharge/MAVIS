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
import traceback
import getpass
import platform
import shutil
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

def find_gpp():
    """
    Searches for the g++ compiler in the system path using the "where" command.

    Returns:
        str: Path to the g++ compiler if found, otherwise None.
    """
    logger.info("Searching for g++ compiler in the system path...")
    try:
        result = subprocess.run(
            ["where", "g++"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        # Use the first found path
        gpp_path = result.stdout.splitlines()[0].strip()
        logger.info("Found g++ compiler: %s", gpp_path)
        return gpp_path
    except Exception as e:
        logger.error("g++ compiler could not be found: %s", e)
        return None

def write_logfile(target_dir, gpp_path):
    """
    Writes a log file with information about the found g++ environment.

    Args:
        target_dir (str): Target directory where the log file will be placed.
        gpp_path (str): Path to the g++ compiler.
    """
    log_file = os.path.join(target_dir, "gpp_installed.txt")
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("g++ Compiler detected and ready.\n")
            f.write(f"g++ path: {gpp_path}\n")
        logger.info("Installation status logged in: %s", log_file)
    except Exception as e:
        logger.warning("Log file could not be written: %s", e)

def verify_compiler(gpp_path, temp_dir):
    """
    Creates a temporary test C++ file and compiles it with g++ to ensure
    that the g++ compiler is working correctly.

    Args:
        gpp_path (str): Path to the g++ compiler.
        temp_dir (str): Temporary directory for the compilation test.

    Returns:
        bool: True if the test was successful, otherwise False.
    """
    logger.info("Testing g++ compiler availability...")
    test_cpp = os.path.join(temp_dir, "test.cpp")
    exe_output = os.path.join(temp_dir, "test.exe")

    # Create the test C++ file
    try:
        with open(test_cpp, "w", encoding="utf-8") as f:
            f.write('#include <iostream>\n')
            f.write('int main() { std::cout << "Hello from g++!" << std::endl; return 0; }\n')
    except Exception as e:
        logger.error("Error creating test file: %s", e)
        return False

    # Compile the test file with g++
    compile_cmd = [gpp_path, test_cpp, "-o", exe_output]
    try:
        result = subprocess.run(
            compile_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='cp850',
            errors='replace',
            check=False
        )
        logger.info("Output of the compilation test:\n%s", result.stdout)
    except Exception as e:
        logger.error("Error running compilation test: %s", e)
        return False

    if os.path.exists(exe_output):
        logger.info("Compilation successful. g++ is working correctly.")
        return True
    else:
        logger.error("Compilation failed. Please ensure that g++ is correctly installed.")
        return False

def create_compiler_folder(target_dir, gpp_path):
    """
    Creates a folder in the specified target directory ('institution-gpp-compiler') with a batch file
    that invokes the g++ compiler and runs an example compilation command.

    Args:
        target_dir (str): The directory where the compiler tools will be placed.
        gpp_path (str): Path to the g++ compiler.
    """
    os.makedirs(target_dir, exist_ok=True)

    batch_file = os.path.join(target_dir, "build_institution.bat")
    try:
        with open(batch_file, "w", encoding="utf-8") as f:
            f.write("@echo off\n")
            f.write("echo g++ Compiler Environment enabled.\n")
            # Example: Change to the project directory and compile a specific source file.
            f.write('cd /d "%~dp0\\..\\..\\InstitutionProject"\n')
            f.write("echo Starting the compilation of the Institution project...\n")
            # Placeholder: Adjust the g++ command according to your project structure.
            f.write('"' + gpp_path + '" main.cpp -o institution_project.exe\n')
            f.write("pause\n")
        logger.info("Batch file created for the compiler: %s", batch_file)
    except Exception as e:
        logger.error("Error creating batch file: %s", e)

def main():
    """
    Main function that controls the flow:
      - Determine the project directory.
      - Search for the g++ compiler.
      - Test the compiler.
      - Create the special 'institution-gpp-compiler' folder with a batch file
        that can be used to compile the Institution project.
      - Write a log file in the target directory.
    """
    try:
        if platform.system() != "Windows":
            raise EnvironmentError("This installation script is only intended for Windows.")

        username = getpass.getuser()
        project_root = os.path.join("C:\\Users", username, "PycharmProjects", "InstitutionProject")
        # Target folder for the "Compiler"
        compiler_dir = os.path.join(project_root, "institution-gpp-compiler")
        os.makedirs(compiler_dir, exist_ok=True)
        logger.info("Project directory: %s", project_root)

        # Temporary directory for the compilation test
        temp_dir = os.path.join(project_root, "gpp_test")
        os.makedirs(temp_dir, exist_ok=True)

        logger.info("Searching for the g++ compiler...")
        gpp_path = find_gpp()
        if not gpp_path:
            raise FileNotFoundError("g++ compiler could not be found. Please ensure that g++ is installed.")

        # Test the g++ compiler
        if verify_compiler(gpp_path, temp_dir):
            write_logfile(compiler_dir, gpp_path)
            create_compiler_folder(compiler_dir, gpp_path)
            logger.info("g++ compiler successfully detected and tested.")
        else:
            raise Exception("The compilation test failed.")

        # Cleanup: Remove the temporary directory
        shutil.rmtree(temp_dir, ignore_errors=True)
        logger.info("Temporary files have been removed.")

    except Exception as e:
        logger.error("An error occurred during installation:")
        logger.error(str(e))
        logger.error("Stacktrace:\n%s", traceback.format_exc())
        logger.error("Please ensure that g++ is correctly installed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
