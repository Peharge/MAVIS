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
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel,
                             QScrollArea, QTextEdit, QPushButton, QHBoxLayout, QMessageBox)
from PyQt6.QtGui import QPalette, QColor, QIcon
from PyQt6.QtCore import Qt


def get_installed_frameworks():
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_list_cmd = f"{env_path}\\Scripts\\python.exe -m pip list"

    try:
        result = subprocess.run(pip_list_cmd, shell=True, capture_output=True, text=True, check=True)
        lines = result.stdout.split('\n')[2:]
        frameworks = {}

        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                frameworks[parts[0]] = parts[1]

        return frameworks
    except Exception as e:
        return {"Error": str(e)}


def get_framework_details(name):
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_show_cmd = f"{env_path}\\Scripts\\python.exe -m pip show {name}"

    try:
        result = subprocess.run(pip_show_cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error retrieving details: {str(e)}"


def install_framework(name):
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_install_cmd = f"{env_path}\\Scripts\\python.exe -m pip install {name}"

    try:
        result = subprocess.run(pip_install_cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error installing framework: {str(e)}"


def uninstall_framework(name):
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_uninstall_cmd = f"{env_path}\\Scripts\\python.exe -m pip uninstall -y {name}"

    try:
        result = subprocess.run(pip_uninstall_cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error uninstalling framework: {str(e)}"


class FrameworkViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Framework Viewer Deluxe")
        self.setGeometry(100, 100, 1000, 800)

        self.set_dark_mode()

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Apply styles to the QApplication instance
        app.setStyleSheet("""
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

            QTreeWidget {
                background-color: transparent;
                border: 1px solid #778899;
                border-radius: 8px;
            }

            QTreeWidget::item {
                background-color: transparent;
                padding: 8px;
                border-bottom: 1px solid #778899;
            }

            QTreeWidget::item:selected {
                background-color: transparent;
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
                background-color: transparent;
                width: 10px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background-color: #ffffff;
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

            QHBoxLayout {
                background-color: transparent;
            }
        """)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Framework", "Version", "Actions"])
        self.tree.itemExpanded.connect(self.load_details_on_expand)
        layout.addWidget(self.tree)

        self.status_label = QLabel("Loading...")
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.load_frameworks()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

    def load_frameworks(self):
        frameworks = get_installed_frameworks()
        self.tree.clear()

        for name, version in frameworks.items():
            item = QTreeWidgetItem([name, version])
            item.setChildIndicatorPolicy(QTreeWidgetItem.ChildIndicatorPolicy.ShowIndicator)
            self.tree.addTopLevelItem(item)
            self.add_actions(item, name, version)

        self.status_label.setText("Frameworks loaded successfully.")

    def add_actions(self, item, name, version):
        # Add uninstall button if the framework is installed
        if version:
            uninstall_button = QPushButton("Uninstall")
            uninstall_button.clicked.connect(lambda: self.uninstall_framework(name))
            uninstall_button.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ec7063, stop:1 #b03a2e);
                    color: #ffffff;
                    border: none;
                    padding: 4px 8px;
                    border-radius: 8px;
                    max-width: 90px;
                    height: 40px;
                }
                QPushButton:hover {
                    background-color: #b03a2e;
                }
            """)
            actions_layout = QHBoxLayout()
            actions_layout.addWidget(uninstall_button)
        else:
            install_button = QPushButton("Install")
            install_button.clicked.connect(lambda: self.install_framework(name))
            actions_layout = QHBoxLayout()
            actions_layout.addWidget(install_button)

        actions_widget = QWidget()
        actions_widget.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
            QHBoxLayout {
                background-color: transparent;
            }
        """)
        actions_widget.setLayout(actions_layout)
        self.tree.setItemWidget(item, 2, actions_widget)

    def install_framework(self, name): # soon!!!
        response = install_framework(name)
        QMessageBox.information(self, "Install Framework", response)
        self.load_frameworks()

    def uninstall_framework(self, name):
        response = uninstall_framework(name)
        QMessageBox.information(self, "Uninstall Framework", response)
        self.load_frameworks()

    def load_details_on_expand(self, item):
        if item.childCount() == 0:  # Load details only if not already loaded
            details_text = get_framework_details(item.text(0))
            details_widget = QTextEdit()
            details_widget.setPlainText(details_text)
            details_widget.setReadOnly(True)
            details_widget.setStyleSheet("""background-color: transparent; color: white; border: none; padding: 5px;""")
            details_widget.setFixedHeight(200)

            container = QTreeWidgetItem()
            item.addChild(container)
            self.tree.setItemWidget(container, 0, details_widget)
            item.setExpanded(True)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # 50% der Breite für die 'Framework' Spalte
        width = self.width()
        self.tree.setColumnWidth(0, int(width * 0.50))  # Erste Spalte (Framework) 50% der Fensterbreite
        self.tree.setColumnWidth(1, int(width * 0.15))  # Zweite Spalte (Version) 15% der Fensterbreite
        self.tree.setColumnWidth(2, int(width * 0.20))  # Dritte Spalte (Actions) 20% der Fensterbreite

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FrameworkViewer()
    window.show()
    sys.exit(app.exec())
