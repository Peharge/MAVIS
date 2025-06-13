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
import platform
import cpuinfo
import psutil
import shutil
import time
import socket
from typing import Tuple
import pip
import subprocess

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


def format_bytes(byte_value: int) -> float:
    """Hilfsfunktion, um Bytes in GB umzuwandeln"""
    return round(byte_value / (1024 ** 3), 2)


def get_system_info() -> dict:
    """Funktion, um alle Systeminformationen zu sammeln"""
    system_info = {}

    # OS-Informationen
    system_info['os_name'] = platform.system()
    system_info['os_version'] = platform.version()
    system_info['os_release'] = platform.release()
    system_info['os_arch'] = platform.architecture()[0]

    # CPU-Informationen
    cpu_info = cpuinfo.get_cpu_info()
    system_info['cpu_model'] = cpu_info.get("brand_raw", "N/A")
    system_info['cpu_arch'] = cpu_info.get("arch", "N/A")
    system_info['cpu_cores'] = psutil.cpu_count(logical=False)
    system_info['cpu_threads'] = psutil.cpu_count(logical=True)
    system_info['cpu_freq'] = psutil.cpu_freq().max if psutil.cpu_freq() else "N/A"

    # RAM Informationen
    ram = psutil.virtual_memory()
    system_info['ram_total'] = format_bytes(ram.total)
    system_info['ram_used'] = format_bytes(ram.used)
    system_info['ram_free'] = format_bytes(ram.available)
    system_info['ram_usage'] = ram.percent

    # Swap Informationen
    swap = psutil.swap_memory()
    system_info['swap_total'] = format_bytes(swap.total)
    system_info['swap_used'] = format_bytes(swap.used)
    system_info['swap_free'] = format_bytes(swap.free)

    # Festplatteninformationen
    total_storage, used_storage, free_storage = shutil.disk_usage("/")
    system_info['storage_total'] = format_bytes(total_storage)
    system_info['storage_used'] = format_bytes(used_storage)
    system_info['storage_free'] = format_bytes(free_storage)

    # Netzwerkinformationen
    system_info['hostname'] = socket.gethostname()
    system_info['ip_address'] = socket.gethostbyname(system_info['hostname'])

    # Netzwerk-Interfaces
    network_interfaces = psutil.net_if_addrs()
    interfaces_info = {}
    for interface, addresses in network_interfaces.items():
        interface_details = {}
        for address in addresses:
            if address.family == socket.AF_INET:
                interface_details['IPv4'] = address.address
            elif address.family == socket.AF_INET6:
                interface_details['IPv6'] = address.address
            elif address.family == psutil.AF_LINK:
                interface_details['MAC'] = address.address
        interfaces_info[interface] = interface_details
    system_info['network_interfaces'] = interfaces_info

    # Load Average
    if system_info['os_name'] == "Windows":
        system_info['load_avg'] = f"CPU Usage: {psutil.cpu_percent(interval=1)}%"
    else:
        try:
            load_avg_values = os.getloadavg()
            system_info['load_avg'] = {
                "1m": load_avg_values[0],
                "5m": load_avg_values[1],
                "15m": load_avg_values[2]
            }
        except OSError:
            system_info['load_avg'] = "Not available"

    # Uptime des Systems
    uptime_seconds = time.time() - psutil.boot_time()
    system_info['uptime'] = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    # Benutzerinformationen
    user_info = psutil.users()
    system_info['user_info'] = [{
        'user': user.name,
        'terminal': user.terminal or 'N/A',
        'started': time.ctime(user.started)
    } for user in user_info]

    return system_info

def get_powershell_version():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "$PSVersionTable.PSVersion.ToString()"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "Fehler beim Abrufen der PowerShell-Version."
    except FileNotFoundError:
        return "PowerShell ist nicht installiert oder nicht im PATH."

def get_wsl_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[0]  # WSL-Version extrahieren
        return version
    except subprocess.CalledProcessError:
        return "Fehler beim Abrufen der WSL-Version."
    except FileNotFoundError:
        return "WSL ist nicht installiert oder nicht im PATH."

def get_kernel_version():
    try:
        result = subprocess.run(
            ["wsl", "uname", "-r"],
            capture_output=True, text=True, check=True
        )
        kernel_version = result.stdout.strip()
        return kernel_version
    except subprocess.CalledProcessError:
        return "Fehler beim Abrufen der Kernel-Version."
    except FileNotFoundError:
        return "WSL ist nicht installiert oder nicht im PATH."

def get_wslg_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[4]  # 5. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return "Fehler beim Abrufen der WSL-Version."
    except FileNotFoundError:
        return "WSL ist nicht installiert oder nicht im PATH."

