import subprocess
import sys
import os
import shutil

def start_jupyter():
    try:
        # Vor der Ausführung nach Bestätigung fragen
        user_input = input("Möchtest du Jupyter starten? (y/n): ").strip().lower()
        if user_input != 'y':
            print("Jupyter wird nicht gestartet.")
            sys.exit(0)

        # Überprüfen, ob der Pfad zum Jupyter korrekt ist
        jupyter_path = "jupyter"
        if not shutil.which(jupyter_path):
            print("Fehler: Jupyter Notebook ist nicht installiert oder im Systempfad nicht gefunden.")
            sys.exit(1)

        # Benutzername dynamisch ermitteln und den Pfad zur virtuellen Umgebung erstellen
        user_home = os.path.expanduser("~")  # Das Home-Verzeichnis des Benutzers
        venv_python = os.path.join(user_home, "PycharmProjects", "MAVIS", ".env", "Scripts", "python.exe")

        # Überprüfen, ob die virtuelle Umgebung existiert
        if not os.path.isfile(venv_python):
            print(f"Fehler: Die virtuelle Umgebung {venv_python} existiert nicht.")
            sys.exit(1)

        # Zielordner für Jupyter Notebooks
        jupyter_directory = os.path.join(user_home, "PycharmProjects", "MAVIS", "main", "jupyter")
        if not os.path.isdir(jupyter_directory):
            print(f"Fehler: Das angegebene Verzeichnis '{jupyter_directory}' existiert nicht.")
            sys.exit(1)

        # Jupyter mit dem Python-Interpreter aus der virtuellen Umgebung starten
        subprocess.run([
            venv_python,
            '-m', 'notebook',
            '--NotebookApp.ip=0.0.0.0',
            '--NotebookApp.port=8888',
            f'--NotebookApp.notebook_dir={jupyter_directory}'
        ], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Starten von Jupyter Notebook: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        sys.exit(1)


if __name__ == "__main__":
    start_jupyter()
