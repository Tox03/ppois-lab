#pragma once
#include <string>

/**
 * @brief Класс пользовательского интерфейса для Нормальных алгорифмов Маркова.
 * Полностью изолирует ввод/вывод от реализации самой машины.
 */
class MarkovUI {
public:
    /** @brief Запуск интерактивного меню Алгорифмов Маркова. */
    static void interactiveMode();

    /** @brief Запуск Алгорифма Маркова из файла. */
    static int runFromFile(const std::string& filename, bool log_mode);

    /** @brief Обработка аргументов командной строки для Алгорифмов Маркова. */
    static int runFromArgs(int argc, char* argv[]);
};
