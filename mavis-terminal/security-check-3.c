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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <errno.h>
#include <stdarg.h>
#include <signal.h>
#include <ctype.h>
#include <sys/stat.h>
#include <sys/types.h>
#ifdef _WIN32
  #include <windows.h>
  #define popen _popen
  #define pclose _pclose
  #define PATH_SEPARATOR "\\"
#else
  #include <dirent.h>
  #include <pthread.h>
  #include <unistd.h>
  #define PATH_SEPARATOR "/"
#endif

// Falls OpenSSL installiert ist: Für SHA256 (optional)
// #include <openssl/sha.h>

// ANSI-Farbdefinitionen
const char* RED     = "\033[91m";
const char* GREEN   = "\033[92m";
const char* YELLOW  = "\033[93m";
const char* BLUE    = "\033[94m";
const char* MAGENTA = "\033[95m";
const char* CYAN    = "\033[96m";
const char* WHITE   = "\033[97m";
const char* RESET   = "\033[0m";
const char* BOLD    = "\033[1m";

// Kritische Sicherheitsvariablen
const char* CRITICAL_VARS[] = {
    "SECRET_KEY", "DB_PASSWORD", "API_KEY", "JWT_SECRET", "EMAIL_PASSWORD", "DEBUG",
    "ALLOWED_HOSTS", "DATABASE_URL", "REDIS_URL", "CELERY_BROKER_URL", "LOG_LEVEL",
    "SSL_CERT_PATH", "SSL_KEY_PATH", "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET",
    "S3_BUCKET_NAME", "S3_ACCESS_KEY", "S3_SECRET_KEY", "SENDGRID_API_KEY",
    "GITHUB_TOKEN", "TWITTER_API_KEY", "TWITTER_API_SECRET"
};
const size_t NUM_CRITICAL_VARS = sizeof(CRITICAL_VARS)/sizeof(CRITICAL_VARS[0]);

// Bekannte bösartige IPs und verdächtige Ports (Beispieldaten – bitte anpassen)
const char* KNOWN_MALICIOUS_IPS[] = {"192.168.1.100", "203.0.113.5"};
const size_t NUM_MALICIOUS_IPS = sizeof(KNOWN_MALICIOUS_IPS)/sizeof(KNOWN_MALICIOUS_IPS[0]);
// Für verdächtige Ports (hier nur als Beispiel, wird aber im C-Code nicht weiter verwendet)
const int SUSPICIOUS_PORTS[] = {22, 23, 25, 3306, 3389};
const size_t NUM_SUSPICIOUS_PORTS = sizeof(SUSPICIOUS_PORTS)/sizeof(SUSPICIOUS_PORTS[0]);
const int MAX_CONNECTIONS_FROM_SAME_IP = 10;

/*  --- Logger ---  */
#ifdef _WIN32
// Unter Windows können kritische Sektionen statt pthread_mutex_t verwendet werden.
static CRITICAL_SECTION logger_mutex;
#else
#include <pthread.h>
static pthread_mutex_t logger_mutex = PTHREAD_MUTEX_INITIALIZER;
#endif

static FILE *logfile = NULL;

void log_message(const char* level, const char* fmt, ...) {
#ifdef _WIN32
    EnterCriticalSection(&logger_mutex);
#else
    pthread_mutex_lock(&logger_mutex);
#endif

    // Zeitstempel generieren
    char timestamp[64];
    time_t now = time(NULL);
    struct tm tm_now;
#ifdef _WIN32
    localtime_s(&tm_now, &now);
#else
    localtime_r(&now, &tm_now);
#endif
    strftime(timestamp, sizeof(timestamp), "[%Y-%m-%d %H:%M:%S]", &tm_now);

    // Formatierte Nachricht vorbereiten
    char message[1024];
    va_list args;
    va_start(args, fmt);
    vsnprintf(message, sizeof(message), fmt, args);
    va_end(args);

    // Konsolenausgabe
    printf("%s %s: %s\n", timestamp, level, message);

    // In Log-Datei schreiben, falls geöffnet
    if (logfile) {
        fprintf(logfile, "%s %s: %s\n", timestamp, level, message);
        fflush(logfile);
    }

#ifdef _WIN32
    LeaveCriticalSection(&logger_mutex);
#else
    pthread_mutex_unlock(&logger_mutex);
#endif
}

