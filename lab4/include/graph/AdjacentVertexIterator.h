#pragma once

#include <cstddef>
#include <iterator>
#include <memory>
#include <vector>

/**
 * @brief Двунаправленный итератор вершин, смежных с заданной вершиной.
 * В ориентированном графе смежными считаются вершины, в которые ведут рёбра из данной вершины.
 * 
 * @tparam T Тип значения вершин графа.
 */
template <typename T>
class AdjacentVertexIterator {
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = T;
    using difference_type = std::ptrdiff_t;
    using pointer = T*;
    using reference = T&;

    /**
     * @brief Конструктор по умолчанию.
     */
    AdjacentVertexIterator();

    /**
     * @brief Параметризованный конструктор.
     * @param vertices Указатель на вектор вершин графа.
     * @param indices Разделяемый вектор индексов смежных вершин.
     * @param pos Начальная позиция в списке индексов.
     */
    AdjacentVertexIterator(std::vector<T>* vertices,
                           std::shared_ptr<std::vector<std::size_t>> indices,
                           std::size_t pos);

    /**
     * @brief Оператор разыменования.
     * @return Ссылка на смежную вершину.
     */
    reference operator*() const;

    /**
     * @brief Оператор стрелка.
     * @return Указатель на смежную вершину.
     */
    pointer operator->() const;

    /**
     * @brief Префиксный инкремент.
     */
    AdjacentVertexIterator& operator++();

    /**
     * @brief Постфиксный инкремент.
     */
    AdjacentVertexIterator operator++(int);

    /**
     * @brief Префиксный декремент.
     */
    AdjacentVertexIterator& operator--();

    /**
     * @brief Постфиксный декремент.
     */
    AdjacentVertexIterator operator--(int);

    /**
     * @brief Проверка равенства двух итераторов.
     */
    bool operator==(const AdjacentVertexIterator& other) const;

    /**
     * @brief Проверка неравенства двух итераторов.
     */
    bool operator!=(const AdjacentVertexIterator& other) const;

    /**
     * @brief Получить текущую позицию в списке смежных вершин.
     */
    std::size_t getPosition() const;

    /**
     * @brief Получить индекс текущей вершины в основном контейнере.
     */
    std::size_t getVertexIndex() const;

    /**
     * @brief Получить указатель на контейнер вершин.
     */
    const std::vector<T>* getContainer() const;
    std::vector<T>* getContainer();

    /**
     * @brief Получить разделяемый список индексов.
     */
    std::shared_ptr<std::vector<std::size_t>> getIndices() const;

    /**
     * @brief Проверить валидность итератора.
     */
    bool isValid() const;

private:
    std::vector<T>* vertices_{nullptr};                           ///< Указатель на контейнер вершин
    std::shared_ptr<std::vector<std::size_t>> indices_{nullptr};  ///< Список индексов смежных вершин
    std::size_t pos_{0};                                          ///< Текущая позиция в списке
};

#include "graph/AdjacentVertexIterator.cpp"
