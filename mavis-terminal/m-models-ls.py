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
import logging
from concurrent.futures import ThreadPoolExecutor

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea,
    QFrame, QSizePolicy, QPushButton, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QPalette, QColor, QIcon, QFont
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QObject, pyqtSignal, QThread

# Logging konfigurieren
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_model_with_ollama(model_version: str) -> bool:
    """
    Überprüft, ob ein Modell in Ollama verfügbar ist.
    """
    try:
        result = subprocess.run(
            ["ollama", "show", model_version],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            check=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        return False
    except Exception as e:
        logging.error(f"Unknown error while validating the model {model_version}: {e}")
        return False


def fetch_models():
    # Beispielhafte Modelle mit Name, Version, Kategorie und Bewertung
    return [
        {"name": "Xc++ I 11b", "av": "only pro users", "version": "xcpp:11b", "category": "Vision Tool", "rating": 4},
        {"name": "Xc++ II 11b", "av": "only pro users", "version": "xcpp2:11b", "category": "Vision Tool", "rating": 5},
        {"name": "Xc++ III 11b", "av": "only pro users", "version": "xcpp3:11b", "category": "Vision Tool", "rating": 5},
        {"name": "Xc++ IV 11b", "av": "only pro users", "version": "xcpp4:11b", "category": "Vision Tool", "rating": 6},
        {"name": "Chat++ I 70b", "av": "only pro users", "version": "chatpp1:70b", "category": "Vision Tool", "rating": 2},
        {"name": "Chat++ II 70b", "av": "only pro users", "version": "chatpp2:70b", "category": "Vision Tool", "rating": 2},
        {"name": "Chat++ III 70b", "av": "only pro users", "version": "chatpp3:70b", "category": "Vision Tool", "rating": 3},
        {"name": "Chat++ IV 70b", "av": "only pro users", "version": "chatpp4:70b", "category": "Vision Tool", "rating": 4},
        {"name": "Chat++ mini 8b", "av": "only pro users", "version": "chatppmini:8b", "category": "Vision Tool", "rating": 4},
        {"name": "Chat++ V 70b", "av": "only pro users", "version": "chatpp5:70b", "category": "Vision Tool", "rating": 5},
        {"name": "Woyzy 8b", "av": "only pro users", "version": "woyzy:8b", "category": "Vision Tool", "rating": 4},
        {"name": "Qwen 3 0.6b", "av": "Free", "version": "qwen3:0.6b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 3 1.7b", "av": "Free", "version": "qwen3:1.7b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 3 4b", "av": "Free", "version": "qwen3:4b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 3 8b", "av": "Free", "version": "qwen3:8b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 14b", "av": "Free", "version": "qwen3:14b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 32b", "av": "Free", "version": "qwen3:32b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 30b-A3B", "av": "Free", "version": "qwen3:30b-a3b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 235b-A3B", "av": "Free", "version": "qwen3:235b-a22b", "category": "Language Model",
         "rating": 6},
        {"name": "Llama 4 Scout 109B-A17B", "av": "Free", "version": "llama4:scout", "category": "Vision Tool", "rating": 6},
        {"name": "Llama4 Maverick 400B-A17B", "av": "Free", "version": "llama4:maverick", "category": "Vision Tool", "rating": 6},
        {"name": "Gemma 3 4b", "av": "Free", "version": "gemma3:4b", "category": "Vision Tool", "rating": 5},
        {"name": "Gemma 3 12b", "av": "Free", "version": "gemma3:12b", "category": "Vision Tool", "rating": 6},
        {"name": "Gemma 3 27b", "av": "Free", "version": "gemma3:27b", "category": "Vision Tool", "rating": 6},
        {"name": "QwQ", "av": "Free", "version": "qwq", "category": "Language Model", "rating": 6},
        {"name": "Mistral Small 3.1 24b", "av": "Free", "version": "mistral-small3.1", "category": "Vision Tool", "rating": 6},
        {"name": "Llama 3.1 8b", "av": "Free", "version": "llama3.1:8b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 70b", "av": "Free", "version": "llama3.1:70b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 405b", "av": "Free", "version": "llama3.1:405b", "category": "Language Model", "rating": 5},
        {"name": "Llama 3.2 1b", "av": "Free", "version": "llama3.2:1b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 3b", "av": "Free", "version": "llama3.2:3b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 Vision 11b", "av": "Free", "version": "llama3.2-vision:11b", "category": "Vision Tool", "rating": 5},
        {"name": "Llama 3.2 Vision 90b", "av": "Free", "version": "llama3.2-vision:90b", "category": "Vision Tool", "rating": 5},
        {"name": "Llama 3.3 70b", "av": "Free", "version": "llama3.3", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 14b", "av": "Free", "version": "phi4", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 reasoning 14b", "av": "Free", "version": "phi4-reasoning", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 mini 3.8b", "av": "Free", "version": "phi4-mini", "category": "Language Model", "rating": 4},
        {"name": "Phi 4 mini reasoning 3.8b", "av": "Free", "version": "phi4-mini-reasoning", "category": "Language Model", "rating": 4},
        {"name": "DeepSeek-v3 671", "av": "Free", "version": "deepseek-v3", "category": "Language Model", "rating": 4},
        {"name": "DeepSeek-r1 1.5b", "av": "Free", "version": "deepseek-r1:1.5b", "category": "Language Model", "rating": 5},
        {"name": "DeepSeek-r1 7b", "av": "Free", "version": "deepseek-r1:7b", "category": "Language Model", "rating": 5},
        {"name": "DeepSeek-r1 8b", "av": "Free", "version": "deepseek-r1:8b", "category": "Language Model", "rating": 5},
        {"name": "DeepSeek-r1 14b", "av": "Free", "version": "deepseek-r1:14b", "category": "Language Model", "rating": 6},
        {"name": "DeepSeek-r1 32b", "av": "Free", "version": "deepseek-r1:32b", "category": "Language Model", "rating": 6},
        {"name": "DeepSeek-r1 70b", "av": "Free", "version": "deepseek-r1:70b", "category": "Language Model", "rating": 6},
        {"name": "DeepSeek-r1 671b", "av": "Free", "version": "deepseek-r1:671b", "category": "Language Model", "rating": 6},
        {"name": "DeepCodern 1.5b", "av": "Free", "version": "deepcoder:1.5b", "category": "Language Model", "rating": 5},
        {"name": "DeepCodern 14b", "av": "Free", "version": "deepcoder:14b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 3b", "av": "Free", "version": "cogito:3b", "category": "Language Model", "rating": 4},
        {"name": "Cogito 8b", "av": "Free", "version": "cogito:8b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 14b", "av": "Free", "version": "cogito:14b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 32b", "av": "Free", "version": "cogito:32b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 70b", "av": "Free", "version": "cogito:70b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 vl 3b", "av": "Free", "version": "qwen2.5vl:3b", "category": "Vision Tool", "rating": 5},
        {"name": "Qwen 2.5 vl 7b", "av": "Free", "version": "qwen2.5vl:7b", "category": "Vision Tool", "rating": 5},
        {"name": "Qwen 2.5 vl 32b", "av": "Free", "version": "qwen2.5vl:32b", "category": "Vision Tool", "rating": 6},
        {"name": "Qwen 2.5 vl 72b", "av": "Free", "version": "qwen2.5vl:72b", "category": "Vision Tool", "rating": 6},
        {"name": "Qwen 2.5 0.5b", "av": "Free", "version": "qwen2.5:0.5b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 1.5b", "av": "Free", "version": "qwen2.5:1.5b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 3b", "av": "Free", "version": "qwen2.5:3b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 7b", "av": "Free", "version": "qwen2.5:7b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 14b", "av": "Free", "version": "qwen2.5:14b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 32b", "av": "Free", "version": "qwen2.5:32b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 72b", "av": "Free", "version": "qwen2.5:72b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 coder 0.5b", "av": "Free", "version": "qwen2.5-coder:0.5b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 1.5b", "av": "Free", "version": "qwen2.5-coder:1.5b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 3b", "av": "Free", "version": "qwen2.5-coder:3b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 7b", "av": "Free", "version": "qwen2.5-coder:7b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 14b", "av": "Free", "version": "qwen2.5-coder:14b", "category": "Language Model", "rating": 5},
        {"name": "Granite 3.3 2b", "av": "Free", "version": "granite3.3:2b", "category": "Language Model", "rating": 4},
        {"name": "Granite 3.3 8b", "av": "Free", "version": "granite3.3:8b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 coder 32b", "av": "Free", "version": "qwen2.5-coder:32b", "category": "Language Model", "rating": 5},
        {"name": "EXAONE Deep 2.4b", "av": "Free", "version": "exaone-deep:2.4b", "category": "Language Model", "rating": 3},
        {"name": "EXAONE Deep 7.8b", "av": "Free", "version": "exaone-deep:7.8b", "category": "Language Model", "rating": 3},
        {"name": "EXAONE Deep 32b", "av": "Free", "version": "exaone-deep:32b", "category": "Language Model", "rating": 3},
        {"name": "DeepScaleR 1.5b", "av": "Free", "version": "deepscaler", "category": "Language Model", "rating": 5},
        {"name": "Mistral Large 123B", "av": "Free", "version": "mistral-large", "category": "Language Model", "rating": 5},
        {"name": "Qwen 0.5b", "av": "Free", "version": "qwen:0.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 1.8b", "av": "Free", "version": "qwen:1.8b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 4b", "av": "Free", "version": "qwen:4b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 7b", "av": "Free", "version": "qwen:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 14b", "av": "Free", "version": "qwen:14b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 32b", "av": "Free", "version": "qwen:32b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 72b", "av": "Free", "version": "qwen:72b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 110b", "av": "Free", "version": "qwen:110b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 0.5b", "av": "Free", "version": "qwen2:0.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 1.5b", "av": "Free", "version": "qwen2:1.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 7b", "av": "Free", "version": "qwen2:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 110b", "av": "Free", "version": "qwen2:110b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3 3.8b", "av": "Free", "version": "phi3:14b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3 14b", "av": "Free", "version": "phi3:14b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2b", "av": "Free", "version": "gemma:2b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 7b", "av": "Free", "version": "gemma:7b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 2b", "av": "Free", "version": "gemma3:2b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 9b", "av": "Free", "version": "gemma3:9b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 27b", "av": "Free", "version": "gemma3:27b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 7b", "av": "Free", "version": "codellama:7b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 13b", "av": "Free", "version": "codellama:13b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 34b", "av": "Free", "version": "codellama:32b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 70b", "av": "Free", "version": "codellama:70b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 7b", "av": "Free", "version": "llama2:8b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 13b", "av": "Free", "version": "llama2:13b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 70b", "av": "Free", "version": "llama2:70b", "category": "Language Model", "rating": 3},
        {"name": "Llama 3 8b", "av": "Free", "version": "llama3:8b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3 70b", "av": "Free", "version": "llama3:70b", "category": "Language Model", "rating": 4},
        {"name": "Mistral 7b", "av": "Free", "version": "mistral", "category": "Language Model", "rating": 4},
        {"name": "Mistral nemo 12b", "av": "Free", "version": "mistral-nemo", "category": "Language Model", "rating": 4},
        {"name": "LlaVA 7b", "av": "Free", "version": "llava:7b", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA 13b", "av": "Free", "version": "llava:13b", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA 34b", "av": "Free", "version": "llava:34b", "category": "Vision Tool", "rating": 3},
        {"name": "Tinyllama 1.1b", "av": "Free", "version": "tinyllama", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 3b", "av": "Free", "version": "starcoder2:3b", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 7b", "av": "Free", "version": "starcoder2:7b", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 15b", "av": "Free", "version": "starcoder2:15b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 uncensored 7b", "av": "Free", "version": "llama2-uncensored:7b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 uncensored 70b", "av": "Free", "version": "llama2-uncensored:70b", "category": "Language Model",
         "rating": 3},
        {"name": "DeepSeek coder v2 16b", "av": "Free", "version": "deepseek-coder-v2:16b", "category": "Language Model",
         "rating": 4},
        {"name": "DeepSeek coder v2 236", "av": "Free", "version": "deepseek-coder-v2:236b", "category": "Language Model",
         "rating": 4},
        {"name": "Minicpm v 8b", "av": "Free", "version": "minicpm-v", "category": "Vision Tool", "rating": 3},
        {"name": "Deepseek coder 1.3b", "av": "Free", "version": "deepseek-coder:1.3b", "category": "Language Model", "rating": 3},
        {"name": "Deepseek coder 6.7b", "av": "Free", "version": "deepseek-coder:6.7b", "category": "Language Model", "rating": 3},
        {"name": "Deepseek coder 33b", "av": "Free", "version": "deepseek-coder:33b", "category": "Language Model", "rating": 3},
        {"name": "Mixtral 8x7b", "av": "Free", "version": "mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "Mixtral 8x22b", "av": "Free", "version": "mixtral:8x22b", "category": "Language Model", "rating": 5},
        {"name": "codegemma 2b", "av": "Free", "version": "codegemma:2b", "category": "Language Model", "rating": 3},
        {"name": "codegemma 7b", "av": "Free", "version": "codegemma:7b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Mixtral 8x7b", "av": "Free", "version": "dolphin-mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "Dolphin Mixtral 8x22b", "av": "Free", "version": "dolphin-mixtral:8x22b", "category": "Language Model",
         "rating": 4},
        {"name": "Open Thinker 7b", "av": "Free", "version": "openthinker:7b", "category": "Language Model", "rating": 4},
        {"name": "Open Thinker 32b", "av": "Free", "version": "openthinker:32b", "category": "Language Model", "rating": 4},
        {"name": "Phi 2.7b", "av": "Free", "version": "phi", "category": "Language Model", "rating": 3},
        {"name": "LlaVA Llama3 8b", "av": "Free", "version": "llava-llama3", "category": "Vision Tool", "rating": 4},
        {"name": "Dolphin 3 8b", "av": "Free", "version": "dolphin3", "category": "Language Model", "rating": 3},
        {"name": "Olmo 2 7b", "av": "Free", "version": "olmo2:7b", "category": "Language Model", "rating": 3},
        {"name": "Olmo 2 13b", "av": "Free", "version": "olmo2:13b", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 135m", "av": "Free", "version": "smollm2:135m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 360m", "av": "Free", "version": "smollm2:360m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 1.7b", "av": "Free", "version": "smollm2:1.7b", "category": "Language Model", "rating": 3},
        {"name": "Wizardlm 2 7b", "av": "Free", "version": "wizardlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "Wizardlm 2 8x22b", "av": "Free", "version": "wizardlm2:8x22b", "category": "Language Model", "rating": 4},
        {"name": "Mistral small 22b", "av": "Free", "version": "mistral-small:22b", "category": "Language Model", "rating": 4},
        {"name": "Mistral small 24b", "av": "Free", "version": "mistral-small:24b", "category": "Language Model", "rating": 4},
        {"name": "Dolphin mistral 7b", "av": "Free", "version": "dolphin-mistral:7b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Llama 3 8b", "av": "Free", "version": "dolphin-llama3:8b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Llama 3 70b", "av": "Free", "version": "dolphin-llama3:70b", "category": "Language Model", "rating": 3},
        {"name": "Command r 35b", "av": "Free", "version": "command-r", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 3b", "av": "Free", "version": "orca-mini:3b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 7b", "av": "Free", "version": "orca-mini:7b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 13b", "av": "Free", "version": "orca-mini:13b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 70b", "av": "Free", "version": "orca-mini:70b", "category": "Language Model", "rating": 3},
        {"name": "yi 6b", "av": "Free", "version": "yi:6b", "category": "Language Model", "rating": 3},
        {"name": "yi 9b", "av": "Free", "version": "yi:69b", "category": "Language Model", "rating": 3},
        {"name": "yi 34b", "av": "Free", "version": "yi:34b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 1.5b", "av": "Free", "version": "qwen2-math:1.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 7b", "av": "Free", "version": "qwen2-math:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 72b", "av": "Free", "version": "qwen2-math:72b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 3b", "av": "Free", "version": "hermes3:3b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 8b", "av": "Free", "version": "hermes3:8b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 70b", "av": "Free", "version": "hermes3:70b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 405b", "av": "Free", "version": "hermes3:405b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3.5 3.8b", "av": "Free", "version": "phi3.5", "category": "Language Model", "rating": 4},
        {"name": "Smollm 125m", "av": "Free", "version": "smollm:135m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 360m", "av": "Free", "version": "smollm:360m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 1.7b", "av": "Free", "version": "smollm:1.7b", "category": "Language Model", "rating": 3},
        {"name": "Nuextract 3.8b", "av": "Free", "version": "nuextract", "category": "Language Model", "rating": 3},
        {"name": "Firefunction v2 70b", "av": "Free", "version": "firefunction-v2", "category": "Language Model", "rating": 3},
        {"name": "Llama 3 groq tool use 8b", "av": "Free", "version": "llama3-groq-tool-use:8b", "category": "Language Model",
         "rating": 3},
        {"name": "Llama 3 groq tool use 70b", "av": "Free", "version": "llama3-groq-tool-use:70b", "category": "Language Model",
         "rating": 3},
        {"name": "Mathstral 7b", "av": "Free", "version": "mathstral", "category": "Language Model", "rating": 3},
        {"name": "Codegee x4 9b", "av": "Free", "version": "codegeex4", "category": "Language Model", "rating": 3},
        {"name": "glm4 9b", "av": "Free", "version": "glm4", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 1m", "av": "Free", "version": "internlm2:1m", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 1.8b", "av": "Free", "version": "internlm2:1.8b", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 7b", "av": "Free", "version": "internlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 20b", "av": "Free", "version": "internlm2:20b", "category": "Language Model", "rating": 3},
        {"name": "Codestral 22b", "av": "Free", "version": "codestral", "category": "Language Model", "rating": 4},
        {"name": "Granite 3.2 Vision 2b", "av": "Free", "version": "granite3.2-vision", "category": "Vision Tool", "rating": 3},
        {"name": "Moon Dream 1.8b", "av": "Free", "version": "moondream", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA Llama3 8b", "av": "Free", "version": "llava-llama3", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA Phi3 3.8b", "av": "Free", "version": "llava-phi3", "category": "Vision Tool", "rating": 3},
        {"name": "Bak LlaVA 7b", "av": "Free", "version": "bakllava", "category": "Vision Tool", "rating": 3},
        {"name": "DBRX 132b", "av": "Free", "version": "dbrx", "category": "Language Model", "rating": 4},
        {"name": "notus 7b", "av": "Free", "version": "notus", "category": "Language Model", "rating": 4},
        {"name": "Tulu 3 8b", "av": "Free", "version": "tulu3:8b", "category": "Language Model", "rating": 4},
        {"name": "Tulu 3 70b", "av": "Free", "version": "tulu3:70b", "category": "Language Model", "rating": 4},
        {"name": "Notux 8x7b", "av": "Free", "version": "notux", "category": "Language Model", "rating": 4},
        {"name": "megadolphin 120b", "av": "Free", "version": "megadolphin", "category": "Language Model", "rating": 4},
        {"name": "Wizard Vicuna 13b", "av": "Free", "version": "wizard-vicuna", "category": "Language Model", "rating": 4},
        {"name": "Duckdb NSQL 7b", "av": "Free", "version": "duckdb-nsql", "category": "Language Model", "rating": 4}
    ]

class CommandWorker(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, command: list):
        super().__init__()
        self.command = command

    def run(self):
        try:
            result = subprocess.run(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8"
            )
            # Nutze stdout, falls vorhanden, sonst stderr
            output = result.stdout.strip() if result.stdout.strip() else result.stderr.strip()
            self.finished.emit(output)
        except Exception as e:
            self.error.emit(str(e))


class ModelCard(QFrame):
    def __init__(self, model: dict, is_installed: bool, parent=None):
        super().__init__(parent)
        self.model = model
        self.is_installed = is_installed
        self.details_shown = False  # Status, ob der Detailbereich ein- oder ausgeblendet ist
        self.setup_ui()
        self.setup_shadow()
        self.setMouseTracking(True)

    def setup_ui(self):
        # Gesamtlayout: Header (fester Bereich) + Details-Bereich (ausklappbar)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.main_layout.setSpacing(5)

        # Header-Bereich (fixe Höhe für Listendarstellung)
        self.header_widget = QWidget()
        self.header_widget.setFixedHeight(100)
        self.header_widget.setStyleSheet("background: transparent")
        header_layout = QHBoxLayout(self.header_widget)
        header_layout.setContentsMargins(10, 5, 10, 5)
        header_layout.setSpacing(15)

        # Name Label
        self.name_label = QLabel(self.model["name"])
        self.name_label.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        self.name_label.setStyleSheet("""
            QFrame {
                background: transparent;
                border: none;
                color: #ffffff;
            }
        """)
        header_layout.addWidget(self.name_label, 2)

        # Version
        self.av_label = QLabel(self.model["av"])
        self.av_label.setFont(QFont("Segoe UI", 11))
        self.av_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #bbdefb);
            color: #000000;
            padding: 2px 8px;
            border-radius: 8px;
        """)
        self.av_label.setFixedHeight(35)
        header_layout.addWidget(self.av_label, 1)

        # Kategorie als Badge
        self.category_label = QLabel(self.model["category"])
        self.category_label.setFont(QFont("Segoe UI", 11))
        self.category_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.category_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #bbdefb);
            color: #000000;
            padding: 2px 8px;
            border-radius: 8px;
        """)
        self.category_label.setFixedHeight(35)
        header_layout.addWidget(self.category_label, 1)

        # Version
        self.version_label = QLabel("Version: '" + self.model["version"] + "'")
        self.version_label.setFont(QFont("Segoe UI", 11))
        self.version_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #bbdefb);
            color: #000000;
            padding: 2px 8px;
            border-radius: 8px;
        """)
        self.version_label.setFixedHeight(35)
        header_layout.addWidget(self.version_label, 1)

        # Installationsstatus
        status_text = "Installed" if self.is_installed else "Not Installed"
        status_color = "stop:0 #81c784, stop:1 #43a047" if self.is_installed else "stop:0 #ec7063, stop:1 #b03a2e"
        self.status_label = QLabel(status_text)
        self.status_label.setFont(QFont("Segoe UI", 11))
        self.status_label.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, {status_color});
            color: #000000;
            border: none;
            padding: 4px 8px;
            border-radius: 8px;
        """)
        self.status_label.setFixedHeight(35)
        header_layout.addWidget(self.status_label, 1)

        # Sternebewertung
        stars = "★" * self.model["rating"] + "☆" * (6 - self.model["rating"])
        self.rating_label = QLabel(stars)
        self.rating_label.setFont(QFont("Segoe UI", 12))
        self.rating_label.setStyleSheet("""
            QFrame {
                background: transparent;
                border: none;
                color: #f1c40f;
            }
        """)
        header_layout.addWidget(self.rating_label, 1)

        # Buttons basierend auf Installationsstatus hinzufügen
        if self.is_installed:
            self.show_info_button = QPushButton("Show Info")
            self.show_info_button.setFont(QFont("Segoe UI", 11))
            self.show_info_button.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #bbdefb);
                    color: #000000;
                    border: none;
                    padding: 4px 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #bbdefb;
                }
            """)
            self.show_info_button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.show_info_button.setFixedHeight(35)
            self.show_info_button.clicked.connect(self.on_show_info_clicked)
            header_layout.addWidget(self.show_info_button, 1)

            # Neuer Delete-Button
            self.delete_button = QPushButton("Delete")
            self.delete_button.setFont(QFont("Segoe UI", 11))
            self.delete_button.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ec7063, stop:1 #b03a2e);
                    color: #ffffff;
                    border: none;
                    padding: 4px 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #b03a2e;
                }
            """)
            self.delete_button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.delete_button.setFixedHeight(35)
            self.delete_button.clicked.connect(self.on_delete_clicked)
            header_layout.addWidget(self.delete_button, 1)

        else:
            self.install_button = QPushButton("Install")
            self.install_button.setFont(QFont("Segoe UI", 11))
            self.install_button.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #81c784, stop:1 #43a047);
                    color: #ffffff;
                    border: none;
                    padding: 4px 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #43a047;
                }
            """)
            self.install_button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.install_button.setFixedHeight(35)
            self.install_button.clicked.connect(self.on_installed_clicked)
            header_layout.addWidget(self.install_button, 1)

        self.main_layout.addWidget(self.header_widget)

        # Details-Bereich: hier wird die Ausgabe von "ollama show" angezeigt
        self.details_label = QLabel("")
        self.details_label.setFont(QFont("Segoe UI", 10))
        self.details_label.setStyleSheet("color: #ecf0f1; padding: 5px; border-radius: 5px;")
        self.details_label.setWordWrap(True)
        self.details_label.setVisible(False)
        self.main_layout.addWidget(self.details_label)

        # Gesamte Card-Styles
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border-radius: 12px;
                border: 1px solid #566573;
            }
            QFrame:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
                border: 1px solid #778899;
            }
            QLabel {
                background: transparent;
            }
        """)

    def setup_shadow(self):
        # Schatteneffekt für 3D-Optik
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)

    def enterEvent(self, event):
        # Schatten wird beim Hover animiert
        self.anim = QPropertyAnimation(self.shadow, b"blurRadius")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(20)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Schatten kehrt zurück
        self.anim = QPropertyAnimation(self.shadow, b"blurRadius")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(10)
        self.anim.start()
        super().leaveEvent(event)

    def on_delete_clicked(self):
        """ Führt 'ollama rm {model["version"]}' asynchron aus und aktualisiert den Status. """
        command = ["ollama", "rm", self.model["version"]]
        self.delete_button.setEnabled(False)
        self.run_command(command, self.handle_delete_result)

    def on_installed_clicked(self):
        """ Führt 'ollama rm {model["version"]}' asynchron aus und aktualisiert den Status. """
        command = ["ollama", "run", self.model["version"]]
        self.install_button.setEnabled(False)
        self.run_command(command, self.handle_install_result)

    def on_show_info_clicked(self):
        """ Führt 'ollama show {model["version"]}' aus, zeigt die Ausgabe an,
            oder klappt die Details wieder zusammen, wenn sie schon angezeigt werden.
        """
        if self.details_shown:
            # Animation zum Zusammenklappen auf die ursprüngliche Höhe (Header-Höhe: 100)
            self.animate_contraction()
            return

        command = ["ollama", "show", self.model["version"]]
        self.show_info_button.setEnabled(False)
        self.run_command(command, self.handle_show_info_result)

    def run_command(self, command: list, callback):
        """ Führt einen Kommando in einem separaten Thread aus. """
        self.thread = QThread()
        self.worker = CommandWorker(command)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(callback)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.error.connect(lambda err: logging.error(f"Error: {err}"))
        self.worker.error.connect(self.thread.quit)
        self.thread.start()

    def handle_delete_result(self, output: str):
        logging.info(f"Delete Output for {self.model['version']}: {output}")
        # Nach erfolgreicher Löschung den Status aktualisieren
        self.is_installed = False
        self.status_label.setText("Not Installed")
        self.status_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ec7063, stop:1 #b03a2e);
            color: #000000;
            border: none;
            padding: 4px 8px;
            border-radius: 8px;
        """)
        self.delete_button.setEnabled(True)

    def handle_install_result(self, output: str):
        logging.info(f"Delete Output for {self.model['version']}: {output}")
        # Nach erfolgreicher Löschung den Status aktualisieren
        self.is_installed = True
        self.status_label.setText("Installed")
        self.status_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #81c784, stop:1 #43a047);
            color: #000000;
            border: none;
            padding: 4px 8px;
            border-radius: 8px;
        """)
        self.delete_button.setEnabled(False)

    def handle_show_info_result(self, output: str):
        logging.info(f"Show Output for {self.model['version']}: {output}")
        # Ausgabe in den Details-Bereich schreiben und diesen einblenden
        self.details_label.setText(output)
        self.details_label.setVisible(True)
        self.details_shown = True
        self.show_info_button.setText("Hide Info")
        self.show_info_button.setEnabled(True)
        self.animate_expansion()

    def animate_expansion(self):
        """ Animiert die Box beim Ausklappen. """
        start_height = self.height()  # Aktuelle Höhe der Box
        # Neue Höhe berechnen, basierend auf den Details
        new_height = start_height + self.details_label.sizeHint().height() + 20  # Extra Puffer
        self.anim_height = QPropertyAnimation(self, b"fixedHeight")
        self.anim_height.setDuration(300)
        self.anim_height.setStartValue(start_height)
        self.anim_height.setEndValue(new_height)
        self.anim_height.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim_height.start()

    def animate_contraction(self):
        """ Animiert die Box beim Zusammenklappen auf die ursprüngliche Höhe. """
        current_height = self.height()
        target_height = 100  # Ursprüngliche Höhe (z. B. 100)
        self.anim_height = QPropertyAnimation(self, b"fixedHeight")
        self.anim_height.setDuration(300)
        self.anim_height.setStartValue(current_height)
        self.anim_height.setEndValue(target_height)
        self.anim_height.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim_height.finished.connect(self.on_contraction_finished)
        self.anim_height.start()

    def on_contraction_finished(self):
        self.details_label.setVisible(False)  # Details ausblenden
        self.details_shown = False
        self.show_info_button.setText("Show Info")  # Button-Text zurücksetzen


