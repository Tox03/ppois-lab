#pragma once

#include <cstddef>
#include <iterator>
#include <vector>

template <typename T>
class Edge;

/**
 * @brief Двунаправленный итератор рёбер графа.
 * Позволяет последовательно обходить все рёбра графа.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class EdgeIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = Edge<T>;
    using difference_type = std::ptrdiff_t;
    using pointer = Edge<T>*;
    using reference = Edge<T>&;

    /**
     * @brief Конструктор по умолчанию.
     */
    EdgeIterator();

    /**
     * @brief Конструктор итератора с привязкой к вектору рёбер и индексу.
     * @param edges Указатель на вектор рёбер.
     * @param index Текущий индекс ребра.
     */
    EdgeIterator(std::vector<Edge<T>>* edges, std::size_t index);

    /**
     * @brief Оператор разыменования.
     * @return Ссылка на текущее ребро.
     */
    reference operator*() const;

    /**
     * @brief Оператор стрелка.
     * @return Указатель на текущее ребро.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент.
     */
    EdgeIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    EdgeIterator operator++(int);

    /**
     * @brief Префиксный декремент.
     */
    EdgeIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    EdgeIterator operator--(int);

    /**
     * @brief Проверка равенства двух итераторов.
     */
    bool operator==(const EdgeIterator& other) const;

    /**
     * @brief Проверка неравенства двух итераторов.
     */
    bool operator!=(const EdgeIterator& other) const;

    /**
     * @brief Получить текущий индекс ребра.
     */
    std::size_t getIndex() const;

    /**
     * @brief Получить указатель на контейнер рёбер.
     */
    const std::vector<Edge<T>>* getContainer() const;
    std::vector<Edge<T>>* getContainer();

    /**
     * @brief Проверить валидность итератора.
     */
    bool isValid() const;

private:
    std::vector<Edge<T>>* edges_{nullptr}; ///< Указатель на контейнер рёбер
    std::size_t index_{0};                 ///< Текущий индекс в контейнере
};

#include "graph/EdgeIterator.cpp"
