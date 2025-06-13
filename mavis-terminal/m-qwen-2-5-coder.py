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
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QComboBox, QScrollArea, QFrame
from PyQt6.QtGui import QTextCursor, QFont, QIcon, QKeyEvent
from PyQt6.QtCore import QThread, pyqtSignal, Qt
import ollama
import ctypes
from PyQt6.QtGui import QFont, QColor
from PyQt6 import QtGui
import os
import platform
import subprocess
import time
import sys

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


def fetch_models():
    return {
        "Qwen 2.5 coder 0.5b": "qwen2.5-coder:0.5b",
        "Qwen 2.5 coder 1.5b": "qwen2.5-coder:1.5b",
        "Qwen 2.5 coder 3b": "qwen2.5-coder:3b",
        "Qwen 2.5 coder 7b": "qwen2.5-coder:7b",
        "Qwen 2.5 coder 14b": "qwen2.5-coder:14b",
        "Qwen 2.5 coder 32b": "qwen2.5-coder:32b"
    }


def check_ollama_update():
    """
    Prüft, ob eine neue Version von Ollama verfügbar ist, und bietet ein Update an.
    """
    try:
        result = subprocess.run(["ollama", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            local_version = result.stdout.strip()
            remote_version = subprocess.run(["curl", "-s", "https://api.ollama.ai/version"],
                                            stdout=subprocess.PIPE, text=True).stdout.strip()

            if local_version != remote_version:
                print(f"{yellow}New Ollama version available: {remote_version} (Current: {local_version}){reset}")
                while True:
                    user_input = input("Do you want to update Ollama? [y/n]:").strip().lower()
                    if user_input in ["y", "yes"]:
                        subprocess.run(["ollama", "update"], check=True)
                        print(f"{green}Ollama updated successfully! Please restart the script.{reset}")
                        exit()
                    elif user_input in ["n", "no"]:
                        print("Skipping update.")
                        break
                    else:
                        print(f"{red}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

    except Exception as e:
        print(f"{red}Error checking for updates: {e}{reset}")


def find_ollama_path():
    """
    Findet den Installationspfad von Ollama basierend auf dem Betriebssystem.
    """
    try:
        if platform.system() == "Windows":
            base_path = os.environ.get("LOCALAPPDATA", "C:\\Users\\Default\\AppData\\Local")
            return os.path.join(base_path, "Programs", "Ollama", "ollama app.exe")
        elif platform.system() == "Darwin":  # macOS
            return "/Applications/Ollama.app/Contents/MacOS/Ollama"
        else:
            raise EnvironmentError("Unsupported Operating System. Ollama is not supported on this platform.")
    except Exception as e:
        raise FileNotFoundError(f"Error finding Ollama path: {e}")


def start_ollama():
    """
    Startet Ollama, falls es noch nicht läuft.
    """
    try:
        # Überprüfen, ob Ollama bereits läuft
        result = subprocess.run(
            ["tasklist"] if platform.system() == "Windows" else ["ps", "aux"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if "ollama" not in result.stdout.lower():
            print(f"{blue}Ollama is not running. Starting Ollama...{reset}")

            # Pfad zu Ollama finden
            ollama_path = find_ollama_path()

            if not os.path.exists(ollama_path):
                raise FileNotFoundError(f"Ollama executable not found at: {ollama_path}")

            # Ollama starten
            subprocess.Popen([ollama_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                             close_fds=True if platform.system() != "Windows" else False)
            time.sleep(5)  # Warten, bis Ollama gestartet ist
            print(f"{green}Ollama started successfully.{reset}\n")
        else:
            print(f"{green}Ollama is already running.{reset}\n")
    except Exception as e:
        print(f"{red}Error starting Ollama: {e}{reset}")


class OllamaWorker(QThread):
    response_signal = pyqtSignal(str)

    def __init__(self, model, conversation):
        super().__init__()
        self.model = model
        self.conversation = conversation

    def run(self):
        try:
            response_stream = ollama.chat(model=self.model, messages=self.conversation, stream=True)
            response_content = ""
            for chunk in response_stream:
                content = chunk['message']['content']
                response_content += content
                self.response_signal.emit(content)
                time.sleep(0.05)
            self.conversation.append({'role': 'assistant', 'content': response_content})
        except Exception as e:
            self.response_signal.emit(f"An error has occurred: {e}")


class CustomTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            if event.modifiers() == Qt.KeyboardModifier.NoModifier:
                self.on_enter()
                event.accept()
                return
        super().keyPressEvent(event)

    def on_enter(self):
        # Dies kann in der Unterklasse überschrieben werden
        pass


class Terminal(QWidget):
    def __init__(self):
        super().__init__()
        start_ollama()
        check_ollama_update()
        self.initUI()
        self.conversation = []
        self.models = fetch_models()
        self.populate_model_selector()

    def initUI(self):
        self.setWindowTitle('X++ ❤️')
        self.setGeometry(100, 100, 800, 800)

        self.setWindowIcon(QtGui.QIcon(
            ''))  # important

        myappid = u'mycompany.myproduct.subproduct.version'  # Arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        background_color = QColor(30, 30, 30)
        self.setStyleSheet("background-color: rgb({},{},{})".format(
            background_color.red(), background_color.green(),
            background_color.blue()))

        self.setWindowOpacity(1)

        glass_frame = QFrame(self)
        glass_frame.setGeometry(0, 0, 1920, 1000)
        glass_frame.setStyleSheet("""
            background-color: #1e1e1e; 
            color: #ffffff;
        """)

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        icon_path_3 = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo-new.png"
        self.setWindowIcon(QIcon(icon_path))

        self.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")

        layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
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
        """)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: #1e1e1e; color: #ffffff; border: none;")
        self.output.setFont(QFont("Courier New", 12))
        self.output.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        self.model_selector = QComboBox()
        self.model_selector.setFont(QFont("Courier", 12))
        self.model_selector.setStyleSheet("""
            QComboBox {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 2px solid #333;
                border-radius: 5px;
                padding: 5px;
                padding-right: 35px;
            }

            QComboBox:focus {
                background-color: #2e2e2e;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 35px;
                border-left: 1px solid #555555;
                background-color: #2b2b2b;
            }

            QComboBox::down-arrow {
                image: url({icon_path_3});
                width: 20px;
                height: 20px;
            }

            QComboBox QAbstractItemView {
                background-color: #1e1e1e;
                color: #ffffff;
                border-radius: 8px;
                selection-background-color: #2e2e2e;
                selection-color: #ffffff;
                border: 2px solid #333;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        self.scroll_content = QWidget()
        self.scroll_content_layout = QVBoxLayout()
        self.scroll_content_layout.addWidget(self.output)
        self.scroll_content_layout.addWidget(self.model_selector)
        self.scroll_content.setLayout(self.scroll_content_layout)
        self.scroll_area.setWidget(self.scroll_content)

        layout.addWidget(self.scroll_area)

        self.input = CustomTextEdit()
        self.input.setFont(QFont("Courier", 12))
        self.input.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                padding: 5px;
                border: 2px solid #333;
                border-radius: 5px;
                color: #e0e0e0;
                selection-background-color: #0078d7;
                selection-color: #ffffff;
            }

            QTextEdit:focus {
                background-color: #2e2e2e;
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
        """)
        self.input.setPlaceholderText("Enter your message here...")
        self.input.setToolTip("Enter your message here and press Enter.")
        self.input.textChanged.connect(self.adjust_height)
        self.input.setFixedHeight(40)

        # Verbinde die benutzerdefinierte on_enter-Methode der CustomTextEdit-Klasse
        self.input.on_enter = self.on_enter

        layout.addWidget(self.input)
        self.setLayout(layout)

        self.append_banner()
        self.append_welcome_message()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            if event.modifiers() == Qt.KeyboardModifier.NoModifier:
                self.on_enter()
                event.accept()
                return
        super().keyPressEvent(event)

    def adjust_height(self):
        document = self.input.document()
        desired_height = int(
            document.size().height() + self.input.contentsMargins().top() + self.input.contentsMargins().bottom())
        self.input.setFixedHeight(min(200, max(40, desired_height)))  # Maximale Höhe auf 200px begrenzen

    def on_enter(self):
        user_input = self.input.toPlainText().strip()
        if not user_input:
            return

        if user_input.lower() == 'exit':
            self.close()
            return

        self.append_user_input(user_input)
        self.conversation.append({'role': 'user', 'content': user_input})
        self.input.clear()

        selected_model_key = self.model_selector.currentText()
        selected_model = self.models[selected_model_key]
        self.worker = OllamaWorker(model=selected_model, conversation=self.conversation)
        self.worker.response_signal.connect(self.update_output)
        self.worker.start()

    def append_user_input(self, user_input):
        self.output.append(f"<p style='color: white;'><br>User: {user_input}<br><br>X++> </p>")

    def update_output(self, content):
        self.output.moveCursor(QTextCursor.MoveOperation.End)
        self.output.insertPlainText(content)
        self.output.moveCursor(QTextCursor.MoveOperation.End)
        self.output.ensureCursorVisible()

    def update_model_info(self, model_name):
        # HTML-Tag für roten Text
        model_info = f"<p style='color: red;'><br>Ausgewähltes Modell: {model_name}</p>"
        self.output.append(model_info)

    def populate_model_selector(self):
        for model_name in self.models.keys():
            self.model_selector.addItem(model_name)
        self.model_selector.currentTextChanged.connect(self.update_model_info)
        self.update_model_info(self.model_selector.currentText())

    def append_banner(self):

        banner_text = (
            '\n'
            '  _      _                                     \n'
            '/_/\    /\ \           _             _         \n'
            '\ \ \   \ \_\         /\ \          /\ \       \n'
            ' \ \ \__/ / /      ___\ \_\      ___\ \_\      \n'
            '  \ \__ \/_/      /___/\/_/_    /___/\/_/_     \n'
            '   \/_/\__/\      \__ \/___/\   \__ \/___/\    \n'
            '    _/\/__\ \       /\/____\/     /\/____\/    \n'
            '   / _/_/\ \ \      \ \_\         \ \_\        \n'
            '  / / /   \ \ \      \/_/          \/_/        \n'
            ' / / /    /_/ /                                \n'
            ' \/_/     \_\/                                 \n'
        )
        self.output.append(banner_text)

    def append_welcome_message(self):
        welcome_text = (
            "Welcome from Peharge\n"
            "\nroot@MAVIS:~$ run all"
        )
        self.output.append(welcome_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    terminal = Terminal()
    terminal.show()
    sys.exit(app.exec())
