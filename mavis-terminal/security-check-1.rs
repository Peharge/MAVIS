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

// Vollständige professionelle Rust-Übersetzung des C++-Programms
// Fokus: Sicherheit, Stabilität, Lesbarkeit, Logging und Multithreading

use std::{
    env,
    fs,
    io::{self, BufRead, BufReader, Write},
    path::PathBuf,
    sync::{Arc, Mutex},
    thread,
    time::{Duration, Instant},
};

use chrono::Local;
use lazy_static::lazy_static;
use regex::Regex;
use sha2::{Digest, Sha256};
use signal_hook::{consts::signal::*, iterator::Signals};
use std::sync::atomic::{AtomicBool, Ordering};

lazy_static! {
    static ref CRITICAL_VARS: Vec<&'static str> = vec![
        "SECRET_KEY", "DB_PASSWORD", "API_KEY", "JWT_SECRET",
        "EMAIL_PASSWORD", "DEBUG", "ALLOWED_HOSTS", "DATABASE_URL",
        "REDIS_URL", "CELERY_BROKER_URL", "LOG_LEVEL", "SSL_CERT_PATH",
        "SSL_KEY_PATH", "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET",
        "S3_BUCKET_NAME", "S3_ACCESS_KEY", "S3_SECRET_KEY",
        "SENDGRID_API_KEY", "GITHUB_TOKEN", "TWITTER_API_KEY",
        "TWITTER_API_SECRET"
    ];

    static ref WEAK_PATTERNS: Vec<&'static str> = vec![
        "1234", "password", "test", "admin", "secret", "abc123",
        "letmein", "12345", "123456", "qwerty", "password1",
        "1q2w3e4r", "welcome", "123123", "root", "admin123",
        "football", "iloveyou", "123qwe", "changeme", "welcome1",
        "123321", "password123", "1password", "1234abcd",
        "111111", "123", "123abc", "letmein1", "newpassword",
        "passw0rd", "guest", "password1234", "987654321", "1qaz2wsx"
    ];
}

const GREEN: &str = "\x1b[92m";
const RED: &str = "\x1b[91m";
const YELLOW: &str = "\x1b[93m";
const BLUE: &str = "\x1b[94m";
const RESET: &str = "\x1b[0m";

struct Logger {
    logfile: Option<Mutex<fs::File>>,
}

impl Logger {
    fn new(log_path: Option<&str>) -> Self {
        let logfile = log_path.map(|path| Mutex::new(fs::OpenOptions::new()
            .append(true)
            .create(true)
            .open(path)
            .expect("Unable to open log file")));
        Logger { logfile }
    }

    fn log(&self, level: &str, msg: &str) {
        let timestamp = Local::now().format("[%Y-%m-%d %H:%M:%S]");
        let full_msg = format!("{} {}: {}", timestamp, level, msg);
        println!("{}", full_msg);
        if let Some(ref file_mutex) = self.logfile {
            if let Ok(mut f) = file_mutex.lock() {
                let _ = writeln!(f, "{}", full_msg);
            }
        }
    }
}

fn trim(s: &str) -> &str {
    s.trim_matches(|c| c == ' ' || c == '\t' || c == '"')
}

fn get_env_path() -> PathBuf {
    let home = env::var("HOME").or_else(|_| env::var("USERPROFILE"))
        .expect("No HOME directory found");
    PathBuf::from(home).join("PycharmProjects/MAVIS/.env")
}

fn load_env(path: &PathBuf, logger: &Logger) {
    if let Ok(file) = fs::File::open(path) {
        let reader = BufReader::new(file);
        for line in reader.lines() {
            if let Ok(line) = line {
                if line.starts_with('#') || line.trim().is_empty() {
                    continue;
                }
                if let Some((k, v)) = line.split_once('=') {
                    env::set_var(trim(k), trim(v));
                }
            }
        }
        logger.log("INFO", &format!("{}{}.env-Datei geladen.{}", GREEN, "", RESET));
    } else {
        logger.log("WARNING", &format!("{}Keine .env-Datei gefunden.{}", RED, RESET));
    }
}

fn check_env_vars(logger: &Logger) {
    logger.log("INFO", &format!("{}Checking .env security variables...{}", BLUE, RESET));
    for var in CRITICAL_VARS.iter() {
        match env::var(var) {
            Ok(value) => {
                if value.len() < 8 {
                    logger.log("WARNING", &format!("{}{} may be too short!{}", YELLOW, var, RESET));
                }
                for pattern in WEAK_PATTERNS.iter() {
                    let re = Regex::new(&format!("(?i){}", regex::escape(pattern))).unwrap();
                    if re.is_match(&value) {
                        logger.log("WARNING", &format!("{}{} uses weak pattern ({})!{}", YELLOW, var, pattern, RESET));
                        break;
                    }
                }
            }
            Err(_) => {
                logger.log("ERROR", &format!("{}{} is not set!{}", RED, var, RESET));
            }
        }
    }
}

fn compute_sha256(path: &PathBuf) -> io::Result<String> {
    let mut file = fs::File::open(path)?;
    let mut hasher = Sha256::new();
    let mut buffer = [0u8; 4096];
    loop {
        let bytes_read = file.read(&mut buffer)?;
        if bytes_read == 0 { break; }
        hasher.update(&buffer[..bytes_read]);
    }
    Ok(format!("{:x}", hasher.finalize()))
}

fn check_env_integrity(path: &PathBuf, logger: &Logger) {
    logger.log("INFO", &format!("{}Checking .env file integrity...{}", BLUE, RESET));
    match compute_sha256(path) {
        Ok(hash) => logger.log("INFO", &format!("SHA256: {}", hash)),
        Err(e) => logger.log("ERROR", &format!("{}SHA256 failed: {}{}", RED, e, RESET)),
    }
}

fn display_loading_bar(seconds: u64, message: &str) {
    let bar_len = 50;
    let start = Instant::now();
    loop {
        let elapsed = start.elapsed().as_secs_f64();
        let progress = (elapsed / seconds as f64 * 100.0).min(100.0);
        let pos = (bar_len as f64 * progress / 100.0) as usize;
        print!("\r{} [", message);
        for i in 0..bar_len {
            print!("{}", if i < pos { "█" } else { "-" });
        }
        print!("] {:>3.0}%", progress);
        io::stdout().flush().unwrap();
        if progress >= 100.0 { break; }
        thread::sleep(Duration::from_millis(100));
    }
    println!();
}

fn main() {
    let logger = Logger::new(Some("security_check.log"));
    let running = Arc::new(AtomicBool::new(true));
    let r = running.clone();
    let mut signals = Signals::new(&[SIGINT, SIGTERM]).unwrap();

    thread::spawn(move || {
        for sig in signals.forever() {
            println!("{}Signal {:?} empfangen, beende...{}", YELLOW, sig, RESET);
            r.store(false, Ordering::SeqCst);
        }
    });

    let env_path = get_env_path();

    load_env(&env_path, &logger);
    check_env_vars(&logger);
    check_env_integrity(&env_path, &logger);
    logger.log("INFO", &format!("{}Security check complete.{}", GREEN, RESET));

    display_loading_bar(5, &format!("{}Running Security Check{}", BLUE, RESET));

    while running.load(Ordering::SeqCst) {
        thread::sleep(Duration::from_secs(1));
    }
}
