# Dont runn!!!

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

from flask import Flask, render_template, request, jsonify, send_from_directory, session
import ollama
from transformers import Qwen2VLForConditionalGeneration, AutoModelForCausalLM, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
from accelerate import infer_auto_device_map
import torch
import os
from werkzeug.utils import secure_filename
import markdown
import re
import io
import sys
import base64
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import plotly.io as pio
import seaborn as sns
import pandas as pd
import numpy as np
import sympy as sp
import datetime
import dash
from dash import Dash, html, dcc, callback, Output, Input
import math
from IPython.display import display

# Optional: pip install -U kaleido für Plotly Export

#---soon für Maschinenbau---

# FEniCS, PyDy, PyCalculix, SolidPython, Pyomo, GEKKO, CasADi, Control Systems Library, ROS, PyBullet, H2O.ai, Pint, CoolProp, PyThermo

#---ultimate für Deep Learning etc.---

# import scipy as sp
# import geopandas as gpd

# Importiere die wichtigsten Komponenten von PyTorch für Deep Learning (sehr mächtig) (Install: https://pytorch.org/)

# from torch import *
# from torch.nn import *
# from torch.optim import *
# from torch.autograd import *
# from torch.utils.data import *

# Importiere die wichtigsten Komponenten von TensorFlow für Deep Learning (sehr mächtig) (Install: pip install tensorflow)

# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers, models, optimizers
# from tensorflow.data import Dataset

# Importiere die wichtigsten Komponenten von Scikit-Learn für Deep Learning (sehr mächtig) (Install: pip install scikit-learn)

# import sklearn as skl

# Importiere die wichtigsten Komponenten von Transformers für Deep Learning (sehr mächtig) (Install: pip install transformers)

# from transformers import pipeline

app = Flask(__name__)
# Setze einen geheimen Schlüssel für die Session
app.secret_key = os.urandom(24)  # Generiert einen zufälligen Schlüssel mit 24 Bytes
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_URL'] = '/uploads/'
DEFAULT_IMAGE_PATH = r""

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def execute_python_code(md_content):

    # Sucht nach Python-Code im Markdown-Inhalt, führt ihn aus und fügt die Ausgaben (Text oder Bild) zum Markdown hinzu.
    # Unterstützt Matplotlib, Seaborn, Plotly und Altair.

    code_pattern = re.compile(r"```python(.*?)```", re.DOTALL)
    matches = code_pattern.findall(md_content)

    # Falls kein Code gefunden wird, gib einen leeren String zurück
    if not matches:
        return "---"

    # Verzeichnis für gespeicherte Bilder
    image_dir = r"C:\Users\julia\PycharmProjects\MAVIS\static\image"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for match in matches:
        code = match.strip()
        try:
            # Umleiten der Ausgaben in einen String-Buffer
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()

            # Ersetze plt.show() durch Speichern der Grafik
            code = code.replace("plt.show()", "# plt.show() ersetzt durch Speichern der Grafik")

            # Kontext für die Code-Ausführung erstellen
            exec_globals = {}
            exec_locals = {}
            exec(code, exec_globals, exec_locals)

            # Erhalte alle Ausgaben, die während der Code-Ausführung erzeugt wurden
            output_text = sys.stdout.getvalue()
            # Wiederherstellen der normalen Ausgabe
            sys.stdout = old_stdout

            img_html = ""

            # Verarbeitung von Matplotlib- oder Seaborn-Grafiken
            fig = plt.gcf()  # Seaborn nutzt Matplotlib für die Visualisierung
            if fig and fig.get_axes():  # Überprüfen, ob eine Grafik vorhanden ist
                # Generiere einen eindeutigen Dateinamen
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                image_filename = f"fig_matplotlib_{timestamp}.png"
                image_path = os.path.join(image_dir, image_filename)
                # Diagramm speichern
                plt.savefig(image_path, format='png', bbox_inches='tight')
                plt.close(fig)  # Grafik schließen, um Speicher freizugeben
                # Relativer Pfad für HTML (basierend auf Flask-Static-Serving)
                image_url = f"/static/image/{image_filename}"

                # Füge das Bild in den HTML-Output ein
                img_html += f'<img class="img-out" src="{image_url}" alt="Generated Matplotlib Plot" />'

            # Verarbeitung von Plotly-Grafiken
            for var_name, var_value in exec_locals.items():
                if hasattr(var_value, "write_html") and callable(var_value.write_html):
                    # Prüfen, ob die Variable eine Plotly-Figur ist
                    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    html_filename = f"fig_plotly_{timestamp}.html"  # HTML-Datei
                    html_path = os.path.join(image_dir, html_filename)

                    # Diagramm als interaktive HTML-Datei speichern
                    var_value.write_html(html_path)

                    # Relativer Pfad für HTML (basierend auf Flask-Static-Serving)
                    image_url = f"/static/image/{html_filename}"

                    # Füge das HTML-Dokument in den HTML-Output ein
                    img_html += f'<iframe src="{image_url}" width="800px" height="500px" frameborder="0"></iframe>'
                    break  # Nur das erste Plotly-Diagramm verarbeiten

            for var_name, var_value in exec_locals.items():
                if isinstance(var_value, alt.Chart):  # Prüfen, ob es sich um ein Altair-Diagramm handelt
                    try:
                        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                        image_filename = f"fig_altair_{timestamp}.svg"
                        image_path = os.path.join(image_dir, image_filename)

                        # Versuchen, die SVG-Datei zu speichern
                        var_value.save(image_path, format="svg")

                        # Relativer Pfad für die HTML-Ausgabe
                        image_url = f"/static/image/{image_filename}"
                        img_html += f'<img class="img-out" src="{image_url}" width="600px" height="400px" />'

                    except Exception as e:
                        print(f"Fehler beim Speichern des Altair-Diagramms: {e}")
                        # Alternativ: Als PNG speichern
                        try:
                            png_filename = f"fig_altair_{timestamp}.png"
                            png_path = os.path.join(image_dir, png_filename)
                            var_value.save(png_path, format="png")
                            png_url = f"/static/image/{png_filename}"
                            img_html += f'<img class="img-out" src="{png_url}" width="600px" height="400px" />'
                        except Exception as png_error:
                            print(f"Fehler beim Fallback auf PNG: {png_error}")
                            img_html += f"<div class='error'>Fehler: Altair-Diagramm konnte weder als SVG noch als PNG gespeichert werden.</div>"

            # Ersetze den Codeblock im Markdown durch den Ausgabeblock (Text oder Bild)
            result = f"<div class='code-output-box'>{output_text}{img_html}</div>"

        except Exception as e:
            # Fehler beim Ausführen des Codes
            error_msg = f"Fehler beim Ausführen des Codes: {e}"
            error_html = f"<div class='code-output-box error'>Execution Error: {error_msg}</div>"
            result = error_html

        session['result'] = result
        return result