class ModelShop(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS Model Shop")
        self.setGeometry(100, 100, 1200, 600)
        self.set_dark_mode()
        self.set_background_gradient()

        # Optional: Icon setzen, falls vorhanden
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = os.path.join(f"C:/Users/{user}/PycharmProjects/MAVIS/icons", "mavis-logo.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        main_layout = QVBoxLayout(self)
        header = QLabel("Welcome to MAVIS Model Shop")
        header.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        header.setStyleSheet("""
            QFrame {
                background: transparent;
                border: none;
                color: #ffffff; 
                padding: 20px;
            }
        """)
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        # ScrollArea konfigurieren für die Listendarstellung
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

        self.content_widget = QWidget()
        # Verwende ein vertikales Layout für die Listendarstellung
        self.vbox_layout = QVBoxLayout(self.content_widget)
        self.vbox_layout.setSpacing(15)
        self.vbox_layout.setContentsMargins(30, 30, 30, 30)
        self.scroll_area.setWidget(self.content_widget)
        main_layout.addWidget(self.scroll_area)

        self.load_models()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Button, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
        self.setPalette(palette)

    def set_background_gradient(self):
        # Dezenter vertikaler Farbverlauf als Hintergrund
        self.setStyleSheet("""
            QWidget { 
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
            }
        """)

    def load_models(self):
        models = fetch_models()
        with ThreadPoolExecutor() as executor:
            futures = {model["name"]: executor.submit(check_model_with_ollama, model["version"]) for model in models}
            for model in models:
                is_installed = futures[model["name"]].result()
                card = ModelCard(model, is_installed)
                # Jedes Card-Widget wird untereinander im V-Layout eingefügt
                self.vbox_layout.addWidget(card)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelShop()
    window.show()
    sys.exit(app.exec())
