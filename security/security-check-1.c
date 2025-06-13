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
#include <time.h>
#include <stdarg.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/stat.h>
#include <pthread.h>
#include <signal.h>
#include <openssl/sha.h>
#include <regex.h>
#include <stdbool.h>

// ANSI-Farbdefinitionen für Konsolenoutput
#define GREEN   "\033[92m"
#define RED     "\033[91m"
#define YELLOW  "\033[93m"
#define BLUE    "\033[94m"
#define RESET   "\033[0m"

// Kritische Sicherheitsvariablen (gleich wie im C++-Code)
const char* CRITICAL_VARS[] = {
    "SECRET_KEY", "DB_PASSWORD", "API_KEY", "JWT_SECRET",
    "EMAIL_PASSWORD", "DEBUG", "ALLOWED_HOSTS", "DATABASE_URL",
    "REDIS_URL", "CELERY_BROKER_URL", "LOG_LEVEL", "SSL_CERT_PATH",
    "SSL_KEY_PATH", "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET",
    "S3_BUCKET_NAME", "S3_ACCESS_KEY", "S3_SECRET_KEY",
    "SENDGRID_API_KEY", "GITHUB_TOKEN", "TWITTER_API_KEY",
    "TWITTER_API_SECRET"
};
const int CRITICAL_VARS_COUNT = sizeof(CRITICAL_VARS) / sizeof(CRITICAL_VARS[0]);

// Schwache Passwortelemente (Patterns)
const char* WEAK_PATTERNS[] = {
    "1234", "password", "test", "admin", "secret", "abc123",
    "letmein", "12345", "123456", "qwerty", "password1",
    "1q2w3e4r", "welcome", "123123", "root", "admin123",
    "football", "iloveyou", "123qwe", "changeme", "welcome1",
    "123321", "password123", "1password", "1234abcd",
    "111111", "123", "123abc", "letmein1", "newpassword",
    "passw0rd", "guest", "password1234", "987654321", "1qaz2wsx"
};
const int WEAK_PATTERNS_COUNT = sizeof(WEAK_PATTERNS) / sizeof(WEAK_PATTERNS[0]);

// ---------------------------
// Logger (thread-sicher) mit globaler Variablen und Mutex
// ---------------------------
static FILE* log_file = NULL;
static pthread_mutex_t log_mutex = PTHREAD_MUTEX_INITIALIZER;

void logger_set_logfile(const char* filename) {
    pthread_mutex_lock(&log_mutex);
    log_file = fopen(filename, "a");
    if (!log_file) {
        fprintf(stderr, "ERROR: Could not open log file: %s\n", filename);
    }
    pthread_mutex_unlock(&log_mutex);
}

void logger_log(const char* level, const char* format, ...) {
    pthread_mutex_lock(&log_mutex);

    // Zeitstempel erzeugen
    time_t now = time(NULL);
    struct tm tm_info;
    localtime_r(&now, &tm_info);
    char timestamp[32];
    strftime(timestamp, sizeof(timestamp), "[%Y-%m-%d %H:%M:%S]", &tm_info);

    // Nachricht formatieren
    va_list args;
    va_start(args, format);
    printf("%s %s: ", timestamp, level);
    vprintf(format, args);
    printf("\n");

    if (log_file) {
        fprintf(log_file, "%s %s: ", timestamp, level);
        va_start(args, format);  // Erneut initialisieren
        vfprintf(log_file, format, args);
        va_end(args);
        fprintf(log_file, "\n");
        fflush(log_file);
    } else {
        va_end(args);
    }
    pthread_mutex_unlock(&log_mutex);
}

// ---------------------------
// Utility: trim-Funktion (entfernt führende und endende Leerzeichen und Anführungszeichen)
// ---------------------------
char* trim(char* str) {
    if (str == NULL) return NULL;

    // führende Zeichen trimmen
    while (*str == ' ' || *str == '\t' || *str == '"') str++;

    // Ende trimmen
    size_t len = strlen(str);
    if(len == 0)
        return str;
    char* end = str + len - 1;
    while (end > str && (*end == ' ' || *end == '\t' || *end == '"')) {
        *end = '\0';
        end--;
    }
    return str;
}

// ---------------------------
// Liefert den Pfad zur .env-Datei im Home-Verzeichnis
// ---------------------------
char* getEnvFilePath() {
    const char* home = getenv("HOME");
#ifdef _WIN32
    if (!home) {
        home = getenv("USERPROFILE");
    }
#endif
    if (!home) {
        fprintf(stderr, "No HOME directory found!\n");
        exit(EXIT_FAILURE);
    }
    // Speicher für den Pfad reservieren (hier Anpassung je nach Bedarf)
    char* path = malloc(512);
    if (!path) {
        fprintf(stderr, "Memory allocation error!\n");
        exit(EXIT_FAILURE);
    }
    snprintf(path, 512, "%s/%s", home, "PycharmProjects/MAVIS/.env");
    return path;
}

