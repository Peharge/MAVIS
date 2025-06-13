#!/bin/bash

# Englisch Peharge: This source code is released under the MIT License.
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
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
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
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français Peharge: Ce code source est publié sous la licence MIT.
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
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

# Set variables
LC_ALL=en_US.UTF-8
export LC_ALL

# Display the logo with colored text
echo -e "\n"
echo -e "\033[34m      ██╗     █╗     \033[0m\033[34m    ███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗\033[0m"
echo -e "\033[34m    ██████╗  ████╗   \033[0m\033[34m    ████╗ ████║██╔══██╗██║   ██║██║██╔════╝\033[0m"
echo -e "\033[34m   ████████╗  ████╗  \033[0m\033[34m    ██╔████╔██║███████║██║   ██║██║███████╗\033[0m"
echo -e "\033[34m  ████╔█████╗  ████╗ \033[0m\033[34m    ██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║\033[0m"
echo -e "\033[34m ████╔╝ █████╗  ████╗\033[0m\033[34m    ██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║\033[0m"
echo -e "\033[34m ╚═══╝   ███╔╝  ╚═══╝\033[0m\033[34m    ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝\033[0m"
echo -e "\033[34m          █╔╝\033[0m\033[34m"
echo -e "\033[34m          ╚╝\033[0m\033[34m"

echo -e "\n"
echo -e "\033[37m ██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗     ██╗  ██╗\033[0m"
echo -e "\033[37m ██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗    ██║  ██║\033[0m"
echo -e "\033[37m ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝    ███████║\033[0m"
echo -e "\033[37m ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗    ╚════██║\033[0m"
echo -e "\033[37m ███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║         ██║\033[0m"
echo -e "\033[37m ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝         ╚═╝\033[0m"
echo -e "\n"
echo "Initiating high-tech installation..."
echo "Prepare for the next level!"
echo -e "\n"
echo "MIT License"
echo "Copyright (c) 2024"
echo "Peharge"
echo -e "\n"
echo "Permission is hereby granted, free of charge, to any person obtaining a copy"
echo "of this software and associated documentation files (the \"Software\"), to deal"
echo "in the Software without restriction, including without limitation the rights"
echo "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"
echo "copies of the Software, and to permit persons to whom the Software is"
echo "furnished to do so, subject to the following conditions:"
echo -e "\n"
echo "The above copyright notice and this permission notice shall be included in all"
echo "copies or substantial portions of the Software."
echo -e "\n"
echo "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR"
echo "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"
echo "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"
echo "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"
echo "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"
echo "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE"
echo "SOFTWARE."
echo -e "\n"
echo "Gooo..."
echo -e "\n"

# ----------------------------------------------------------------------------
# Peharge Python 3.12 Installation Script
# ----------------------------------------------------------------------------
# This script checks if Python 3.12 is already installed, and if not, offers to
# install it either via the system's package manager or by downloading the
# installer directly from the official Python website.
# ----------------------------------------------------------------------------

# Check if Python is already installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3.12 is not installed."
    read -p "Would you like to install Python 3.12? [y/n]:" install_python

    if [[ "$install_python" =~ ^[Yy]$ ]]; then
        echo "Downloading Python 3.12 installer..."

        # Define the Python download URL and file paths
        PYTHON_URL="https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz"
        PYTHON_TAR="$TEMP_DIR/python-3.12.2.tgz"
        PYTHON_DIR="$HOME/python-3.12"

        # Download Python tarball
        wget "$PYTHON_URL" -O "$PYTHON_TAR"

        if [[ -f "$PYTHON_TAR" ]]; then
            echo "Extracting Python tarball..."
            mkdir -p "$PYTHON_DIR"
            tar -xzf "$PYTHON_TAR" -C "$PYTHON_DIR" --strip-components=1
            rm -f "$PYTHON_TAR"

            # Install dependencies
            sudo apt update && sudo apt install -y build-essential libssl-dev zlib1g-dev \
                libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
                libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

            # Configure, build, and install Python
            cd "$PYTHON_DIR"
            ./configure --enable-optimizations
            make -j "$(nproc)"
            sudo make altinstall

            # Verify installation
            if python3.12 --version &>/dev/null; then
                echo "✅ Python 3.12 successfully installed!"
            else
                echo "❌ Error: Python installation failed! Manual installation required."
                echo "Please visit https://www.python.org/downloads to install Python manually."
            fi
        else
            echo "❌ Error: Python installer could not be downloaded!"
        fi
    else
        echo "Installation aborted. Please install Python 3.12 manually: https://www.python.org/downloads"
    fi
