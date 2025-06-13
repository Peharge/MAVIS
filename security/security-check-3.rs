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

use chrono::Local;
use regex::Regex;
use std::collections::HashMap;
use std::env;
use std::fs::{self, File, OpenOptions};
use std::io::{self, BufRead, BufReader, Write};
use std::path::Path;
use std::process::Command;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;
use walkdir::WalkDir;

// ANSI-Farbdefinitionen für Konsolenausgaben
const RED: &str     = "\x1B[91m";
const GREEN: &str   = "\x1B[92m";
const YELLOW: &str  = "\x1B[93m";
const BLUE: &str    = "\x1B[94m";
const MAGENTA: &str = "\x1B[95m";
const CYAN: &str    = "\x1B[96m";
const WHITE: &str   = "\x1B[97m";
const RESET: &str   = "\x1B[0m";
const BOLD: &str    = "\x1B[1m";

// Kritische Sicherheitsvariablen, die aus der .env-Datei gelesen werden sollen
const CRITICAL_VARS: &[&str] = &[
    "SECRET_KEY", "DB_PASSWORD", "API_KEY", "JWT_SECRET", "EMAIL_PASSWORD", "DEBUG",
    "ALLOWED_HOSTS", "DATABASE_URL", "REDIS_URL", "CELERY_BROKER_URL", "LOG_LEVEL",
    "SSL_CERT_PATH", "SSL_KEY_PATH", "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET",
    "S3_BUCKET_NAME", "S3_ACCESS_KEY", "S3_SECRET_KEY", "SENDGRID_API_KEY",
    "GITHUB_TOKEN", "TWITTER_API_KEY", "TWITTER_API_SECRET"
];

// Bekannte bösartige IPs und verdächtige Ports (Beispieldaten – bitte anpassen)
const KNOWN_MALICIOUS_IPS: &[&str] = &["192.168.1.100", "203.0.113.5"];
const MAX_CONNECTIONS_FROM_SAME_IP: usize = 10;

/// Gibt den aktuellen Zeitstempel als String zurück.
fn get_timestamp() -> String {
    Local::now().format("[%Y-%m-%d %H:%M:%S]").to_string()
}

/// Logger-Struktur: thread-sichere Konsolen- und Datei-Ausgabe.
struct Logger {
    logfile: Mutex<Option<File>>,
}

impl Logger {
    fn new() -> Self {
        Self {
            logfile: Mutex::new(None),
        }
    }

    /// Konfiguriert die Log-Datei.
    fn set_log_file(&self, filename: &str) {
        match OpenOptions::new().append(true).create(true).open(filename) {
            Ok(file) => {
                let mut log_lock = self.logfile.lock().unwrap();
                *log_lock = Some(file);
            }
            Err(e) => {
                eprintln!(
                    "{}ERROR: Could not open log file: {} - {}{}",
                    RED, filename, e, RESET
                );
            }
        }
    }

    /// Schreibt eine Log-Nachricht mit Zeitstempel und Level.
    fn log(&self, level: &str, message: &str) {
        let timestamp = get_timestamp();
        let log_message = format!("{} {}: {}", timestamp, level, message);
        println!("{}", log_message);
        if let Ok(mut lock) = self.logfile.lock() {
            if let Some(ref mut file) = *lock {
                let _ = writeln!(file, "{}", log_message);
            }
        }
    }
}

/// Globale Logger-Instanz (als Singleton)
static LOGGER: once_cell::sync::Lazy<Logger> = once_cell::sync::Lazy::new(|| Logger::new());

