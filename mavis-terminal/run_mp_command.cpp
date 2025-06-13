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
#include <windows.h>
#include <string>

// Hilfsfunktion zur Fehlerausgabe inklusive GetLastError-Code
void printError(const std::string& msg) {
    std::cerr << "[ERROR] " << msg << " Fehlercode: " << GetLastError() << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "[ERROR] Kein Befehl angegeben.\n";
        std::cout << "\nDrücken Sie eine beliebige Taste, um zu beenden..." << std::endl;
        system("pause");
        return 1;
    }

    // Befehl aus den Programmparametern zusammensetzen
    std::string command;
    for (int i = 1; i < argc; ++i) {
        if (i > 1) {
            command += " ";
        }
        command += argv[i];
    }

    // Sicherheitsattribute für den Pipe-Handle
    SECURITY_ATTRIBUTES sa;
    sa.nLength = sizeof(SECURITY_ATTRIBUTES);
    sa.bInheritHandle = TRUE;  // Erlaubt Vererbung an untergeordnete Prozesse
    sa.lpSecurityDescriptor = NULL;

    // Pipe für die Ausgabe des Kindprozesses erstellen
    HANDLE hStdOutRead = NULL, hStdOutWrite = NULL;
    if (!CreatePipe(&hStdOutRead, &hStdOutWrite, &sa, 0)) {
        printError("Pipe konnte nicht erstellt werden.");
        std::cout << "\nDrücken Sie eine beliebige Taste, um zu beenden..." << std::endl;
        system("pause");
        return 1;
    }

    // Den Lese-Handle vom Kindprozess unzugänglich machen (d.h. er soll nicht erben)
    if (!SetHandleInformation(hStdOutRead, HANDLE_FLAG_INHERIT, 0)) {
        printError("SetHandleInformation schlug fehl.");
        CloseHandle(hStdOutRead);
        CloseHandle(hStdOutWrite);
        std::cout << "\nDrücken Sie eine beliebige Taste, um zu beenden..." << std::endl;
        system("pause");
        return 1;
    }

    // STARTUPINFOA konfigurieren, damit der Kindprozess unseren Pipe-Handle nutzt
    STARTUPINFOA si;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    si.dwFlags |= STARTF_USESTDHANDLES;
    si.hStdOutput = hStdOutWrite;
    si.hStdError = hStdOutWrite;

    PROCESS_INFORMATION pi;
    ZeroMemory(&pi, sizeof(pi));

    // Erstellen der Befehlszeile: "cmd.exe /c <Befehl>" führt den Befehl aus,
    // /c sorgt dafür, dass cmd.exe nach Ausführung beendet wird (danach wird über system("pause") das Fenster offen gehalten)
    std::string cmdLine = "cmd.exe /c " + command;

    // Kindprozess erstellen
    if (!CreateProcessA(
            NULL,
            &cmdLine[0], // modifizierbarer String
            NULL,
            NULL,
            TRUE,       // Handles vererben
            0,
            NULL,
            NULL,
            &si,
            &pi)) {
        printError("Kindprozess konnte nicht gestartet werden.");
        CloseHandle(hStdOutRead);
        CloseHandle(hStdOutWrite);
        std::cout << "\nDrücken Sie eine beliebige Taste, um zu beenden..." << std::endl;
        system("pause");
        return 1;
    }

    // Schreibende Seite der Pipe kann im Elternprozess geschlossen werden,
    // da sie vom Kindprozess benötigt wurde und nun seine Ausgabe an den Lese-Handle gesendet wird.
    CloseHandle(hStdOutWrite);

    // Ausgabe des Kindprozesses lesen und an die Konsole weiterleiten
    char buffer[4096];
    DWORD bytesRead = 0;
    while (true) {
        BOOL success = ReadFile(hStdOutRead, buffer, sizeof(buffer) - 1, &bytesRead, NULL);
        if (!success || bytesRead == 0) {
            break;
        }
        buffer[bytesRead] = '\0';
        std::cout << buffer;
    }

    // Warten auf den Abschluss des Kindprozesses (bei /c wird er nun beendet sein)
    WaitForSingleObject(pi.hProcess, INFINITE);

    // Optional: Exit-Code des Kindprozesses ermitteln (für weiterführende Logik oder Fehleranalyse)
    DWORD exitCode;
    if (GetExitCodeProcess(pi.hProcess, &exitCode) == 0) {
        printError("Exit-Code konnte nicht ermittelt werden.");
    } else {
        std::cout << "\nProzess beendete mit Exit-Code: " << exitCode << std::endl;
    }

    // Handles freigeben
    CloseHandle(hStdOutRead);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    // Terminal offen halten, damit der Benutzer die Ausgabe lesen kann
    std::cout << "\nDrücken Sie eine beliebige Taste, um zu beenden..." << std::endl;
    system("pause");

    return static_cast<int>(exitCode);
}