else
    echo "✅ Python is already installed."
fi

# ----------------------------------------------------------------------------
# Peharge Git Installation Script
# ----------------------------------------------------------------------------
# This script checks if Git is installed, and if not, offers to install it
# either via the system's package manager or by downloading the portable Git
# release from GitHub.
# ----------------------------------------------------------------------------

# Check if Git is already installed
if ! command -v git &>/dev/null; then
    echo "Git is not installed."
    read -p "Would you like to install Git? [y/n]:" install_git

    if [[ "$install_git" =~ ^[Yy]$ ]]; then
        echo "Downloading Git installer..."

        # Define the Git download URL and file paths
        GIT_URL="https://github.com/git-for-windows/git/releases/latest/download/PortableGit-2.44.0-64-bit.zip"
        GIT_ZIP="$TEMP_DIR/git-portable.zip"
        GIT_DIR="$HOME/git-portable"

        # Download Git ZIP
        wget "$GIT_URL" -O "$GIT_ZIP"

        if [[ -f "$GIT_ZIP" ]]; then
            echo "Extracting Git ZIP..."
            mkdir -p "$GIT_DIR"
            unzip -q "$GIT_ZIP" -d "$GIT_DIR"
            rm -f "$GIT_ZIP"

            # Add Git to PATH
            echo "Adding Git to PATH..."
            export PATH="$GIT_DIR/bin:$PATH"
            echo "export PATH=\"$GIT_DIR/bin:\$PATH\"" >> "$HOME/.bashrc"

            # Verify installation
            if git --version &>/dev/null; then
                echo "✅ Git successfully installed!"
            else
                echo "❌ Error: Git installation failed! Manual installation required."
                echo "Please visit https://git-scm.com/downloads to install Git manually."
            fi
        else
            echo "❌ Error: Git ZIP download failed! Manual installation required."
        fi
    else
        echo "Installation aborted. Please install Git manually: https://git-scm.com/downloads"
    fi
else
    echo "✅ Git is already installed."
fi

# ----------------------------------------------------------------------------
# Peharge Ollama Installation Script
# ----------------------------------------------------------------------------
# This script checks if Ollama is installed, and if not, offers to install it
# either via downloading the Ollama setup package or using a portable ZIP version.
# ----------------------------------------------------------------------------

# Check if Ollama is already installed
if ! command -v ollama &>/dev/null; then
    echo "Ollama is not installed."
    read -p "Would you like to install Ollama? [y/n]:" install_ollama

    if [[ "$install_ollama" =~ ^[Yy]$ ]]; then
        echo "Downloading Ollama installer..."

        # Define the Ollama download URL and file paths
        OLLAMA_URL="https://ollama.com/download/OllamaPortable.zip"
        OLLAMA_ZIP="$TEMP_DIR/OllamaPortable.zip"
        OLLAMA_DIR="$HOME/ollama"

        # Download Ollama ZIP
        wget "$OLLAMA_URL" -O "$OLLAMA_ZIP"

        if [[ -f "$OLLAMA_ZIP" ]]; then
            echo "Extracting Ollama ZIP..."
            mkdir -p "$OLLAMA_DIR"
            unzip -q "$OLLAMA_ZIP" -d "$OLLAMA_DIR"
            rm -f "$OLLAMA_ZIP"

            # Add Ollama to PATH
            echo "Adding Ollama to PATH..."
            export PATH="$OLLAMA_DIR:$PATH"
            echo "export PATH=\"$OLLAMA_DIR:\$PATH\"" >> "$HOME/.bashrc"

            # Verify installation
            if ollama --version &>/dev/null; then
                echo "✅ Ollama successfully installed!"
            else
                echo "❌ Error: Ollama installation failed! Manual installation required."
                echo "Please visit https://ollama.com/download to install Ollama manually."
            fi
        else
            echo "❌ Error: Ollama ZIP download failed! Manual installation required."
        fi
    else
        echo "Installation aborted. Please install Ollama manually: https://ollama.com/download"
    fi