/// Führt einen Systembefehl aus und gibt dessen Ausgabe als String zurück.
fn exec_command(cmd: &str) -> io::Result<String> {
    #[cfg(windows)]
    let output = Command::new("cmd").args(&["/C", cmd]).output()?;
    #[cfg(not(windows))]
    let output = Command::new("sh").arg("-c").arg(cmd).output()?;
    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

/// Liest eine Zeile und trimmt Whitespace sowie Anführungszeichen.
fn trim(s: &str) -> String {
    s.trim_matches(|c: char| c.is_whitespace() || c == '"').to_string()
}

/// Lädt eine .env-Datei, liest deren Inhalt und setzt die Variablen ins Environment.
fn load_env_file() -> io::Result<String> {
    let home = if cfg!(windows) {
        env::var("USERPROFILE").map_err(|e| io::Error::new(io::ErrorKind::NotFound, e))?
    } else {
        env::var("HOME").map_err(|e| io::Error::new(io::ErrorKind::NotFound, e))?
    };
    let env_path = if cfg!(windows) {
        format!("{}\\PycharmProjects\\MAVIS\\.env", home)
    } else {
        format!("{}/PycharmProjects/MAVIS/.env", home)
    };
    if !Path::new(&env_path).exists() {
        LOGGER.log("WARNING", &format!("{}No .env file found: {}{}", YELLOW, env_path, RESET));
        return Ok(String::new());
    }
    let file = File::open(&env_path)?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line = line?;
        if line.is_empty() || line.starts_with('#') {
            continue;
        }
        if let Some(eq_pos) = line.find('=') {
            let key = trim(&line[..eq_pos]);
            let value = trim(&line[eq_pos + 1..]);
            if !key.is_empty() {
                env::set_var(&key, &value);
            }
        }
    }
    LOGGER.log("INFO", &format!("{}{}.env-Datei successfully loaded.{}", GREEN, ".env", RESET));
    Ok(env_path)
}

/// Gibt alle Dateien in einem Verzeichnis (rekursiv) aus und zählt sie.
fn list_files_for_scan(directory: &str) -> usize {
    let mut file_count = 0;
    LOGGER.log("INFO", &format!("{}Files to scan into: {}{}", BLUE, directory, RESET));
    for entry in WalkDir::new(directory).into_iter().filter_map(|e| e.ok()) {
        if entry.file_type().is_file() {
            println!("   - {}", entry.path().display());
            file_count += 1;
        }
    }
    file_count
}

/// Führt einen Sicherheitsscan (mittels Defender oder ClamAV) im angegebenen Verzeichnis durch.
fn scan_with_defender(directory: &str) -> usize {
    let total_files = list_files_for_scan(directory);
    #[cfg(windows)]
    let command = format!(
        "powershell -Command \"Start-MpScan -ScanType CustomScan -ScanPath '{}'\"",
        directory
    );
    #[cfg(not(windows))]
    let command = format!("clamscan -r {}", directory);

    LOGGER.log("INFO", &format!("{}Start scan in: {}{}", BLUE, directory, RESET));
    match exec_command(&command) {
        Ok(result) => {
            if !result.trim().is_empty() {
                println!("{}", result);
                LOGGER.log("INFO", &format!("Scan-Result: {}", result));
            } else {
                println!("{}No threats found.{}", GREEN, RESET);
                LOGGER.log("INFO", "No threats found.");
            }
        }
        Err(e) => {
            LOGGER.log("ERROR", &format!("Scan failed: {}", e));
        }
    }
    total_files
}

/// Überprüft den Firewall-Status.
fn check_firewall_status() {
    LOGGER.log("INFO", &format!("{}Check firewall status...{}", BLUE, RESET));
    #[cfg(windows)]
    let command = "netsh advfirewall show allprofiles";
    #[cfg(not(windows))]
    let command = "ufw status";

    match exec_command(command) {
        Ok(output) => {
            if output.contains("State") || output.contains("active") {
                println!("{}Firewall is enabled.{}", GREEN, RESET);
                LOGGER.log("INFO", "Firewall is enabled.");
            } else {
                println!("{}Firewall is NOT enabled.{}", RED, RESET);
                LOGGER.log("WARNING", "Firewall is NOT enabled.");
            }
        }
        Err(e) => {
            LOGGER.log("ERROR", &format!("Firewall check error: {}", e));
        }
    }
}

