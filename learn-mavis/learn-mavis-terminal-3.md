<p align="center">
    <img src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/mavis-terminal-3-banner.png" alt="mavis" width="400" style="margin: 10px;">
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

### Additional Tools and Applications

- **`grafana`**: Runs the Grafana application.
- **`run deepseek-r1:1.5b`**: Runs the DeepSeek model version 1.5b.
- **`install deepseek-r1:70b`**: Installs the DeepSeek model version 70b.

### Miscellaneous

- **`m run all`**: Runs all available scripts in a graphic window.
- **`m htop`**: Displays a system resource overview (htop) in a graphic window.
- **`m pip list`**: Lists all installed Python packages (pip list), in a graphic window.
- **`m git`**: Lists git repositories.

---

## **Using `pip` for Package Management**  

`pip` (Python Package Installer) is the standard package manager for Python. It allows users to install and manage dependencies required by Python applications.  

### **Basic Commands**  
- **Check if `pip` is installed:**  
  ```sh
  python -m pip --version
  ```
- **Upgrade `pip` to the latest version:**  
  ```sh
  python -m pip install --upgrade pip
  ```
- **Install a package:**  
  ```sh
  pip install <package_name>
  ```
- **Uninstall a package:**  
  ```sh
  pip uninstall <package_name>
  ```
- **List installed packages:**  
  ```sh
  pip list
  ```
- **Check for outdated packages:**  
  ```sh
  pip list --outdated
  ```
- **Update all outdated packages:**  
  ```sh
  pip install --upgrade $(pip list --outdated | awk 'NR>2 {print $1}')
  ```

---

## **Introduction to PowerShell**  

PowerShell is a powerful scripting language and command-line shell designed for system administration and automation on Windows.  

### **Common PowerShell Commands**  
| Command | Description |
|---------|-------------|
| `Get-Help` | Displays help information about PowerShell commands. |
| `Get-Process` | Lists currently running processes. |
| `Get-Service` | Shows the status of system services. |
| `Get-Command` | Displays all available PowerShell commands. |
| `Set-ExecutionPolicy RemoteSigned` | Allows running scripts on the system. |
| `Start-Process` | Launches a new process. |
| `Stop-Process -Name <process_name>` | Terminates a running process. |
| `New-Item -ItemType File -Path "C:\example.txt"` | Creates a new file. |
| `Remove-Item "C:\example.txt"` | Deletes a specified file. |

### **Running a Python Script in PowerShell**  
To execute a Python script using PowerShell, navigate to the script's directory and run:  
```powershell
python script_name.py
```

### **Running Mavis in PowerShell**  
Navigate to the Mavis directory and execute:  
```powershell
python mavis-installer-3-main-windows.py
```
