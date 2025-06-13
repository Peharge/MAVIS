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

#include <windows.h>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "[ERROR] No command provided." << std::endl;
        return 1;
    }

    // Baue den WSL-Befehl zusammen.
    // Jeder Parameter wird einzeln angehängt; falls ein Parameter Leerzeichen enthält, wird er nicht explizit in zusätzliche Anführungszeichen eingeschlossen,
    // da wir hier einen einfachen Befehl erwarten (z. B. nano test.py).
    std::string wslCommand = "wsl.exe";
    for (int i = 1; i < argc; ++i) {
        wslCommand += " " + std::string(argv[i]);
    }

    // Erzeuge ein Terminalfenster, in dem das WSL-Programm interaktiv gestartet wird.
    // "cmd.exe /k" startet das Terminal und hält es offen, nachdem der Befehl ausgeführt wurde.
    std::string fullCommand = "cmd.exe /k " + wslCommand;

    // Ausgabe des Befehls (optional zu Debug-Zwecken)
    std::cout << "Executing the following command on Linux: " << fullCommand << std::endl;

    // Prozessstart konfigurieren
    STARTUPINFOA si = { 0 };
    PROCESS_INFORMATION pi = { 0 };
    si.cb = sizeof(si);

    // Erstelle einen modifizierbaren Puffer für den Befehl
    std::vector<char> buffer(fullCommand.begin(), fullCommand.end());
    buffer.push_back('\0');

    // Starte den Prozess in einem neuen Konsolenfenster, damit wir eine voll interaktive Session bekommen.
    BOOL success = CreateProcessA(
        NULL,                   // Keine Modulname, nur Commandline
        buffer.data(),          // Commandline-Puffer
        NULL,                   // Standardprozesseigenschaften
        NULL,                   // Standardthread-Eigenschaften
        FALSE,                  // Handle nicht erben
        CREATE_NEW_CONSOLE,     // Neues Konsolenfenster
        NULL,                   // Standardumgebungsblock
        NULL,                   // Aktuelles Verzeichnis verwenden
        &si,                    // STARTUPINFO
        &pi                     // PROCESS_INFORMATION
    );

    if (!success) {
        std::cerr << "[ERROR] Failed to start process. Error code: " << GetLastError() << std::endl;
        return 1;
    }

    // Warte auf Beendigung des gestarteten Prozesses
    WaitForSingleObject(pi.hProcess, INFINITE);

    DWORD exitCode = 0;
    GetExitCodeProcess(pi.hProcess, &exitCode);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return static_cast<int>(exitCode);
}