/// Überprüft laufende Prozesse auf verdächtige Namen.
fn check_suspicious_processes() {
    LOGGER.log("INFO", &format!("{}Check ongoing processes for suspicion...{}", BLUE, RESET));
    let suspicious_processes = vec![
        "cmd.exe", "powershell.exe", "netstat.exe", "whois.exe",
        "python.exe", "java.exe", "wget.exe", "curl.exe", "nc.exe", "nmap.exe",
    ];
    #[cfg(windows)]
    let command = "tasklist /FO CSV";
    #[cfg(not(windows))]
    let command = "ps -eo pid,comm,%cpu,%mem";

    if let Ok(result) = exec_command(command) {
        for line in result.lines() {
            for proc in &suspicious_processes {
                if line.contains(proc) {
                    println!("{}Suspicious process found: {}{}", YELLOW, line, RESET);
                    LOGGER.log("WARNING", &format!("Suspicious process: {}", line));
                }
            }
        }
    }
    println!("{}Process review completed.{}", GREEN, RESET);
}

/// Überprüft aktive Netzwerkverbindungen mittels "netstat" und wertet verdächtige Aktivitäten aus.
fn check_network_connections() {
    LOGGER.log("INFO", &format!("{}Check active network connections...{}", BLUE, RESET));
    let command = "netstat -an";
    let mut ip_count: HashMap<String, usize> = HashMap::new();
    if let Ok(net_output) = exec_command(command) {
        // Ein einfaches Regex zur Extraktion von IPv4-Adressen.
        let ip_regex = Regex::new(r"(\d+\.\d+\.\d+\.\d+)").unwrap();
        for line in net_output.lines() {
            if line.contains("ESTABLISHED") {
                if let Some(cap) = ip_regex.captures(line) {
                    let ip = cap.get(1).unwrap().as_str().to_string();
                    let counter = ip_count.entry(ip.clone()).or_insert(0);
                    *counter += 1;
                    // Überprüfe bekannte bösartige IPs.
                    if KNOWN_MALICIOUS_IPS.contains(&ip.as_str()) {
                        println!("{}Warnung: Connection to known malicious IP: {}{}", RED, ip, RESET);
                        LOGGER.log("WARNING", &format!("Malicious IP detected: {}", ip));
                    }
                    // DDoS-Schutz: zu viele Verbindungen von derselben IP.
                    if *counter > MAX_CONNECTIONS_FROM_SAME_IP {
                        println!("{}Possible DDoS attack: {} has {} connections.{}",
                            RED, ip, counter, RESET);
                        LOGGER.log("WARNING", &format!("DDoS attack suspected at IP: {}", ip));
                    }
                }
            }
        }
    }
    println!("{}Network connection check completed.{}", GREEN, RESET);
}

/// Liest (unter Linux) oder ruft (unter Windows) die letzten sicherheitsrelevanten Logs ab.
fn check_security_logs() {
    LOGGER.log("INFO", &format!("{}Check security-relevant logs...{}", BLUE, RESET));
    #[cfg(windows)]
    {
        let command = "wevtutil qe Security /c:50 /f:text";
        match exec_command(command) {
            Ok(logs) => {
                println!("{}", logs);
                LOGGER.log("INFO", "Security logs (Windows) retrieved.");
            }
            Err(e) => {
                LOGGER.log("ERROR", &format!("Failed to retrieve security logs: {}", e));
            }
        }
    }
    #[cfg(not(windows))]
    {
        let log_file = "/var/log/auth.log";
        if Path::new(log_file).exists() {
            match fs::read_to_string(log_file) {
                Ok(contents) => {
                    println!("{}", contents);
                    LOGGER.log("INFO", &format!("Security logs from {} retrieved.", log_file));
                }
                Err(e) => {
                    LOGGER.log("WARNING", &format!("Log file {} could not be opened: {}", log_file, e));
                }
            }
        } else {
            LOGGER.log("WARNING", &format!("Log file {} not found.", log_file));
        }
    }
}

/// Überprüft Systemdateiberechtigungen in einem definierten Verzeichnis.
/// Unter Unix wird z. B. mit `PermissionsExt` geprüft.
#[cfg(not(windows))]
fn check_system_permissions(directory: &str) {
    use std::os::unix::fs::PermissionsExt;
    LOGGER.log("INFO", &format!("{}Check file permissions in: {}{}", BLUE, directory, RESET));
    for entry in WalkDir::new(directory).into_iter().filter_map(|e| e.ok()) {
        if entry.file_type().is_file() {
            if let Ok(metadata) = entry.metadata() {
                let mode = metadata.permissions().mode();
                // Prüfe, ob "others" Schreibrechte besitzen (world writable)
                if mode & 0o002 != 0 {
                    println!("{}Warning: Excessive permissions for: {}{}", YELLOW, entry.path().display(), RESET);
                    LOGGER.log("WARNING", &format!("Excessive file permissions: {}", entry.path().display()));
                }
            }
        }
    }
}

