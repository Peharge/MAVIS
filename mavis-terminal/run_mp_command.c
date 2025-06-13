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
#include <windows.h>

// Hilfsfunktion zur Fehlerausgabe mit GetLastError-Code
void printError(const char* msg) {
    fprintf(stderr, "[ERROR] %s Fehlercode: %lu\n", msg, GetLastError());
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "[ERROR] Kein Befehl angegeben.\n");
        printf("\nDrücken Sie eine beliebige Taste, um zu beenden...\n");
        system("pause");
        return 1;
    }

    // Gesamtlänge des Befehls aus den Programmparametern ermitteln
    size_t totalLen = 0;
    for (int i = 1; i < argc; i++) {
        totalLen += strlen(argv[i]) + 1; // +1 für das Leerzeichen oder Nullterminator
    }

    // Präfix, damit cmd.exe den Befehl ausführt
    const char *prefix = "cmd.exe /c ";
    size_t prefixLen = strlen(prefix);

    // Dynamisch genügend Speicher reservieren
    char *cmdLine = (char *)malloc(prefixLen + totalLen + 1);
    if (cmdLine == NULL) {
        printError("Speicherallokation fehlgeschlagen");
        return 1;
    }

    // Befehlskette aufbauen: "cmd.exe /c <Befehl>"
    strcpy(cmdLine, prefix);
    for (int i = 1; i < argc; i++) {
        strcat(cmdLine, argv[i]);
        if (i < argc - 1) {
            strcat(cmdLine, " ");
        }
    }

    // Sicherheitsattribute für die Pipe erstellen
    SECURITY_ATTRIBUTES sa;
    sa.nLength = sizeof(SECURITY_ATTRIBUTES);
    sa.lpSecurityDescriptor = NULL;
    sa.bInheritHandle = TRUE;  // Erlaubt die Vererbung an Kindprozesse

    // Pipe für die Ausgabe des Kindprozesses erstellen
    HANDLE hStdOutRead = NULL, hStdOutWrite = NULL;
    if (!CreatePipe(&hStdOutRead, &hStdOutWrite, &sa, 0)) {
        printError("CreatePipe fehlgeschlagen");
        free(cmdLine);
        printf("\nDrücken Sie eine beliebige Taste, um zu beenden...\n");
        system("pause");
        return 1;
    }

    // Den Lese-Handle so einstellen, dass er nicht vererbt wird
    if (!SetHandleInformation(hStdOutRead, HANDLE_FLAG_INHERIT, 0)) {
        printError("SetHandleInformation fehlgeschlagen");
        CloseHandle(hStdOutRead);
        CloseHandle(hStdOutWrite);
        free(cmdLine);
        printf("\nDrücken Sie eine beliebige Taste, um zu beenden...\n");
        system("pause");
        return 1;
    }

    // STARTUPINFOA konfigurieren, damit der Kindprozess unsere Pipe als Standardausgabe erhält
    STARTUPINFOA si;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    si.dwFlags |= STARTF_USESTDHANDLES;
    si.hStdOutput = hStdOutWrite;
    si.hStdError  = hStdOutWrite;

    PROCESS_INFORMATION pi;
    ZeroMemory(&pi, sizeof(pi));

    // Kindprozess erstellen
    if (!CreateProcessA(
            NULL,
            cmdLine,   // modifizierbarer String (muss beschreibbar sein)
            NULL,
            NULL,
            TRUE,      // Handles vererben erlauben
            0,
            NULL,
            NULL,
            &si,
            &pi)) {
        printError("CreateProcess fehlgeschlagen");
        CloseHandle(hStdOutRead);
        CloseHandle(hStdOutWrite);
        free(cmdLine);
        printf("\nDrücken Sie eine beliebige Taste, um zu beenden...\n");
        system("pause");
        return 1;
    }

    // Schreibenden Teil der Pipe im Elternprozess schließen
    CloseHandle(hStdOutWrite);

    // Ausgabe des Kindprozesses über die Pipe lesen und in die Konsole schreiben
    char buffer[4096];
    DWORD bytesRead;
    while (1) {
        BOOL success = ReadFile(hStdOutRead, buffer, sizeof(buffer) - 1, &bytesRead, NULL);
        if (!success || bytesRead == 0) {
            break;
        }
        buffer[bytesRead] = '\0';
        printf("%s", buffer);
    }

    // Warten, bis der Kindprozess beendet wird
    WaitForSingleObject(pi.hProcess, INFINITE);

    DWORD exitCode;
    if (GetExitCodeProcess(pi.hProcess, &exitCode) == 0) {
        printError("GetExitCodeProcess fehlgeschlagen");
    } else {
        printf("\nProzess beendete mit Exit-Code: %lu\n", exitCode);
    }

    // Alle Handles freigeben
    CloseHandle(hStdOutRead);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    free(cmdLine);

    // Terminal offen halten, damit der Benutzer die Ausgabe lesen kann
    printf("\nDrücken Sie eine beliebige Taste, um zu beenden...\n");
    system("pause");

    return (int)exitCode;
}
