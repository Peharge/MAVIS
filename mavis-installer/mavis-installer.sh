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

# Funktionen für die Installation
install_git() {
    if command -v git >/dev/null 2>&1; then
        echo "✅ Git is already installed."
    else
        echo "🔄 Installing Git..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install git || { echo "❌ Git installation failed. Visit https://git-scm.com."; exit 1; }
        else
            sudo apt update && sudo apt install -y git || { echo "❌ Git installation failed. Visit https://git-scm.com."; exit 1; }
        fi
    fi
}

install_python() {
    if command -v python3 >/dev/null 2>&1; then
        echo "✅ Python is already installed."
    else
        echo "🔄 Installing Python..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install python || { echo "❌ Python installation failed. Visit https://www.python.org."; exit 1; }
        else
            sudo apt update && sudo apt install -y python3 python3-venv || { echo "❌ Python installation failed. Visit https://www.python.org."; exit 1; }
        fi
    fi
}

install_ollama() {
    if command -v ollama >/dev/null 2>&1; then
        echo "✅ Ollama is already installed."
    else
        echo "🔄 Installing Ollama..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install --cask ollama || { echo "❌ Ollama installation failed. Visit https://ollama.com/download."; exit 1; }
        else
            curl -fsSL https://ollama.com/download | sh || { echo "❌ Ollama installation failed. Visit https://ollama.com/download."; exit 1; }
        fi
    fi
}

create_folder() {
    folder="$HOME/PycharmProjects"
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
        echo "✅ Folder created: $folder"
    else
        echo "ℹ️ Folder already exists: $folder"
    fi
}

clone_repository() {
    repo_url="https://github.com/Peharge/MAVIS"
    target_path="$HOME/PycharmProjects/MAVIS"
    if [ -d "$target_path" ]; then
        echo "ℹ️ Repository has already been cloned."
    else
        echo "🔄 Cloning repository..."
        git clone "$repo_url" "$target_path" || { echo "❌ Repository could not be cloned."; exit 1; }
    fi
}

create_virtual_environment() {
    env_path="$HOME/PycharmProjects/MAVIS/env"
    if [ -d "$env_path" ]; then
        echo "ℹ️ Virtual environment already exists."
    else
        echo "🔄 Creating virtual environment..."
        python3 -m venv "$env_path" || { echo "❌ Virtual environment could not be created."; exit 1; }
    fi
}

start_ui() {
    script_path="$HOME/PycharmProjects/MAVIS/run-mavis-all.sh"
    if [ -f "$script_path" ]; then
        echo "🚀 Starting User Interface..."
        bash "$script_path"
    else
        echo "❌ User interface script not found."
        exit 1
    fi
}

menu() {
    clear
    echo "MAVIS Installer"
    echo "================="
    echo "1. Install prerequisites (Git, Python, Ollama)"
    echo "2. Create folder"
    echo "3. Clone repository"
    echo "4. Create virtual environment"
    echo "5. Start user interface"
    echo "6. Finish"
    echo "================="
    read -rp "Select an option: " choice
    case $choice in
        1) install_git; install_python; install_ollama ;;
        2) create_folder ;;
        3) clone_repository ;;
        4) create_virtual_environment ;;
        5) start_ui ;;
        6) exit 0 ;;
        *) echo "❌ Invalid input. Please try again." ;;
    esac
    sleep 2
    menu
}

menu
