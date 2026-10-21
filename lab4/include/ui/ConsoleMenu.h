#pragma once

#include <iostream>
#include <string>
#include "graph/DirectedIncidenceMatrixGraph.h"

/**
 * @brief Класс консольного меню для взаимодействия с пользователем.
 * Реализует симметричные операции добавления/удаления, включения/отключения,
 * сортировки по возрастанию/убыванию, а также запуск демонстрационного режима.
 */
class ConsoleMenu {
public:
    /**
     * @brief Конструктор по умолчанию.
     */
    ConsoleMenu();

    /**
     * @brief Запуск интерактивного меню с чтением из потока ввода.
     * @param in Входной поток (по умолчанию std::cin).
     * @param out Выходной поток (по умолчанию std::cout).
     */
    void run(std::istream& in = std::cin, std::ostream& out = std::cout);

    /**
     * @brief Запуск полного неинтерактивного демонстрационного режима.
     * @param out Выходной поток для вывода результатов.
     */
    void runDemo(std::ostream& out = std::cout);

    /**
     * @brief Вывести список доступных команд меню.
     * @param out Выходной поток.
     */
    void printMenu(std::ostream& out) const;

    /**
     * @brief Очистить граф.
     */
    void clearGraph();

    /**
     * @brief Заполнить граф демонстрационными данными.
     */
    void populateDemoGraph();

private:
    void handleAddVertex(std::istream& in, std::ostream& out);
    void handleRemoveVertex(std::istream& in, std::ostream& out);
    void handleCheckVertex(std::istream& in, std::ostream& out);

    void handleAddEdge(std::istream& in, std::ostream& out);
    void handleRemoveEdge(std::istream& in, std::ostream& out);
    void handleCheckEdge(std::istream& in, std::ostream& out);

    void handlePrintMatrix(std::ostream& out);
    void handlePrintSummary(std::ostream& out);
    void handlePrintIterators(std::ostream& out);

    void handleSortNumbersAscending(std::ostream& out);
    void handleSortNumbersDescending(std::ostream& out);
    void handleSortStudentsAscending(std::ostream& out);
    void handleSortStudentsDescending(std::ostream& out);

    DirectedIncidenceMatrixGraph<std::string> graph_; ///< Рабочий экземпляр графа
};
