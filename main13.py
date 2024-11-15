from flask import Flask, render_template, request, jsonify, send_from_directory
import ollama
import os
from werkzeug.utils import secure_filename
import markdown

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_URL'] = '/uploads/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index10.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '')

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if 'image' not in request.files:
        try:

            response = ollama.chat(
                model='llama3.2-vision',
                messages=[{
                    'role': 'user',
                    'content': user_message
                }]
            )

            response_content = response['message']['content']

            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')

            wrapped_html_content = f"<div style='display:block;'>{html_content}</div>"

            return jsonify({'response': wrapped_html_content, 'image_url': app.config['UPLOAD_URL']})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:

            response_content = """Welchen Code möchtest du gerne haben? Eine einfache Aufgabe, ein Spiel oder etwas komplexeres?

Hier sind einige Ideen:

1. **Zahlenraten-Spiel**: Ein einfaches Spiel, bei dem der Benutzer eine Zahl erraten muss.
2. **Wetter-App**: Ein kleines Programm, das den aktuellen Wetterbericht liefert.
3. **To-Do-Liste**: Ein einfacher To-Do-Listen-Manager.
4. **Fibonacci-Zahlen**: Eine Funktion, die Fibonacci-Zahlen generiert.

$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$

Welche von diesen Ideen gefällt dir oder hast du etwas anderes im Sinn?

Ich kann auch einen grundlegenden Code schreiben, wie zum Beispiel:

**Einfaches Python-Programm**
```python
# Ein einfaches Python-Programm

print("Hallo, Welt!")

name = input("Wie heißt du? ")

print(f"Hallo, {name}!")
```
Oder ein kleines Spiel:
```python
# Zahlenraten-Spiel

import random

zahl = random.randint(1, 100)
versuche = 0

while True:
    user_input = int(input("Bitte eine Zahl zwischen 1 und 100 eingeben: "))
    versuche += 1

    if user_input < zahl:
        print("Die Zahl ist höher!")
    elif user_input > zahl:
        print("Die Zahl ist niedriger!")
    else:
        print(f"Herzlichen Glückwunsch! Du hast die Zahl erraten. Es gab {versuche} Versuche.")
        break
```
Sag mir, was du möchtest!"""

            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')

            wrapped_html_content = f"<div style='display:block;'>{html_content}</div>"

            return jsonify({'response': wrapped_html_content, 'image_url': app.config['UPLOAD_URL'] + filename})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == "__main__":
    app.run(debug=True)
