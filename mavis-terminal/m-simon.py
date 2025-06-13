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
import subprocess
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QGraphicsDropShadowEffect,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QThread, pyqtSignal

# Stylesheet für einen modernen, dunklen Look
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
"""

# Spaltenüberschriften für die "pip show"-Ausgabe
COLUMNS = [
    "Name", "Version", "Summary", "Home-page", "Author",
    "Author-email", "License", "Location", "Requires", "Required-by"
]

class PackageInfoWorker(QThread):
    # Signal wird für jedes einzelne Paket gesendet
    packageInfoReady = pyqtSignal(dict)

    def __init__(self, packages):
        super().__init__()
        self.packages = packages

    def run(self):
        for pkg in self.packages:
            info_dict = {}
            try:
                result = subprocess.run(
                    ["pip", "show", pkg],
                    capture_output=True, text=True, check=False
                )
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if ':' in line:
                            key, value = line.split(":", 1)
                            info_dict[key.strip()] = value.strip()
                if "Name" not in info_dict:
                    info_dict["Name"] = pkg
            except Exception as e:
                info_dict["Name"] = pkg
                info_dict["Error"] = str(e)
            # Jedes Ergebnis wird sofort ausgestrahlt
            self.packageInfoReady.emit(info_dict)
            # Kurze Pause, sodass die Einträge nacheinander erscheinen (500 ms)
            self.msleep(500)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS SIMON Info")
        # zentrales Widget erstellen
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setStyleSheet(STYLE_SHEET)
        # Layout im zentralen Widget
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setup_ui()
        # Fenstergröße initial setzen, kann aber maximiert werden
        self.resize(800, 600)
        self.center_on_screen()
        self.start_package_info_worker()

        # Dynamically set the application icon
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

    def center_on_screen(self):
        # Zentriert das Fenster auf dem verfügbaren Bildschirm
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setup_ui(self):
        # Logo einfügen
        logo_label = QLabel()
        try:
            # Es wird ein dynamischer Pfad basierend auf dem aktuellen Nutzer verwendet
            logo_path = os.path.join("C:\\", "Users", os.getlogin(), "PycharmProjects", "MAVIS", "icons", "simon-logo.ico")
        except Exception:
            logo_path = ""
        pixmap = QPixmap(logo_path)
        if pixmap.isNull():
            logo_label.setText("Logo not found")
            logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            logo_label.setPixmap(pixmap)
            logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(logo_label)
        self.main_layout.addSpacing(15)

        # Container für die Buttons
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.setSpacing(40)

        install_button = QPushButton("install 3d Slicer")
        install_button.clicked.connect(self.run_install)
        install_button.setFixedHeight(35)
        self.add_shadow_effect(install_button)
        button_layout.addWidget(install_button)

        run_button = QPushButton("run 3d Slicer")
        run_button.clicked.connect(self.run_run)
        run_button.setFixedHeight(35)
        self.add_shadow_effect(run_button)
        button_layout.addWidget(run_button)

        simon_button = QPushButton("SIMON GitHub")
        simon_button.clicked.connect(self.simon_github)
        simon_button.setFixedHeight(35)
        self.add_shadow_effect(simon_button)
        button_layout.addWidget(simon_button)

        self.main_layout.addLayout(button_layout)
        self.main_layout.addSpacing(30)

        # Tabelle zur Anzeige der "pip show"-Ausgaben
        self.table = QTableWidget()
        self.table.setColumnCount(len(COLUMNS))
        self.table.setHorizontalHeaderLabels(COLUMNS)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setWordWrap(True)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.main_layout.addWidget(self.table)

    def add_shadow_effect(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(3)
        shadow.setColor(Qt.GlobalColor.black)
        widget.setGraphicsEffect(shadow)

    def run_install(self):
        script_path = os.path.join("C:\\", "Users", os.getlogin(), "PycharmProjects", "MAVIS", "run", "simon", "3d-slicer", "install-3d-slicer.py")
        try:
            subprocess.Popen(["python", script_path])
        except Exception as e:
            print(f"Error executing {script_path}: {e}")

    def run_run(self):
        script_path = os.path.join("C:\\", "Users", os.getlogin(), "PycharmProjects", "MAVIS", "run", "simon", "3d-slicer", "run-3d-slicer.py")
        try:
            subprocess.Popen(["python", script_path])
        except Exception as e:
            print(f"Error executing {script_path}: {e}")

    def simon_github(self):
        try:
            user_folder = os.path.expanduser("~")  # Plattformunabhängig
            script_path = os.path.join(user_folder, "PycharmProjects", "MAVIS", "mavis-terminal", "m-simon-git.py")

            if not os.path.exists(script_path):
                print(f"Script nicht gefunden: {script_path}")
                return

            subprocess.Popen([sys.executable, script_path])
            print(f"Starte Script: {script_path}")

        except Exception as e:
            print(f"Fehler beim Ausführen von {script_path}: {e}")


    def start_package_info_worker(self):
        packages = [
            "monai", "monailabel", "monai-deploy-app-sdk", "jupyter", "jupyterlab",
            "torch", "torchvision", "torchaudio", "nibabel", "SimpleITK", "medpy",
            "opencv-python", "tensorboard", "wandb", "pydicom"
        ]
        self.worker = PackageInfoWorker(packages)
        self.worker.packageInfoReady.connect(self.add_package_info_row)
        self.worker.start()

    def add_package_info_row(self, info):
        # Eine neue Zeile anfügen und die Informationen eintragen.
        current_row = self.table.rowCount()
        self.table.insertRow(current_row)
        for col, key in enumerate(COLUMNS):
            value = info.get(key, "")
            item = QTableWidgetItem(value)
            # Deaktiviert die Editierbarkeit des Feldes
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(current_row, col, item)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # Optional: Fenster direkt maximieren
    # window.showMaximized()
    window.show()
    sys.exit(app.exec())
