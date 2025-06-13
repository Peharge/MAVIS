<p align="center">
    <img src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/mavis-terminal-5-banner-3.png" alt="mavis" width="1400" style="margin: 10px;">
</p>

<div align="left">
   <img alt="mavis" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-icon-banner-3.svg">
   <img alt="mavis-launcher" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-launcher-icon-banner-3.svg">
   <img alt="mavis-terminal" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-terminal-icon-banner-3.svg">
   <img alt="tg-loerrach" src="https://img.shields.io/badge/TG Lörrach-red?style=flat">
   <img alt="peharge" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/Peharge-icon-banner-3.svg">
</div>

# _**Mavis Terminal - Command Reference and Setup Guide**_

## **Overview**  
Mavis Terminal is a powerful command-line interface designed to streamline development, system monitoring, and AI model execution. This document provides a comprehensive list of available commands, along with usage guidelines for `pip` and PowerShell.  

---

If you start MAVIS Terminal 5 out of [mavis-launcher-4.bat](https://github.com/Peharge/MAVIS/raw/main/mavis-launcher-4.bat), and if you do, it looks like this:

```bash
Aktive Codepage: 65001.

      ██╗     █╗
     ████╗   ███╗        ███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗
    ██████╗  ████╗       ████╗ ████║██╔══██╗██║   ██║██║██╔════╝
   ████████╗  ████╗      ██╔████╔██║███████║██║   ██║██║███████╗
  ████╔█████╗  ████╗     ██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║
 ████╔╝ █████╗  ████╗    ██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚═══╝   ███╔╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
          █╔╝
          ╚╝

██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗     ██╗  ██╗
██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗    ██║  ██║
██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝    ███████║
██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗    ╚════██║
███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║         ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝         ╚═╝

Initiating high-tech installation...
Prepare for the next level

MIT License
Copyright (c) 2024
Peharge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Initializing MAVIS Terminal 5
Gooo...

✅ Python is already installed.
✅ Git is already installed.
✅ Ollama is already installed.
✅ FFmpeg is already installed.
✅ Rustup is already installed.
✅ PowerShell 7 is already installed.
Checking if WSL is installed...
✅ WSL is already installed.
✅ WSL is already configured with the distribution: "U".
MAVIS repository already exists. Checking for updates...
Updates available, pulling changes...
✅ MAVIS repository updated successfully
✅ MAVIS update process completed successfully.
✅ .env file already exists.
Starting MAVIS Terminal...
✅ MAVIS C++ Compiler available and the folder "C:\Users\julia\PycharmProjects\MAVIS\mavis-cpp-compier" exists.
✅ MAVIS C Compiler available and the folder "C:\Users\julia\PycharmProjects\MAVIS\mavis-c-compiler" exists.
✅ All tasks were completed successfully
Virtual environment C:\Users\julia\PycharmProjects\MAVIS\.env activated.
Installing missing packages: python-dotenv, PyQt6-sip, PyQt6-Charts, PyQt6-WebEngine...
All missing packages installed.
C:\Users\julia\PycharmProjects\MAVIS\mavis-terminal-5.py:111: DeprecationWarning: 'cgitb' is deprecated and slated for removal in Python 3.13
  from cgitb import strong

      ██╗     █╗
     ████╗   ███╗        ███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗
    ██████╗  ████╗       ████╗ ████║██╔══██╗██║   ██║██║██╔════╝
   ████████╗  ████╗      ██╔████╔██║███████║██║   ██║██║███████╗
  ████╔█████╗  ████╗     ██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║
 ████╔╝ █████╗  ████╗    ██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚═══╝   ███╔╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
          █╔╝
          ╚╝

 ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ███████╗
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██╔════╝
    ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ███████╗
    ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ╚════██║
    ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗    ███████║
    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚══════╝

A warm welcome, julia, to MAVIS (MAth Visual Intelligent System) Terminal 5
Developed by Peharge and JK (Peharge Projects 2025)
Thank you so much for using MAVIS. We truly appreciate your support ❤️

MAVIS Version: 4
MAVIS Launcher Version: 4
MAVIS Terminal Version: 5
MAVIS License: MIT

████████
████████

┌──(julia㉿MAVIS)-[C:\Users\julia\PycharmProjects\MAVIS]-[.\MAVIS\.env]
└─#
```

## Problems with Installing the MAVIS Terminal

The MAVIS Terminal should generally install automatically. However, issues may arise during installation, which might make it necessary to manually install specific dependencies.

Typically, all required dependencies are included in the automatic installation. However, if a dependency is not installed correctly, you only need to install that specific dependency afterward.

### 1. **Git**
   Git is required to clone the code and track changes. 
   Download Git from the official website:
   [Download Git](https://git-scm.com/downloads)

### 2. **Python**
   It is recommended to use **Python 3.12** (Python 3.11 is also supported, but not Python 3.13).
   Download Python from the official website:
   [Download Python](https://www.python.org/downloads/) or directly from the Microsoft Store.

### 3. **Ollama**
   Ollama is a required tool for MAVIS. Install Ollama from the official website:
   [Download Ollama](https://ollama.com/download)

### 4. **FFmpeg**
   FFmpeg is another important dependency for the MAVIS Terminal. Make sure it is installed on your system. More information can be found on the official website: [FFmpeg](https://ffmpeg.org/)

### 5. **Rustup**
   Rustup is required to install Rust and related tools. You can download it from the official Rust website:
   [Download Rustup](https://rustup.rs/)

### 6. **PowerShell 7**
   PowerShell 7 is a modern version of PowerShell and is recommended for using the MAVIS Terminal. Download PowerShell 7 from the official Microsoft site:
   [Download PowerShell 7](https://github.com/PowerShell/PowerShell/releases)

### 7. **Windows Subsystem for Linux (WSL)**  
   To use the MAVIS Terminal optimally, you need the Windows Subsystem for Linux (WSL). Supported distributions are:

   - **Ubuntu**  
     Install Ubuntu from the Microsoft Store:  
     [Ubuntu in Microsoft Store](https://aka.ms/wslubuntu)  
     Or use the WSL installation command:
     ```bash
     wsl --install -d Ubuntu
     ```

   - **Debian**  
     Install Debian from the Microsoft Store:  
     [Debian in Microsoft Store](https://aka.ms/wsldebian)  
     Or use the WSL installation command:
     ```bash
     wsl --install -d Debian
     ```

   - **Kali Linux**  
     Install Kali Linux from the Microsoft Store:  
     [Kali Linux in Microsoft Store](https://aka.ms/wslkali)  
     Or use the WSL installation command:
     ```bash
     wsl --install -d Kali-Linux
     ```

   - **Arch Linux**  
     Arch Linux is not directly available in the Microsoft Store, but you can install it using [WSL installation scripts](https://github.com/yuk7/wsldl):  
     [Arch Linux WSL Script](https://github.com/yuk7/wsldl)  
     Alternatively, you can manually install Arch through the AUR (Arch User Repository).

   - **openSUSE**  
     Install openSUSE from the Microsoft Store:  
     [openSUSE in Microsoft Store](https://aka.ms/wslsuse)  
     Or use the WSL installation command:
     ```bash
     wsl --install -d openSUSE
     ```

   - **Linux Mint**  
     Linux Mint is also not directly available in the Microsoft Store, but you can install it via [WSL2](https://www.linuxmint.com/) and follow the installation instructions.

   - **Fedora**  
     Fedora is directly available in the Microsoft Store:  
     [Fedora in Microsoft Store](https://aka.ms/wslfedora)  
     Or use the WSL installation command:
     ```bash
     wsl --install -d Fedora
     ```

   - **Red Hat**  
     Red Hat Enterprise Linux (RHEL) is available from the Red Hat website. More information on installation can be found here:  
     [Install RHEL on WSL](https://developers.redhat.com/blog/2020/06/25/introducing-red-hat-enterprise-linux-on-wsl)

   More information on installing WSL can be found here:
   [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

### 8. **MAVIS Repository**
   Clone the MAVIS repository from GitHub:
   [MAVIS GitHub Repository](https://github.com/Peharge/MAVIS)

### 9. **C++ Extensions for Desktop Development**
   For the development and execution of MAVIS, you will also need the C++ extensions for Visual Studio. You can download them here:
   [Download C++ Extensions](https://visualstudio.microsoft.com/de/downloads/)

## **Command Reference**  

Below is a structured list of available commands and their corresponding functions:  

### Environment Setup and Updates

- **`env install`**: Installs the required environment for Mavis.
- **`install env`**: Installs the Mavis environment.
- **`mavis env install`**: Installs the Mavis environment for the Mavis project.
- **`install mavis env`**: Installs the specific Mavis environment for the project.
- **`env update`**: Updates the Mavis environment to the latest version.
- **`update env`**: Updates the environment to the latest version.
- **`mavis env update`**: Updates the Mavis environment to the latest version.
- **`update mavis env`**: Updates the specific Mavis environment to the latest version.

### Repository and Project Updates

- **`update`**: Performs a repository update.
- **`mavis update`**: Performs an update for the Mavis project.
- **`update mavis`**: Performs an update for the Mavis installation.

### Security and System Information

- **`security`**: Checks the system’s security.
- **`mavis security`**: Performs a security check for the Mavis project.
- **`securitycheck`**: Initiates a security check for the system.
- **`info`**: Displays general system information.
- **`mavis info`**: Displays specific information about the Mavis project.
- **`info mavis`**: Shows information about the Mavis installation.
- **`neofetch`**: Displays system information in a visually appealing format.
- **`fastfetch`**: Displays system information using Neofetch.

### Jupyter and Mavis Model Running Commands

- **`jupyter`**: Launches the Jupyter Notebook environment.
- **`run jupyter`**: Starts the Jupyter Notebook environment.

### Running Mavis Versions
The following commands run different versions of Mavis (1.2, 1.5, 3, etc.), along with specific versions for math and coding tasks:

- **`run mavis-1-5-main`**: Runs the main version of Mavis 1.5.
- **`run mavis-1-5-math`**: Runs the mathematical version of Mavis 1.5.
- **`run mavis-1-5-math-pro`**: Runs the professional math version of Mavis 1.5.
- **`run mavis-1-5-math-ultra`**: Runs the ultra math version of Mavis 1.5.
- **`run mavis-1-5-math-mini`**: Runs the mini math version of Mavis 1.5.
- **`run mavis-1-5-code`**: Runs the coding version of Mavis 1.5.
- **`run mavis-1-5-code-pro`**: Runs the professional coding version of Mavis 1.5.
- **`run mavis-3-main`**: Runs the main version of Mavis 3.
- **`run mavis-3-math`**: Runs the math version of Mavis 3.

Additional specific versions for each Mavis iteration are also available, e.g., **`mavis-1-5-main-mini`** or **`mavis-3-code-mini`**, tailored to different needs (mini, ultra-mini, professional, etc.).

### Ollama Mavis Versions
- **`run ollama mavis-3-main`**: Runs the Ollama Mavis 3 Main model.
- **`run ollama mavis-3-math`**: Runs the Ollama Mavis 3 Math model.
- **`install ollama mavis-1-5-main`**: Installs Ollama for Mavis 1.5 main version.
- Additional models available for installation or running, e.g., **`install ollama mavis-3-code-mini`**.

### Model-Specific Commands

The following are commands to run or install various models like DeepSeek, Llama3, Mistral, Phi4, Qwen2.5, and others.

- **DeepSeek Models**:
  - **`run deepseek-r1:1.5b`**: Runs the DeepSeek model version 1.5b.
  - **`install deepseek-r1:70b`**: Installs the DeepSeek model version 70b.

- **Llama3 Models**:
  - **`run llama3.1:8b`**: Runs the Llama3 model version 3.1 8b.
  - **`install llama3.2:1b`**: Installs the Llama3 model version 3.2 1b.

- **Mistral Models**:
  - **`run mistral`**: Runs the Mistral model.
  - **`install mistral-large`**: Installs the Mistral Large model.

- **Phi4 Models**:
  - **`run phi4`**: Runs the Phi4 model.
  - **`install phi4-mini`**: Installs the Phi4-Mini tool.

- **Qwen2.5 Models**:
  - **`run qwen2.5:0.5b`**: Runs the Qwen2.5 model version 0.5b.
  - **`install qwen2.5-coder:1.5b`**: Installs the Qwen2.5 Coder model version 1.5b.

- **Gemma3 Models**:
  - **`run gemma3:1b`**: Runs the Gemma3 model version 1b.
  - **`install gemma3:27b`**: Installs the Gemma3 model version 27b.

and more...

### Additional Tools and Applications

- **`grafana`**: Runs the Grafana application.
- **`run deepseek-r1:1.5b`**: Runs the DeepSeek model version 1.5b.
- **`install deepseek-r1:70b`**: Installs the DeepSeek model version 70b.

### Script Execution
- `m run all` - Runs all available scripts in a graphical window.
- `m run gemma3` - Runs the Gemma3 script in a graphical window.
- `m run deepseek-r1` - Runs all Deepseek-R1 versions in a graphical window.
- `m run qwen2.5` - Runs all Qwen 2.5 versions in a graphical window.
- `m run qwen2.5-coder` - Runs the Qwen 2.5 Coder versions in a graphical window.
- `m python frameworks` - Runs the Python frameworks versions in a graphical window.

### System Monitoring
- `m htop` - Displays a system resource overview (htop) in a graphical window.

### Package Management
- `m pip list` - Lists all installed Python packages (pip list) in a graphical window.
- `m pip ls` - Lists all installed Python packages (pip ls) in a graphical window.

### Git Management
- `m git` - Lists all installed and uninstalled commits in a graphical window.

### Filesystem Overview
- `m ls` - Displays a filesystem overview from the MAVIS folder (ls) in a graphical window.
- `m models ls` - Lists all LLM models for MAVIS 4 in a graphical window.

### Web Search & Online Platforms
- `m search` - Opens the DuckDuckGo search engine.
- `m ollama` - Opens ollama.com.
- `m huggingface` - Opens huggingface.co.
- `m github` - Opens github.com.
- `m github mavis` - Opens the MAVIS GitHub repository.
- `m google` - Opens google.com.

### How to Use the Linux Command Executor

#### Instructions
1. To execute a Linux command on a specific distribution, use the following format:
   - `lx <command>`, `ubuntu <command>`, `debian <command>`, `kali <command>`, `arch <command>`, `mint <command>`, `redhat <command>`
   - Example: `lx neofetch` will execute 'neofetch' on the default Linux distro (WSL).
   - Example: `ubuntu sudo apt update` will run 'sudo apt update' on an Ubuntu system.
   - Example: `arch pacman -Syu` will update Arch Linux using 'pacman -Syu'.

#### Example Commands
- **Linux (WSL):** `lx <command>` (e.g., `lx neofetch`)
- **Ubuntu:** `ubuntu <command>` (e.g., `ubuntu sudo apt update`)
- **Debian:** `debian <command>` (e.g., `debian sudo apt upgrade`)
- **Kali Linux:** `kali <command>` (e.g., `kali apt-get install nmap`)
- **Arch Linux:** `arch <command>` (e.g., `arch pacman -Syu`)
- **Mint:** `mint <command>` (e.g., `mint sudo apt install vlc`)
- **Red Hat:** `redhat <command>` (e.g., `redhat sudo yum install git`)

#### Notes
- You can replace `<command>` with any valid Linux command, e.g., `lx neofetch`, `ubuntu ls -l`, `kali sudo apt install nmap`.
- The distribution alias (e.g., `lx`, `ubuntu`, `debian`) determines which environment the command will be executed in.

---

## Using pip (Python Package Installer)

1. To install a Python package, execute the following command in your terminal or command prompt:
   ```sh
   pip install <package_name>
   ```
   Example:
   ```sh
   pip install numpy
   ```
2. To upgrade pip itself, run:
   ```sh
   python -m pip install --upgrade pip
   ```
3. Note: In some environments, you may need to use `pip3` instead of `pip`.

## Using PowerShell

1. To run Python scripts in PowerShell, navigate to the script directory and execute the command:
   ```sh
   python <script_name>.py
   ```
   Example:
   ```sh
   python my_script.py
   ```
2. To install Python packages in PowerShell using pip, run:
   ```sh
   pip install <package_name>
   ```
   Example:
   ```sh
   pip install requests
   ```
3. If you're using PowerShell as an administrator and face any permission issues, try running it as Administrator.

## How to Use Ollama

1. To use Ollama in PowerShell, you first need to have Ollama installed. If it's not installed, run:
   ```sh
   pip install ollama
   ```
2. After installation, you can use the following commands to interact with Ollama:
   
   **Available Ollama Commands:**
   - `ollama serve` - Start Ollama server
   - `ollama create` - Create a model from a Modelfile
   - `ollama show` - Show information for a model
   - `ollama run` - Run a model
   - `ollama stop` - Stop a running model
   - `ollama pull` - Pull a model from a registry
   - `ollama push` - Push a model to a registry
   - `ollama list` - List available models
   - `ollama ps` - List running models
   - `ollama cp` - Copy a model
   - `ollama rm` - Remove a model
   - `ollama help` - Get help for any command

3. To see version information, use the command:
   ```sh
   ollama --version
   ```
   Example:
   ```sh
   ollama --version
   ```
4. For additional help on any command, type:
   ```sh
   ollama [command] --help
   ```
   Example:
   ```sh
   ollama run --help
   ```

## PowerShell Basics

### File and Directory Management
- List contents of the current directory:
  ```sh
  dir
  ```
- Change directories:
  ```sh
  cd <path>
  ```
  Example:
  ```sh
  cd C:\Users\UserName\Documents
  ```
- Go back to the previous directory:
  ```sh
  cd ..
  ```
- Go to the root of the current drive:
  ```sh
  cd \
  ```
- Create a new directory:
  ```sh
  mkdir <folder_name>
  ```
  Example:
  ```sh
  mkdir NewFolder
  ```
- Remove a file:
  ```sh
  rm <file_name>
  ```
  Example:
  ```sh
  rm file.txt
  ```
- Remove an empty folder:
  ```sh
  rmdir <folder_name>
  ```
  Example:
  ```sh
  rmdir EmptyFolder
  ```
- View the contents of a file:
  ```sh
  cat <file_name>
  ```
  Example:
  ```sh
  cat file.txt
  ```

### Process Management
- List running processes:
  ```sh
  Get-Process
  ```
- Stop a process:
  ```sh
  Stop-Process -Name <process_name>
  ```
  Example:
  ```sh
  Stop-Process -Name notepad
  ```

### System Information
- View system information:
  ```sh
  Get-ComputerInfo
  ```
- Get help on a specific command:
  ```sh
  Get-Help <command>
  ```
  Example:
  ```sh
  Get-Help dir
  ```
- View command history:
  ```sh
  Get-History
  ```
- Clear the screen:
  ```sh
  Clear
  ```
- Get the current working directory:
  ```sh
  Get-Location
  ```

### Running PowerShell Scripts
- Set execution policy to allow scripts to run:
  ```sh
  Set-ExecutionPolicy RemoteSigned
  ```
- Run a script:
  ```sh
  .\script.ps1
  ```

### Environment Variables
- See all environment variables:
  ```sh
  Get-ChildItem Env:
  ```
- Add a new environment variable:
  ```sh
  $env:VariableName = "Value"
  ```
  Example:
  ```sh
  $env:MyVar = "Hello"
  ```
- Display the contents of an environment variable:
  ```sh
  echo $env:VariableName
  ```

### PowerShell Scripting Basics
- Create a loop:
  ```sh
  foreach ($item in 1..5) { Write-Output $item }
  ```
- Use an `if` statement:
  ```sh
  if ($a -gt $b) { Write-Output "a is greater than b" }
  ```
- Use pipelines to filter data:
  ```sh
  Get-Process | Where-Object {$_.CPU -gt 100}
  ```

and more...