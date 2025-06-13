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

"""
Comprehensive Fedora System Information in WSL – Enhanced Design

This enhanced PyQt6 application displays detailed system information obtained from Fedora running in WSL.
It retrieves various data sets such as distribution details, kernel information, disk usage, and memory usage
via individual WSL commands. The UI has been visually improved with a modern color scheme, optimized spacing,
enhanced scaling, and a status bar that provides user feedback throughout the process.

Author: Peharge
Date: 2025-04-19
"""

import sys
import subprocess
import logging
import os
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QLabel,
    QPushButton,
    QScrollArea,
    QTextEdit,
    QStatusBar,
    QSizePolicy
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QIcon

# Configure logging for detailed debugging and error tracking.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Enhanced QSS Style Sheet for a modern look.
STYLE_SHEET = """
QWidget {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
    color: #FFFFFF;
    font-family: 'Roboto', sans-serif;
    font-size: 14px;
}
QLineEdit {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
    border: 1px solid #778899;
    border-radius: 5px;
    padding: 5px;
    color: #FFFFFF;
}
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #bbdefb);
    color: #000000;
    padding: 2px 8px;
    border-radius: 8px;
}
QPushButton:hover {
    background-color: #bbdefb;
}
QTreeWidget {
    background-color: transparent;
    border: 1px solid #778899;
    border-radius: 8px;
}
QTreeWidget::item {
    padding: 8px;
    border-bottom: 1px solid #778899;
}
QTreeWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
    color: #FFFFFF;
}
QHeaderView::section {
    background-color: transparent;
    padding: 8px;
    border: none;
}
QLabel {
    background: transparent;
    font-size: 16px;
}
QTextEdit {
    background-color: transparent;
    border: 1px solid #778899;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
}
QTableWidget {
    background-color: #222;
    gridline-color: #566573;
}
QHeaderView::section {
    background-color: #2c3e50;
    padding: 4px;
    border: 1px solid #566573;
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
QStatusBar {
    background-color: #1c2833;
    color: #FFFFFF;
    padding: 4px;
}

QFrame#metricCard {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
    border: 1px solid #566573;
    border-radius: 12px;
    padding: 15px;
    margin: 10px;
}

QFrame#metricCard:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
    border: 1px solid #778899;
}

QLabel#title {
    font-size: 18px;
    font-weight: bold;
}
"""


def detect_fedora_distro():
    """
    Detects installed WSL distributions and returns the first Fedora-based one found.
    """
    try:
        output = subprocess.check_output(["wsl", "--list", "--quiet"], text=True)
        for line in output.splitlines():
            if "Fedora-Remix" in line:
                logging.info(f"Detected Fedora distro: {line.strip()}")
                return line.strip()
        raise RuntimeError("No Fedora WSL distribution found.")
    except Exception as e:
        logging.error(f"Could not detect Fedora WSL distribution: {e}")
        return "Fedora-Remix"  # Fallback


