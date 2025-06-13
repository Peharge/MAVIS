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
#include <stdexcept>

#pragma comment(lib, "Advapi32.lib")

const std::wstring CRED_TARGET_NAME = L"WSL_Command_Executor";

// RAII wrapper for DPAPI protected data
struct ProtectedBlob {
    DATA_BLOB blob{};
    ProtectedBlob() = default;
    ~ProtectedBlob() {
        if (blob.pbData) LocalFree(blob.pbData);
    }
};

// Encrypt plaintext using DPAPI Current User
std::vector<BYTE> EncryptData(const std::string& plaintext) {
    DATA_BLOB input{};
    input.cbData = static_cast<DWORD>(plaintext.size());
    input.pbData = reinterpret_cast<BYTE*>(const_cast<char*>(plaintext.data()));

    ProtectedBlob output;
    if (!CryptProtectData(
            &input,
            L"WSLExecutor",
            nullptr,
            nullptr,
            nullptr,
            CRYPTPROTECT_LOCAL_MACHINE,
            &output.blob))
    {
        throw std::runtime_error("CryptProtectData failed: " + std::to_string(GetLastError()));
    }
    return std::vector<BYTE>(output.blob.pbData, output.blob.pbData + output.blob.cbData);
}

// Decrypt ciphertext using DPAPI
std::string DecryptData(const std::vector<BYTE>& ciphertext) {
    DATA_BLOB input{};
    input.cbData = static_cast<DWORD>(ciphertext.size());
    input.pbData = const_cast<BYTE*>(ciphertext.data());

    ProtectedBlob output;
    if (!CryptUnprotectData(
            &input,
            nullptr,
            nullptr,
            nullptr,
            nullptr,
            0,
            &output.blob))
    {
        throw std::runtime_error("CryptUnprotectData failed: " + std::to_string(GetLastError()));
    }
    return std::string(reinterpret_cast<char*>(output.blob.pbData), output.blob.cbData);
}

// Store encrypted password in Windows Credential Manager
bool StorePasswordSecure(const std::string& password) {
    // Encrypt
    auto encrypted = EncryptData(password);

    CREDENTIALW cred = {};
    cred.Type = CRED_TYPE_GENERIC;
    cred.TargetName = const_cast<LPWSTR>(CRED_TARGET_NAME.c_str());
    cred.CredentialBlobSize = static_cast<DWORD>(encrypted.size());
    cred.CredentialBlob = encrypted.data();
    cred.Persist = CRED_PERSIST_LOCAL_MACHINE;
    cred.UserName = const_cast<LPWSTR>(L"WSLExecutorUser");
    cred.Comment = const_cast<LPWSTR>(L"WSL Command Executor Encrypted Password");

    return CredWriteW(&cred, 0) == TRUE;
}

// Load and decrypt password from Windows Credential Manager
std::string LoadPasswordSecure() {
    PCREDENTIALW pcred = nullptr;
    if (!CredReadW(CRED_TARGET_NAME.c_str(), CRED_TYPE_GENERIC, 0, &pcred)) {
        return {};
    }
    try {
        std::vector<BYTE> blob(pcred->CredentialBlob, pcred->CredentialBlob + pcred->CredentialBlobSize);
        std::string pwd = DecryptData(blob);
        CredFree(pcred);
        return pwd;
    } catch (...) {
        CredFree(pcred);
        throw;
    }
}

// Build WSL command with proper quoting
std::wstring BuildWSLCommand(int argc, wchar_t* argv[]) {
    std::wstringstream ss;
    ss << L"wsl.exe";
    for (int i = 1; i < argc; ++i) {
        ss << L" \"" << argv[i] << L"\"";
    }
    return ss.str();
}

// Execute command and return exit code
int ExecuteCommand(const std::wstring& command) {
    STARTUPINFOW si{};
    PROCESS_INFORMATION pi{};
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESTDHANDLES;
    si.hStdInput = GetStdHandle(STD_INPUT_HANDLE);
    si.hStdOutput = GetStdHandle(STD_OUTPUT_HANDLE);
    si.hStdError = GetStdHandle(STD_ERROR_HANDLE);

    std::vector<wchar_t> cmd(command.begin(), command.end());
    cmd.push_back(L'\0');

    if (!CreateProcessW(nullptr, cmd.data(), nullptr, nullptr, TRUE,
                        CREATE_NO_WINDOW, nullptr, nullptr, &si, &pi)) {
        DWORD err = GetLastError();
        std::cerr << "[ERROR] CreateProcessW failed: " << err << std::endl;
        return static_cast<int>(err);
    }
    WaitForSingleObject(pi.hProcess, INFINITE);
    DWORD exitCode = 0;
    GetExitCodeProcess(pi.hProcess, &exitCode);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    return static_cast<int>(exitCode);
}

int wmain(int argc, wchar_t* argv[]) {
    if (argc < 2) {
        std::cerr << "[ERROR] No command specified." << std::endl;
        return 1;
    }

    std::string password;
    try {
        password = LoadPasswordSecure();
        if (password.empty()) {
            std::cout << "[INFO] Enter password for sudo (will be stored securely): ";
            std::getline(std::cin, password);
            if (!StorePasswordSecure(password)) {
                std::cerr << "[ERROR] Could not store password." << std::endl;
                return 1;
            }
            std::cout << "[INFO] Password stored encrypted." << std::endl;
        } else {
            std::cout << "[INFO] Loaded stored password." << std::endl;
        }
    } catch (const std::exception& ex) {
        std::cerr << "[ERROR] " << ex.what() << std::endl;
        return 1;
    }

    // Prepend sudo if needed
    std::wstring cmd = BuildWSLCommand(argc, argv);
    // Uncomment next line to use sudo with stored password
    // cmd = L"echo \"" + std::wstring(password.begin(), password.end()) + L"\" | sudo -S " + cmd;

    return ExecuteCommand(cmd);
}
