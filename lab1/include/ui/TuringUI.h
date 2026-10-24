#pragma once
#include <string>

/**
 * @brief Класс пользовательского интерфейса для Машины Тьюринга.
 * Полностью изолирует ввод/вывод от реализации самой машины.
 */
class TuringUI {
public:
    /** @brief Запуск интерактивного меню Машины Тьюринга. */
    static void interactiveMode();

    /** @brief Запуск Машины Тьюринга из файла. */
    static int runFromFile(const std::string& filename, bool log_mode);

    /** @brief Обработка аргументов командной строки для Машины Тьюринга. */
    static int runFromArgs(int argc, char* argv[]);
};
