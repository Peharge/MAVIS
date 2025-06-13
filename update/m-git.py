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
import subprocess
import sys
from PyQt6.QtGui import QColor, QIcon, QPalette, QSyntaxHighlighter, QTextCharFormat
from PyQt6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTreeWidgetItem,
                             QTreeWidget, QVBoxLayout, QWidget, QHeaderView,
                             QLineEdit, QPushButton, QHBoxLayout, QTextEdit)

def get_git_commits(repo_path):
    os.chdir(repo_path)
    try:
        # Retrieve local commits
        local_commits = subprocess.check_output(["git", "log", "--pretty=format:%H %h %s %an %ar"], text=True).split("\n")

        # Determine the main branch
        branches = subprocess.check_output(["git", "ls-remote", "--heads", "origin"], text=True).split("\n")
        main_branch = None
        for branch in branches:
            if "refs/heads/main" in branch:
                main_branch = "origin/main"
                break
            elif "refs/heads/master" in branch:
                main_branch = "origin/master"
                break

        if not main_branch:
            return []  # No main branch found

        # Retrieve remote commits
        remote_commits = subprocess.check_output(["git", "log", main_branch, "--pretty=format:%H"], text=True).split("\n")
        remote_hashes = set(remote_commits)

        commits = []
        for commit in local_commits:
            if commit:
                full_hash, short_hash, message, author, date = commit.split(" ", 4)
                color = "red" if full_hash not in remote_hashes else "green"
                commits.append((full_hash, short_hash, message, author, date, color))

        return commits
    except subprocess.CalledProcessError:
        return []

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QTextDocument
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
import subprocess

class DiffHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self.format_addition = QTextCharFormat()
        self.format_addition.setBackground(QColor(0, 255, 0, 100))  # Green with 0.4 opacity

        self.format_deletion = QTextCharFormat()
        self.format_deletion.setBackground(QColor(255, 0, 0, 100))  # Red with 0.4 opacity

    def highlightBlock(self, text):
        if text.startswith('+'):
            self.setFormat(0, len(text), self.format_addition)
        elif text.startswith('-'):
            self.setFormat(0, len(text), self.format_deletion)

def get_commit_diff(repo_path, commit_hash):
    try:
        result = subprocess.run(["git", "show", commit_hash], cwd=repo_path, text=True, encoding='utf-8', capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Failed to retrieve diff. Error: {e.stderr}"

class CommitExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS Commit Explorer Deluxe")
        self.setGeometry(100, 100, 1200, 900)
        self.set_dark_mode()

        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/PycharmProjects/MAVIS"
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        main_layout = QVBoxLayout()

        # Search bar
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search commits...")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_commits)
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)
        main_layout.addLayout(search_layout)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Commit Hash", "Message", "Author", "Date", "Status"])
        self.tree.header().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tree.itemClicked.connect(self.display_commit_diff)
        main_layout.addWidget(self.tree)

        self.status_label = QLabel("Loading...")
        main_layout.addWidget(self.status_label)

        self.diff_text = QTextEdit()
        self.diff_text.setReadOnly(True)
        self.highlighter = DiffHighlighter(self.diff_text.document())
        main_layout.addWidget(self.diff_text)

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
                background: transparent.
            }

            QLabel {
                background: transparent;
                font-size: 16px.
            }

            QTextEdit {
                background-color: transparent;
                border: 1px solid #778899;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px.
            }
        """)

        self.setLayout(main_layout)
        self.load_commits()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(46, 46, 46))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

    def load_commits(self):
        self.tree.clear()
        commits = get_git_commits(self.repo_path)
        for full_hash, short_hash, message, author, date, color in commits:
            item = QTreeWidgetItem([short_hash, message, author, date, "Not Pulled" if color == "red" else "Pulled"])
            item.setData(0, 1, full_hash)
            item.setForeground(4, QColor(color))
            self.tree.addTopLevelItem(item)

        self.status_label.setText("Commits loaded successfully.")

    def search_commits(self):
        search_text = self.search_bar.text().lower()
        for i in range(self.tree.topLevelItemCount()):
            item = self.tree.topLevelItem(i)
            item.setHidden(search_text not in item.text(1).lower() and
                           search_text not in item.text(2).lower() and
                           search_text not in item.text(3).lower())

    def display_commit_diff(self, item):
        commit_hash = item.data(0, 1)
        diff = get_commit_diff(self.repo_path, commit_hash)
        self.diff_text.setPlainText(diff)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommitExplorer()
    window.show()
    sys.exit(app.exec())