#[cfg(windows)]
fn check_system_permissions(directory: &str) {
    // Unter Windows können Dateiberechtigungen anders geprüft werden. Hier wird nur das Verzeichnis gelistet.
    LOGGER.log("INFO", &format!("{}(Windows) Skipping detailed file permissions check in: {}{}", BLUE, directory, RESET));
}

/// Extrahiert aus den kritischen Umgebungsvariablen potentielle Pfade (lokal oder URLs).
fn extract_paths_from_env() -> Vec<String> {
    let mut paths = Vec::new();
    for &var in CRITICAL_VARS {
        if let Ok(val) = env::var(var) {
            if Path::new(&val).exists() {
                paths.push(val);
            } else if val.starts_with("http") {
                println!("{}URL found for {}: {}{}", BLUE, var, val, RESET);
                LOGGER.log("INFO", &format!("URL in {}: {}", var, val));
            }
        }
    }
    paths
}

/// Führt den gesamten Sicherheits-Scan aus, indem alle Prüfungen aufgerufen werden.
fn scan_all_files() -> io::Result<()> {
    let env_path = load_env_file()?;
    let base_dir = if !env_path.is_empty() {
        Path::new(&env_path)
            .parent()
            .and_then(|p| p.to_str())
            .unwrap_or(".")
            .to_string()
    } else {
        return Err(io::Error::new(io::ErrorKind::NotFound, "No .env file found, scan aborted."));
    };

    LOGGER.log("INFO", &format!("{}{} Start comprehensive security check...{}", BOLD, "INFO", RESET));

    // Systemberechtigungen prüfen
    check_system_permissions(&base_dir);

    // Definiere die zu scannenden Pfade: Basisverzeichnis plus aus den Umgebungsvariablen extrahierte Pfade.
    let mut paths_to_scan = vec![base_dir.clone()];
    let env_paths = extract_paths_from_env();
    paths_to_scan.extend(env_paths);

    let mut total_files_scanned = 0;
    for path in paths_to_scan {
        let p = Path::new(&path);
        if p.exists() {
            if p.is_dir() {
                println!("{}Scan directory: {}{}", BLUE, path, RESET);
                total_files_scanned += scan_with_defender(&path);
            } else if p.is_file() {
                println!("{}Scan file: {}{}", BLUE, path, RESET);
                total_files_scanned += scan_with_defender(&path);
            } else {
                println!("{}Skip (not file/directory): {}{}", MAGENTA, path, RESET);
            }
        }
    }
    println!("{}Total scanned files: {}{}", GREEN, total_files_scanned, RESET);

    // Zusätzliche Sicherheitsprüfungen
    check_firewall_status();
    check_suspicious_processes();
    check_network_connections();
    check_security_logs();

    LOGGER.log("INFO", &format!("{}Security check completed!{}", GREEN, RESET));
    Ok(())
}

fn main() {
    // Konfiguriere die Log-Datei.
    LOGGER.set_log_file("security_scan.log");

    // Atomic flag für den sauberen Shutdown
    let running = Arc::new(AtomicBool::new(true));
    let r = running.clone();

    // Registrierung eines Signal-Handlers (Ctrl+C)
    ctrlc::set_handler(move || {
        LOGGER.log("INFO", &format!("{}Interrupt signal received. Ending...{}", YELLOW, RESET));
        r.store(false, Ordering::SeqCst);
    })
    .expect("Error setting Ctrl-C handler");

    if let Err(e) = scan_all_files() {
        LOGGER.log("ERROR", &format!("Critical error: {}", e));
        std::process::exit(1);
    }

    // Halte das Programm aktiv, falls asynchrone Prozesse laufen.
    while running.load(Ordering::SeqCst) {
        thread::sleep(Duration::from_secs(1));
    }
    LOGGER.log("INFO", &format!("{}Program ended.{}", GREEN, RESET));
}
