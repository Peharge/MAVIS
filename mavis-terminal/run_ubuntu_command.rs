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
use std::ffi::CString;
use std::io::{self, Write};
use std::os::windows::io::AsRawHandle;
use std::ptr;
use windows_sys::Win32::Foundation::*;
use windows_sys::Win32::System::Threading::*;
use windows_sys::Win32::System::Console::*;
use windows_sys::Win32::System::Diagnostics::Debug::*;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("[ERROR] No command provided.");
        std::process::exit(1);
    }

    // Build the WSL command line
    let mut command = String::from("wsl.exe -d ubuntu");
    for arg in &args[1..] {
        command.push(' ');
        command.push('"');
        command.push_str(arg);
        command.push('"');
    }

    // Convert Rust String to a mutable null-terminated C string buffer
    let mut command_bytes = Vec::from(command.clone().into_bytes());
    command_bytes.push(0); // Null terminator

    // Setup STARTUPINFO and PROCESS_INFORMATION
    let mut si: STARTUPINFOA = unsafe { std::mem::zeroed() };
    let mut pi: PROCESS_INFORMATION = unsafe { std::mem::zeroed() };
    si.cb = std::mem::size_of::<STARTUPINFOA>() as u32;
    si.dwFlags = STARTF_USESTDHANDLES;
    si.hStdInput = unsafe { GetStdHandle(STD_INPUT_HANDLE) };
    si.hStdOutput = unsafe { GetStdHandle(STD_OUTPUT_HANDLE) };
    si.hStdError = unsafe { GetStdHandle(STD_ERROR_HANDLE) };

    let success = unsafe {
        CreateProcessA(
            ptr::null(),                         // lpApplicationName
            command_bytes.as_mut_ptr() as *mut i8, // lpCommandLine
            ptr::null_mut(),                     // lpProcessAttributes
            ptr::null_mut(),                     // lpThreadAttributes
            1,                                   // bInheritHandles
            0,                                   // dwCreationFlags
            ptr::null_mut(),                     // lpEnvironment
            ptr::null(),                         // lpCurrentDirectory
            &si,                                 // lpStartupInfo
            &mut pi                              // lpProcessInformation
        )
    };

    if success == 0 {
        let error_code = unsafe { GetLastError() };
        eprintln!(
            "[ERROR] Failed to start process. Error code: {}",
            error_code
        );
        std::process::exit(1);
    }

    // Wait until process finishes
    unsafe {
        WaitForSingleObject(pi.hProcess, INFINITE);

        let mut exit_code: u32 = 0;
        GetExitCodeProcess(pi.hProcess, &mut exit_code);

        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);

        std::process::exit(exit_code as i32);
    }
}
