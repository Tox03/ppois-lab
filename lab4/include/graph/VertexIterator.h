#pragma once

#include <cstddef>
#include <iterator>
#include <vector>

/**
 * @brief Двунаправленный итератор вершин графа.
 * Позволяет последовательно обходить вершины графа в прямом и обратном направлениях
 * с возможностью модификации значений вершин.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class VertexIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = T;
    using difference_type = std::ptrdiff_t;
    using pointer = T*;
    using reference = T&;

    /**
     * @brief Конструктор по умолчанию (неинициализированный итератор).
     */
    VertexIterator();

    /**
     * @brief Конструктор итератора с привязкой к вектору вершин и индексу.
     * @param vertices Указатель на вектор вершин.
     * @param index Текущий индекс вершины.
     */
    VertexIterator(std::vector<T>* vertices, std::size_t index);

    /**
     * @brief Оператор разыменования.
     * @return Ссылка на значение текущей вершины.
     */
    reference operator*() const;

    /**
     * @brief Оператор доступа к членам объекта вершины.
     * @return Указатель на значение текущей вершины.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент (переход к следующей вершине).
     */
    VertexIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    VertexIterator operator++(int);

    /**
     * @brief Префиксный декремент (переход к предыдущей вершине).
     */
    VertexIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    VertexIterator operator--(int);

    /**
     * @brief Проверка равенства двух итераторов.
     */
    bool operator==(const VertexIterator& other) const;

    /**
     * @brief Проверка неравенства двух итераторов.
     */
    bool operator!=(const VertexIterator& other) const;

    /**
     * @brief Получить текущий индекс вершины.
     */
    std::size_t getIndex() const;

    /**
     * @brief Получить указатель на контейнер вершин.
     */
    const std::vector<T>* getContainer() const;
    std::vector<T>* getContainer();

    /**
     * @brief Проверить валидность итератора (указывает ли на допустимый элемент).
     */
    bool isValid() const;

private:
    std::vector<T>* vertices_{nullptr}; ///< Указатель на контейнер вершин
    std::size_t index_{0};              ///< Текущий индекс в контейнере
};

#include "graph/VertexIterator.cpp"