@app.route('/')
def index():
    return render_template('index20.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '').strip()
    file = request.files.get('image', None)

    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400

    if file and file.filename and allowed_file(file.filename):
        # Verarbeite die Nachricht mit dem hochgeladenen Bild
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Standard: Laden Sie das Modell auf die verfügbaren Geräte.
            model = Qwen2VLForConditionalGeneration.from_pretrained(
                "Qwen/Qwen2-VL-2B-Instruct", torch_dtype="auto", device_map="auto"
            )

            # Wir empfehlen die Aktivierung von flash_attention_2 für eine bessere Beschleunigung und Speichereinsparung, insbesondere in Szenarien mit mehreren Bildern und Videos.
            # model = Qwen2VLForConditionalGeneration.from_pretrained(
            #     "Qwen/Qwen2-VL-2B-Instruct",
            #     torch_dtype=torch.bfloat16,
            #     attn_implementation="flash_attention_2",
            #     device_map="auto",
            # )

            # Standardprozessor
            processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

            # Der Standardbereich für die Anzahl der visuellen Token pro Bild im Modell liegt zwischen 4 und 16384. Sie können min_pixels und max_pixels entsprechend Ihren Anforderungen festlegen, z. B. einen Token-Zählungsbereich von 256–1280, um Geschwindigkeit und Speichernutzung auszugleichen.
            # min_pixels = 256*28*28
            # max_pixels = 1280*28*28
            # processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)

            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": filepath},
                        {"type": "text", "text": user_message},
                    ],
                }
            ]

            text = processor.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )

            if isinstance(text, list):
                text = text[0]

            image_inputs, video_inputs = process_vision_info(messages)
            inputs = processor(
                text=[text],
                images=image_inputs,
                videos=video_inputs,
                padding=True,
                return_tensors="pt",
            )
            device = "cuda" if torch.cuda.is_available() else "cpu"
            inputs = inputs.to(device)

            # Inferenz: Generierung der Ausgabe
            generated_ids = model.generate(**inputs, max_new_tokens=128)
            generated_ids_trimmed = [
                out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
            ]
            response_content = processor.batch_decode(
                generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )[0]
            response_content_code = execute_python_code(response_content)

            # Rückgabe der Antwort als JSON
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            return jsonify({
                'response': wrapped_html_content,
                'image_url': app.config['UPLOAD_URL'] + filename,
                'code': response_content_code
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        # Verarbeite die Nachricht ohne Bild, benutze das Standardbild
        try:
            model_name = "Qwen/Qwen2.5-14B-Instruct"

            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype="auto",
                device_map="auto"
            )
            tokenizer = AutoTokenizer.from_pretrained(model_name)

            messages = [
                {"role": "system", "content": "You are a helpful and harmless assistant. You should think step-by-step."},
                {"role": "user", "content": user_message}
            ]
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

            generated_ids = model.generate(
                **model_inputs,
                max_new_tokens=512
            )
            generated_ids = [
                output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
            ]

            response_content = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

            response_content_code = execute_python_code(response_content)

            # Rückgabe der Antwort als JSON
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            return jsonify({
                'response': wrapped_html_content,
                'image_url': DEFAULT_IMAGE_PATH,
                'code': response_content_code
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)