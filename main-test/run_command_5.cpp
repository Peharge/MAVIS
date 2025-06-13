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
#include <wincred.h>
#include <dpapi.h>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
#include <ctime>
#include <stdexcept>

#pragma comment(lib, "Advapi32.lib")

const std::wstring CRED_TARGET_NAME = L"WSL_Command_Executor";
const std::wstring LOG_FILE = L"wsl_executor.log";

struct ProtectedBlob {
    DATA_BLOB blob{};
    ~ProtectedBlob() { if (blob.pbData) LocalFree(blob.pbData); }
};

std::vector<BYTE> EncryptData(const std::string& plaintext) {
    DATA_BLOB input{ (DWORD)plaintext.size(), (BYTE*)plaintext.data() };
    ProtectedBlob output;
    if (!CryptProtectData(&input, L"WSLExecutor", nullptr, nullptr, nullptr,
                          CRYPTPROTECT_LOCAL_MACHINE, &output.blob)) {
        throw std::runtime_error("CryptProtectData failed: " + std::to_string(GetLastError()));
    }
    return { output.blob.pbData, output.blob.pbData + output.blob.cbData };
}

std::string DecryptData(const std::vector<BYTE>& ciphertext) {
    DATA_BLOB input{ (DWORD)ciphertext.size(), (BYTE*)ciphertext.data() };
    ProtectedBlob output;
    if (!CryptUnprotectData(&input, nullptr, nullptr, nullptr, nullptr, 0, &output.blob)) {
        throw std::runtime_error("CryptUnprotectData failed: " + std::to_string(GetLastError()));
    }
    return std::string((char*)output.blob.pbData, output.blob.cbData);
}

bool StorePasswordSecure(const std::string& password) {
    auto encrypted = EncryptData(password);
    CREDENTIALW cred{};
    cred.Type = CRED_TYPE_GENERIC;
    cred.TargetName = (LPWSTR)CRED_TARGET_NAME.c_str();
    cred.CredentialBlobSize = (DWORD)encrypted.size();
    cred.CredentialBlob = const_cast<BYTE*>(encrypted.data());
    cred.Persist = CRED_PERSIST_LOCAL_MACHINE;
    cred.UserName = (LPWSTR)L"WSLExecutorUser";
    cred.Comment = (LPWSTR)L"Encrypted sudo password for WSL Executor";
    return CredWriteW(&cred, 0) == TRUE;
}

std::string LoadPasswordSecure() {
    PCREDENTIALW pcred = nullptr;
    if (!CredReadW(CRED_TARGET_NAME.c_str(), CRED_TYPE_GENERIC, 0, &pcred)) return {};
    std::vector<BYTE> blob(pcred->CredentialBlob, pcred->CredentialBlob + pcred->CredentialBlobSize);
    std::string pwd = DecryptData(blob);
    CredFree(pcred);
    return pwd;
}

std::wstring BuildWSLCommand(const std::wstring& base, const std::vector<std::wstring>& args) {
    std::wstringstream ss;
    ss << L"wsl.exe " << base;
    for (const auto& a : args) ss << L" \"" << a << L"\"";
    return ss.str();
}

int ExecuteCommand(const std::wstring& cmd) {
    STARTUPINFOW si{};
    PROCESS_INFORMATION pi{};
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESTDHANDLES;
    si.hStdInput = GetStdHandle(STD_INPUT_HANDLE);
    si.hStdOutput = GetStdHandle(STD_OUTPUT_HANDLE);
    si.hStdError = GetStdHandle(STD_ERROR_HANDLE);
    std::vector<wchar_t> buffer(cmd.begin(), cmd.end()); buffer.push_back(L'\0');
    if (!CreateProcessW(nullptr, buffer.data(), nullptr, nullptr, TRUE,
                        CREATE_NO_WINDOW, nullptr, nullptr, &si, &pi)) {
        std::wcerr << L"[ERROR] CreateProcessW failed: " << GetLastError() << L"\n";
        return 1;
    }
    WaitForSingleObject(pi.hProcess, INFINITE);
    DWORD code = 0; GetExitCodeProcess(pi.hProcess, &code);
    CloseHandle(pi.hProcess); CloseHandle(pi.hThread);
    return (int)code;
}

void Log(const std::wstring& entry) {
    std::wofstream ofs(LOG_FILE, std::ios::app);
    auto t = std::time(nullptr); wchar_t buf[64];
    _wctime_s(buf, &t);
    ofs << buf << L" - " << entry << L"\n";
}

void PrintMenu() {
    std::wcout << L"\n=== WSL Executor Menu ===\n"
               << L"1) Run Command\n"
               << L"2) View History\n"
               << L"3) Change Password\n"
               << L"4) Clear Password\n"
               << L"5) Exit\n"
               << L"Select an option: ";
}

int wmain(int argc, wchar_t* argv[]) {
    std::string password;
    try { password = LoadPasswordSecure(); }
    catch (const std::exception& ex) { std::wcerr << L"[ERROR] " << ex.what() << L"\n"; return 1; }

    bool running = true;
    while (running) {
        PrintMenu(); int choice; std::wcin >> choice;
        std::wstring dummy; std::getline(std::wcin, dummy);
        switch (choice) {
        case 1: {
            std::wstring cmd; std::vector<std::wstring> args;
            std::wcout << L"Enter base command (e.g., 'sudo ls'): ";
            std::getline(std::wcin, cmd);
            std::wcout << L"Enter arguments separated by space: ";
            std::wstring line; std::getline(std::wcin, line);
            std::wistringstream iss(line);
            for (std::wstring a; iss >> a;) args.push_back(a);

            if (cmd.rfind(L"sudo", 0) == 0 && password.empty()) {
                std::wcout << L"Enter sudo password: ";
                std::string pwd; std::getline(std::cin, pwd);
                if (!StorePasswordSecure(pwd)) std::wcerr << L"[ERROR] Could not store password\n";
                else { password = pwd; std::wcout << L"[INFO] Password stored securely\n"; }
            }
            auto full = BuildWSLCommand(cmd, args);
            Log(full);
            std::wcout << L"[INFO] Executing: " << full << L"\n";
            ExecuteCommand(full);
            break;
        }
        case 2: {
            std::wcout << L"=== Command History ===\n";
            std::wifstream ifs(LOG_FILE);
            for (std::wstring line; std::getline(ifs, line);)
                std::wcout << line << L"\n";
            break;
        }
        case 3: {
            std::wcout << L"Enter new password: ";
            std::string newpwd; std::getline(std::cin, newpwd);
            if (StorePasswordSecure(newpwd)) {
                password = newpwd;
                std::wcout << L"[INFO] Password updated.\n";
                Log(L"Password changed");
            }
            else std::wcerr << L"[ERROR] Could not update password\n";
            break;
        }
        case 4: {
            if (CredDeleteW(CRED_TARGET_NAME.c_str(), CRED_TYPE_GENERIC, 0)) {
                password.clear();
                std::wcout << L"[INFO] Password cleared\n";
                Log(L"Password cleared");
            } else std::wcerr << L"[ERROR] Failed to clear password\n";
            break;
        }
        case 5:
            running = false;
            break;
        default:
            std::wcout << L"Invalid choice.\n";
        }
    }
    return 0;
}
