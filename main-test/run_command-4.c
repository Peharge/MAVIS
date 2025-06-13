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

#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <wincred.h>
#include <dpapi.h>
#include <stdio.h>
#include <wchar.h>
#include <stdlib.h>
#include <time.h>

#pragma comment(lib, "Advapi32.lib")

static const wchar_t* CRED_TARGET_NAME = L"WSL_Command_Executor";
static const wchar_t* LOG_FILE = L"wsl_executor.log";

// Encrypt plaintext using DPAPI Current Machine
BOOL EncryptData(const char* plaintext, BYTE** outBlob, DWORD* outSize) {
    DATA_BLOB input = {(DWORD)strlen(plaintext), (BYTE*)plaintext};
    DATA_BLOB output = {0};
    if (!CryptProtectData(&input, L"WSLExecutor", NULL, NULL, NULL,
                           CRYPTPROTECT_LOCAL_MACHINE, &output)) {
        return FALSE;
    }
    *outSize = output.cbData;
    *outBlob = (BYTE*)LocalAlloc(LMEM_FIXED, output.cbData);
    if (!*outBlob) {
        LocalFree(output.pbData);
        return FALSE;
    }
    memcpy(*outBlob, output.pbData, output.cbData);
    LocalFree(output.pbData);
    return TRUE;
}

// Decrypt ciphertext using DPAPI
BOOL DecryptData(const BYTE* blob, DWORD blobSize, char** outData) {
    DATA_BLOB input = {blobSize, (BYTE*)blob};
    DATA_BLOB output = {0};
    if (!CryptUnprotectData(&input, NULL, NULL, NULL, NULL, 0, &output)) {
        return FALSE;
    }
    *outData = (char*)malloc(output.cbData + 1);
    if (!*outData) {
        LocalFree(output.pbData);
        return FALSE;
    }
    memcpy(*outData, output.pbData, output.cbData);
    (*outData)[output.cbData] = '\0';
    LocalFree(output.pbData);
    return TRUE;
}

// Store encrypted password in Credential Manager
BOOL StorePasswordSecure(const char* password) {
    BYTE* blob = NULL;
    DWORD blobSize = 0;
    if (!EncryptData(password, &blob, &blobSize)) return FALSE;

    CREDENTIALW cred = {0};
    cred.Type = CRED_TYPE_GENERIC;
    cred.TargetName = (LPWSTR)CRED_TARGET_NAME;
    cred.CredentialBlobSize = blobSize;
    cred.CredentialBlob = blob;
    cred.Persist = CRED_PERSIST_LOCAL_MACHINE;
    cred.UserName = (LPWSTR)L"WSLExecutorUser";
    cred.Comment = (LPWSTR)L"Encrypted sudo password for WSL Executor";

    BOOL ok = CredWriteW(&cred, 0);
    LocalFree(blob);
    return ok;
}

// Load and decrypt password
BOOL LoadPasswordSecure(char** outPwd) {
    PCREDENTIALW pcred = NULL;
    if (!CredReadW(CRED_TARGET_NAME, CRED_TYPE_GENERIC, 0, &pcred)) return FALSE;

    BOOL success = FALSE;
    if (pcred->CredentialBlob && pcred->CredentialBlobSize > 0) {
        success = DecryptData(pcred->CredentialBlob, pcred->CredentialBlobSize, outPwd);
    }
    CredFree(pcred);
    return success;
}

// Log entry to file with timestamp
void LogEntry(const wchar_t* entry) {
    FILE* f = _wfopen(LOG_FILE, L"a, ccs=UTF-8");
    if (!f) return;
    time_t t = time(NULL);
    struct tm tm;
    localtime_s(&tm, &t);
    wchar_t buf[64];
    wcsftime(buf, 64, L"%Y-%m-%d %H:%M:%S", &tm);
    fwprintf(f, L"%ls - %ls\n", buf, entry);
    fclose(f);
}