else
    echo "✅ Ollama is already installed."
fi

# ----------------------------------------------------------------------------
# FFmpeg Installation Script for Linux (Debian/Arch)
# ----------------------------------------------------------------------------
# This script checks if FFmpeg is installed, and if not, offers to install it
# either via downloading the FFmpeg build from a URL or using a portable ZIP version.
# ----------------------------------------------------------------------------

# Check if FFmpeg is already installed
if ! command -v ffmpeg &>/dev/null; then
    echo "FFmpeg is not installed."
    read -p "Would you like to install FFmpeg? [y/n]:" install_ffmpeg

    if [[ "$install_ffmpeg" =~ ^[Yy]$ ]]; then
        echo "Downloading FFmpeg installer..."

        # Define the FFmpeg download URL and file paths
        FFMPEG_URL="https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        FFMPEG_ZIP="$TEMP_DIR/ffmpeg.zip"
        FFMPEG_DIR="$HOME/ffmpeg"

        # Download FFmpeg ZIP
        wget "$FFMPEG_URL" -O "$FFMPEG_ZIP"

        if [[ -f "$FFMPEG_ZIP" ]]; then
            echo "Extracting FFmpeg..."
            mkdir -p "$FFMPEG_DIR"
            unzip -q "$FFMPEG_ZIP" -d "$FFMPEG_DIR"
            rm -f "$FFMPEG_ZIP"

            # Add FFmpeg to PATH
            echo "Adding FFmpeg to PATH..."
            export PATH="$FFMPEG_DIR/bin:$PATH"
            echo "export PATH=\"$FFMPEG_DIR/bin:\$PATH\"" >> "$HOME/.bashrc"

            # Verify installation
            if ffmpeg -version &>/dev/null; then
                echo "✅ FFmpeg successfully installed!"
            else
                echo "❌ Error: FFmpeg installation failed! Manual installation required."
                echo "Please visit https://ffmpeg.org/download.html#build-linux to install FFmpeg manually."
            fi
        else
            echo "❌ Error: FFmpeg ZIP download failed! Manual installation required."
        fi
    else
        echo "Installation aborted. Please install FFmpeg manually: https://ffmpeg.org/download.html#build-linux"
    fi
else
    echo "✅ FFmpeg is already installed."
fi

# ----------------------------------------------------------------------------
# Rustup Installation Script for Linux (Debian/Arch)
# ----------------------------------------------------------------------------
# This script checks if Rustup is installed, and if not, offers to install it
# using the official installation method or an alternative method if necessary.
# ----------------------------------------------------------------------------

# Check if rustc is already installed
if ! command -v rustc &>/dev/null; then
    echo "rustc (Rust compiler) is not installed."
    read -p "Would you like to install Rustup (to get rustc)? [y/n]: " install_rustup

    if [[ "$install_rustup" =~ ^[Yy]$ ]]; then
        echo "Downloading Rustup installer..."

        # Define the Rustup installation URL
        RUSTUP_URL="https://win.rustup.rs"
        TEMP_DIR="$(mktemp -d)"
        RUSTUP_INSTALLER="$TEMP_DIR/rustup-init.sh"

        # Download the Rustup installer script
        curl --proto '=https' --tlsv1.2 -sSf "$RUSTUP_URL" > "$RUSTUP_INSTALLER"

        if [[ -f "$RUSTUP_INSTALLER" ]]; then
            echo "Running Rustup installer..."
            bash "$RUSTUP_INSTALLER" -y

            # Verify installation
            if command -v rustc &>/dev/null; then
                echo "✅ rustc successfully installed via Rustup!"
            else
                echo "❌ Error: rustc installation failed! Retrying..."
                rm -f "$RUSTUP_INSTALLER"
                curl --proto '=https' --tlsv1.2 -sSf "$RUSTUP_URL" > "$RUSTUP_INSTALLER"
                bash "$RUSTUP_INSTALLER" -y

                if command -v rustc &>/dev/null; then
                    echo "✅ rustc successfully installed on second attempt!"
                else
                    echo "❌ Second installation attempt failed! Trying alternative method..."

                    # Alternative method to download the installer
                    RUSTUP_ALT_URL="https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init.sh"
                    curl --proto '=https' --tlsv1.2 -sSf "$RUSTUP_ALT_URL" > "$RUSTUP_INSTALLER"
                    bash "$RUSTUP_INSTALLER" -y

                    if command -v rustc &>/dev/null; then
                        echo "✅ rustc successfully installed using alternative method!"
                    else
                        echo "❌ Alternative installation failed! Manual installation required."
                        echo "Please visit https://rustup.rs/ for manual installation."
                    fi
                fi
            fi
        else
            echo "❌ Error: Rustup installer could not be downloaded!"
        fi
    else
        echo "Installation aborted. Please install Rustup manually: https://rustup.rs/"
    fi
