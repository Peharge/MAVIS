import os
import getpass
import subprocess
import re
import datetime
import logging


def find_vcvarsall_c():
    """
    Sucht nach der Visual Studio Entwicklungsumgebung (vcvarsall.bat).
    """
    vs_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if not os.path.isfile(vs_path):
        logging.error("Visual Studio vcvarsall.bat file not found.")
        raise FileNotFoundError("vcvarsall.bat not found. Please ensure Visual Studio is installed.")
    return vs_path


def get_project_paths_c():
    """
    Ermittelt das MAVIS-Projektverzeichnis und Pfade für C-Code und zugehörige Dateien.
    """
    base_dir = r"/"
    build_script = os.path.join(base_dir, "mavis-c-compiler", "build_mavis_c.bat")
    ready_indicator = os.path.join(base_dir, "mavis-c-compiler", "c_compiler_ready.txt")
    return base_dir, build_script, ready_indicator


def compile_c_with_vs(c_filename, exe_filename):
    """
    Kompiliert die angegebene C-Datei mit cl.exe über die Visual Studio-Umgebung.
    Führt vcvarsall.bat auf (x64) und cl.exe im selben Shell-Prozess aus.
    Gibt (success: bool, error_message: str) zurück.
    """
    logging.info(f"Kompiliere {c_filename} mit Visual Studio C...")
    try:
        vcvarsall = find_vcvarsall_c()
    except FileNotFoundError as e:
        logging.error(str(e))
        return False, str(e)

    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{c_filename}" /Fe:"{exe_filename}"'
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        err_out = result.stdout + result.stderr
        logging.error("Compilation fehlgeschlagen.")
        logging.error(err_out)
        return False, err_out

    logging.info("Compilation erfolgreich.")
    return True, None


def execute_c_code(md_content: str) -> str:
    """
    Sucht im Markdown-Inhalt nach C-Codeblöcken, kompiliert und führt diese aus.
    Rückgabe: HTML-formatiertes Ergebnis.
    """
    c_pattern = re.compile(r"```c\n(.*?)```", re.DOTALL | re.IGNORECASE)
    matches = c_pattern.findall(md_content)

    if not matches:
        return "<div class='code-output-box'>Keine C-Codeblöcke gefunden.</div>"

    outputs = []
    tmp_dir = os.getcwd()
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    for idx, code in enumerate(matches, start=1):
        c_filename = os.path.join(tmp_dir, f"c_block_{timestamp}_{idx}.c")
        exe_filename = os.path.join(tmp_dir, f"c_block_{timestamp}_{idx}.exe")
        with open(c_filename, "w", encoding="utf-8") as f:
            f.write(code)

        success, compile_err = compile_c_with_vs(c_filename, exe_filename)
        if not success:
            outputs.append(f"Kompilierung fehlgeschlagen:\n{compile_err}")
            continue

        try:
            proc = subprocess.run(
                [exe_filename],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=True
            )
            outputs.append(proc.stdout + proc.stderr)
        except subprocess.CalledProcessError as e:
            outputs.append(e.stdout + e.stderr)
        except Exception as e:
            outputs.append(f"Fehler bei der Ausführung: {str(e)}")

    combined = "\n".join(outputs)
    result = f"<div class='code-output-box'><pre>{combined}</pre></div>"
    return result


# Beispiel Usage
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    md = '''
```c
#include <stdio.h>
int main() { printf("Hello MAVIS C!\\n"); return 0; }
```
'''
print(execute_c_code(md))