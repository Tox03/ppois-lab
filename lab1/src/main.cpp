#include <iostream>
#include <string>
#include <vector>
#ifdef _WIN32
#include <windows.h>
#endif
#include "ui/MenuManager.h"
#include "ui/TuringUI.h"
#include "ui/MarkovUI.h"

void printUsage(const char* progName) {
    std::cout << "Использование:\n"
              << "  Интерактивный режим (консольное меню):\n"
              << "    " << progName << "\n\n"
              << "  Режим командной строки (CLI):\n"
              << "    " << progName << " turing <имя_файла> [-log]\n"
              << "    " << progName << " markov <имя_файла> [-log]\n"
              << "    " << progName << " -m <turing|markov> <имя_файла> [-log]\n\n"
              << "  Справка:\n"
              << "    " << progName << " --help | -h\n";
}

int main(int argc, char* argv[]) {
#ifdef _WIN32
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
#endif
    if (argc == 1) {
        MenuManager::runMainMenu();
        return 0;
    }

    std::string first_arg = argv[1];

    if (first_arg == "--help" || first_arg == "-h") {
        printUsage(argv[0]);
        return 0;
    }

    if (first_arg == "turing") {
        return TuringUI::runFromArgs(argc - 1, argv + 1);
    }

    if (first_arg == "markov") {
        return MarkovUI::runFromArgs(argc - 1, argv + 1);
    }

    // Поддержка синтаксиса -m / --machine <turing|markov>
    if ((first_arg == "-m" || first_arg == "--machine") && argc >= 3) {
        std::string machine = argv[2];
        std::vector<char*> shifted_args;
        shifted_args.push_back(argv[0]);
        for (int i = 3; i < argc; ++i) {
            shifted_args.push_back(argv[i]);
        }
        if (machine == "turing") {
            return TuringUI::runFromArgs(static_cast<int>(shifted_args.size()), shifted_args.data());
        } else if (machine == "markov") {
            return MarkovUI::runFromArgs(static_cast<int>(shifted_args.size()), shifted_args.data());
        } else {
            std::cerr << "Неизвестный тип машины: " << machine << ". Ожидалось 'turing' или 'markov'.\n";
            return 1;
        }
    }

    std::cerr << "Нераспознанная команда или тип машины: " << first_arg << "\n";
    printUsage(argv[0]);
    return 1;
}