// ---------------------------
// Laden der .env-Datei und Setzen der Umgebungsvariablen
// ---------------------------
void loadEnvFile(const char* path) {
    struct stat st;
    if (stat(path, &st) != 0) {
        logger_log("WARNING", RED "Keine .env-Datei gefunden." RESET);
        return;
    }
    FILE* fp = fopen(path, "r");
    if (!fp) {
        fprintf(stderr, "Error opening .env file.\n");
        exit(EXIT_FAILURE);
    }
    char line[1024];
    while (fgets(line, sizeof(line), fp)) {
        // Zeilenumbruch entfernen
        line[strcspn(line, "\n")] = 0;
        if (line[0] == '#' || strlen(line) == 0)
            continue;
        char* eq = strchr(line, '=');
        if (eq) {
            *eq = '\0';
            char* key = trim(line);
            char* value = trim(eq + 1);
            if (strlen(key) > 0) {
                setenv(key, value, 1);
            }
        }
    }
    fclose(fp);
    logger_log("INFO", GREEN ".env-Datei successfully loaded." RESET);
}

// ---------------------------
// Überprüfung der kritischen Umgebungsvariablen auf Existenz und schwache Muster
// ---------------------------
void checkEnvSecurity() {
    logger_log("INFO", BLUE "Checking the .env security variables" RESET);
    for (int i = 0; i < CRITICAL_VARS_COUNT; i++) {
        const char* var = CRITICAL_VARS[i];
        const char* value = getenv(var);
        if (!value) {
            logger_log("ERROR", RED "%s is not set!" RESET, var);
        } else {
            size_t len = strlen(value);
            if (len < 8) {
                logger_log("WARNING", YELLOW "%s may be too short!" RESET, var);
            }
            // Überprüfung auf schwache Muster mittels POSIX regex
            for (int j = 0; j < WEAK_PATTERNS_COUNT; j++) {
                regex_t regex;
                int ret = regcomp(&regex, WEAK_PATTERNS[j], REG_ICASE | REG_EXTENDED);
                if (ret) {
                    logger_log("ERROR", RED "Regex error in %s: Unable to compile pattern." RESET, var);
                    continue;
                }
                ret = regexec(&regex, value, 0, NULL, 0);
                if (ret == 0) {
                    logger_log("WARNING", YELLOW "%s uses a weak pattern (%s)!" RESET, var, WEAK_PATTERNS[j]);
                    regfree(&regex);
                    break;
                }
                regfree(&regex);
            }
        }
    }
}

