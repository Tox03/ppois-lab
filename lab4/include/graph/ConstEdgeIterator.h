#pragma once

#include <cstddef>
#include <iterator>
#include <vector>

template <typename T>
class Edge;

template <typename T>
class EdgeIterator;

/**
 * @brief Константный двунаправленный итератор рёбер графа.
 * Обеспечивает безопасный доступ только для чтения к рёбрам графа.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class ConstEdgeIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = const Edge<T>;
    using difference_type = std::ptrdiff_t;
    using pointer = const Edge<T>*;
    using reference = const Edge<T>&;

    /**
     * @brief Конструктор по умолчанию.
     */
    ConstEdgeIterator();

    /**
     * @brief Конструктор константного итератора с привязкой к вектору рёбер и индексу.
     * @param edges Указатель на константный вектор рёбер.
     * @param index Текущий индекс ребра.
     */
    ConstEdgeIterator(const std::vector<Edge<T>>* edges, std::size_t index);

    /**
     * @brief Конструктор преобразования из неконстантного итератора.
     * @param other Неконстантный итератор рёбер.
     */
    ConstEdgeIterator(const EdgeIterator<T>& other);

    /**
     * @brief Оператор разыменования (только чтение).
     * @return Константная ссылка на ребро.
     */
    reference operator*() const;

    /**
     * @brief Оператор стрелка (только чтение).
     * @return Константный указатель на ребро.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент.
     */
    ConstEdgeIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    ConstEdgeIterator operator++(int);

    /**
     * @brief Префиксный декремент.
     */
    ConstEdgeIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    ConstEdgeIterator operator--(int);

    /**
     * @brief Проверка равенства.
     */
    bool operator==(const ConstEdgeIterator& other) const;

    /**
     * @brief Проверка неравенства.
     */
    bool operator!=(const ConstEdgeIterator& other) const;

    /**
     * @brief Получить текущий индекс ребра.
     */
    std::size_t getIndex() const;

    /**
     * @brief Проверить валидность итератора.
     */
    bool isValid() const;

private:
    const std::vector<Edge<T>>* edges_{nullptr}; ///< Указатель на контейнер рёбер
    std::size_t index_{0};                       ///< Текущий индекс в контейнере
};

#include "graph/ConstEdgeIterator.cpp"