// Execute wide-char command
int ExecuteCommand(const wchar_t* cmdLine) {
    STARTUPINFOW si = { sizeof(si) };
    PROCESS_INFORMATION pi;
    si.dwFlags = STARTF_USESTDHANDLES;
    si.hStdInput = GetStdHandle(STD_INPUT_HANDLE);
    si.hStdOutput = GetStdHandle(STD_OUTPUT_HANDLE);
    si.hStdError = GetStdHandle(STD_ERROR_HANDLE);

    wchar_t* cmd = _wcsdup(cmdLine);
    if (!CreateProcessW(NULL, cmd, NULL, NULL, TRUE, CREATE_NO_WINDOW,
                        NULL, NULL, &si, &pi)) {
        DWORD err = GetLastError();
        fwprintf(stderr, L"[ERROR] CreateProcessW failed: %lu\n", err);
        free(cmd);
        return (int)err;
    }
    free(cmd);
    WaitForSingleObject(pi.hProcess, INFINITE);
    DWORD code;
    GetExitCodeProcess(pi.hProcess, &code);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    return (int)code;
}

// Build WSL command string
wchar_t* BuildWSLCommand(const wchar_t* base, const wchar_t* args) {
    size_t len = wcslen(L"wsl.exe ") + wcslen(base) + 1 + (args ? wcslen(args) : 0) + 1;
    wchar_t* buf = (wchar_t*)malloc(len * sizeof(wchar_t));
    if (!buf) return NULL;
    wcscpy(buf, L"wsl.exe ");
    wcscat(buf, base);
    if (args && args[0]) {
        wcscat(buf, L" ");
        wcscat(buf, args);
    }
    return buf;
}

void ShowMenu() {
    wprintf(L"\n=== WSL Executor Menu ===\n");
    wprintf(L"1) Run Command\n2) View History\n3) Change Password\n4) Clear Password\n5) Exit\n");
    wprintf(L"Select an option: ");
}

int wmain(int argc, wchar_t* argv[]) {
    char* password = NULL;
    if (!LoadPasswordSecure(&password)) password = NULL;

    int running = 1;
    while (running) {
        ShowMenu();
        int choice = 0;
        wscanf(L"%d", &choice);
        fgetws(argv[0], 1, stdin); // clear newline
        switch (choice) {
        case 1: {
            wchar_t base[256] = {0};
            wchar_t args[512] = {0};
            wprintf(L"Enter base command (e.g., 'sudo ls'): ");
            fgetws(base, 256, stdin);
            base[wcslen(base)-1] = L'\0';
            wprintf(L"Enter arguments: ");
            fgetws(args, 512, stdin);
            args[wcslen(args)-1] = L'\0';

            if (wcsncmp(base, L"sudo", 4) == 0 && !password) {
                char pwdbuf[128];
                wprintf(L"Enter sudo password: ");
                fgets(pwdbuf, 128, stdin);
                pwdbuf[strcspn(pwdbuf, "\n")] = '\0';
                if (StorePasswordSecure(pwdbuf)) {
                    password = _strdup(pwdbuf);
                    wprintf(L"[INFO] Password stored.\n");
                    LogEntry(L"Password stored");
                }
            }
            wchar_t* cmd = BuildWSLCommand(base, args);
            wprintf(L"[INFO] Executing: %ls\n", cmd);
            LogEntry(cmd);
            ExecuteCommand(cmd);
            free(cmd);
            break;
        }
        case 2: {
            FILE* f = _wfopen(LOG_FILE, L"r, ccs=UTF-8");
            if (!f) { wprintf(L"No history found.\n"); break; }
            wchar_t line[1024];
            wprintf(L"=== Command History ===\n");
            while (fgetws(line, 1024, f)) wprintf(L"%ls", line);
            fclose(f);
            break;
        }
        case 3: {
            char newpwd[128];
            wprintf(L"Enter new password: ");
            fgets(newpwd, 128, stdin);
            newpwd[strcspn(newpwd, "\n")] = '\0';
            if (StorePasswordSecure(newpwd)) {
                free(password);
                password = _strdup(newpwd);
                wprintf(L"[INFO] Password updated.\n");
                LogEntry(L"Password changed");
            }
            break;
        }
        case 4: {
            if (CredDeleteW(CRED_TARGET_NAME, CRED_TYPE_GENERIC, 0)) {
                free(password);
                password = NULL;
                wprintf(L"[INFO] Password cleared.\n");
                LogEntry(L"Password cleared");
            } else {
                wprintf(L"[ERROR] Failed to clear password.\n");
            }
            break;
        }
        case 5:
            running = 0;
            break;
        default:
            wprintf(L"Invalid choice.\n");
        }
    }
    free(password);
    return 0;
}