/*  --- Hilfsfunktionen ---  */

// Trimmt führende und nachfolgende Leerzeichen und Anführungszeichen
char* trim(const char* s) {
    if (s == NULL)
        return NULL;
    const char* start = s;
    while(*start && (isspace(*start) || *start == '\"')) start++;
    if(*start == '\0') {
        char* res = malloc(1);
        res[0] = '\0';
        return res;
    }
    const char* end = s + strlen(s) - 1;
    while(end > start && (isspace(*end) || *end == '\"')) end--;
    size_t len = end - start + 1;
    char* ret = malloc(len + 1);
    if(ret) {
        strncpy(ret, start, len);
        ret[len] = '\0';
    }
    return ret;
}

// Führt einen Systembefehl aus und gibt dessen Ausgabe als dynamisch allozierten String zurück.
// Aufrufende Funktion muss das Ergebnis mit free() freigeben.
char* execCommand(const char* cmd) {
    char buffer[128];
    size_t result_size = 1;
    char *result = malloc(result_size);
    if (!result) return NULL;
    result[0] = '\0';

    FILE *pipe = popen(cmd, "r");
    if (!pipe) {
        log_message("ERROR", RED "execCommand: popen() fehlgeschlagen!" RESET);
        free(result);
        return NULL;
    }
    while (fgets(buffer, sizeof(buffer), pipe) != NULL) {
        size_t old_len = strlen(result);
        size_t add_len = strlen(buffer);
        result_size = old_len + add_len + 1;
        result = realloc(result, result_size);
        if (!result) break;
        strcat(result, buffer);
    }
    pclose(pipe);
    return result;
}

/* --- Environment File Laden --- */
#ifdef _WIN32
#define HOME_ENV "USERPROFILE"
#else
#define HOME_ENV "HOME"
#endif

// Überprüft, ob eine Datei existiert
bool file_exists(const char* path) {
    struct stat st;
    return (stat(path, &st) == 0);
}

char* loadEnvFile(void) {
    const char *home = getenv(HOME_ENV);
    if (!home) {
        log_message("ERROR", "Kein HOME-Verzeichnis gefunden!");
        return NULL;
    }
    // Beispielpfad anpassen
#ifdef _WIN32
    size_t len = strlen(home) + strlen("\\PycharmProjects\\MAVIS\\.env") + 1;
    char *envPath = malloc(len);
    snprintf(envPath, len, "%s\\PycharmProjects\\MAVIS\\.env", home);
#else
    size_t len = strlen(home) + strlen("/PycharmProjects/MAVIS/.env") + 1;
    char *envPath = malloc(len);
    snprintf(envPath, len, "%s/PycharmProjects/MAVIS/.env", home);
#endif

    if (!file_exists(envPath)) {
        log_message("WARNING", YELLOW "Keine .env-Datei gefunden: %s" RESET, envPath);
        free(envPath);
        return NULL;
    }
    FILE *fp = fopen(envPath, "r");
    if (!fp) {
        log_message("ERROR", RED "Fehler beim Öffnen der .env-Datei: %s" RESET, envPath);
        free(envPath);
        return NULL;
    }
    char line[1024];
    while (fgets(line, sizeof(line), fp) != NULL) {
        // Zeile trimmen & Zeilenumbrüche entfernen
        char *pos;
        if ((pos = strchr(line, '\n')) != NULL)
            *pos = '\0';
        if (line[0] == '#' || strlen(line) == 0)
            continue;
        char *eq = strchr(line, '=');
        if (eq) {
            *eq = '\0';
            char *key = trim(line);
            char *value = trim(eq + 1);
            if (key && strlen(key) > 0) {
#ifdef _WIN32
                // Unter Windows: _putenv erwartet "key=value"
                size_t envSettingLen = strlen(key) + 1 + strlen(value) + 1;
                char *envSetting = malloc(envSettingLen);
                snprintf(envSetting, envSettingLen, "%s=%s", key, value);
                _putenv(envSetting);
                free(envSetting);
#else
                setenv(key, value, 1);
#endif
            }
            free(key);
            free(value);
        }
    }
    fclose(fp);
    log_message("INFO", GREEN ".env-Datei erfolgreich geladen." RESET);
    return envPath; // Aufrufende Funktion ist für free() verantwortlich.
}

