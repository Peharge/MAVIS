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
import sys
from PyQt6.QtGui import QColor, QIcon, QPalette
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QScrollArea, QSizePolicy, QTreeWidget,
                             QTreeWidgetItem, QVBoxLayout, QWidget, QTextEdit)


class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS File Explorer")
        self.setGeometry(100, 100, 1200, 800)

        self.set_dark_mode()

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        main_layout = QVBoxLayout()

        # Tree widget for file explorer
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Name", "Type", "Size", "Date Modified"])
        self.tree.itemClicked.connect(self.display_file_content)
        main_layout.addWidget(self.tree)

        # Scroll area for file content
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        main_layout.addWidget(self.scroll_area)

        # File content display
        self.file_content = QTextEdit()
        self.file_content.setReadOnly(True)
        self.scroll_area.setWidget(self.file_content)

        self.status_label = QLabel("Loading...")
        main_layout.addWidget(self.status_label)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setStyleSheet("""
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
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
                color: #FFFFFF;
            }
            
            QPushButton:hover {
                background-color: #1c2833;
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
            
            QLabel {
                background: transparent;
                font-size: 16px;
            }
            
            QTextEdit {
                background-color: transparent;
                color: #FFFFFF;
                border: 1px solid #778899;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
        """)

        self.setLayout(main_layout)

        self.load_directory_structure()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(46, 46, 46))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

    def load_directory_structure(self):
        directory_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\"
        self.tree.clear()

        self.add_directory_to_tree(directory_path)

        self.status_label.setText("Directory structure loaded successfully.")

    def add_directory_to_tree(self, path, parent=None):
        try:
            items = os.listdir(path)
        except PermissionError:
            return

        for item in items:
            item_path = os.path.join(path, item)

            if "doom.run" in item_path:
                continue

            item_type = "Directory" if os.path.isdir(item_path) else "File"
            item_size = os.path.getsize(item_path) if os.path.isfile(item_path) else ""

            try:
                item_mtime = os.path.getmtime(item_path)  # Fehlerquelle
                formatted_date = self.format_date(item_mtime)
            except OSError:
                formatted_date = "N/A"

            tree_item = QTreeWidgetItem([item, item_type, str(item_size), formatted_date])

            if os.path.isdir(item_path):
                self.add_directory_to_tree(item_path, tree_item)

            if parent:
                parent.addChild(tree_item)
            else:
                self.tree.addTopLevelItem(tree_item)

    def format_date(self, timestamp):
        import datetime
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def display_file_content(self, item):
        if item.text(1) == "File":
            file_path = self.get_full_path(item)
            with open(file_path, 'r') as file:
                content = file.read()
            self.file_content.setPlainText(content)
        else:
            self.file_content.clear()

    def get_full_path(self, item):
        path = item.text(0)
        parent = item.parent()
        while parent:
            path = os.path.join(parent.text(0), path)
            parent = parent.parent()
        return os.path.join(f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\", path)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # 50% der Breite für die 'Name' Spalte
        width = self.width()
        self.tree.setColumnWidth(0, int(width * 0.40))  # Erste Spalte (Name) 40% der Fensterbreite
        self.tree.setColumnWidth(1, int(width * 0.20))  # Zweite Spalte (Type) 20% der Fensterbreite
        self.tree.setColumnWidth(2, int(width * 0.20))  # Dritte Spalte (Size) 20% der Fensterbreite
        self.tree.setColumnWidth(3, int(width * 0.20))  # Vierte Spalte (Date Modified) 20% der Fensterbreite


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec())
