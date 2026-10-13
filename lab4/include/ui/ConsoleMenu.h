#pragma once

#include <iostream>
#include <string>

/**
 * @brief Класс интерактивного консольного меню для демонстрации лабораторной работы №4.
 * Позволяет тестировать обобщённые алгоритмы сортировки (Gnome sort, Pigeonhole sort)
 * и контейнер ориентированного графа на основе матрицы инцидентности.
 */
class ConsoleMenu {
public:
    /**
     * @brief Конструктор консольного меню.
     */
    ConsoleMenu();

    /**
     * @brief Запуск интерактивного цикла меню с заданными потоками ввода/вывода.
     * @param in Поток ввода (по умолчанию std::cin).
     * @param out Поток вывода (по умолчанию std::cout).
     */
    void run(std::istream& in = std::cin, std::ostream& out = std::cout);

    /**
     * @brief Запуск автоматической демонстрации всех возможностей (без ожидания ввода).
     * @param out Поток вывода.
     */
    void runDemo(std::ostream& out = std::cout);

private:
    void showMainMenu(std::ostream& out) const;
    void handleGnomeSortMenu(std::istream& in, std::ostream& out);
    void handlePigeonholeSortMenu(std::istream& in, std::ostream& out);
    void handleGraphMenu(std::istream& in, std::ostream& out);
};
