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
import os

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

def start_jupyter():
    try:
        print("\nJupyter Information:")
        print("--------------------")

        user_home = os.path.expanduser("~")
        venv_python = os.path.join(user_home, "PycharmProjects", "MAVIS", ".env", "Scripts", "python.exe")

        if not os.path.isfile(venv_python):
            print(f"{red}Error{reset}: The virtual environment {venv_python} does not exist.")
            sys.exit(1)

        try:
            subprocess.run([venv_python, "-m", "pip", "show", "jupyter"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print(f"{red}Error: Jupyter is not installed in the virtual environment.{reset}")
            sys.exit(1)

        jupyter_directory = os.path.join(user_home, "PycharmProjects", "MAVIS", "jupyter")
        if not os.path.isdir(jupyter_directory):
            print(f"{red}Error: The specified directory '{jupyter_directory}' does not exist.{reset}")
            sys.exit(1)

        # Starten von Jupyter ohne Token und Passwort, mit verbesserten CORS- und Sicherheitskonfigurationen
        jupyter_command = [
            venv_python,
            "-m", "notebook",
            "--NotebookApp.ip=0.0.0.0",
            "--NotebookApp.port=8888",
            f"--NotebookApp.notebook_dir={jupyter_directory}",
            "--NotebookApp.disable_check_xsrf=True",
            "--NotebookApp.allow_origin='*'",
            "--NotebookApp.allow_root=True",
            "--NotebookApp.token=",  # Kein Token
            "--NotebookApp.password=",  # Kein Passwort
            "--no-browser",
            "--NotebookApp.tornado_settings={\"headers\": {\"Content-Security-Policy\": \"frame-ancestors *\"}}",
            "--NotebookApp.log_level=DEBUG"  # Aktiviertes Debug-Logging
        ]

        # Versuch, den Jupyter-Server zu starten
        try:
            subprocess.run(jupyter_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"{yellow}Restarting Jupyter due to error:{reset} {e}")
            subprocess.run(jupyter_command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"{red}Error starting Jupyter Notebook{reset}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"{red}Unexpected error{reset}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_jupyter()