// ---------------------------
// Sichere und speichereffiziente SHA-256-Berechnung in Blöcken
// ---------------------------
char* computeSHA256(const char* filePath) {
    const size_t BUF_SIZE = 4096;
    FILE* fp = fopen(filePath, "rb");
    if (!fp) {
        fprintf(stderr, "Error opening file for SHA256 calculation: %s\n", filePath);
        exit(EXIT_FAILURE);
    }
    SHA256_CTX ctx;
    if (SHA256_Init(&ctx) != 1) {
        fclose(fp);
        fprintf(stderr, "SHA256_Init failed.\n");
        exit(EXIT_FAILURE);
    }
    unsigned char buffer[BUF_SIZE];
    size_t bytesRead;
    while ((bytesRead = fread(buffer, 1, BUF_SIZE, fp)) > 0) {
        if (SHA256_Update(&ctx, buffer, bytesRead) != 1) {
            fclose(fp);
            fprintf(stderr, "SHA256_Update failed.\n");
            exit(EXIT_FAILURE);
        }
    }
    fclose(fp);
    unsigned char hash[SHA256_DIGEST_LENGTH];
    if (SHA256_Final(hash, &ctx) != 1) {
        fprintf(stderr, "SHA256_Final failed.\n");
        exit(EXIT_FAILURE);
    }
    // Speicher für den Hex-String (SHA256_DIGEST_LENGTH * 2 + 1)
    char* result = malloc(SHA256_DIGEST_LENGTH * 2 + 1);
    if (!result) {
        fprintf(stderr, "Memory allocation error!\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        sprintf(result + (i * 2), "%02x", hash[i]);
    }
    result[SHA256_DIGEST_LENGTH * 2] = '\0';
    return result;
}

// ---------------------------
// Prüfung der .env-Datei-Integrität anhand des SHA-256-Hashes
// ---------------------------
void checkEnvIntegrity(const char* path) {
    logger_log("INFO", BLUE "Performing the .env integrity check" RESET);
    struct stat st;
    if (stat(path, &st) != 0) {
        logger_log("ERROR", RED ".env file not found!" RESET);
        return;
    }
    char* hash = computeSHA256(path);
    logger_log("INFO", "SHA256: %s", hash);
    free(hash);
}

// ---------------------------
// Stub für zukünftige Checks (z. B. Paket-Updates, Netzwerkverbindungen etc.)
//
// Hinweis: Hier nur ein Logeintrag, weitere Systemaufrufe können hinzugefügt werden.
// ---------------------------
void checkExternalDependencies() {
    logger_log("INFO", BLUE "Checking external dependencies (stub)" RESET);
}

// ---------------------------
// File Monitor (Polling-Lösung) für die .env-Datei in einem separaten Thread
// ---------------------------
typedef struct {
    char envPath[512];
    unsigned int intervalMs;
    volatile bool stopMonitoring;
    char lastHash[SHA256_DIGEST_LENGTH * 2 + 1];
} EnvFileMonitor;

EnvFileMonitor monitor;

void* monitorThreadFunc(void* arg) {
    EnvFileMonitor* mon = (EnvFileMonitor*)arg;
    while (!mon->stopMonitoring) {
        // Schlafzeit: interval in ms
        usleep(mon->intervalMs * 1000);
        struct stat st;
        if (stat(mon->envPath, &st) == 0) {
            char* currentHash = computeSHA256(mon->envPath);
            if (strcmp(currentHash, mon->lastHash) != 0) {
                logger_log("WARNING", RED ".env file has been modified!" RESET);
                strncpy(mon->lastHash, currentHash, sizeof(mon->lastHash));
            }
            free(currentHash);
        } else {
            logger_log("ERROR", RED ".env file was deleted!" RESET);
        }
    }
    return NULL;
}

pthread_t monitor_thread;

// ---------------------------
// Fortschrittsbalken als visuelle Rückmeldung
// ---------------------------
void displayLoadingBar(unsigned int durationSeconds, const char* message) {
    const int barLength = 50;
    struct timespec start, now;
    clock_gettime(CLOCK_MONOTONIC, &start);
    int progress = 0;
    while (progress < 100) {
        clock_gettime(CLOCK_MONOTONIC, &now);
        double elapsed = now.tv_sec - start.tv_sec + (now.tv_nsec - start.tv_nsec) / 1e9;
        progress = (int)((elapsed / durationSeconds) * 100);
        if (progress > 100) progress = 100;
        int pos = (barLength * progress) / 100;
        printf("\r%s [", message);
        for (int i = 0; i < barLength; i++) {
            if (i < pos)
                printf("█");
            else
                printf("-");
        }
        printf("] %d%%", progress);
        fflush(stdout);
        if (progress >= 100)
            break;
        usleep(100000); // 100 ms
    }
    printf("\n");
}

// ---------------------------
// Signal-Handling für einen sauberen Shutdown
// ---------------------------
volatile sig_atomic_t running = 1;
void signalHandler(int signal) {
    logger_log("INFO", YELLOW "Interrupt signal (%d) received. End..." RESET, signal);
    running = 0;
}

// ---------------------------
// Main-Funktion
// ---------------------------
int main() {
    // Log-Datei konfigurieren
    logger_set_logfile("security_check.log");

    // Signal-Handler registrieren
    signal(SIGINT, signalHandler);
    signal(SIGTERM, signalHandler);

    // .env-Pfad ermitteln
    char* envPath = getEnvFilePath();

    // Sicherheitschecks
    loadEnvFile(envPath);
    checkEnvSecurity();
    checkEnvIntegrity(envPath);
    checkExternalDependencies();

    // Initialisiere den File Monitor
    memset(&monitor, 0, sizeof(monitor));
    strncpy(monitor.envPath, envPath, sizeof(monitor.envPath)-1);
    // Initialer Hash
    char* initialHash = computeSHA256(monitor.envPath);
    strncpy(monitor.lastHash, initialHash, sizeof(monitor.lastHash));
    free(initialHash);
    monitor.intervalMs = 1000; // 1000 ms Polling-Intervall
    monitor.stopMonitoring = false;

    // Starte den Monitor-Thread
    if (pthread_create(&monitor_thread, NULL, monitorThreadFunc, (void*)&monitor) != 0) {
        logger_log("ERROR", RED "Failed to create file monitor thread." RESET);
        free(envPath);
        return EXIT_FAILURE;
    }

    // Fortschrittsbalken anzeigen (5 Sekunden, Nachricht)
    displayLoadingBar(5, BLUE "Running Security Check" RESET);

    logger_log("INFO", GREEN "Security check successfully completed!" RESET);

    // Hauptschleife: Halte das Programm am Laufen, bis ein Abbruchsignal empfangen wird.
    while (running) {
        sleep(1);
    }

    // Stoppe den Monitor-Thread
    monitor.stopMonitoring = true;
    pthread_join(monitor_thread, NULL);

    free(envPath);
    if (log_file)
        fclose(log_file);
    return EXIT_SUCCESS;
}
