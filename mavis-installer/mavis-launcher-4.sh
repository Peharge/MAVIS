#!/bin/bash

# ----------------------------------------------------------------------------
# Peharge Script - MIT License
# ----------------------------------------------------------------------------
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private
# and commercial purposes. However, it is recommended to modify the code only if
# you have sufficient programming knowledge, as changes could cause unintended
# errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required
# for functionality.
# It is strongly recommended to perform installation and configuration in an
# isolated environment (e.g., a virtual environment) to avoid potential conflicts
# with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other
# issues that may arise directly or indirectly from the use, modification, or
# redistribution of the code.
# ----------------------------------------------------------------------------

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

# Check if Rustup is already installed
if ! command -v rustup &>/dev/null; then
    echo "Rustup is not installed."
    read -p "Would you like to install Rustup? [y/n]:" install_rustup

    if [[ "$install_rustup" =~ ^[Yy]$ ]]; then
        echo "Downloading Rustup installer..."

        # Define the Rustup installation URL
        RUSTUP_URL="https://win.rustup.rs"
        RUSTUP_INSTALLER="$TEMP_DIR/rustup-init.sh"

        # Download the Rustup installer script
        curl --proto '=https' --tlsv1.2 -sSf "$RUSTUP_URL" > "$RUSTUP_INSTALLER"

        if [[ -f "$RUSTUP_INSTALLER" ]]; then
            echo "Running Rustup installer..."
            bash "$RUSTUP_INSTALLER" -y

            # Verify installation
            if rustup --version &>/dev/null; then
                echo "✅ Rustup successfully installed!"
            else
                echo "❌ Error: Rustup installation failed! Retrying..."
                rm -f "$RUSTUP_INSTALLER"
                curl --proto '=https' --tlsv1.2 -sSf "$RUSTUP_URL" > "$RUSTUP_INSTALLER"
                bash "$RUSTUP_INSTALLER" -y

                if rustup --version &>/dev/null; then
                    echo "✅ Rustup successfully installed!"
                else
                    echo "❌ Second installation attempt failed! Trying alternative method..."

                    # Alternative method to download the installer
                    RUSTUP_ALT_URL="https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init.sh"
                    curl --proto '=https' --tlsv1.2 -sSf "$RUSTUP_ALT_URL" > "$RUSTUP_INSTALLER"
                    bash "$RUSTUP_INSTALLER" -y

                    if rustup --version &>/dev/null; then
                        echo "✅ Rustup successfully installed using alternative method!"
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
    echo "✅ Rustup is already installed."
fi

# Define project path
PYCHARM_PROJECTS="$HOME/PycharmProjects"
MAVIS_DIR="$PYCHARM_PROJECTS/MAVIS"
MAVIS_ENV_FILE="$MAVIS_DIR/.env"
MAVIS_RUN_FILE="$MAVIS_DIR/run-mavis-4-all.sh"

# Ensure PyCharm Projects directory exists
if [ ! -d "$PYCHARM_PROJECTS" ]; then
    echo "Creating project directory: $PYCHARM_PROJECTS..."
    mkdir -p "$PYCHARM_PROJECTS"
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to create directory $PYCHARM_PROJECTS. Exiting..."
        exit 1
    fi
fi

# Change to PyCharm Projects directory
cd "$PYCHARM_PROJECTS" || exit 1

# Check if the MAVIS directory exists
if [ ! -d "$MAVIS_DIR" ]; then
    echo "Cloning MAVIS repository from GitHub..."

    # Check if Git is installed
    if ! command -v git &>/dev/null; then
        echo "❌ Error: Git is not installed. Please install Git first."
        exit 1
    fi

    # Check if GitHub is reachable
    echo "Testing connection to GitHub..."
    if ! ping -c 1 -W 5 github.com &>/dev/null; then
        echo "❌ Error: Cannot reach GitHub! Check your internet connection or firewall settings."
        exit 1
    fi

    # GitHub is accessible, clone repository
    echo "Running git clone..."
    git clone https://github.com/Peharge/MAVIS.git "$MAVIS_DIR"

    if [ $? -ne 0 ]; then
        echo "❌ Error: Cloning MAVIS repository failed! Make sure GitHub is accessible and the URL is correct."
        exit 1
    else
        echo "✅ MAVIS repository cloned successfully!"
    fi
else
    echo "MAVIS repository already exists. Checking for updates..."

    cd "$MAVIS_DIR" || exit 1

    # Check if the repository is in the correct state (no uncommitted changes)
    if ! git diff-index --quiet HEAD --; then
        echo "❌ Error: There are uncommitted changes! Please commit or discard them first."
        exit 1
    fi

    # Perform Git Fetch
    echo "Fetching latest changes..."
    git fetch --quiet
    if [ $? -ne 0 ]; then
        echo "❌ Error: Could not fetch updates from the remote repository! Check your internet connection or Git configuration."
        exit 1
    fi

    # Check the status of the repository to see if updates are available
    if git status | grep -q "Your branch is behind"; then
        echo "Updates available, pulling changes..."

        # Perform Git Pull
        git pull --quiet
        if [ $? -ne 0 ]; then
            echo "❌ Error: Could not update MAVIS repository! Check your internet connection or Git configuration."
            exit 1
        else
            echo "✅ MAVIS repository updated successfully!"
        fi
    else
        echo "✅ MAVIS repository is already up-to-date!"
    fi

    # Check Git status after pull for merge conflicts
    if git status | grep -q "Merge conflict"; then
        echo "❌ Error: Merge conflicts detected. Please resolve them manually."
        exit 1
    fi

    echo "✅ MAVIS update process completed successfully."
