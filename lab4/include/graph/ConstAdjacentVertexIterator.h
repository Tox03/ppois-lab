#pragma once

#include <cstddef>
#include <iterator>
#include <memory>
#include <vector>

template <typename T>
class AdjacentVertexIterator;

/**
 * @brief Константный двунаправленный итератор вершин, смежных с заданной вершиной.
 * Обеспечивает безопасный доступ только для чтения к смежным вершинам.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class ConstAdjacentVertexIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = const T;
    using difference_type = std::ptrdiff_t;
    using pointer = const T*;
    using reference = const T&;

    /**
     * @brief Конструктор по умолчанию.
     */
    ConstAdjacentVertexIterator();

    /**
     * @brief Параметризованный конструктор.
     * @param vertices Указатель на константный вектор вершин графа.
     * @param indices Разделяемый вектор индексов смежных вершин.
     * @param pos Начальная позиция в списке индексов.
     */
    ConstAdjacentVertexIterator(const std::vector<T>* vertices,
                                std::shared_ptr<std::vector<std::size_t>> indices,
                                std::size_t pos);

    /**
     * @brief Конструктор преобразования из неконстантного итератора.
     * @param other Неконстантный итератор смежных вершин.
     */
    ConstAdjacentVertexIterator(const AdjacentVertexIterator<T>& other);

    /**
     * @brief Оператор разыменования (только чтение).
     * @return Константная ссылка на смежную вершину.
     */
    reference operator*() const;

    /**
     * @brief Оператор стрелка (только чтение).
     * @return Константный указатель на смежную вершину.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент.
     */
    ConstAdjacentVertexIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    ConstAdjacentVertexIterator operator++(int);

    /**
     * @brief Префиксный декремент.
     */
    ConstAdjacentVertexIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    ConstAdjacentVertexIterator operator--(int);

    /**
     * @brief Проверка равенства двух итераторов.
     */
    bool operator==(const ConstAdjacentVertexIterator& other) const;

    /**
     * @brief Проверка неравенства двух итераторов.
     */
    bool operator!=(const ConstAdjacentVertexIterator& other) const;

    /**
     * @brief Получить текущую позицию в списке смежных вершин.
     */
    std::size_t getPosition() const;

    /**
     * @brief Получить индекс вершины в основном векторе.
     */
    std::size_t getVertexIndex() const;

    /**
     * @brief Проверить валидность итератора.
     */
    bool isValid() const;

private:
    const std::vector<T>* vertices_{nullptr};                     ///< Указатель на контейнер вершин
    std::shared_ptr<std::vector<std::size_t>> indices_{nullptr};  ///< Список индексов смежных вершин
    std::size_t pos_{0};                                          ///< Текущая позиция в списке
};

#include "graph/ConstAdjacentVertexIterator.cpp"
