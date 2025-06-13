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
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <regex>
#include <filesystem>
#include <cstdlib>
#include <thread>
#include <chrono>
#include <mutex>
#include <iomanip>
#include <ctime>
#include <stdexcept>
#include <atomic>
#include <csignal>
#include <openssl/sha.h>
#include <cstdio>
#include <memory>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

namespace fs = std::filesystem;

// ANSI-Farbdefinitionen (für Konsolenoutput)
const std::string GREEN   = "\033[92m";
const std::string RED     = "\033[91m";
const std::string YELLOW  = "\033[93m";
const std::string BLUE    = "\033[94m";
const std::string RESET   = "\033[0m";

// Kritische Sicherheitsvariablen und schwache Passwortelemente
const std::vector<std::string> CRITICAL_VARS = {
    "SECRET_KEY", "DB_PASSWORD", "API_KEY", "JWT_SECRET",
    "EMAIL_PASSWORD", "DEBUG", "ALLOWED_HOSTS", "DATABASE_URL",
    "REDIS_URL", "CELERY_BROKER_URL", "LOG_LEVEL", "SSL_CERT_PATH",
    "SSL_KEY_PATH", "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET",
    "S3_BUCKET_NAME", "S3_ACCESS_KEY", "S3_SECRET_KEY",
    "SENDGRID_API_KEY", "GITHUB_TOKEN", "TWITTER_API_KEY",
    "TWITTER_API_SECRET"
};

const std::vector<std::string> WEAK_PATTERNS = {
    "1234", "password", "test", "admin", "secret", "abc123",
    "letmein", "12345", "123456", "qwerty", "password1",
    "1q2w3e4r", "welcome", "123123", "root", "admin123",
    "football", "iloveyou", "123qwe", "changeme", "welcome1",
    "123321", "password123", "1password", "1234abcd",
    "111111", "123", "123abc", "letmein1", "newpassword",
    "passw0rd", "guest", "password1234", "987654321", "1qaz2wsx"
};

// Utility: String-Trimming-Funktionen
std::string trim(const std::string &s) {
    const std::string whitespace = " \t\"";
    size_t start = s.find_first_not_of(whitespace);
    if (start == std::string::npos)
        return "";
    size_t end = s.find_last_not_of(whitespace);
    return s.substr(start, end - start + 1);
}

// Logger-Klasse: Singleton mit thread-sicherer und optionaler Dateiausgabe
class Logger {
public:
    static Logger& getInstance() {
        static Logger instance;
        return instance;
    }

    // Setze optional eine Log-Datei (sollte vor Verwendung gesetzt werden)
    void setLogFile(const std::string &filename) {
        std::lock_guard<std::mutex> lock(mtx);
        logfile.open(filename, std::ios::app);
        if (!logfile) {
            std::cerr << "ERROR: Could not open log file: " << filename << std::endl;
        }
    }

    void log(const std::string &level, const std::string &message) {
        std::lock_guard<std::mutex> lock(mtx);
        std::string timestamp = getTimestamp();
        std::string logMessage = timestamp + " " + level + ": " + message;
        // Ausgabe in Konsole
        std::cout << logMessage << std::endl;
        // Ausgabe in Datei, falls aktiviert
        if (logfile)
            logfile << logMessage << std::endl;
    }

private:
    std::mutex mtx;
    std::ofstream logfile;
    Logger() {}
    ~Logger() {
        if (logfile.is_open())
            logfile.close();
    }
    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;

    std::string getTimestamp() {
        std::time_t now = std::time(nullptr);
        std::tm tm_now;
#ifdef _WIN32
        localtime_s(&tm_now, &now);
#else
        localtime_r(&now, &tm_now);
#endif
        std::ostringstream oss;
        oss << std::put_time(&tm_now, "[%Y-%m-%d %H:%M:%S]");
        return oss.str();
    }
};

// Liefert den Pfad zur .env-Datei im Home-Verzeichnis
std::string getEnvFilePath() {
#ifdef _WIN32
    const char* home = getenv("USERPROFILE");
#else
    const char* home = getenv("HOME");
#endif
    if (!home) {
        throw std::runtime_error("No HOME directory found!");
    }
    // Der Pfad kann hier bei Bedarf angepasst werden
    return std::string(home) + "/PycharmProjects/MAVIS/.env";
}

