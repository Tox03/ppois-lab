#include "ui/TuringUI.h"
#include "turing/TuringMachine.h"
#include <iostream>
#include <fstream>
#include <string>

static void printTuringMenu() {
    std::cout << "\n=== Меню Машины Тьюринга ===\n";
    std::cout << "1. Задать начальное состояние ленты\n";
    std::cout << "2. Добавить правило\n";
    std::cout << "3. Удалить правило\n";
    std::cout << "4. Вывести текущую ленту\n";
    std::cout << "5. Вывести набор правил\n";
    std::cout << "6. Выполнить один шаг\n";
    std::cout << "7. Запустить выполнение программы\n";
    std::cout << "8. Запустить с пошаговым логированием (-log)\n";
    std::cout << "9. Сбросить состояние машины\n";
    std::cout << "0. Назад в главное меню\n";
    std::cout << "Выберите пункт: ";
}

void TuringUI::interactiveMode() {
    TuringMachine tm;
    int choice = -1;
    
    while (choice != 0) {
        printTuringMenu();
        if (!(std::cin >> choice)) {
            std::cin.clear();
            std::string dummy;
            std::getline(std::cin, dummy);
            continue;
        }

        switch (choice) {
            case 1: {
                std::cout << "Введите начальное состояние ленты (например, 1101): ";
                std::cin >> tm.get_tape();
                std::cout << "Лента загружена.\n";
                break;
            }
            case 2: {
                std::cout << "Введите правило (сост_вх симв_чт сост_вых симв_зап напр [R/L/N]): ";
                Rule r;
                if (std::cin >> r.current_state >> r.read_symbol >> r.next_state >> r.write_symbol >> r.direction) {
                    tm.get_rules() += r;
                    std::cout << "Правило добавлено.\n";
                } else {
                    std::cin.clear();
                    std::string dummy;
                    std::getline(std::cin, dummy);
                    std::cout << "Некорректный ввод.\n";
                }
                break;
            }
            case 3: {
                std::cout << "Введите состояние и символ для удаления (например, q0 1): ";
                std::string st;
                char sym;
                if (std::cin >> st >> sym) {
                    tm.get_rules().remove_rule(st, sym);
                    std::cout << "Правило удалено (если существовало).\n";
                }
                break;
            }
            case 4:
                std::cout << "\nТекущая лента:\n" << tm.get_tape();
                break;
            case 5:
                std::cout << "\nТекущие правила:\n" << tm.get_rules();
                break;
            case 6: {
                bool ok = tm.step();
                if (ok) {
                    std::cout << "Шаг выполнен. Текущее состояние:\n" << tm << "\n";
                } else {
                    std::cout << "Машина остановлена (правило не найдено или работа завершена).\n";
                }
                break;
            }
            case 7:
                tm.run(false);
                std::cout << "\nФинальное состояние:\n" << tm << "\n";
                break;
            case 8:
                tm.run(true);
                break;
            case 9:
                tm = TuringMachine();
                std::cout << "Состояние машины сброшено.\n";
                break;
            case 0:
                std::cout << "Возврат в главное меню...\n";
                break;
            default:
                std::cout << "Неверный пункт меню.\n";
        }
    }
}

int TuringUI::runFromFile(const std::string& filename, bool log_mode) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Ошибка: не удалось открыть файл " << filename << "\n";
        return 1;
    }

    TuringMachine tm;
    tm.load_from_stream(file);
    file.close();

    std::cout << "Выполнение Машины Тьюринга из файла " << filename << "...\n";
    tm.run(log_mode);

    if (!log_mode) {
        std::cout << "\nФинальное состояние:\n" << tm << "\n";
    }

    return 0;
}

int TuringUI::runFromArgs(int argc, char* argv[]) {
    std::string filename;
    bool log_mode = false;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-log") {
            log_mode = true;
        } else if (filename.empty() && arg[0] != '-') {
            filename = arg;
        }
    }

    if (filename.empty()) {
        std::cout << "Файл не указан. Запуск интерактивного режима...\n";
        interactiveMode();
        return 0;
    }

    return runFromFile(filename, log_mode);
}