fi

# Ensure MAVIS directory exists
if [ ! -d "$MAVIS_DIR" ]; then
    echo "❌ Error: MAVIS directory does not exist!"
    echo "Make sure the repository was cloned correctly."
    exit 1
fi

# Change to MAVIS directory
cd "$MAVIS_DIR" || exit 1

# Ensure .env file exists and is correctly configured
if [ ! -f "$MAVIS_ENV_FILE" ]; then
    echo "Creating .env file..."
    {
        echo "# Environment variables for MAVIS"
        echo "PYTHONPATH=$MAVIS_DIR"
    } > "$MAVIS_ENV_FILE"

    if [ $? -ne 0 ]; then
        echo "❌ Error: Could not create .env file!"
        exit 1
    else
        echo "✅ .env file created successfully!"
    fi
else
    echo "✅ .env file already exists."
fi

# Optionally, run MAVIS
if [ -f "$MAVIS_RUN_FILE" ]; then
    echo "Running MAVIS..."
    bash "$MAVIS_RUN_FILE"
else
    echo "❌ Error: Run file not found: $MAVIS_RUN_FILE"
    exit 1
fi

# Define the username variable dynamically
# username="$USER"

# Detect the OneDrive folder dynamically
# onedriveFolder=""
# onedriveFolder=$(find "$HOME" -type d -iname "OneDrive" -maxdepth 1)

# If OneDrive folder is found, set the Desktop path
# if [ -n "$onedriveFolder" ]; then
#     # Handle paths with spaces in OneDrive folder names properly
#     desktop=$(find "$HOME/OneDrive" -type d -name "Desktop" | head -n 1)
# fi

# If Desktop path is not found under OneDrive, fall back to default Desktop path
# if [ -z "$desktop" ]; then
#     desktop="$HOME/Desktop"
# fi

# Check if Desktop path is found, if not skip step and continue
# if [ -z "$desktop" ]; then
#     echo "❌ Could not find Desktop path. Skipping step..."
#     desktop=""
#     exit 0
# fi

# Print the Desktop path for verification
# echo "Desktop Path: $desktop"

# Define the paths for the shortcut, target, and icon
# shortcut="$desktop/MAVIS Installer 4.desktop"
# targetPath="$HOME/PycharmProjects/MAVIS/mavis-launcher-4.sh"
# startIn="$HOME/PycharmProjects/MAVIS"
# iconPath="$HOME/PycharmProjects/MAVIS/icons/MAVIS-3-logo-1.ico"

# Check if the target files exist, if not skip
# if [ ! -f "$targetPath" ]; then
#     echo "❌ Target path ($targetPath) does not exist. Skipping step..."
#     targetPath=""
# fi

# if [ ! -f "$iconPath" ]; then
#     echo "❌ Icon path ($iconPath) does not exist. Skipping step..."
#     iconPath=""
# fi

# Check if the shortcut already exists
# if [ -f "$shortcut" ]; then
#     echo "✅ Shortcut 'MAVIS Installer 4' already exists. No new shortcut will be created."
# else
#     if [ -n "$desktop" ] && [ -n "$targetPath" ] && [ -n "$iconPath" ]; then
#         echo "❌ Shortcut 'MAVIS Installer 4' does not exist. Creating shortcut now..."

#         # Create the shortcut using a .desktop file (Linux equivalent of a Windows shortcut)
#         echo "[Desktop Entry]" > "$shortcut"
#         echo "Name=MAVIS Installer 4" >> "$shortcut"
#         echo "Exec=$targetPath" >> "$shortcut"
#         echo "Icon=$iconPath" >> "$shortcut"
#         echo "Terminal=true" >> "$shortcut"
#         echo "Type=Application" >> "$shortcut"

#         # Check if the shortcut was created successfully
#         if [ ! -f "$shortcut" ]; then
#             echo "❌ Failed to create the shortcut. Skipping step..."
#             exit 0
#         fi

#         echo "✅ Shortcut 'MAVIS Installer 4' has been created successfully."
#     else
#         echo "❌ Skipping shortcut creation due to missing paths."
#     fi
# fi

# Check if MAVIS run file exists
if [ ! -f "$MAVIS_RUN_FILE" ]; then
    echo "❌ Error: run-mavis-4-all.sh not found!"
    echo "Please verify that the file exists in: $MAVIS_DIR"
    exit 1
fi

# Execute run-mavis-4-all.sh
echo "✅ Starting MAVIS..."

# Check if the file is executable (check for executable file)
# Test if the file is an .sh file
if [[ ! "$MAVIS_RUN_FILE" =~ \.sh$ ]]; then
    echo "❌ Error: The file is not an executable file!"
    exit 1
fi

# Final report
echo "✅ All tasks were completed successfully!"
echo

# Try to start the file and check if it is successful
bash "$MAVIS_RUN_FILE"
if [ $? -ne 0 ]; then
    echo "❌ Error: MAVIS could not be started successfully!"
    exit 1
else
    echo "✅ MAVIS was successfully launched!"
fi

exit 0
