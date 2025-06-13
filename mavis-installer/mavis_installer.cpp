/*
   Englisch | Peharge: This source code is released under the MIT License.

   Usage Rights:
   The source code may be copied, modified, and adapted to individual requirements.
   Users are permitted to use this code in their own projects, both for private and commercial purposes.
   However, it is recommended to modify the code only if you have sufficient programming knowledge,
   as changes could cause unintended errors or security risks.

   Dependencies and Additional Frameworks:
   The code relies on the use of various frameworks and executes additional files.
   Some of these files may automatically install further dependencies required for functionality.
   It is strongly recommended to perform installation and configuration in an isolated environment
   (e.g., a virtual environment) to avoid potential conflicts with existing software installations.

   Disclaimer:
   Use of the code is entirely at your own risk.
   Peharge assumes no liability for damages, data loss, system errors, or other issues
   that may arise directly or indirectly from the use, modification, or redistribution of the code.

   Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.
*/

/*
   Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.

   Nutzungsrechte:
   Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
   Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
   Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
   da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.

   Abhängigkeiten und zusätzliche Frameworks:
   Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
   Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
   Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
   um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.

   Haftungsausschluss:
   Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
   Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
   die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.

   Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.
*/

/*
   Français | Peharge: Ce code source est publié sous la licence MIT.

   Droits d'utilisation:
   Le code source peut être copié, édité et adapté aux besoins individuels.
   Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
   Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
   car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.

   Dépendances et frameworks supplémentaires:
   Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
   Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
   Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
   pour éviter d'éventuels conflits avec les installations de logiciels existantes.

   Clause de non-responsabilité:
   L'utilisation du code est entièrement à vos propres risques.
   Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
   pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.

   Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.
*/

#include <iostream>
#include <cstdlib>
#include <filesystem>
#include <string>
#include <fstream>
#include <thread>
#include <chrono>

#ifdef _WIN32
#include <windows.h>
#define CLEAR_SCREEN "cls"
#else
#include <unistd.h>
#define CLEAR_SCREEN "clear"
#endif

namespace fs = std::filesystem;

// Hilfsfunktionen
void clearScreen() {
    std::system(CLEAR_SCREEN);
}

bool isCommandAvailable(const std::string& command) {
#ifdef _WIN32
    std::string checkCmd = "where " + command + " >nul 2>nul";
#else
    std::string checkCmd = "command -v " + command + " >/dev/null 2>&1";
#endif
    return std::system(checkCmd.c_str()) == 0;
}

bool isDirectoryWritable(const std::string& path) {
    std::string testFile = path + "/.test_write";
    std::ofstream ofs(testFile);
    bool writable = ofs.is_open();
    if (writable) {
        ofs.close();
        fs::remove(testFile);
    }
    return writable;
}

void runCommand(const std::string& command, const std::string& errorMessage = "", int retries = 3, int delay = 5) {
    int attempt = 0;
    int result = -1;
    while (attempt < retries) {
        result = std::system(command.c_str());
        if (result == 0) {
            break;
        }
        std::cerr << "Attempt " << (attempt + 1) << " failed: " << errorMessage << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(delay)); // Verzögerung zwischen den Versuchen
        attempt++;
    }
    if (result != 0) {
        std::cerr << "❌ Critical error: " << errorMessage << std::endl;
        std::cerr << "Command: " << command << std::endl;
        exit(EXIT_FAILURE);
    }
}

bool checkInternetConnectivity() {
#ifdef _WIN32
    return std::system("ping -n 1 google.com >nul 2>nul") == 0;
#else
    return std::system("ping -c 1 google.com >/dev/null 2>&1") == 0;
#endif
}

// Installationsfunktionen
void installGit() {
    if (isCommandAvailable("git")) {
        std::cout << "✅ Git is already installed." << std::endl;
        return;
    }
    std::cout << "🔄 Installing Git..." << std::endl;
#ifdef _WIN32
    runCommand("winget install --id Git.Git -e --source winget", "Git installation failed. Visit https://git-scm.com.");
#elif __APPLE__
    runCommand("brew install git", "Git installation failed. Visit https://git-scm.com.");
#else
    runCommand("sudo apt update && sudo apt install -y git", "Git installation failed. Visit https://git-scm.com.");
#endif
    std::cout << "✅ Git installed successfully." << std::endl;
}

void installPython() {
    if (isCommandAvailable("python3")) {
        std::cout << "✅ Python is already installed." << std::endl;
        return;
    }
    std::cout << "🔄 Installing Python..." << std::endl;
#ifdef _WIN32
    runCommand("winget install --id Python.Python.3 -e --source winget", "Python installation failed. Visit https://www.python.org.");
#elif __APPLE__
    runCommand("brew install python", "Python installation failed. Visit https://www.python.org.");
#else
    runCommand("sudo apt update && sudo apt install -y python3 python3-venv", "Python installation failed. Visit https://www.python.org.");
#endif
    std::cout << "✅ Python installed successfully." << std::endl;
}