// Laden der .env-Datei und Setzen der Umgebungsvariablen
void loadEnvFile(const std::string& path) {
    if (!fs::exists(path)) {
        Logger::getInstance().log("WARNING", RED + "Keine .env-Datei gefunden." + RESET);
        return;
    }
    std::ifstream envFile(path);
    if (!envFile.is_open()) {
        throw std::runtime_error("Error opening .env file.");
    }
    std::string line;
    while (std::getline(envFile, line)) {
        if (line.empty() || line[0] == '#')
            continue;
        size_t eq = line.find('=');
        if (eq != std::string::npos) {
            std::string key = trim(line.substr(0, eq));
            std::string value = trim(line.substr(eq + 1));
            if (!key.empty()) {
                setenv(key.c_str(), value.c_str(), 1);
            }
        }
    }
    Logger::getInstance().log("INFO", GREEN + ".env-Datei successfully loaded." + RESET);
}

// Überprüfung der kritischen Umgebungsvariablen auf Existenz und schwache Muster
void checkEnvSecurity() {
    Logger::getInstance().log("INFO", BLUE + "Checking the .env security variables" + RESET);
    for (const auto& var : CRITICAL_VARS) {
        const char* value = getenv(var.c_str());
        if (!value) {
            Logger::getInstance().log("ERROR", RED + var + " is not set!" + RESET);
        } else {
            std::string valStr(value);
            // Mindestlänge prüfen, falls sinnvoll
            if (valStr.size() < 8) {
                Logger::getInstance().log("WARNING", YELLOW + var + " may be too short!" + RESET);
            }
            // Überprüfung auf schwache Muster
            for (const auto& pattern : WEAK_PATTERNS) {
                try {
                    if (std::regex_search(valStr, std::regex(pattern, std::regex::icase))) {
                        Logger::getInstance().log("WARNING", YELLOW + var + " uses a weak pattern (" + pattern + ")!" + RESET);
                        break;
                    }
                } catch (const std::regex_error& e) {
                    Logger::getInstance().log("ERROR", RED + "Regex error in " + var + ": " + e.what() + RESET);
                }
            }
        }
    }
}

// Sichere und speichereffiziente SHA-256-Berechnung in Blöcken
std::string computeSHA256(const std::string& filePath) {
    const size_t BUF_SIZE = 1 << 12; // 4KB-Buffer
    std::ifstream file(filePath, std::ios::binary);
    if (!file.is_open()) {
        throw std::runtime_error("Error opening file for SHA256 calculation.");
    }

    SHA256_CTX ctx;
    if (SHA256_Init(&ctx) != 1) {
        throw std::runtime_error("SHA256_Init failed.");
    }

    std::vector<char> buffer(BUF_SIZE);
    while (file.good()) {
        file.read(buffer.data(), BUF_SIZE);
        std::streamsize bytesRead = file.gcount();
        if (bytesRead > 0) {
            if (SHA256_Update(&ctx, buffer.data(), bytesRead) != 1) {
                throw std::runtime_error("SHA256_Update failed.");
            }
        }
    }
    unsigned char hash[SHA256_DIGEST_LENGTH];
    if (SHA256_Final(hash, &ctx) != 1) {
        throw std::runtime_error("SHA256_Final failed.");
    }
    std::ostringstream result;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        result << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(hash[i]);
    }
    return result.str();
}

// Prüfung der .env-Datei-Integrität anhand des SHA-256-Hashes
void checkEnvIntegrity(const std::string& path) {
    Logger::getInstance().log("INFO", BLUE + "Performing the .env integrity check" + RESET);
    if (!fs::exists(path)) {
        Logger::getInstance().log("ERROR", RED + ".env file not found!" + RESET);
        return;
    }
    try {
        std::string hash = computeSHA256(path);
        Logger::getInstance().log("INFO", "SHA256: " + hash);
    } catch (const std::exception &e) {
        Logger::getInstance().log("ERROR", RED + std::string("SHA256 calculation failed:") + e.what() + RESET);
    }
}

