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
#include <cstdio>
#include <array>

// OpenSSL für SHA256 (optional: zur Dateiintegritätsprüfung)
#include <openssl/sha.h>

#ifdef _WIN32
    #include <windows.h>
    #define popen _popen
    #define pclose _pclose
#else
    #include <unistd.h>
#endif

namespace fs = std::filesystem;

// ANSI-Farbdefinitionen für Konsolenausgaben
const std::string RED     = "\033[91m";
const std::string GREEN   = "\033[92m";
const std::string YELLOW  = "\033[93m";
const std::string BLUE    = "\033[94m";
const std::string MAGENTA = "\033[95m";
const std::string CYAN    = "\033[96m";
const std::string WHITE   = "\033[97m";
const std::string RESET   = "\033[0m";
const std::string BOLD    = "\033[1m";

// Kritische Sicherheitsvariablen – diese werden später in der .env-Datei gesucht
const std::vector<std::string> CRITICAL_VARS = {
    "SECRET_KEY", "DB_PASSWORD", "API_KEY", "JWT_SECRET", "EMAIL_PASSWORD", "DEBUG",
    "ALLOWED_HOSTS", "DATABASE_URL", "REDIS_URL", "CELERY_BROKER_URL", "LOG_LEVEL",
    "SSL_CERT_PATH", "SSL_KEY_PATH", "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET",
    "S3_BUCKET_NAME", "S3_ACCESS_KEY", "S3_SECRET_KEY", "SENDGRID_API_KEY",
    "GITHUB_TOKEN", "TWITTER_API_KEY", "TWITTER_API_SECRET"
};

// Bekannte bösartige IPs und verdächtige Ports (Beispieldaten – bitte anpassen)
const std::vector<std::string> KNOWN_MALICIOUS_IPS = {"192.168.1.100", "203.0.113.5"};
const std::vector<int> SUSPICIOUS_PORTS = {22, 23, 25, 3306, 3389};
const int MAX_CONNECTIONS_FROM_SAME_IP = 10;

// Logger-Klasse: Singleton mit thread-sicherer Konsolen- und Dateiausgabe
class Logger {
public:
    static Logger& getInstance() {
        static Logger instance;
        return instance;
    }

    void setLogFile(const std::string &filename) {
        std::lock_guard<std::mutex> lock(mtx);
        logfile.open(filename, std::ios::app);
        if (!logfile.is_open()) {
            std::cerr << RED << "ERROR: Could not open log file: " << filename << RESET << std::endl;
        }
    }

