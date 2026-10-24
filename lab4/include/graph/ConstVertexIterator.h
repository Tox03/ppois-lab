#pragma once

#include <cstddef>
#include <iterator>
#include <vector>

template <typename T>
class VertexIterator;

/**
 * @brief Константный двунаправленный итератор вершин графа.
 * Обеспечивает безопасный доступ только для чтения к вершинам графа.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class ConstVertexIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = const T;
    using difference_type = std::ptrdiff_t;
    using pointer = const T*;
    using reference = const T&;

    /**
     * @brief Конструктор по умолчанию.
     */
    ConstVertexIterator();

    /**
     * @brief Конструктор константного итератора с привязкой к вектору вершин и индексу.
     * @param vertices Указатель на константный вектор вершин.
     * @param index Текущий индекс вершины.
     */
    ConstVertexIterator(const std::vector<T>* vertices, std::size_t index);

    /**
     * @brief Конструктор преобразования из неконстантного итератора.
     * @param other Неконстантный итератор вершин.
     */
    ConstVertexIterator(const VertexIterator<T>& other);

    /**
     * @brief Оператор разыменования (только чтение).
     * @return Константная ссылка на вершину.
     */
    reference operator*() const;

    /**
     * @brief Оператор стрелка (только чтение).
     * @return Константный указатель на вершину.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент.
     */
    ConstVertexIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    ConstVertexIterator operator++(int);

    /**
     * @brief Префиксный декремент.
     */
    ConstVertexIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    ConstVertexIterator operator--(int);

    /**
     * @brief Проверка равенства двух константных итераторов.
     */
    bool operator==(const ConstVertexIterator& other) const;

    /**
     * @brief Проверка неравенства двух константных итераторов.
     */
    bool operator!=(const ConstVertexIterator& other) const;

    /**
     * @brief Получить текущий индекс вершины.
     */
    std::size_t getIndex() const;

    /**
     * @brief Проверить валидность итератора.
     */
    bool isValid() const;

private:
    const std::vector<T>* vertices_{nullptr}; ///< Указатель на константный контейнер вершин
    std::size_t index_{0};                    ///< Текущий индекс в контейнере
};

#include "graph/ConstVertexIterator.cpp"