/* --- Rekursive Dateisuche --- */
// Gibt alle Dateien in einem Verzeichnis (rekursiv) aus und zählt sie.
size_t listFilesForScan(const char *directory) {
    size_t fileCount = 0;
    log_message("INFO", BLUE "Dateien in Verzeichnis: %s" RESET, directory);

#ifdef _WIN32
    // Windows-Variante: einfache Implementierung mittels FindFirstFile / FindNextFile
    WIN32_FIND_DATA findFileData;
    char searchPath[MAX_PATH];
    snprintf(searchPath, MAX_PATH, "%s\\*", directory);
    HANDLE hFind = FindFirstFile(searchPath, &findFileData);
    if (hFind == INVALID_HANDLE_VALUE) {
        log_message("ERROR", RED "Verzeichnis %s konnte nicht durchsucht werden." RESET, directory);
        return 0;
    }
    do {
        if (strcmp(findFileData.cFileName, ".") == 0 ||
            strcmp(findFileData.cFileName, "..") == 0)
            continue;
        char fullPath[MAX_PATH];
        snprintf(fullPath, MAX_PATH, "%s\\%s", directory, findFileData.cFileName);
        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            fileCount += listFilesForScan(fullPath);
        } else {
            printf("   - %s\n", fullPath);
            fileCount++;
        }
    } while (FindNextFile(hFind, &findFileData));
    FindClose(hFind);
#else
    DIR *dir = opendir(directory);
    if (!dir) {
        log_message("ERROR", RED "Verzeichnis %s konnte nicht geöffnet werden: %s" RESET, directory, strerror(errno));
        return 0;
    }
    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 ||
            strcmp(entry->d_name, "..") == 0)
            continue;

        char *fullPath;
        size_t path_len = strlen(directory) + strlen(entry->d_name) + 2;
        fullPath = malloc(path_len);
        snprintf(fullPath, path_len, "%s/%s", directory, entry->d_name);

        struct stat st;
        if (stat(fullPath, &st) == 0) {
            if (S_ISDIR(st.st_mode)) {
                fileCount += listFilesForScan(fullPath);
            } else if (S_ISREG(st.st_mode)) {
                printf("   - %s\n", fullPath);
                fileCount++;
            }
        }
        free(fullPath);
    }
    closedir(dir);
#endif
    return fileCount;
}

/* --- Scan-Funktion --- */
// Führt einen Sicherheits-Scan der Dateien in einem Verzeichnis durch.
// Unter Windows wird Windows Defender (über PowerShell) aufgerufen,
// unter Linux ein ClamAV-Scan mittels 'clamscan' (wenn installiert).
size_t scanWithDefender(const char *directory) {
    size_t totalFiles = listFilesForScan(directory);
#ifdef _WIN32
    log_message("INFO", BLUE "Starte Windows Defender Scan im Verzeichnis: %s" RESET, directory);
    // Beispielbefehl: je nach Konfiguration ggf. anpassen
    char command[1024];
    snprintf(command, sizeof(command),
             "powershell -Command \"Start-MpScan -ScanType CustomScan -ScanPath '%s'\"", directory);
#else
    log_message("INFO", BLUE "Starte ClamAV Scan im Verzeichnis: %s" RESET, directory);
    char command[1024];
    snprintf(command, sizeof(command), "clamscan -r %s", directory);
#endif
    char* result = execCommand(command);
    if (result && strlen(result) > 0) {
        printf("%s\n", result);
        log_message("INFO", "Scan-Ergebnis: %s", result);
    } else {
        printf("%sNo threats found.%s\n", GREEN, RESET);
        log_message("INFO", "Keine Bedrohungen gefunden.");
    }
    free(result);
    return totalFiles;
}

