#pragma once

#include <cstddef>
#include <iterator>
#include <memory>
#include <vector>

template <typename T>
class Edge;

/**
 * @brief Двунаправленный итератор рёбер, инцидентных определённой вершине.
 * Позволяет перебирать все рёбра, входящие в вершину или исходящие из неё.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class IncidentEdgeIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = Edge<T>;
    using difference_type = std::ptrdiff_t;
    using pointer = Edge<T>*;
    using reference = Edge<T>&;

    /**
     * @brief Конструктор по умолчанию.
     */
    IncidentEdgeIterator();

    /**
     * @brief Параметризованный конструктор.
     * @param edges Указатель на вектор рёбер графа.
     * @param indices Разделяемый вектор индексов инцидентных рёбер.
     * @param pos Начальная позиция в списке индексов.
     */
    IncidentEdgeIterator(std::vector<Edge<T>>* edges,
                         std::shared_ptr<std::vector<std::size_t>> indices,
                         std::size_t pos);

    /**
     * @brief Оператор разыменования.
     * @return Ссылка на инцидентное ребро.
     */
    reference operator*() const;

    /**
     * @brief Оператор стрелка.
     * @return Указатель на инцидентное ребро.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент.
     */
    IncidentEdgeIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    IncidentEdgeIterator operator++(int);

    /**
     * @brief Префиксный декремент.
     */
    IncidentEdgeIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    IncidentEdgeIterator operator--(int);

    /**
     * @brief Проверка равенства двух итераторов.
     */
    bool operator==(const IncidentEdgeIterator& other) const;

    /**
     * @brief Проверка неравенства двух итераторов.
     */
    bool operator!=(const IncidentEdgeIterator& other) const;

    /**
     * @brief Получить текущую позицию в списке инцидентных рёбер.
     */
    std::size_t getPosition() const;

    /**
     * @brief Получить индекс текущего ребра в графе.
     */
    std::size_t getEdgeIndex() const;

    /**
     * @brief Получить указатель на контейнер рёбер.
     */
    const std::vector<Edge<T>>* getContainer() const;
    std::vector<Edge<T>>* getContainer();

    /**
     * @brief Получить разделяемый список индексов.
     */
    std::shared_ptr<std::vector<std::size_t>> getIndices() const;

    /**
     * @brief Проверить валидность итератора.
     */
    bool isValid() const;

private:
    std::vector<Edge<T>>* edges_{nullptr};                        ///< Указатель на контейнер рёбер
    std::shared_ptr<std::vector<std::size_t>> indices_{nullptr};  ///< Список индексов инцидентных рёбер
    std::size_t pos_{0};                                          ///< Текущая позиция в списке
};

#include "graph/IncidentEdgeIterator.cpp"
