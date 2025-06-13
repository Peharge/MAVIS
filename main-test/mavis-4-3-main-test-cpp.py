import os
import getpass
import subprocess
import re
import datetime
import logging


def find_vcvarsall():
    """
    Sucht nach der Visual Studio-Initialisierungsdatei (vcvarsall.bat).
    """
    path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if os.path.isfile(path):
        return path
    raise FileNotFoundError("vcvarsall.bat not found. Please make sure Visual Studio is installed.")


def get_project_paths_cpp():
    """
    Ermittelt das MAVIS-Projektverzeichnis und Pfade zu Quelle und Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    src_dir = os.path.join(base_dir, "mavis-terminal")
    cpp_file = os.path.join(src_dir, "run_lx_command.cpp")
    exe_file = os.path.join(src_dir, "run_lx_command.exe")
    return src_dir, cpp_file, exe_file


def compile_cpp_with_vs(cpp_filename, exe_filename):
    """
    Kompiliert die angegebene C++-Datei mit cl.exe über die Visual Studio-Umgebung.
    Führt vcvarsall.bat auf (x64) und cl.exe im selben Shell-Prozess aus.
    Gibt (success: bool, error_message: str) zurück.
    """
    logging.info(f"Kompiliere {cpp_filename} mit Visual Studio C++...")
    try:
        vcvarsall = find_vcvarsall()
    except FileNotFoundError as e:
        logging.error(str(e))
        return False, str(e)

    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{cpp_filename}" /Fe:"{exe_filename}"'
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


def execute_cpp_code(md_content: str) -> str:
    """
    Sucht im Markdown-Inhalt nach C++-Codeblöcken, kompiliert und führt diese aus.
    Rückgabe: HTML-formatiertes Ergebnis.
    """
    cpp_pattern = re.compile(r"```(?:cpp|c\+\+)\n(.*?)```", re.DOTALL | re.IGNORECASE)
    matches = cpp_pattern.findall(md_content)

    if not matches:
        return "<div class='code-output-box'>Keine C++-Codeblöcke gefunden.</div>"

    outputs = []
    tmp_dir = os.getcwd()
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    for idx, code in enumerate(matches, start=1):
        cpp_filename = os.path.join(tmp_dir, f"cpp_block_{timestamp}_{idx}.cpp")
        exe_filename = os.path.join(tmp_dir, f"cpp_block_{timestamp}_{idx}.exe")
        with open(cpp_filename, "w", encoding="utf-8") as f:
            f.write(code)

        success, compile_err = compile_cpp_with_vs(cpp_filename, exe_filename)
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
    md = '''```cpp
#include <iostream>
int main() { std::cout << "Hello MAVIS!" << std::endl; return 0; }
```'''
    print(execute_cpp_code(md))
