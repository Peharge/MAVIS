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

import sys
import os
import platform
import cpuinfo
import psutil
import shutil
import time
import socket
import subprocess
import logging

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# MAVIS Static Versions
MAVIS_VERSION = "4.3"
MAVSI_LAUNCHER_VERSION = "4"
MAVIS_TERMINAL_VERSION = "5"

# Inline QSS Stylesheet
INLINE_QSS = r"""
/* MAVIS Neofetch Stylesheet */

QWidget {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 #1b2631, stop:1 #0f1626);
    color: #FFFFFF;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
}

QLineEdit {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 #2c3e50, stop:1 #1c2833);
    border: 1px solid #778899;
    border-radius: 5px;
    padding: 5px;
    color: #FFFFFF;
}

QLabel#HeaderLabel {
    font-size: 18px;
    font-weight: bold;
    padding: 8px;
}

QPlainTextEdit {
    background-color: transparent;
    font-family: 'Consolas', monospace;
    color: #FFFFFF;
    border: none;
}

QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 #2c3e50, stop:1 #1c2833);
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    color: #FFFFFF;
}

QPushButton:hover {
    background-color: #1c2833;
}

QTabWidget::pane {
    border: 1px solid #778899;
    border-radius: 8px;
}

QTabBar::tab {
    background: transparent;
    padding: 8px;
    margin: 2px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #34495e, stop:1 #1c2833);
    color: #FFFFFF;
}

QStatusBar {
    background-color: #1b2631;
    padding: 4px;
    color: #FFFFFF;
}

QScrollArea {
    border: none;
    background-color: transparent;
}

QScrollBar:vertical {
    background-color: transparent;
    width: 10px;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background-color: #FFFFFF;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical,
QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical,
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: transparent;
}

QScrollBar:horizontal {
    background-color: transparent;
    height: 10px;
    border-radius: 5px;
}

QScrollBar::handle:horizontal {
    background-color: #FFFFFF;
    min-width: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal,
QScrollBar::left-arrow:horizontal,
QScrollBar::right-arrow:horizontal,
QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {
    background: transparent;
}

QTextEdit {
    background-color: transparent;
    border: 1px solid #778899;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    padding: 8px;
}

QLabel {
    font-size: 16px;
    padding: 4px;
}
"""


def format_bytes(byte_value: int) -> float:
    """Helper function to convert bytes to gigabytes."""
    return round(byte_value / (1024 ** 3), 2)


def run_subprocess(cmd: list[str]) -> str:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.warning(f"Command failed {cmd}: {e}")
    except FileNotFoundError:
        logging.warning(f"Command not found: {cmd[0]}")
    return "Not available"


_wsl_info_lines = run_subprocess(["wsl", "--version"]).splitlines()


def get_powershell_version() -> str:
    return run_subprocess(["powershell", "-Command", "$PSVersionTable.PSVersion.ToString()"])


def get_wsl_version() -> str:
    return _wsl_info_lines[0] if _wsl_info_lines else "Not available"


def get_kernel_version() -> str:
    return run_subprocess(["wsl", "uname", "-r"])


def get_wslg_version() -> str:
    return _wsl_info_lines[4] if len(_wsl_info_lines) > 4 else "Not available"


def get_msrpc_version() -> str:
    return _wsl_info_lines[6] if len(_wsl_info_lines) > 6 else "Not available"


def get_direct3d_version() -> str:
    return _wsl_info_lines[8] if len(_wsl_info_lines) > 8 else "Not available"


def get_dxcore_version() -> str:
    return _wsl_info_lines[10] if len(_wsl_info_lines) > 10 else "Not available"