/* --- Firewall Status --- */
void checkFirewallStatus(void) {
    log_message("INFO", BLUE "Überprüfe Firewall-Status..." RESET);
#ifdef _WIN32
    const char *command = "netsh advfirewall show allprofiles";
#else
    const char *command = "ufw status";
#endif
    char* output = execCommand(command);
    if (output) {
        if (strstr(output, "State") || strstr(output, "active")) {
            printf("%sFirewall ist aktiviert.%s\n", GREEN, RESET);
            log_message("INFO", "Firewall ist aktiviert.");
        } else {
            printf("%sFirewall ist NICHT aktiviert.%s\n", RED, RESET);
            log_message("WARNING", "Firewall ist NICHT aktiviert.");
        }
        free(output);
    }
}

/* --- Verdächtige Prozesse prüfen --- */
void checkSuspiciousProcesses(void) {
    log_message("INFO", BLUE "Überprüfe laufende Prozesse auf Verdacht..." RESET);
    const char* suspiciousProcesses[] = {
        "cmd.exe", "powershell.exe", "netstat.exe", "whois.exe",
        "python.exe", "java.exe", "wget.exe", "curl.exe", "nc.exe", "nmap.exe"
    };
    const size_t numSuspicious = sizeof(suspiciousProcesses)/sizeof(suspiciousProcesses[0]);
#ifdef _WIN32
    const char *command = "tasklist /FO CSV";
#else
    const char *command = "ps -eo pid,comm,%cpu,%mem";
#endif
    char* result = execCommand(command);
    if (result) {
        char* line = strtok(result, "\n");
        while (line) {
            for (size_t i = 0; i < numSuspicious; i++) {
                if (strstr(line, suspiciousProcesses[i])) {
                    printf("%sVerdächtiger Prozess gefunden: %s%s\n", YELLOW, line, RESET);
                    log_message("WARNING", "Verdächtiger Prozess: %s", line);
                }
            }
            line = strtok(NULL, "\n");
        }
        free(result);
    }
    printf("%sProzessprüfung abgeschlossen.%s\n", GREEN, RESET);
}

/* --- Netzwerkverbindungen prüfen --- */
// Hier wird eine einfache Logik verwendet, um Zeilen mit "ESTABLISHED" zu prüfen und IP-Adressen zu extrahieren.
// Zur Zählung der Verbindungen pro IP wird eine einfache Struktur verwendet.
typedef struct IpCount {
    char ip[32];
    int count;
} IpCount;

#define MAX_IPS 1024

// Extrahiert eine IP-Adresse (einfache Implementierung)
bool extractIp(const char* line, char* ipOut, size_t ipOutSize) {
    // Sucht nach einem Muster: "xxx.xxx.xxx.xxx" (ohne exakte Validierung)
    const char *p = line;
    while (*p) {
        if (isdigit(*p)) {
            int dots = 0;
            const char *start = p;
            while (*p && (isdigit(*p) || *p == '.')) {
                if (*p == '.')
                    dots++;
                p++;
            }
            if (dots == 3 && (size_t)(p - start) < ipOutSize) {
                strncpy(ipOut, start, p - start);
                ipOut[p - start] = '\0';
                return true;
            }
        } else {
            p++;
        }
    }
    return false;
}