def get_msrpc_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[6]  # 7. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return "Fehler beim Abrufen der WSL-Version."
    except FileNotFoundError:
        return "WSL ist nicht installiert oder nicht im PATH."

def get_direct3d_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[8]  # 9. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return "Fehler beim Abrufen der WSL-Version."
    except FileNotFoundError:
        return "WSL ist nicht installiert oder nicht im PATH."

def get_dxcore_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[10]  # 11. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return "Fehler beim Abrufen der WSL-Version."
    except FileNotFoundError:
        return "WSL ist nicht installiert oder nicht im PATH."

def print_system_info(system_info: dict):
    """Funktion, um die Systeminformationen im Terminal auszugeben"""
    print(f"""
                     =                     {blue}*{reset}                        {blue}MAVIS Terminal{reset}
                    ===                   {blue}***{reset}                       --------------
                   =====                 ++{blue}***{reset}                      {blue}MAVIS Version{reset}: 4.3
                  =======               +++{blue}****{reset}                     {blue}MAVIS Installer Version{reset}: 4
                 =========             ++++{blue}*****{reset}                    {blue}MAVIS Terminal Version{reset}: 5
                ===========           +++++{blue}******{reset}                   {blue}MAVIS License{reset}: MIT
               =============         ++++++{blue}*******{reset}                  {blue}OS{reset}: {system_info['os_name']} {system_info['os_release']}
              ===============       {blue}#*{reset}+++++{blue}********{reset}                 {blue}Version{reset}: {system_info['os_version']}
             =================     {blue}##*{reset}++++{blue}*********#{reset}                {blue}Architecture{reset}: {system_info['os_arch']}
            ===================     {blue}##*{reset}+++{blue}*******####{reset}               {blue}Hostname{reset}: {system_info['hostname']}
           =====================     {blue}##*{reset}+{blue}********#####{reset}              {blue}IP Address{reset}: {system_info['ip_address']}
          ======================+     {blue}##********#######{reset}             {blue}CPU{reset}: {system_info['cpu_model']}
         +=====================+++     {blue}##*******########{reset}            {blue}Architecture{reset}: {system_info['cpu_arch']}
        +++++================++++++     {blue}##*****##########{reset}           {blue}Max Frequency{reset}: {system_info['cpu_freq']} MHz
       {blue}*{reset}++++++++++++++++++++++++++++     {blue}##****###########{reset}          {blue}RAM Usage{reset}: {system_info['ram_usage']}%
      {blue}***{reset}+++++++++++++++++++++++++++{blue}*{reset}     {blue}##*##############{reset}         {blue}RAM Total{reset}: {system_info['ram_total']} GB
     {blue}****{reset}+++++++++++{blue}***{reset}+++++++++++{blue}****{reset}     {blue}################%{reset}        {blue}PIP Version{reset}: {pip.__version__}
    {blue}********{reset}+++++{blue}*##{reset}  {blue}***{reset}++++{blue}**********{blue}     {blue}##############%%%{reset}       {blue}PowerShell-Version{reset}: {get_powershell_version()}
   {blue}*************###{reset}    {blue}****************#{reset}     {blue}#############%%%%{reset}      {blue}WSL-Version{reset}: {get_wsl_version()}
  {blue}####********####{reset}      {blue}*************####{reset}     {blue}###########%%%%%%{reset}     {blue}Kernelversion{reset}: {get_kernel_version()}
 {blue}################{reset}        {blue}**********#######{reset}     {blue}#########%%%%%%%%{reset}    {blue}WSLg-Version{reset}: {get_wslg_version()}
                          {blue}***############{reset}                           {blue}MSRDC-Version{reset}: {get_msrpc_version()}
                           {blue}*############{reset}                            {blue}Direct3D-Version{reset}: {get_direct3d_version()}
                            {blue}###########{reset}                             {blue}DXCore-Version{reset}: {get_dxcore_version()}
                             {blue}#########{reset}                              
                              {blue}#######{reset}                               {show_color_palette_1()}
                               {blue}#####{reset}                                {show_color_palette_3()}
                                {blue}###{reset}                              
                                 {blue}#{reset}
""")

def show_color_palette_1():
    """Funktion zur Anzeige der 16 Farbpaletten ohne Abstände und Zahlen"""
    palette = ""

    # Anzeige der Farben (0-7)
    for i in range(8):
        palette += f"\033[48;5;{i}m  \033[0m"  # Farben ohne Zahlen und ohne Abstände

    return palette

def show_color_palette_3():
    palette = ""
    # Anzeige der helleren Farben (8-15)
    for i in range(8, 16):
        palette += f"\033[48;5;{i}m  \033[0m"  # Farben ohne Zahlen und ohne Abstände

    # Noch ein Zeilenumbruch am Ende
    return palette

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)