// Stub für zukünftige Checks (z. B. Paket-Updates, Netzwerkverbindungen usw.)
void checkExternalDependencies() {
    Logger::getInstance().log("INFO", BLUE + "Checking external dependencies (stub)" + RESET);
    // Hier können systemnahe Aufrufe mit strenger Timeout-Kontrolle und erweitertem Fehlerhandling implementiert werden
}

// File Monitor (Polling-Lösung) für die .env-Datei in einem separaten Thread
class EnvFileMonitor {
public:
    EnvFileMonitor(const std::string &path, unsigned int pollIntervalMs = 1000)
        : envPath(path), intervalMs(pollIntervalMs), stopMonitoring(false) {
        if (!fs::exists(envPath)) {
            throw std::runtime_error(".env file does not exist for monitoring.");
        }
        lastHash = computeSHA256(envPath);
    }

    void start() {
        monitorThread = std::thread(&EnvFileMonitor::monitor, this);
    }

    void stop() {
        stopMonitoring = true;
        if (monitorThread.joinable()) {
            monitorThread.join();
        }
    }

    ~EnvFileMonitor() {
        stop();
    }

private:
    std::string envPath;
    std::string lastHash;
    unsigned int intervalMs;
    std::atomic<bool> stopMonitoring;
    std::thread monitorThread;

    void monitor() {
        while (!stopMonitoring) {
            std::this_thread::sleep_for(std::chrono::milliseconds(intervalMs));
            try {
                if (fs::exists(envPath)) {
                    std::string currentHash = computeSHA256(envPath);
                    if (currentHash != lastHash) {
                        Logger::getInstance().log("WARNING", RED + ".env file has been modified!" + RESET);
                        lastHash = currentHash;
                    }
                } else {
                    Logger::getInstance().log("ERROR", RED + ".env file was deleted!" + RESET);
                }
            } catch (const std::exception &e) {
                Logger::getInstance().log("ERROR", RED + std::string("Monitor error: ") + e.what() + RESET);
            }
        }
    }
};

// Fortschrittsbalken als zusätzliche visuelle Rückmeldung (optional, thread-sicher)
void displayLoadingBar(unsigned int durationSeconds = 5, const std::string& message = BLUE + "Running Security Check" + RESET) {
    const int barLength = 50;
    auto start = std::chrono::steady_clock::now();
    while (true) {
        auto now = std::chrono::steady_clock::now();
        double elapsed = std::chrono::duration<double>(now - start).count();
        int progress = static_cast<int>((elapsed / durationSeconds) * 100);
        if (progress > 100) progress = 100;
        int pos = (barLength * progress) / 100;
        std::cout << "\r" << message << " [";
        for (int i = 0; i < barLength; ++i) {
            std::cout << (i < pos ? "█" : "-");
        }
        std::cout << "] " << progress << "%" << std::flush;
        if (progress >= 100) break;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    std::cout << std::endl;
}

// Signal-Handling für einen sauberen Shutdown
std::atomic<bool> running(true);
void signalHandler(int signal) {
    Logger::getInstance().log("INFO", YELLOW + "Interrupt signal (" + std::to_string(signal) + ") received. End..." + RESET);
    running = false;
}

int main() {
    try {
        // Konfiguration der optionalen Log-Datei (Passe den Pfad bei Bedarf an)
        Logger::getInstance().setLogFile("security_check.log");

        // Registrierung der Signal-Handler für sauberen Abbruch
        std::signal(SIGINT, signalHandler);
        std::signal(SIGTERM, signalHandler);

        std::string envPath = getEnvFilePath();

        // Sicherheitschecks in definierten Schritten
        loadEnvFile(envPath);
        checkEnvSecurity();
        checkEnvIntegrity(envPath);
        checkExternalDependencies();

        // Starte den Datei-Monitor in einem Hintergrund-Thread
        EnvFileMonitor monitor(envPath);
        monitor.start();

        // Optionale visuelle Rückmeldung mittels Fortschrittsbalken
        displayLoadingBar(5);

        Logger::getInstance().log("INFO", GREEN + "Security check successfully completed!" + RESET);

        // Hauptschleife: Halte das Programm aktiv, bis ein Abbruchsignal empfangen wird.
        while (running) {
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    } catch (const std::exception &e) {
        Logger::getInstance().log("ERROR", RED + std::string("Exception occurred: ") + e.what() + RESET);
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
