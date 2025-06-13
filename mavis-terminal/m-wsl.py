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
import subprocess
import logging
from pathlib import Path
from datetime import datetime
import os

from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPlainTextEdit, QPushButton, QLabel, QTabWidget, QMessageBox, QStatusBar
)
from PyQt6.QtCore import Qt, QRunnable, QThreadPool, pyqtSignal, QObject

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Styling
STYLE_SHEET = """
QWidget {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
    color: #FFFFFF;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
}

QLineEdit {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
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
    color: #ffffff;
    border: none;
}

QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
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
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
    color: #FFFFFF;
}

QStatusBar {
    background: #1b2631;
    padding: 4px;
}

QScrollArea {
    border: none;
    background-color: transparent;
}

QScrollBar:vertical {
    background-color: transparent;  /* Hintergrund (Schiene) in transparent */
    width: 10px;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background-color: #ffffff;  /* Schieber (Block) in Weiß */
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    background: transparent;
}

QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    background: transparent;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: transparent;
}

QScrollBar:horizontal {
    background-color: transparent;  /* Auch der horizontale Balken in transparent */
    height: 10px;
    border-radius: 5px;
}

QScrollBar::handle:horizontal {
    background-color: #ffffff;
    min-width: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    background: transparent;
}

QScrollBar::left-arrow:horizontal,
QScrollBar::right-arrow:horizontal {
    background: transparent;
}

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
QStatusBar {
    background-color: #1b2631;
    color: #FFFFFF;
}
"""

# Worker for Asynchronous Execution
class WorkerSignals(QObject):
    """Signals for worker thread."""
    finished = pyqtSignal(str)
    error = pyqtSignal(str)


class CommandWorker(QRunnable):
    """Executes a shell command in a separate thread."""
    def __init__(self, command: list[str]):
        super().__init__()
        self.command = command
        self.signals = WorkerSignals()

    def run(self) -> None:
        try:
            logger.info(f"Running command: {' '.join(self.command)}")
            result = subprocess.run(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            self.signals.finished.emit(result.stdout.strip())
        except subprocess.CalledProcessError as e:
            err = e.stderr.strip() or e.stdout.strip()
            logger.error(f"Command error: {err}")
            self.signals.error.emit(err)
        except FileNotFoundError:
            err = f"Command not found: {self.command[0]}"
            logger.error(err)
            self.signals.error.emit(err)


# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS WSL Information")
        self.resize(900, 650)

        # Annahme: Das Repository befindet sich im MAVIS-Ordner des aktuellen Benutzers
        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/PycharmProjects/MAVIS"
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Thread pool for background tasks
        self.threadpool = QThreadPool.globalInstance()
        logger.info(f"Initialized thread pool with {self.threadpool.maxThreadCount()} threads")

        self._load_fonts()
        self._setup_ui()
        self._load_icon()

        # Initial data fetch
        self.refresh_all()

    def _load_fonts(self):
        # Ensure monospace font is available
        QFontDatabase.addApplicationFont("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf")

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        # Header
        header = QLabel("MAVIS - WSL & Linux Distro Info", objectName="HeaderLabel")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Tabs
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Create tabs
        self._add_tab("Status", "wsl --status", layout_index=0)
        self._add_tab("Distributions", "wsl --list --verbose", layout_index=1)
        self._add_tab("Version", "wsl --version", layout_index=2)

        # Refresh Button
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        self.btn_refresh = QPushButton("Update")
        self.btn_refresh.clicked.connect(self.refresh_all)
        btn_layout.addWidget(self.btn_refresh)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Status Bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Apply stylesheet
        self.setStyleSheet(STYLE_SHEET)

    def _add_tab(self, title: str, command: str, layout_index: int):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        editor = QPlainTextEdit()
        editor.setReadOnly(True)
        vbox.addWidget(editor)
        self.tabs.addTab(widget, title)

        # Store for later updates
        setattr(self, f"cmd_{layout_index}", command.split())
        setattr(self, f"editor_{layout_index}", editor)

    def _load_icon(self):
        # Attempt to load application icon
        user_home = Path.home()
        icon_file = user_home / "PycharmProjects/MAVIS/icons/mavis-logo.ico"
        if icon_file.is_file():
            self.setWindowIcon(QIcon(str(icon_file)))
            logger.info(f"Loaded icon: {icon_file}")

    def refresh_all(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.statusbar.showMessage(f"Update... ({timestamp})")

        for idx in range(self.tabs.count()):
            command = getattr(self, f"cmd_{idx}")
            worker = CommandWorker(command)
            worker.signals.finished.connect(lambda res, i=idx: self._update_tab(i, res))
            worker.signals.error.connect(lambda err, i=idx: self._handle_error(i, err))
            self.threadpool.start(worker)

    def _update_tab(self, index: int, text: str):
        editor = getattr(self, f"editor_{index}")
        editor.setPlainText(text)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.statusbar.showMessage(f"Updated: {timestamp}", 5000)
        logger.info(f"Tab {index} updated successfully.")

    def _handle_error(self, index: int, message: str):
        titles = ["Status", "Distributions", "Version"]
        title = titles[index] if index < len(titles) else "Unknown"
        logger.error(f"Error ({title}): {message}")
        QMessageBox.critical(
            self,
            f"Error in {title}",
            message,
            QMessageBox.StandardButton.Ok
        )
        self.statusbar.showMessage(f"Error updating: {title}", 5000)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
