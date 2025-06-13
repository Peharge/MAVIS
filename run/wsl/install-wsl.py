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

def find_compiler():
    """
    Searches for a C++ compiler in the PATH environment.
    Primarily uses 'g++' and alternatively 'clang++'.

    Returns:
        str: Name of the found compiler or None if none was found.
    """
    for compiler in ["g++", "clang++"]:
        path = shutil.which(compiler)
        if path:
            logger.info("Compiler '%s' found: %s", compiler, path)
            return compiler
    return None

def write_logfile(target_dir, compiler_name):
    """
    Writes a log file with information about the found compiler environment.

    Args:
        target_dir (str): Target directory where the log file will be placed.
        compiler_name (str): Name of the found compiler.
    """
    log_file = os.path.join(target_dir, "institution_installed.txt")
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("C++ Compiler detected and ready.\n")
            f.write(f"Compiler used: {compiler_name}\n")
        logger.info("Installation status written to log file: %s", log_file)
    except Exception as e:
        logger.warning("Error writing log file: %s", e)

def verify_compiler(compiler, temp_dir):
    """
    Creates a temporary test C++ file and compiles it with the found compiler
    to ensure it is working properly.

    Args:
        compiler (str): Name of the compiler (g++ or clang++).
        temp_dir (str): Temporary directory for the compilation test.

    Returns:
        bool: True if the test was successful, otherwise False.
    """
    logger.info("Testing functionality of '%s'...", compiler)
    test_cpp = os.path.join(temp_dir, "institution_test.cpp")
    exe_output = os.path.join(temp_dir, "institution_app")  # In Linux environments, no file extension is needed

    # Create test C++ file
    try:
        with open(test_cpp, "w", encoding="utf-8") as f:
            f.write('#include <iostream>\n'
                    'int main() {\n'
                    '    std::cout << "Hello from ' + compiler + '!" << std::endl;\n'
                                                                 '    return 0;\n'
                                                                 '}\n')
    except Exception as e:
        logger.error("Error creating test file: %s", e)
        return False

    # Compile the test file with the detected compiler
    compile_command = [compiler, test_cpp, "-o", exe_output]
    try:
        result = subprocess.run(
            compile_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False
        )
        logger.info("Compilation output:\n%s", result.stdout)
    except Exception as e:
        logger.error("Error during compilation test: %s", e)
        return False

    # Check if the executable was created
    if os.path.exists(exe_output):
        logger.info("Compilation successful. The '%s' compiler is working properly.", compiler)
        return True
    else:
        logger.error(
            "Compilation failed. Please ensure that a working C++ compiler is installed.")
        return False

def create_compiler_folder(target_dir, compiler):
    """
    Creates a shell script in the specified target directory ('institution-cpp-compiler')
    that invokes the compiler and compiles an example project.

    Args:
        target_dir (str): Directory where the compiler script will be placed.
        compiler (str): Name of the compiler used.
    """
    os.makedirs(target_dir, exist_ok=True)
    script_file = os.path.join(target_dir, "build_institution.sh")
    try:
        with open(script_file, "w", encoding="utf-8") as f:
            f.write("#!/bin/bash\n")
            f.write("echo 'Institution C++ Compiler Environment activated.'\n")
            # Example: Change to the project directory and compile the main source file.
            f.write("cd \"$(dirname \"$0\")/../INSTITUTION\"\n")
            f.write("echo 'Starting compilation of the INSTITUTION project...'\n")
            # Placeholder: Adjust the command according to your project structure and files.
            f.write(f"{compiler} -o institution_app app_main.cpp\n")
            f.write("echo 'Compilation complete.'\n")
            f.write("read -p 'Press any key to continue...'\n")
        # Ensure the script is executable
        os.chmod(script_file, 0o755)
        logger.info("Shell script for the compiler created: %s", script_file)
    except Exception as e:
        logger.error("Error creating the compiler script: %s", e)

def main():
    """
    Main function controlling the installation process:
      - Checks if the script is running in a Linux environment (WSL).
      - Determines the project directory.
      - Searches for a C++ compiler.
      - Runs a compilation test.
      - Creates the special 'institution-cpp-compiler' folder with a start script.
      - Writes a log file in the target directory.
    """
    try:
        if platform.system() != "Linux":
            raise EnvironmentError("This installation script is specifically for WSL (Linux) on Windows.")

        username = getpass.getuser()
        # Example: Project directory in the home directory
        project_root = os.path.join("/home", username, "institution_projects", "INSTITUTION")
        # Target directory for the "Compiler" is created here:
        compiler_dir = os.path.join(project_root, "institution-cpp-compiler")
        os.makedirs(compiler_dir, exist_ok=True)
        logger.info("Project directory: %s", project_root)

        # Temporary directory for the compilation test
        temp_dir = os.path.join(project_root, "ws_test_temp")
        os.makedirs(temp_dir, exist_ok=True)

        logger.info("Searching for a working C++ compiler...")
        compiler = find_compiler()
        if not compiler:
            raise FileNotFoundError("No C++ compiler found. Please install g++ or clang++.")

        # Run the compilation test
        if verify_compiler(compiler, temp_dir):
            write_logfile(compiler_dir, compiler)
            create_compiler_folder(compiler_dir, compiler)
            logger.info("The C++ compiler for Institution was successfully detected and tested.")
        else:
            raise Exception("The compilation test failed.")

        # Cleanup: Remove the temporary directory
        shutil.rmtree(temp_dir, ignore_errors=True)
        logger.info("Temporary files have been removed.")

    except Exception as e:
        logger.error("An error occurred during installation:")
        logger.error(str(e))
        logger.error("Stacktrace:\n%s", traceback.format_exc())
        logger.error(
            "Please ensure that a working C++ compiler is installed and the paths are correct.")
        sys.exit(1)

if __name__ == "__main__":
    main()