else
    echo "✅ rustc is already installed."
fi

#!/usr/bin/env bash

# Exit on errors, undefined variables, and errors in pipelines
set -Eeuo pipefail
trap 'echo "[ERROR] Unexpected error at line $LINENO" >&2; exit 1' ERR

#!/usr/bin/env bash

# Exit on errors, undefined variables, and errors in pipelines
set -Eeuo pipefail
trap 'echo "[ERROR] Unexpected error at line $LINENO" >&2; exit 1' ERR

# Constants
readonly MAVIS_DIR="$HOME/PycharmProjects/MAVIS"
readonly MAVIS_ENV_DIR="$MAVIS_DIR/.env"
readonly MAVIS_RUN_FILE="$MAVIS_DIR/run-mavis-4-all.sh"

log_info() {
  printf "%s\n" "$*"
}

log_success() {
  printf "✅ %s\n" "$*"
}

log_error() {
  printf "❌ %s\n" "$*" >&2
}

# Ensure MAVIS directory exists
if [[ ! -d "$MAVIS_DIR" ]]; then
    log_error "MAVIS directory not found: $MAVIS_DIR"
    exit 1
fi
cd "$MAVIS_DIR"
log_info "Working directory: $PWD"

# Check for existing virtual environment (.env)
if [[ -d "$MAVIS_ENV_DIR" && -f "$MAVIS_ENV_DIR/bin/activate" ]]; then
    log_success "Virtual environment already exists at $MAVIS_ENV_DIR"
else
    # Create Python virtual environment directory
    log_info "Creating Python virtual environment in $MAVIS_ENV_DIR..."
    if python3 -m venv "$MAVIS_ENV_DIR"; then
        log_success "Virtual environment created at $MAVIS_ENV_DIR"
    else
        log_error "Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
if [[ -r "$MAVIS_ENV_DIR/bin/activate" ]]; then
    # shellcheck source=/dev/null
    source "$MAVIS_ENV_DIR/bin/activate"
    log_info "Activated virtual environment"
else
    log_error "Cannot activate virtual environment: activate script missing or unreadable"
    exit 1
fi

# Ensure run script exists and is executable
if [[ ! -e "$MAVIS_RUN_FILE" ]]; then
    log_error "Run file not found: $MAVIS_RUN_FILE"
    deactivate 2>/dev/null || true
    exit 1
fi

if [[ ! -x "$MAVIS_RUN_FILE" ]]; then
    log_info "Making run file executable"
    if chmod +x "$MAVIS_RUN_FILE"; then
        log_success "Set executable permission on $MAVIS_RUN_FILE"
    else
        log_error "Failed to set executable permission on $MAVIS_RUN_FILE"
        deactivate 2>/dev/null || true
        exit 1
    fi
fi

# Execute MAVIS run script
log_info "Executing MAVIS run script"
if bash "$MAVIS_RUN_FILE"; then
    log_success "MAVIS run script completed successfully"
else
    log_error "MAVIS run script failed"
    deactivate 2>/dev/null || true
    exit 1
fi

# Deactivate virtual environment
deactivate 2>/dev/null || true
log_success "All tasks completed successfully"
exit 0
