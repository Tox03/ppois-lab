#include "ui/MarkovUI.h"
#include "markov/MarkovMachine.h"
#include <iostream>
#include <fstream>
#include <string>

static void printMarkovMenu() {
    std::cout << "\n=== Меню Алгорифмов Маркова ===\n";
    std::cout << "1. Показать текущую ленту\n";
    std::cout << "2. Показать правила программы\n";
    std::cout << "3. Добавить правило\n";
    std::cout << "4. Удалить правило по индексу\n";
    std::cout << "5. Задать значение ленты\n";
    std::cout << "6. Выполнить один шаг\n";
    std::cout << "7. Выполнить программу до остановки\n";
    std::cout << "8. Переключить режим логирования (-log)\n";
    std::cout << "9. Сбросить статус остановки машины\n";
    std::cout << "0. Назад в главное меню\n";
    std::cout << "Выберите пункт: ";
}

void MarkovUI::interactiveMode() {
    MarkovMachine machine;
    int choice = -1;

    while (choice != 0) {
        printMarkovMenu();
        if (!(std::cin >> choice)) {
            std::cin.clear();
            std::string dummy;
            std::getline(std::cin, dummy);
            continue;
        }

        switch (choice) {
            case 1:
                std::cout << "Лента: " << machine.getTape() << "\n";
                break;
            case 2: {
                const auto& prog = machine.getProgram();
                std::cout << "\nПравила программы (" << prog.getRuleCount() << " всего):\n";
                for (size_t i = 0; i < prog.getRuleCount(); ++i) {
                    std::cout << "  [" << i << "] " << prog.getRule(i) << "\n";
                }
                break;
            }
            case 3: {
                std::string from, to;
                int is_term = 0;
                std::cout << "Введите исходный образец (from): "; 
                std::cin >> from;
                std::cout << "Введите образец для замены (to, или - для пустой строки): "; 
                std::cin >> to;
                if (to == "-") to = "";
                std::cout << "Терминальное правило? (1 - Да, 0 - Нет): "; 
                std::cin >> is_term;
                
                machine.addRule(MarkovRule(from, to, is_term != 0));
                std::cout << "Правило добавлено.\n";
                break;
            }
            case 4: {
                size_t idx;
                std::cout << "Введите индекс правила для удаления: ";
                if (std::cin >> idx) {
                    try {
                        machine.removeRule(idx);
                        std::cout << "Правило с индексом " << idx << " удалено.\n";
                    } catch (const std::exception& e) {
                        std::cout << "Ошибка: " << e.what() << "\n";
                    }
                }
                break;
            }
            case 5: {
                std::string tape_val;
                std::cout << "Введите новое значение ленты: ";
                std::cin >> tape_val;
                machine.setTape(MarkovString(tape_val));
                std::cout << "Лента обновлена.\n";
                break;
            }
            case 6: {
                bool res = machine.step();
                if (res) {
                    std::cout << "Шаг выполнен успешно. Лента: " << machine.getTape() << "\n";
                } else {
                    std::cout << "Машина остановлена (нет применимых правил "
                              << "или достигнуто терминальное правило).\n";
                }
                break;
            }
            case 7:
                machine.run();
                std::cout << "Выполнение завершено. Итоговая лента: " << machine.getTape() << "\n";
                break;
            case 8:
                machine.setLogEnabled(!machine.isLogEnabled());
                std::cout << "Режим логирования: " << (machine.isLogEnabled() ? "ВКЛ" : "ВЫКЛ") << "\n";
                break;
            case 9:
                machine.reset();
                std::cout << "Статус остановки сброшен.\n";
                break;
            case 0:
                std::cout << "Возврат в главное меню...\n";
                break;
            default:
                std::cout << "Неверный выбор.\n";
        }
    }
}

int MarkovUI::runFromFile(const std::string& filename, bool log_mode) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Ошибка: не удалось открыть файл " << filename << "\n";
        return 1;
    }

    MarkovMachine machine;
    machine.loadFromStream(file);
    file.close();

    machine.setLogEnabled(log_mode);

    std::cout << "Выполнение Алгорифма Маркова из файла " << filename << "...\n";
    std::cout << "Начальная лента: " << machine.getTape() << "\n";
    machine.run();
    std::cout << "Итоговая лента: " << machine.getTape() << "\n";

    return 0;
}

int MarkovUI::runFromArgs(int argc, char* argv[]) {
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
