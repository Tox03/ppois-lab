#pragma once

#include <stdexcept>
#include <string>

/**
 * @brief Класс исключения для операций над графом.
 * Выбрасывается при попытке выполнить недопустимую операцию
 * (например, добавление дубликата вершины, обращение к несуществующему ребру и т.д.).
 */
class GraphException : public std::runtime_error {
public:
    /**
     * @brief Конструктор с сообщением об ошибке типа std::string.
     * @param message Текст сообщения об ошибке.
     */
    explicit GraphException(const std::string& message);

    /**
     * @brief Конструктор с сообщением об ошибке типа const char*.
     * @param message Текст сообщения об ошибке.
     */
    explicit GraphException(const char* message);
};
