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
import pygame
import whisper
import ollama
import cv2
import numpy as np
import wave
import time
import threading
import pyaudio
import webrtcvad
import logging
from TTS.api import TTS
from flask import Flask, jsonify, render_template, request
import json

# TensorFlow Warnungen unterdrücken
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'

# Logging reduzieren
logging.getLogger('tensorflow').setLevel(logging.ERROR)

app = Flask(__name__)

# Sicherstellen, dass das "static" Verzeichnis existiert
os.makedirs("static", exist_ok=True)

# Pfad zur JSON-Datei korrekt zusammensetzen
file_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "model-mavis-4.json")

# Datei öffnen und JSON laden
try:
    with open(file_path, 'r') as file:
        model_config = json.load(file)
    print("Die JSON-Datei wurde erfolgreich geladen.")
except FileNotFoundError:
    print(f"Die Datei {file_path} wurde nicht gefunden.")
except json.JSONDecodeError as e:
    print(f"Fehler beim Parsen der JSON-Datei: {e}")

# Extrahiere die Modelle aus der Konfiguration
model4 = model_config['mavis-4']['model4']

# Pygame initialisieren (für Audioausgabe)
def init_pygame():
    try:
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        print("Pygame initialized.")
    except pygame.error as e:
        print(f"Error initializing Pygame: {e}")


# Bild von der Kamera aufnehmen
def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not available.")
        return None

    ret, frame = cap.read()
    cap.release()

    if ret:
        image_path = f"static/image_{int(time.time())}.jpg"
        cv2.imwrite(image_path, frame)
        return image_path
    return None


# Funktion zur Audioaufnahme mit pyaudio und webrtcvad
def record_audio(filename="input.wav", samplerate=16000, frame_duration_ms=30, vad_mode=1):
    # Initialisierung von VAD (Voice Activity Detection)
    vad = webrtcvad.Vad(vad_mode)  # VAD-Mode kann von 0 bis 3 gehen, wobei 3 am empfindlichsten ist

    # pyaudio Setup
    p = pyaudio.PyAudio()

    # Audio-Stream öffnen
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=samplerate,
                    input=True,
                    frames_per_buffer=int(samplerate * frame_duration_ms / 1000))

    print("Recording started...")

    frames = []
    silence_duration = 0  # Variable, um die Stille zu überwachen

    while True:
        # Audio-Frame aufnehmen
        audio_frame = stream.read(int(samplerate * frame_duration_ms / 1000))
        frames.append(audio_frame)

        # Überprüfen, ob Sprache erkannt wird
        if vad.is_speech(audio_frame, samplerate):
            silence_duration = 0  # Zurücksetzen des Schweigens, wenn Sprache erkannt wird
        else:
            silence_duration += frame_duration_ms / 1000  # Erhöhe die Stille-Zeit

        # Wenn keine Sprache für 1 Sekunde (1000 ms) erkannt wurde, Aufnahme beenden
        if silence_duration >= 1:
            print("No speech detected for 1 second, stopping recording.")
            break

    # Aufnahme beenden
    stream.stop_stream()
    stream.close()
    p.terminate()

    # WAV-Datei speichern
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(samplerate)
        wf.writeframes(b''.join(frames))

    print("Recording finished.")
    return filename

# Funktion zur Transkription der Audiodatei
def transcribe_audio(file_path):
    model = whisper.load_model("small")

    # Load audio and pad/trim it to fit the model
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # Decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # Store the transcribed text in 'message'
    message = result.text
    print(f"{message}")
    return message

# Text in Sprache umwandeln (TTS)
def text_to_speech(text):
    tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
    output_file = f"static/output_{int(time.time())}.wav"

    try:
        tts.tts_to_file(text=text, file_path=output_file)
        print(f"Audio saved: {output_file}")

        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error in TTS output: {e}")

    return output_file


# Mit Ollama KI chatten
def chat_response(message, image_path):
    try:
        response = ollama.chat(
            model=model4,
            messages=[{
                'role': 'user',
                'content': message,
                'images': [image_path]
            }]
        )
        print(f"{response['message']['content']}")
        return response['message']['content']
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return "Error retrieving AI response."


# Flask Routen
@app.route('/')
def index():
    return render_template("index-solution-3.html")


@app.route('/process', methods=['POST'])
def process():
    image_path = capture_image()
    audio_path = record_audio()
    text = transcribe_audio(audio_path)
    response_text = chat_response(text, image_path)

    # Text-to-Speech im Hintergrund starten (damit UI nicht blockiert)
    threading.Thread(target=text_to_speech, args=(response_text,)).start()

    return jsonify({"response": response_text, "image": image_path, "audio": f"/static/{os.path.basename(audio_path)}"})


# Start der Flask-App
if __name__ == '__main__':
    init_pygame()
    app.run(debug=False, host="192.168.0.67", port=5000, threaded=True)