void checkNetworkConnections(void) {
    log_message("INFO", BLUE "Überprüfe aktive Netzwerkverbindungen..." RESET);
#ifdef _WIN32
    const char *command = "netstat -an";
#else
    const char *command = "netstat -an";
#endif
    char* netOutput = execCommand(command);
    IpCount ipCounts[MAX_IPS];
    size_t ipCountNum = 0;

    if (netOutput) {
        char* line = strtok(netOutput, "\n");
        while (line) {
            if (strstr(line, "ESTABLISHED")) {
                char ip[32];
                if (extractIp(line, ip, sizeof(ip))) {
                    // Suche, ob diese IP schon vorhanden ist
                    size_t j;
                    bool found = false;
                    for (j = 0; j < ipCountNum; j++) {
                        if (strcmp(ipCounts[j].ip, ip) == 0) {
                            ipCounts[j].count++;
                            found = true;
                            break;
                        }
                    }
                    if (!found && ipCountNum < MAX_IPS) {
                        strncpy(ipCounts[ipCountNum].ip, ip, sizeof(ipCounts[ipCountNum].ip));
                        ipCounts[ipCountNum].count = 1;
                        ipCountNum++;
                    }
                    // Prüfe bösartige IPs
                    for (size_t k = 0; k < NUM_MALICIOUS_IPS; k++) {
                        if (strcmp(ip, KNOWN_MALICIOUS_IPS[k]) == 0) {
                            printf("%sWarnung: Verbindung zu bekannter bösartiger IP: %s%s\n", RED, ip, RESET);
                            log_message("WARNING", "Bösartige IP entdeckt: %s", ip);
                        }
                    }
                }
            }
            line = strtok(NULL, "\n");
        }
        // Überprüfe DDoS: zu viele Verbindungen von derselben IP
        for (size_t i = 0; i < ipCountNum; i++) {
            if (ipCounts[i].count > MAX_CONNECTIONS_FROM_SAME_IP) {
                printf("%sMöglicher DDoS-Angriff: IP %s hat %d Verbindungen.%s\n", RED,
                       ipCounts[i].ip, ipCounts[i].count, RESET);
                log_message("WARNING", "DDoS-Angriff vermutet bei IP: %s", ipCounts[i].ip);
            }
        }
        free(netOutput);
    }
    printf("%sNetzwerkverbindungsprüfung abgeschlossen.%s\n", GREEN, RESET);
}

/* --- Sicherheitslogs abrufen --- */
void checkSecurityLogs(void) {
    log_message("INFO", BLUE "Überprüfe sicherheitsrelevante Logs..." RESET);
#ifdef _WIN32
    const char *command = "wevtutil qe Security /c:50 /f:text";
    char* logs = execCommand(command);
    if (logs) {
        printf("%s\n", logs);
        log_message("INFO", "Security Logs (Windows) abgerufen.");
        free(logs);
    }
#else
    const char* logFile = "/var/log/auth.log";
    if (file_exists(logFile)) {
        FILE *fp = fopen(logFile, "r");
        if (fp) {
            char line[1024];
            char *allLines = NULL;
            size_t totalLen = 0;
            while (fgets(line, sizeof(line), fp)) {
                size_t lineLen = strlen(line);
                allLines = realloc(allLines, totalLen + lineLen + 1);
                strcpy(allLines + totalLen, line);
                totalLen += lineLen;
            }
            fclose(fp);
            if (allLines) {
                printf("%s\n", allLines);
                log_message("INFO", "Security Logs von %s abgerufen.", logFile);
                free(allLines);
            }
        } else {
            log_message("WARNING", "Log-Datei %s konnte nicht geöffnet werden.", logFile);
        }
    } else {
        log_message("WARNING", "Log-Datei %s nicht gefunden.", logFile);
    }
#endif
}

