#include <iostream>
#include <string>
#include "ui/ConsoleMenu.h"

#ifdef _WIN32
#include <windows.h>
#endif

int main(int argc, char* argv[]) {
#ifdef _WIN32
    // Настройка кодировки UTF-8 для корректного вывода русского текста в консоли Windows
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
#endif

    ConsoleMenu menu;

    if (argc > 1) {
        std::string arg = argv[1];
        if (arg == "--demo" || arg == "-d") {
            menu.runDemo(std::cout);
            return 0;
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Лабораторная работа №4. Вариант 4.\n"
                      << "Использование:\n"
                      << "  " << argv[0] << "         Запуск в интерактивном режиме консольного меню\n"
                      << "  " << argv[0] << " --demo  Автоматическая демонстрация сортировок и графа\n"
                      << "  " << argv[0] << " --help  Справка\n";
            return 0;
        }
    }

    menu.run(std::cin, std::cout);
    return 0;
}
