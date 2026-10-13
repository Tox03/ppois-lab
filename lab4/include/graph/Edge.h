#pragma once

#include <cstddef>
#include <iostream>

/**
 * @brief Класс, представляющий ориентированное ребро графа.
 * Хранит начальную вершину (источник), конечную вершину (приёмник)
 * и уникальный идентификатор ребра.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class Edge {
public:
    /**
     * @brief Конструктор по умолчанию.
     */
    Edge();

    /**
     * @brief Параметризованный конструктор ребра.
     * @param source Начальная вершина ребра.
     * @param target Конечная вершина ребра.
     * @param id Идентификатор ребра.
     */
    Edge(const T& source, const T& target, std::size_t id = 0);

    /**
     * @brief Получить начальную вершину ребра.
     * @return Константная ссылка на начальную вершину.
     */
    const T& getSource() const;

    /**
     * @brief Получить конечную вершину ребра.
     * @return Константная ссылка на конечную вершину.
     */
    const T& getTarget() const;

    /**
     * @brief Получить идентификатор ребра.
     * @return Идентификатор ребра.
     */
    std::size_t getId() const;

    /**
     * @brief Установить начальную вершину ребра.
     * @param source Новая начальная вершина.
     */
    void setSource(const T& source);

    /**
     * @brief Установить конечную вершину ребра.
     * @param target Новая конечная вершина.
     */
    void setTarget(const T& target);

    /**
     * @brief Установить идентификатор ребра.
     * @param id Новый идентификатор.
     */
    void setId(std::size_t id);

    /**
     * @brief Проверить, является ли ребро петлёй (source == target).
     * @return true, если ребро является петлёй, иначе false.
     */
    bool isLoop() const;

    /**
     * @brief Оператор проверки равенства рёбер.
     * @param other Другое ребро для сравнения.
     * @return true, если рёбра равны (совпадают source и target), иначе false.
     */
    bool operator==(const Edge<T>& other) const;

    /**
     * @brief Оператор проверки неравенства рёбер.
     * @param other Другое ребро для сравнения.
     * @return true, если рёбра не равны, иначе false.
     */
    bool operator!=(const Edge<T>& other) const;

    /**
     * @brief Оператор «меньше» для упорядочивания рёбер.
     * @param other Другое ребро для сравнения.
     * @return true, если текущее ребро строго меньше other.
     */
    bool operator<(const Edge<T>& other) const;

    /**
     * @brief Оператор «меньше или равно».
     * @param other Другое ребро для сравнения.
     */
    bool operator<=(const Edge<T>& other) const;

    /**
     * @brief Оператор «больше».
     * @param other Другое ребро для сравнения.
     */
    bool operator>(const Edge<T>& other) const;

    /**
     * @brief Оператор «больше или равно».
     * @param other Другое ребро для сравнения.
     */
    bool operator>=(const Edge<T>& other) const;

    /**
     * @brief Оператор вывода ребра в поток.
     */
    template <typename U>
    friend std::ostream& operator<<(std::ostream& os, const Edge<U>& edge);

private:
    T source_{};        ///< Начальная вершина
    T target_{};        ///< Конечная вершина
    std::size_t id_{0}; ///< Идентификатор ребра
};

#include "graph/Edge.cpp"