/* --- Systemberechtigungen prüfen --- */
// Rekursive Funktion, die für jede Datei die Berechtigungen mittels stat() überprüft.
void checkSystemPermissions(const char *directory) {
    log_message("INFO", BLUE "Überprüfe Dateiberechtigungen in: %s" RESET, directory);

#ifdef _WIN32
    // Windows: Für Dateiberechtigungen müsste man erweiterte API-Aufrufe verwenden.
    log_message("WARNING", "Dateiberechtigungsprüfung unter Windows wird nicht unterstützt.");
#else
    DIR *dir = opendir(directory);
    if (!dir) {
        log_message("ERROR", RED "Verzeichnis %s konnte nicht geöffnet werden: %s" RESET, directory, strerror(errno));
        return;
    }
    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 ||
            strcmp(entry->d_name, "..") == 0)
            continue;
        size_t path_len = strlen(directory) + strlen(entry->d_name) + 2;
        char *fullPath = malloc(path_len);
        snprintf(fullPath, path_len, "%s/%s", directory, entry->d_name);

        struct stat st;
        if (stat(fullPath, &st) == 0) {
            if (S_ISDIR(st.st_mode)) {
                checkSystemPermissions(fullPath);
            } else if (S_ISREG(st.st_mode)) {
                // Überprüfe, ob die Datei "world writable" ist.
                if (st.st_mode & S_IWOTH) {
                    printf("%sWarnung: Zu weite Berechtigungen für: %s%s\n", YELLOW, fullPath, RESET);
                    log_message("WARNING", "Übermäßige Dateiberechtigungen: %s", fullPath);
                }
            }
        }
        free(fullPath);
    }
    closedir(dir);
#endif
}

/* --- Pfade aus Environment extrahieren --- */
char** extractPathsFromEnv(size_t *numPaths) {
    char **paths = NULL;
    *numPaths = 0;
    for (size_t i = 0; i < NUM_CRITICAL_VARS; i++) {
        const char *value = getenv(CRITICAL_VARS[i]);
        if (value) {
            // Prüfen, ob der Wert ein Dateipfad ist
            if (file_exists(value)) {
                paths = realloc(paths, ((*numPaths)+1)*sizeof(char*));
                paths[*numPaths] = strdup(value);
                (*numPaths)++;
            } else if (strncmp(value, "http", 4) == 0) {
                printf("%sURL gefunden für %s: %s%s\n", BLUE, CRITICAL_VARS[i], value, RESET);
                log_message("INFO", "URL in %s: %s", CRITICAL_VARS[i], value);
            }
        }
    }
    return paths;
}