    void log(const std::string &level, const std::string &message) {
        std::lock_guard<std::mutex> lock(mtx);
        std::string timestamp = getTimestamp();
        std::string logMessage = timestamp + " " + level + ": " + message;
        std::cout << logMessage << std::endl;
        if (logfile.is_open())
            logfile << logMessage << std::endl;
    }

private:
    std::mutex mtx;
    std::ofstream logfile;
    Logger() {}
    ~Logger() { if (logfile.is_open()) logfile.close(); }
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

// Hilfsfunktion zum Trimmen von Strings (Entfernen von Leerzeichen und Anführungszeichen)
std::string trim(const std::string &s) {
    const std::string whitespace = " \t\"";
    size_t start = s.find_first_not_of(whitespace);
    if (start == std::string::npos)
        return "";
    size_t end = s.find_last_not_of(whitespace);
    return s.substr(start, end - start + 1);
}

// Führt einen Systembefehl aus und gibt dessen Ausgabe als String zurück.
std::string execCommand(const std::string &cmd) {
    std::array<char, 128> buffer;
    std::string result;
    FILE *pipe = popen(cmd.c_str(), "r");
    if (!pipe) {
        Logger::getInstance().log("ERROR", RED + "execCommand: popen() failed!" + RESET);
        return "";
    }
    while (fgets(buffer.data(), buffer.size(), pipe) != nullptr) {
        result += buffer.data();
    }
    pclose(pipe);
    return result;
}

// Lädt eine .env-Datei und setzt die darin enthaltenen Variablen ins Environment.
// Der Pfad zur .env-Datei wird plattformabhängig ermittelt.
std::string loadEnvFile() {
    std::string homeDir;
#ifdef _WIN32
    char* home = getenv("USERPROFILE");
#else
    char* home = getenv("HOME");
#endif
    if (!home)
        throw std::runtime_error("No HOME directory found!");
    homeDir = home;

    // Beispielhafter Pfad – bitte anpassen
#ifdef _WIN32
    std::string envPath = homeDir + "\\PycharmProjects\\MAVIS\\.env";
#else
    std::string envPath = homeDir + "/PycharmProjects/MAVIS/.env";
#endif

    if (!fs::exists(envPath)) {
        Logger::getInstance().log("WARNING", YELLOW + "No .env file found: " + envPath + RESET);
        return "";
    }

    std::ifstream envFile(envPath);
    if (!envFile.is_open())
        throw std::runtime_error("Error opening .env file: " + envPath);

    std::string line;
    while (std::getline(envFile, line)) {
        if (line.empty() || line[0] == '#')
            continue;
        size_t eqPos = line.find('=');
        if (eqPos != std::string::npos) {
            std::string key = trim(line.substr(0, eqPos));
            std::string value = trim(line.substr(eqPos + 1));
            if (!key.empty()) {
    #ifdef _WIN32
                std::string envSetting = key + "=" + value;
                _putenv(envSetting.c_str());
    #else
                setenv(key.c_str(), value.c_str(), 1);
    #endif
            }
        }
    }
    Logger::getInstance().log("INFO", GREEN + ".env-Datei successfully loaded." + RESET);
    return envPath;
}

// Gibt alle Dateien in einem Verzeichnis (rekursiv) aus und zählt sie.
size_t listFilesForScan(const std::string &directory) {
    size_t fileCount = 0;
    Logger::getInstance().log("INFO", BLUE + "Files to scan into: " + directory + RESET);
    try {
        for (auto &p : fs::recursive_directory_iterator(directory)) {
            if (fs::is_regular_file(p.path())) {
                std::cout << "   - " << p.path().string() << std::endl;
                ++fileCount;
            }
        }
    } catch (const std::exception &e) {
        Logger::getInstance().log("ERROR", RED + "Error browsing directory: " + std::string(e.what()) + RESET);
    }
    return fileCount;
}

// Führt einen Sicherheits-Scan der Dateien in einem Verzeichnis durch.
// Unter Windows wird Windows Defender (über PowerShell) aufgerufen,
// während unter Linux ein ClamAV-Scan mittels 'clamscan' (wenn installiert) versucht wird.
size_t scanWithDefender(const std::string &directory) {
    size_t totalFiles = listFilesForScan(directory);
#ifdef _WIN32
    Logger::getInstance().log("INFO", BLUE + "Start Windows Defender Scan in the directory: " + directory + RESET);
    std::string command = "powershell -Command \"Start-MpScan -ScanType CustomScan -ScanPath '" + directory + "'\"";
#else
    Logger::getInstance().log("INFO", BLUE + "Start ClamAV Scan in the directory: " + directory + RESET);
    // clamscan wird verwendet – bitte sicherstellen, dass es installiert ist
    std::string command = "clamscan -r " + directory;
#endif

    try {
        std::string result = execCommand(command);
        if (!result.empty()) {
            std::cout << result << std::endl;
            Logger::getInstance().log("INFO", "Scan-Result: " + result);
        } else {
            std::cout << GREEN << "No threats found." << RESET << std::endl;
            Logger::getInstance().log("INFO", "No threats found.");
        }
    } catch (const std::exception &e) {
        Logger::getInstance().log("ERROR", RED + "Scan failed: " + std::string(e.what()) + RESET);
    }
    return totalFiles;
}

// Überprüft den Firewall-Status. Unter Windows wird 'netsh advfirewall' verwendet,
// unter Linux wird versucht, den Status von 'ufw' auszulesen.
void checkFirewallStatus() {
    Logger::getInstance().log("INFO", BLUE + "Check firewall status..." + RESET);
#ifdef _WIN32
    std::string command = "netsh advfirewall show allprofiles";
#else
    std::string command = "ufw status";
#endif
    try {
        std::string output = execCommand(command);
        if (output.find("State") != std::string::npos || output.find("active") != std::string::npos) {
            std::cout << GREEN << "Firewall is enabled." << RESET << std::endl;
            Logger::getInstance().log("INFO", "Firewall is enabled.");
        } else {
            std::cout << RED << "Firewall is NOT enabled." << RESET << std::endl;
            Logger::getInstance().log("WARNING", "Firewall is NOT enabled.");
        }
    } catch (const std::exception &e) {
        Logger::getInstance().log("ERROR", RED + "Firewall check error: " + std::string(e.what()) + RESET);
    }
}

// Überprüft laufende Prozesse auf verdächtige Namen und Ressourcen-Nutzung.
// Die Funktion nutzt plattformabhängige Kommandos: Windows 'tasklist /FO CSV' oder Linux 'ps'.
void checkSuspiciousProcesses() {
    Logger::getInstance().log("INFO", BLUE + "Check ongoing processes for suspicion..." + RESET);
    std::vector<std::string> suspiciousProcesses = {
        "cmd.exe", "powershell.exe", "netstat.exe", "whois.exe",
        "python.exe", "java.exe", "wget.exe", "curl.exe", "nc.exe", "nmap.exe"
    };

#ifdef _WIN32
    std::string command = "tasklist /FO CSV";
#else
    std::string command = "ps -eo pid,comm,%cpu,%mem";
#endif

    std::string result = execCommand(command);
    std::istringstream iss(result);
    std::string line;
    while (std::getline(iss, line)) {
        for (const auto &suspProc : suspiciousProcesses) {
            if (line.find(suspProc) != std::string::npos) {
                std::cout << YELLOW << "Suspicious process found: " << line << RESET << std::endl;
                Logger::getInstance().log("WARNING", "Suspicious process: " + line);
            }
        }
    }
    std::cout << GREEN << "Process review completed." << RESET << std::endl;
}

// Überprüft aktive Netzwerkverbindungen mittels 'netstat' und wertet verdächtige Aktivitäten aus.
void checkNetworkConnections() {
    Logger::getInstance().log("INFO", BLUE + "Check active network connections..." + RESET);
#ifdef _WIN32
    std::string command = "netstat -an";
#else
    std::string command = "netstat -an";
#endif
    std::string netOutput = execCommand(command);
    std::istringstream iss(netOutput);
    std::string line;
    // HashMap-ähnliche Zählung (IP -> Anzahl Verbindungen)
    std::unordered_map<std::string, int> ipCount;
    while (std::getline(iss, line)) {
        if (line.find("ESTABLISHED") != std::string::npos) {
            // Einfache Extraktion, evtl. mit Regex verbessern
            std::regex ipRegex("([0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)");
            std::smatch matches;
            if (std::regex_search(line, matches, ipRegex)) {
                std::string ip = matches[0];
                ipCount[ip]++;
                // Überprüfe bekannte bösartige IPs
                if (std::find(KNOWN_MALICIOUS_IPS.begin(), KNOWN_MALICIOUS_IPS.end(), ip) != KNOWN_MALICIOUS_IPS.end()) {
                    std::cout << RED << "Warnung: Connection to known malicious IP: " << ip << RESET << std::endl;
                    Logger::getInstance().log("WARNING", "Malicious IP detected: " + ip);
                }
                // DDoS-Schutz: zu viele Verbindungen von derselben IP
                if (ipCount[ip] > MAX_CONNECTIONS_FROM_SAME_IP) {
                    std::cout << RED << "Possible DDoS attack: " << ip << " has " << ipCount[ip]
                              << " Connections." << RESET << std::endl;
                    Logger::getInstance().log("WARNING", "DDoS attack suspected at IP: " + ip);
                }
            }
        }
    }
    std::cout << GREEN << "Network connection check completed." << RESET << std::endl;
}

// Liest (bei Linux) oder ruft (bei Windows) die letzten Sicherheitslogs ab.
void checkSecurityLogs() {
    Logger::getInstance().log("INFO", BLUE + "Check security-relevant logs..." + RESET);
#ifdef _WIN32
    // Windows: Verwende wevtutil, um die letzten 50 Security-Events zu extrahieren.
    std::string command = "wevtutil qe Security /c:50 /f:text";
    std::string logs = execCommand(command);
    std::cout << logs << std::endl;
    Logger::getInstance().log("INFO", "Security logs (Windows) retrieved.");
#else
    // Linux: /var/log/auth.log als Beispiel (muss ggf. angepasst werden)
    std::string logFile = "/var/log/auth.log";
    if (fs::exists(logFile)) {
        std::ifstream infile(logFile);
        if (infile.is_open()) {
            std::string allLines, line;
            // Lese die gesamte Datei – alternativ kann man die letzten 50 Zeilen speichern
            while (std::getline(infile, line)) {
                allLines += line + "\n";
            }
            std::cout << allLines << std::endl;
            Logger::getInstance().log("INFO", "Security logs from " + logFile + " retrieved.");
        } else {
            Logger::getInstance().log("WARNING", "Log file " + logFile + " could not be opened.");
        }
    } else {
        Logger::getInstance().log("WARNING", "Log file " + logFile + " not found.");
    }
#endif
}

// Überprüft Systemdateiberechtigungen in einem definierten Verzeichnis.
// Hier wird rekursiv jedes Dateiattribut abgefragt und protokolliert.
void checkSystemPermissions(const std::string &directory) {
    Logger::getInstance().log("INFO", BLUE + "Check file permissions in: " + directory + RESET);
    try {
        for (auto &p : fs::recursive_directory_iterator(directory)) {
            if (fs::is_regular_file(p.path())) {
                auto perms = fs::status(p.path()).permissions();
                // Beispiel: Wenn die Datei "world writable" ist
                if ((perms & fs::perms::others_write) != fs::perms::none) {
                    std::cout << YELLOW << "Warning: Excessive permissions for: "
                              << p.path().string() << RESET << std::endl;
                    Logger::getInstance().log("WARNING", "Excessive file permissions: " + p.path().string());
                }
            }
        }
    } catch (const std::exception &e) {
        Logger::getInstance().log("ERROR", RED + "Authorization check error: " + std::string(e.what()) + RESET);
    }
}

// Extrahiert aus den kritischen Umgebungsvariablen potentielle Pfade (lokal oder URLs)
std::vector<std::string> extractPathsFromEnv() {
    std::vector<std::string> paths;
    for (const auto &var : CRITICAL_VARS) {
        const char* value = getenv(var.c_str());
        if (value) {
            std::string valStr(value);
            if (fs::exists(valStr)) {
                paths.push_back(valStr);
            } else if (valStr.rfind("http", 0) == 0) {
                std::cout << BLUE << "URL found for " << var << ": " << valStr << RESET << std::endl;
                Logger::getInstance().log("INFO", "URL in " + var + ": " + valStr);
            }
        }
    }
    return paths;
}

// Führt den gesamten Sicherheits-Scan aus, indem alle vorher implementierten Prüfungen aufgerufen werden.
void scanAllFiles() {
    std::string envPath = loadEnvFile(); // .env laden
    std::string baseDir;
    if (!envPath.empty())
        baseDir = fs::path(envPath).parent_path().string();
    else
        throw std::runtime_error("No .env file found, scan aborted.");

    Logger::getInstance().log("INFO", BOLD + "Start comprehensive security check..." + RESET);

    // Systemberechtigungen prüfen
    checkSystemPermissions(baseDir);

    // Zunächst das Basisverzeichnis und zusätzlich in den Umgebungsvariablen angegebene Pfade
    std::vector<std::string> pathsToScan;
    pathsToScan.push_back(baseDir);
    std::vector<std::string> envPaths = extractPathsFromEnv();
    pathsToScan.insert(pathsToScan.end(), envPaths.begin(), envPaths.end());

    size_t totalFilesScanned = 0;
    for (const auto &path : pathsToScan) {
        if (fs::exists(path)) {
            if (fs::is_directory(path)) {
                std::cout << BLUE << "Scan directory: " << path << RESET << std::endl;
                totalFilesScanned += scanWithDefender(path);
            } else if (fs::is_regular_file(path)) {
                std::cout << BLUE << "Scan file: " << path << RESET << std::endl;
                totalFilesScanned += scanWithDefender(path);
            } else {
                std::cout << MAGENTA << "Skip (not file/directory): " << path << RESET << std::endl;
            }
        }
    }
    std::cout << GREEN << "Total scanned files: " << totalFilesScanned << RESET << std::endl;

    // Zusätzliche Sicherheitsprüfungen
    checkFirewallStatus();
    checkSuspiciousProcesses();
    checkNetworkConnections();
    checkSecurityLogs();

    Logger::getInstance().log("INFO", GREEN + "Security check completed!" + RESET);
}

// Signal-Handler für einen sauberen Shutdown
std::atomic<bool> running(true);
void signalHandler(int signum) {
    Logger::getInstance().log("INFO", YELLOW + "Interrupt signal (" + std::to_string(signum) + ") received. End..." + RESET);
    running = false;
}

int main() {
    try {
        // Optional: Log-Datei konfigurieren
        Logger::getInstance().setLogFile("security_scan.log");

        // Registrierung der Signal-Handler
        std::signal(SIGINT, signalHandler);
        std::signal(SIGTERM, signalHandler);

        // Starte den vollständigen Scan
        scanAllFiles();

        // Halte das Programm aktiv, falls asynchrone Prozesse laufen
        while (running) {
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
        Logger::getInstance().log("INFO", GREEN + "Program ended." + RESET);
    } catch (const std::exception &e) {
        Logger::getInstance().log("ERROR", RED + "Critical error: " + std::string(e.what()) + RESET);
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
