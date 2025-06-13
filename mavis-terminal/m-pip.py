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
import subprocess
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon

# Path to the virtual environment and pip executable
venv_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
pip_executable = os.path.join(venv_path, "Scripts", "pip.exe")

# QSS Stylesheet
STYLE_SHEET = """
QWidget {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
    color: #FFFFFF;
    font-family: 'Roboto', sans-serif;
    font-size: 14px;
}

QFrame.metricCard {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
    border: 1px solid #566573;
    border-radius: 12px;
    padding: 10px;
}

QFrame.metricCard:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
    border: 1px solid #778899;
}

QLabel.title {
    font-size: 16px;
    font-weight: bold;
    background: none;
}

QProgressBar {
    background-color: #222;
    border: none;
    height: 20px;
    border-radius: 10px;
}

QProgressBar::chunk {
    border-radius: 10px;
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

QScrollBar:horizontal {
    background-color: transparent;
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

class PipManagerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MAVIS PIP Package Manager")
        self.resize(1000, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Header label for installed packages and framework info
        header = QtWidgets.QLabel("Installed Packages and Framework Info")
        header.setObjectName("title")
        header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(header)

        # Table to display packages with additional information (Name, Version, Summary)
        self.table = QtWidgets.QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Package", "Version", "Summary", "Actions"])
        self.layout.addWidget(self.table)

        refresh_button = QtWidgets.QPushButton("Refresh List")
        refresh_button.clicked.connect(self.load_packages)

        # Container-Layout für Zentrierung
        button_layout = QtWidgets.QHBoxLayout()

        # Stretch links (nimmt 45%)
        button_layout.addStretch(45)

        # Button (nimmt 10%)
        button_layout.addWidget(refresh_button, stretch=10)

        # Stretch rechts (nimmt 45%)
        button_layout.addStretch(45)

        # Layout hinzufügen
        self.layout.addLayout(button_layout)

        # Start initial loading of packages
        self.load_packages()

    def load_packages(self):
        """Load installed packages using pip freeze and execute 'pip show' sequentially for additional details."""
        self.table.setRowCount(0)
        self.setCursor(QtCore.Qt.CursorShape.WaitCursor)

        # Create a worker for loading packages
        self.loaderThread = QtCore.QThread()
        self.loaderWorker = PackageLoaderWorker()
        self.loaderWorker.moveToThread(self.loaderThread)
        self.loaderWorker.packageLoaded.connect(self.add_package_row)
        self.loaderWorker.finished.connect(self.loaderThread.quit)
        self.loaderWorker.finished.connect(self.loaderWorker.deleteLater)
        self.loaderThread.finished.connect(self.loaderThread.deleteLater)
        self.loaderThread.started.connect(self.loaderWorker.run)
        self.loaderThread.start()

    @QtCore.pyqtSlot(dict)
    def add_package_row(self, package_info):
        """Add a row to the table based on the package details."""
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Add package name
        name_item = QtWidgets.QTableWidgetItem(package_info.get("Name", ""))
        self.table.setItem(row_position, 0, name_item)

        # Version
        version_item = QtWidgets.QTableWidgetItem(package_info.get("Version", ""))
        self.table.setItem(row_position, 1, version_item)

        # Summary
        summary_item = QtWidgets.QTableWidgetItem(package_info.get("Summary", ""))
        self.table.setItem(row_position, 2, summary_item)

        # Actions: Update and Info buttons
        action_widget = QtWidgets.QWidget()
        action_layout = QtWidgets.QHBoxLayout()
        action_layout.setContentsMargins(0, 0, 0, 0)

        update_btn = QtWidgets.QPushButton("Update")
        update_btn.clicked.connect(lambda _, pkg=package_info.get("Name", ""): self.update_package(pkg))
        info_btn = QtWidgets.QPushButton("Info")
        info_btn.clicked.connect(lambda _, data=package_info: self.show_package_info(data))
        action_layout.addWidget(update_btn)
        action_layout.addWidget(info_btn)
        action_widget.setLayout(action_layout)
        self.table.setCellWidget(row_position, 3, action_widget)

        self.table.resizeColumnsToContents()
        self.unsetCursor()

    def update_package(self, package):
        """Run pip update for the specified package and refresh the table afterwards."""
        confirm = QtWidgets.QMessageBox.question(self, "Confirm Update",
                                                 f"Do you want to update the package '{package}'?")
        if confirm != QtWidgets.QMessageBox.StandardButton.Yes:
            return

        progress_dialog = QtWidgets.QProgressDialog(f"Updating {package}...", "Cancel", 0, 0, self)
        progress_dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        progress_dialog.setMinimumDuration(0)
        progress_dialog.show()

        def run_update():
            try:
                result = subprocess.run([pip_executable, "install", "--upgrade", package],
                                        capture_output=True, text=True, check=True)
                output = result.stdout
            except subprocess.CalledProcessError as e:
                output = e.stderr or str(e)
            QtCore.QMetaObject.invokeMethod(
                self, "update_finished", QtCore.Qt.ConnectionType.QueuedConnection,
                QtCore.Q_ARG(str, package), QtCore.Q_ARG(str, output)
            )

        updaterThread = QtCore.QThread()
        updaterWorker = Worker(run_update)
        updaterWorker.moveToThread(updaterThread)
        updaterThread.started.connect(updaterWorker.run)
        updaterWorker.finished.connect(updaterThread.quit)
        updaterWorker.finished.connect(updaterWorker.deleteLater)
        updaterThread.finished.connect(updaterThread.deleteLater)
        updaterThread.start()

    @QtCore.pyqtSlot(str, str)
    def update_finished(self, package, output):
        QtWidgets.QMessageBox.information(self, "Update Complete", f"Update of '{package}' completed:\n{output}")
        self.load_packages()

    def show_package_info(self, package_info):
        """Display detailed package information in a separate dialog."""
        info_text = "\n".join(f"{key}: {value}" for key, value in package_info.items())
        QtWidgets.QMessageBox.information(self, f"Info for {package_info.get('Name', '')}", info_text)


class PackageLoaderWorker(QtCore.QObject):
    packageLoaded = QtCore.pyqtSignal(dict)
    finished = QtCore.pyqtSignal()

    def run(self):
        """Execute pip freeze and then run 'pip show' sequentially for each package to get detailed information."""
        try:
            result = subprocess.run([pip_executable, "freeze"], capture_output=True, text=True, check=True)
            packages = result.stdout.strip().splitlines()
        except subprocess.CalledProcessError as e:
            self.packageLoaded.emit({"Name": "Error", "Version": "", "Summary": f"freeze error: {str(e)}"})
            self.finished.emit()
            return

        for pkg_entry in packages:
            if "==" in pkg_entry:
                pkg_name, pkg_version = pkg_entry.split("==")
            else:
                pkg_name, pkg_version = pkg_entry, "Unknown"

            # Execute pip show for the individual package sequentially
            try:
                show_result = subprocess.run([pip_executable, "show", pkg_name],
                                             capture_output=True, text=True, check=True)
                info_lines = show_result.stdout.strip().splitlines()
                info_dict = {}
                for line in info_lines:
                    if ":" in line:
                        key, value = line.split(":", 1)
                        info_dict[key.strip()] = value.strip()
            except subprocess.CalledProcessError as e:
                info_dict = {"Name": pkg_name, "Version": pkg_version, "Summary": f"show error: {str(e)}"}

            # Ensure that Name, Version and Summary are present
            info_dict.setdefault("Name", pkg_name)
            info_dict.setdefault("Version", pkg_version)
            info_dict.setdefault("Summary", info_dict.get("Summary", "No summary available"))
            self.packageLoaded.emit(info_dict)
        self.finished.emit()


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def run(self):
        self.fn()
        self.finished.emit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET)
    widget = PipManagerWidget()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