/* --- Gesamter Sicherheits-Scan --- */
void scanAllFiles(void) {
    char *envPath = loadEnvFile();
    if (!envPath)
        die: {
            log_message("ERROR", "Keine .env-Datei gefunden, Scan abgebrochen.");
            exit(EXIT_FAILURE);
        };

    // Ableiten des Basisverzeichnisses (z. B. der Ordner der .env-Datei)
    char *baseDir = NULL;
    char *lastSep = strrchr(envPath, (envPath[0] == '\\' ? '\\' : '/'));
    if (lastSep) {
        size_t len = lastSep - envPath;
        baseDir = malloc(len + 1);
        strncpy(baseDir, envPath, len);
        baseDir[len] = '\0';
    } else {
        baseDir = strdup(envPath);
    }
    free(envPath);

    log_message("INFO", BOLD "Starte umfassenden Sicherheitscheck..." RESET);

    // Systemberechtigungen prüfen
    checkSystemPermissions(baseDir);

    // Pfade zum Scan – Basisverzeichnis plus evtl. in Umgebungsvariablen definierte Pfade
    size_t envPathsNum = 0;
    char **envPaths = extractPathsFromEnv(&envPathsNum);
    // Eine dynamische Liste (als Array von Strings) aufbauen:
    size_t totalPaths = 1 + envPathsNum;
    char **pathsToScan = malloc(totalPaths * sizeof(char*));
    pathsToScan[0] = baseDir; // Basisverzeichnis
    for (size_t i = 0; i < envPathsNum; i++) {
        pathsToScan[i+1] = envPaths[i];
    }
    if (envPaths) free(envPaths);

    size_t totalFilesScanned = 0;
    for (size_t i = 0; i < totalPaths; i++) {
        const char *path = pathsToScan[i];
#ifdef _WIN32
        // Windows: file_exists() genügt in den meisten Fällen
        if (file_exists(path)) {
#else
        struct stat st;
        if (stat(path, &st) == 0) {
#endif
            if (
#ifndef _WIN32
                S_ISDIR(st.st_mode)
#else
                1 // Unter Windows vereinfachte Prüfung – weiter anpassen wenn nötig
#endif
                ) {
                printf("%sScan Verzeichnis: %s%s\n", BLUE, path, RESET);
                totalFilesScanned += scanWithDefender(path);
            }
#ifndef _WIN32
            else if (S_ISREG(st.st_mode)) {
                printf("%sScan Datei: %s%s\n", BLUE, path, RESET);
                totalFilesScanned += scanWithDefender(path);
            } else {
                printf("%sÜberspringe (kein reguläres File/Directory): %s%s\n", MAGENTA, path, RESET);
            }
#endif
        }
    }
    printf("%sGesamt gescannte Dateien: %zu%s\n", GREEN, totalFilesScanned, RESET);

    // Weitere Sicherheitsprüfungen
    checkFirewallStatus();
    checkSuspiciousProcesses();
    checkNetworkConnections();
    checkSecurityLogs();

    log_message("INFO", GREEN "Sicherheitscheck abgeschlossen!" RESET);

    // Aufräumen
    for (size_t i = 0; i < totalPaths; i++) {
        free(pathsToScan[i]);
    }
    free(pathsToScan);
}

/* --- Signal-Handler für sauberen Shutdown --- */
#ifdef _WIN32
BOOL WINAPI signalHandler(DWORD signal) {
    if (signal == CTRL_C_EVENT || signal == CTRL_BREAK_EVENT) {
        log_message("INFO", YELLOW "Interrupt-Signal (%d) erhalten. Beende..." RESET, signal);
        exit(EXIT_SUCCESS);
    }
    return TRUE;
}
#else
volatile sig_atomic_t running = 1;
void signalHandler(int signum) {
    log_message("INFO", YELLOW "Interrupt-Signal (%d) erhalten. Beende..." RESET, signum);
    running = 0;
}
#endif

/* --- Main --- */
int main(void) {
#ifdef _WIN32
    InitializeCriticalSection(&logger_mutex);
    // Registrierung des Signal-Handlers unter Windows
    if (!SetConsoleCtrlHandler((PHANDLER_ROUTINE) signalHandler, TRUE)) {
        log_message("ERROR", RED "Fehler beim Einrichten des Signal-Handlers." RESET);
        return EXIT_FAILURE;
    }
#else
    signal(SIGINT, signalHandler);
    signal(SIGTERM, signalHandler);
#endif

    // Optional: Log-Datei konfigurieren
    logfile = fopen("security_scan.log", "a");
    if (!logfile)
        log_message("ERROR", RED "Log-Datei konnte nicht geöffnet werden." RESET);

    // Starte den vollständigen Scan
    scanAllFiles();

    // Halte das Programm aktiv, falls asynchrone Prozesse laufen
#ifndef _WIN32
    while (running) {
        sleep(1);
    }
#else
    // Unter Windows: Eine einfache Endlosschleife
    while (1)
        Sleep(1000);
#endif

    log_message("INFO", GREEN "Programm beendet." RESET);

#ifdef _WIN32
    DeleteCriticalSection(&logger_mutex);
#endif
    if (logfile)
        fclose(logfile);
    return EXIT_SUCCESS;
}
