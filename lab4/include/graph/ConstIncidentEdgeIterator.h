#pragma once

#include <cstddef>
#include <iterator>
#include <memory>
#include <vector>

template <typename T>
class Edge;

template <typename T>
class IncidentEdgeIterator;

/**
 * @brief Константный двунаправленный итератор инцидентных рёбер вершины.
 * Обеспечивает безопасный доступ только для чтения к рёбрам, связанным с вершиной.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class ConstIncidentEdgeIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = const Edge<T>;
    using difference_type = std::ptrdiff_t;
    using pointer = const Edge<T>*;
    using reference = const Edge<T>&;

    /**
     * @brief Конструктор по умолчанию.
     */
    ConstIncidentEdgeIterator();

    /**
     * @brief Параметризованный конструктор.
     * @param edges Указатель на константный вектор рёбер графа.
     * @param indices Разделяемый вектор индексов инцидентных рёбер.
     * @param pos Начальная позиция в списке индексов.
     */
    ConstIncidentEdgeIterator(const std::vector<Edge<T>>* edges,
                              std::shared_ptr<std::vector<std::size_t>> indices,
                              std::size_t pos);

    /**
     * @brief Конструктор преобразования из неконстантного итератора.
     * @param other Неконстантный итератор инцидентных рёбер.
     */
    ConstIncidentEdgeIterator(const IncidentEdgeIterator<T>& other);

    /**
     * @brief Оператор разыменования (только чтение).
     * @return Константная ссылка на инцидентное ребро.
     */
    reference operator*() const;

    /**
     * @brief Оператор стрелка (только чтение).
     * @return Константный указатель на инцидентное ребро.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент.
     */
    ConstIncidentEdgeIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    ConstIncidentEdgeIterator operator++(int);

    /**
     * @brief Префиксный декремент.
     */
    ConstIncidentEdgeIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    ConstIncidentEdgeIterator operator--(int);

    /**
     * @brief Проверка равенства двух итераторов.
     */
    bool operator==(const ConstIncidentEdgeIterator& other) const;

    /**
     * @brief Проверка неравенства двух итераторов.
     */
    bool operator!=(const ConstIncidentEdgeIterator& other) const;

    /**
     * @brief Получить текущую позицию в списке инцидентных рёбер.
     */
    std::size_t getPosition() const;

    /**
     * @brief Получить индекс текущего ребра в графе.
     */
    std::size_t getEdgeIndex() const;

    /**
     * @brief Проверить валидность итератора.
     */
    bool isValid() const;

private:
    const std::vector<Edge<T>>* edges_{nullptr};                  ///< Указатель на контейнер рёбер
    std::shared_ptr<std::vector<std::size_t>> indices_{nullptr};  ///< Список индексов инцидентных рёбер
    std::size_t pos_{0};                                          ///< Текущая позиция в списке
};

#include "graph/ConstIncidentEdgeIterator.cpp"
