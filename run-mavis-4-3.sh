#!/bin/bash

# Englisch Peharge: This source code is released under the MIT License.
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

# Deutsch Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
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

# Français Peharge: Ce code source est publié sous la licence MIT.
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

USERNAME=$(whoami)
PYTHON_PATH="/home/$USERNAME/PycharmProjects/MAVIS/.env/bin/python3"
SCRIPT_PATH_1="/home/$USERNAME/PycharmProjects/MAVIS/info/info-start-mavis-4-3.py"
SCRIPT_PATH_2="/home/$USERNAME/PycharmProjects/MAVIS/install/install-info-mavis-4.py"
SCRIPT_PATH_update="/home/$USERNAME/PycharmProjects/MAVIS/update/update-repository-windows.py"
SCRIPT_PATH_account="/home/$USERNAME/PycharmProjects/MAVIS/account/account-lx.py"
SCRIPT_PATH_3="/home/$USERNAME/PycharmProjects/MAVIS/install/install-ollama-mavis-4-lx.py"
PYTHON_SCRIPT_PATH="/home/$USERNAME/PycharmProjects/MAVIS/run-browser/run-browser-one.py"
run_jup="/home/$USERNAME/PycharmProjects/MAVIS/run-jup/run-jup.py"
run_grafana="/home/$USERNAME/PycharmProjects/MAVIS/run-grafana/run-grafana.py"
run_solution="/home/$USERNAME/PycharmProjects/MAVIS/solution/run-solution-4.py"
SCRIPT_PATH_5="/home/$USERNAME/PycharmProjects/MAVIS/mavis-4-3-main-lx.py"

if [ ! -f "$PYTHON_PATH" ]; then
  echo "Error: Python interpreter not found: $PYTHON_PATH"
  exit 1
fi

for script in "$SCRIPT_PATH_1" "$SCRIPT_PATH_2" "$SCRIPT_PATH_update" \
             "$SCRIPT_PATH_account" "$SCRIPT_PATH_3" \
             "$PYTHON_SCRIPT_PATH"; do
  if [ ! -f "$script" ]; then
    echo "Error: Script not found: $script"
    exit 1
  fi
  "$PYTHON_PATH" "$script"
done

if [ ! -f "$SCRIPT_PATH_5" ]; then
  echo "Error: Script not found: $SCRIPT_PATH_5"
  exit 1
fi
"$PYTHON_PATH" "$SCRIPT_PATH_5"

echo
echo "The scripts have been executed, Ollama has been started, and the browser has been opened."
read -p "Press enter to exit."
