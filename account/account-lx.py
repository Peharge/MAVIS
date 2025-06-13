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

import json
import bcrypt
from datetime import datetime
import re
import os
import getpass

# Dateipfade definieren (plattformunabhängig)
BASE_DIR = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "account")
DATA_FILE = os.path.join(BASE_DIR, "users.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")

# Sicherstellen, dass das Verzeichnis existiert
os.makedirs(BASE_DIR, exist_ok=True)

# Farbcodes (funktionieren in den meisten Linux-Terminals)
red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
reset = "\033[0m"

def load_users():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"{red}ERROR{reset}: Failed to save users:{e}")

def load_tokens():
    try:
        with open(TOKEN_FILE, "r") as file:
            tokens = json.load(file)
        return tokens.get("tokens", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tokens(tokens):
    try:
        with open(TOKEN_FILE, "w") as file:
            json.dump({"tokens": tokens}, file, indent=4)
    except Exception as e:
        print(f"{red}ERROR{reset}: Failed to save tokens:{e}")

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(hashed, password):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def hash_token(token):
    return bcrypt.hashpw(token.encode(), bcrypt.gensalt()).decode()

def check_token(hashed_token, token):
    return bcrypt.checkpw(token.encode(), hashed_token.encode())

def validate_age(birthdate):
    try:
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
        age = (datetime.today() - birth_date).days // 365
        return 18 <= age <= 120
    except ValueError:
        return False

def validate_password(password):
    return (
        8 <= len(password) <= 20
        and re.search(r"[A-Za-z]", password)
        and re.search(r"\d", password)
        and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )

def register(user_type="Standard"):
    print("\nRegistration\n------------")
    users = load_users()

    while True:
        username = input(f"{blue}Username{reset}:").strip()
        if not username:
            print(f"{red}ERROR{reset}: Username cannot be empty!")
            continue
        if username in users:
            print(f"{red}ERROR{reset}: This username is already taken!")
            continue
        break

    while True:
        email = input(f"{blue}E-Mail{reset}:").strip()
        if "@" in email and "." in email:
            if any(user["email"] == email for user in users.values()):
                print(f"{red}ERROR{reset}: This email is already in use.")
                continue
            break
        print(f"{red}ERROR{reset}: Invalid email address!")

    while True:
        birthdate = input(f"{blue}Date of birth (YYYY-MM-DD){reset}:")
        if validate_age(birthdate):
            break
        print(f"{red}ERROR{reset}: Invalid birthdate or age under 18.")

    while True:
        password = getpass.getpass(f"{blue}Password{reset}:")
        if validate_password(password):
            break
        print(f"{red}ERROR{reset}: Password must be 8–20 chars, incl. letters, numbers & symbols.")

    while True:
        confirm_password = getpass.getpass(f"{blue}Repeat password{reset}:")
        if password == confirm_password:
            break
        print(f"{red}ERROR{reset}: Passwords do not match!")

    users[username] = {
        "email": email,
        "birthdate": birthdate,
        "password": hash_password(password),
        "user_type": user_type,
    }
    save_users(users)
    print(f"{green}Registration successful!{reset}")

def register_mavis_ultra():
    print("\nMAVIS Ultra Registration\n------------------------")
    tokens = load_tokens()

    if not tokens:
        print(f"{red}ERROR{reset}: No valid tokens available.")
        return

    while True:
        token = input(f"{blue}Enter your MAVIS Ultra token{reset}:")
        token_valid = any(check_token(hashed_token, token) for hashed_token in tokens)

        if token_valid:
            print(f"{green}Token verified successfully! Proceeding...{reset}")
            break
        else:
            print(f"{red}ERROR{reset}: Invalid token. Try again.")

    register("MAVIS Ultra")

def login():
    print("\nLogin\n-----")
    username_or_email = input(f"{blue}Username or Email{reset}:").strip()
    password = getpass.getpass(f"{blue}Password{reset}:")
    users = load_users()

    for username, data in users.items():
        if username_or_email in [username, data["email"]] and check_password(data["password"], password):
            greeting = f"{green}Welcome MAVIS Ultra User: {username}!{reset}" if data.get("user_type") == "MAVIS Ultra" else f"Welcome {username}!"
            print(greeting)
            exit()

    print(f"{red}ERROR{reset}: Incorrect login details!")

def main():
    tokens = load_tokens()
    if not tokens:
        print(f"{red}ERROR{reset}: No token found. You cannot use this software.")
        return

    while True:
        print("\nOptions:\n [1] Login\n [2] Register\n [3] Register as MAVIS Ultra user")
        choice = input("Selection [1/2/3]:").strip()

        if choice == "1":
            login()
        elif choice == "2":
            register("Standard")
        elif choice == "3":
            register_mavis_ultra()
        else:
            print(f"{red}ERROR{reset}: Invalid selection!")

if __name__ == "__main__":
    main()
