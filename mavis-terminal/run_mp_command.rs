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

use std::env;
use std::io::{self, BufReader, Read, Write};
use std::process::{Command, Stdio};
use std::thread;

fn main() {
    // Kommandozeilenargumente einlesen
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("[ERROR] Kein Befehl angegeben.");
        println!("\nDrücken Sie eine beliebige Taste, um zu beenden...");
        wait_for_enter();
        std::process::exit(1);
    }

    // Befehl aus den Argumenten zusammenfügen
    let command = args[1..].join(" ");

    // Kindprozess starten: cmd.exe /c <Befehl>
    // Wir leiten Standardausgabe (stdout) und Fehlerausgabe (stderr) in Pipes um.
    let mut child = match Command::new("cmd.exe")
        .args(&["/c", &command])
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn() {
            Err(e) => {
                eprintln!("[ERROR] CreateProcess fehlgeschlagen: {}", e);
                println!("\nDrücken Sie eine beliebige Taste, um zu beenden...");
                wait_for_enter();
                std::process::exit(1);
            }
            Ok(child) => child,
        };

    // Auslesen der Standardausgabe (stdout) in einem eigenen Thread
    let stdout_handle = {
        let stdout = child.stdout.take().expect("Kein Handle für stdout");
        thread::spawn(move || {
            let mut reader = BufReader::new(stdout);
            let mut buffer = [0u8; 4096];
            loop {
                match reader.read(&mut buffer) {
                    Ok(0) => break,
                    Ok(n) => {
                        // Ausgabe direkt an stdout weiterleiten
                        print!("{}", String::from_utf8_lossy(&buffer[..n]));
                        io::stdout().flush().unwrap();
                    },
                    Err(e) => {
                        eprintln!("[ERROR] Fehler beim Lesen der stdout: {}", e);
                        break;
                    }
                }
            }
        })
    };

    // Auslesen der Fehlerausgabe (stderr) in einem separaten Thread
    let stderr_handle = {
        let stderr = child.stderr.take().expect("Kein Handle für stderr");
        thread::spawn(move || {
            let mut reader = BufReader::new(stderr);
            let mut buffer = [0u8; 4096];
            loop {
                match reader.read(&mut buffer) {
                    Ok(0) => break,
                    Ok(n) => {
                        // Fehlerausgabe direkt an stderr weiterleiten
                        eprint!("{}", String::from_utf8_lossy(&buffer[..n]));
                        io::stderr().flush().unwrap();
                    },
                    Err(e) => {
                        eprintln!("[ERROR] Fehler beim Lesen der stderr: {}", e);
                        break;
                    }
                }
            }
        })
    };

    // Warten, bis der Kindprozess beendet wird
    let exit_status = match child.wait() {
        Ok(status) => status.code().unwrap_or(-1),
        Err(e) => {
            eprintln!("[ERROR] Fehler beim Warten auf den Kindprozess: {}", e);
            -1
        }
    };

    // Auf die Beendigung der Auslesethreads warten
    let _ = stdout_handle.join();
    let _ = stderr_handle.join();

    println!("\nProzess beendete mit Exit-Code: {}", exit_status);
    println!("\nDrücken Sie eine beliebige Taste, um zu beenden...");
    wait_for_enter();
}

/// Liest eine Zeile von der Standardeingabe, um das Programm anzuhalten.
fn wait_for_enter() {
    let mut dummy = String::new();
    let _ = io::stdin().read_line(&mut dummy);
}
