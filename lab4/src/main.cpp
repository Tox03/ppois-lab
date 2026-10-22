#include <iostream>
#include <string>
#include <cstring>
#include "ui/ConsoleMenu.h"

#ifdef _WIN32
#include <windows.h>
#endif

int main(int argc, char* argv[]) {
#ifdef _WIN32
    // Настройка кодовой страницы UTF-8 для корректного отображения и ввода русского языка в консоли Windows
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
#endif

    ConsoleMenu menu;

    for (int i = 1; i < argc; ++i) {
        if (std::strcmp(argv[i], "--help") == 0 || std::strcmp(argv[i], "-h") == 0) {
            std::cout << "Лабораторная работа №4: Обобщенное программирование (Вариант 4)\n"
                      << "Использование:\n"
                      << "  " << argv[0] << "         Запуск интерактивного консольного меню\n"
                      << "  " << argv[0] << " --demo  Запуск автоматического демонстрационного режима\n"
                      << "  " << argv[0] << " --help  Вывод справки по использованию\n";
            return 0;
        }
        if (std::strcmp(argv[i], "--demo") == 0 || std::strcmp(argv[i], "-d") == 0) {
            menu.runDemo(std::cout);
            return 0;
        }
    }

    menu.run(std::cin, std::cout);
    return 0;
}