def get_system_info() -> dict:
    info = {}
    try:
        # MAVIS-specific static versions
        info['MAVIS Version'] = MAVIS_VERSION
        info['MAVSI Launcher Version'] = MAVSI_LAUNCHER_VERSION
        info['MAVIS Terminal Version'] = MAVIS_TERMINAL_VERSION

        info['Operating System'] = f"{platform.system()} {platform.release()} ({platform.version()})"
        info['Architecture'] = platform.architecture()[0]

        cpu = cpuinfo.get_cpu_info()
        info['CPU Model'] = cpu.get('brand_raw', 'N/A')
        info['Cores'] = psutil.cpu_count(logical=False)
        info['Threads'] = psutil.cpu_count(logical=True)
        freq = psutil.cpu_freq()
        info['Max Frequency'] = f"{freq.max:.2f} MHz" if freq else 'N/A'

        vm = psutil.virtual_memory()
        info['Total RAM'] = f"{format_bytes(vm.total)} GB"
        info['Used RAM'] = f"{format_bytes(vm.used)} GB"
        info['Free RAM'] = f"{format_bytes(vm.available)} GB"
        info['RAM Usage'] = f"{vm.percent}%"

        sw = psutil.swap_memory()
        info['Total Swap'] = f"{format_bytes(sw.total)} GB"
        info['Used Swap'] = f"{format_bytes(sw.used)} GB"
        info['Free Swap'] = f"{format_bytes(sw.free)} GB"

        total, used, free = shutil.disk_usage(os.path.expanduser('~'))
        info['Total Storage'] = f"{format_bytes(total)} GB"
        info['Used Storage'] = f"{format_bytes(used)} GB"
        info['Free Storage'] = f"{format_bytes(free)} GB"

        host = socket.gethostname()
        info['Hostname'] = host
        try:
            info['IP Address'] = socket.gethostbyname(host)
        except Exception:
            info['IP Address'] = 'N/A'

        if platform.system() == 'Windows':
            info['CPU Usage'] = f"{psutil.cpu_percent(interval=1)}%"
        else:
            try:
                la = os.getloadavg()
                info['Load Average'] = f"1m:{la[0]:.2f}, 5m:{la[1]:.2f}, 15m:{la[2]:.2f}"
            except Exception:
                info['Load Average'] = 'Not available'

        secs = time.time() - psutil.boot_time()
        info['Uptime'] = time.strftime('%H:%M:%S', time.gmtime(secs))

        users = psutil.users()
        info['Users'] = ', '.join(
            f"{u.name} (term:{u.terminal or 'N/A'}, start:{time.ctime(u.started)})" for u in users
        )

        pip_ver = run_subprocess([sys.executable, '-m', 'pip', '--version']).split()[1]
        info.update({
            'PIP Version': pip_ver,
            'PowerShell Version': get_powershell_version(),
            'WSL Version': get_wsl_version(),
            'Kernel Version': get_kernel_version(),
            'WSLg Version': get_wslg_version(),
            'MSRDC Version': get_msrpc_version(),
            'Direct3D Version': get_direct3d_version(),
            'DXCore Version': get_dxcore_version()
        })

    except Exception as e:
        logging.error(f"Failed gathering system info: {e}")
        info['Error'] = str(e)
    return info


class InfoWorker(QtCore.QThread):
    updated = QtCore.pyqtSignal(dict)

    def run(self):
        while True:
            self.updated.emit(get_system_info())
            time.sleep(5)


class NeofetchWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS Neofetch")
        self.resize(900, 600)
        self.init_ui()

        # Initial info display
        self.update_system_info(get_system_info())

        self.worker = InfoWorker()
        self.worker.updated.connect(self.update_system_info)
        self.worker.start()

        # Dynamically set the application icon
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

    def init_ui(self):
        splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.setCentralWidget(splitter)

        user = os.getenv('USERNAME') or os.getenv('USER')
        base = os.path.dirname(__file__)
        icon_path = os.path.join(base, 'icons', 'mavis-logo.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            logging.warning(f"Icon not found: {icon_path}")

        self.image_label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        img_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo-new3.png"
        pix = QtGui.QPixmap(img_path)
        if not pix.isNull():
            self.image_label.setPixmap(pix.scaled(400, 600,
                                                  QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                                  QtCore.Qt.TransformationMode.SmoothTransformation))
        else:
            self.image_label.setText("No image found. Place 'mavis-logo-3d.ico' in icons/.")
        splitter.addWidget(self.image_label)

        self.info_text = QtWidgets.QTextEdit(readOnly=True)
        font = QtGui.QFont("Courier New", 10)
        self.info_text.setFont(font)
        splitter.addWidget(self.info_text)

    @QtCore.pyqtSlot(dict)
    def update_system_info(self, info: dict):
        html = ['<html><body style="font-family:Courier New; font-size:10pt;">',
                '<h2 style="color:#ffffff;">System Information</h2>',
                '<table width="100%" cellpadding="4">']
        for k, v in info.items():
            html.append(f'<tr><th align="left">{k}</th><td>{v}</td></tr>')
        html.append('</table></body></html>')
        self.info_text.setHtml("".join(html))


def main():
    app = QtWidgets.QApplication(sys.argv)
    # Apply inline stylesheet
    app.setStyleSheet(INLINE_QSS)

    win = NeofetchWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