void installOllama() {
    if (isCommandAvailable("ollama")) {
        std::cout << "✅ Ollama is already installed." << std::endl;
        return;
    }
    std::cout << "🔄 Installing Ollama..." << std::endl;
#ifdef _WIN32
    runCommand("start https://ollama.com/download", "Ollama installation failed. Visit https://ollama.com/download.");
#elif __APPLE__
    runCommand("brew install --cask ollama", "Ollama installation failed. Visit https://ollama.com/download.");
#else
    runCommand("curl -fsSL https://ollama.com/download | sh", "Ollama installation failed. Visit https://ollama.com/download.");
#endif
    std::cout << "✅ Ollama installed successfully." << std::endl;
}

// MAVIS-Installation
void createFolder(const std::string& path) {
    if (!fs::exists(path)) {
        if (!isDirectoryWritable(fs::path(path).parent_path().string())) {
            std::cerr << "❌ Error: No write permissions in the directory: " << path << std::endl;
            exit(EXIT_FAILURE);
        }
        fs::create_directories(path);
        std::cout << "✅ Folder created: " << path << std::endl;
    } else {
        std::cout << "ℹ️ Folder already exists: " << path << std::endl;
    }
}

void cloneRepository(const std::string& repoUrl, const std::string& targetPath) {
    if (fs::exists(targetPath)) {
        std::cout << "ℹ️ Repository has already been cloned." << std::endl;
        return;
    }
    std::cout << "🔄 Cloning repository..." << std::endl;
    std::string command = "git clone " + repoUrl + " " + targetPath;
    runCommand(command, "Repository could not be cloned.");
    std::cout << "✅ Repository successfully cloned." << std::endl;
}

void createVirtualEnvironment(const std::string& envPath) {
    if (fs::exists(envPath)) {
        std::cout << "ℹ️ Virtual environment already exists." << std::endl;
        return;
    }
    std::cout << "🔄 Creating virtual environment..." << std::endl;
#ifdef _WIN32
    std::string command = "python -m venv " + envPath;
#else
    std::string command = "python3 -m venv " + envPath;
#endif
    runCommand(command, "Virtual environment could not be created.");
    std::cout << "✅ Virtual environment created successfully." << std::endl;
}

void startUI(const std::string& scriptName) {
    std::cout << "🚀 Starting User Interface..." << std::endl;
#ifdef _WIN32
    std::string command = scriptName + ".bat";
#else
    std::string command = "./" + scriptName + ".sh";
#endif
    runCommand(command, "User interface could not be started.");
}

void displayMenu() {
    std::cout << "\nMAVIS Installer\n"
              << "=================\n"
              << "1. Install prerequisites (Git, Python, Ollama)\n"
              << "2. Create folder\n"
              << "3. Clone repository\n"
              << "4. Create virtual environment\n"
              << "5. Start user interface\n"
              << "6. Finish\n"
              << "=================\n";
}

int main() {
    std::string basePath;
#ifdef _WIN32
    basePath = "C:\\Users\\" + std::string(getenv("USERNAME")) + "\\PycharmProjects";
#else
    basePath = fs::path(getenv("HOME")) / "PycharmProjects";
#endif
    std::string repoUrl = "https://github.com/Peharge/MAVIS";
    std::string projectPath = basePath + "/MAVIS";
    std::string envPath = projectPath + "/env";

    if (!checkInternetConnectivity()) {
        std::cerr << "❌ Error: No internet connection. Please check your connection." << std::endl;
        return EXIT_FAILURE;
    }

    int choice;
    do {
        clearScreen();
        displayMenu();
        std::cout << "Select an option:";
        std::cin >> choice;

        switch (choice) {
            case 1:
                installGit();
                installPython();
                installOllama();
                break;
            case 2:
                createFolder(basePath);
                break;
            case 3:
                cloneRepository(repoUrl, projectPath);
                break;
            case 4:
                createVirtualEnvironment(envPath);
                break;
            case 5:
                startUI("run-mavis-all");
                break;
            case 6:
                std::cout << "Finishing..." << std::endl;
                break;
            default:
                std::cout << "❌ Invalid input. Please try again." << std::endl;
        }
#ifdef _WIN32
        Sleep(2000);  // 2 Sekunden Verzögerung für Windows
#else
        sleep(2);  // 2 Sekunden Verzögerung für macOS/Linux
#endif
    } while (choice != 6);

    return 0;
}