def run_command(command: list) -> str:
    """
    Executes a WSL command and returns its output.

    :param command: A list containing the command and its arguments.
    :return: Standard output of the command as a string.
    """
    try:
        logging.info(f"Executing command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        logging.info("Command executed successfully.")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_message = f"Error executing {' '.join(command)}: {e}"
        logging.error(error_message)
        return error_message


class SystemInfoWorker(QThread):
    """
    Worker thread that sequentially executes several WSL commands to fetch system information.
    The aggregated results are emitted via a signal to update the UI.
    """
    infoFetched = pyqtSignal(dict, str)

    def run(self):
        details = {}
        raw_output_aggregate = ""
        distro = detect_fedora_distro()

        # Fetch distribution information.
        distro_output = run_command(["wsl", "-d", distro, "--", "lsb_release", "-a"])
        details["Distribution Info"], _ = parse_key_values(distro_output)
        raw_output_aggregate += "=== Distribution Info ===\n" + distro_output + "\n\n"

        # Fetch kernel information.
        kernel_output = run_command(["wsl", "-d", distro, "--", "uname", "-a"])
        details["Kernel Info"] = {"Kernel": kernel_output}
        raw_output_aggregate += "=== Kernel Info ===\n" + kernel_output + "\n\n"

        # Fetch disk usage information.
        disk_output = run_command(["wsl", "-d", distro, "--", "df", "-h"])
        details["Disk Usage"] = {"Disk": disk_output}
        raw_output_aggregate += "=== Disk Usage ===\n" + disk_output + "\n\n"

        # Fetch memory usage details.
        mem_output = run_command(["wsl", "-d", distro, "--", "free", "-h"])
        details["Memory Usage"] = {"Memory": mem_output}
        raw_output_aggregate += "=== Memory Usage ===\n" + mem_output + "\n\n"

        self.infoFetched.emit(details, raw_output_aggregate)

def parse_key_values(raw_output: str) -> (dict, str):
    """
    Parses output from commands like 'lsb_release -a' into a dictionary.

    :param raw_output: Raw string of the command's output.
    :return: A tuple containing the parsed dictionary and the original output.
    """
    info = {}
    for line in raw_output.splitlines():
        if ':' in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()
    return info, raw_output


class InfoCard(QFrame):
    """
    Custom widget that displays a title and its corresponding value in an attractive card style.
    """

    def __init__(self, title: str, value: str, parent: QWidget = None):
        super().__init__(parent)
        self.setObjectName("metricCard")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.initUI(title, value)

    def initUI(self, title: str, value: str):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        title_label = QLabel(title)
        title_label.setObjectName("title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        value_label.setWordWrap(True)
        layout.addWidget(value_label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    """
    Main application window containing all the information panels, improved scaling,
    and an updated status bar for feedback.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS Fedora System Information in WSL – Enhanced Design")
        self.resize(1200, 800)
        self.initUI()
        self.refresh_info()

    def initUI(self):
        # Central widget and main vertical layout.
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Header layout containing the title and refresh button.
        header_layout = QHBoxLayout()
        self.title_label = QLabel("Fedora System Overview")
        self.title_label.setObjectName("title")
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()

        self.refresh_button = QPushButton("Refresh Data")
        self.refresh_button.clicked.connect(self.refresh_info)
        header_layout.addWidget(self.refresh_button)
        main_layout.addLayout(header_layout)

        # Grid layout for info cards inside a scroll area for better scaling.
        self.cards_widget = QWidget()
        self.cards_layout = QGridLayout()
        self.cards_layout.setContentsMargins(5, 5, 5, 5)
        self.cards_layout.setSpacing(10)
        self.cards_widget.setLayout(self.cards_layout)

        cards_scroll = QScrollArea()
        cards_scroll.setWidgetResizable(True)
        cards_scroll.setWidget(self.cards_widget)
        main_layout.addWidget(cards_scroll, stretch=2)

        # Expandable text area for raw output details.
        self.raw_output_edit = QTextEdit()
        self.raw_output_edit.setReadOnly(True)
        self.raw_output_edit.setMinimumHeight(250)
        raw_scroll = QScrollArea()
        raw_scroll.setWidgetResizable(True)
        raw_scroll.setWidget(self.raw_output_edit)
        main_layout.addWidget(raw_scroll, stretch=1)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Status bar for showing loading and success messages.
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready", 3000)

    def refresh_info(self):
        """
        Disables the refresh button, displays a loading message, and starts the background worker to fetch system data.
        """
        self.refresh_button.setEnabled(False)
        self.raw_output_edit.setPlainText("Loading system information...")
        self.status_bar.showMessage("Loading system information...", 0)
        self.worker = SystemInfoWorker()
        self.worker.infoFetched.connect(self.update_ui)
        self.worker.start()

    def update_ui(self, details: dict, raw_output: str):
        """
        Updates the UI with the fetched data by creating a new info card for each category.

        :param details: Dictionary containing information for each category.
        :param raw_output: Aggregated raw output from all executed commands.
        """
        # Remove old cards.
        for i in reversed(range(self.cards_layout.count())):
            widget = self.cards_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Create and add new info cards.
        row = 0
        col = 0
        for category, info in details.items():
            content_lines = []
            for key, value in info.items():
                content_lines.append(f"{key}: {value}")
            content = "\n".join(content_lines)
            card = InfoCard(title=category, value=content)
            self.cards_layout.addWidget(card, row, col)
            col += 1
            if col >= 2:
                col = 0
                row += 1

        # Update raw output details.
        self.raw_output_edit.setPlainText(raw_output)
        self.refresh_button.setEnabled(True)
        self.status_bar.showMessage("System information updated", 3000)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
