#ifndef ADJACENT_VERTEX_ITERATOR_CPP
#define ADJACENT_VERTEX_ITERATOR_CPP

#include "graph/AdjacentVertexIterator.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
AdjacentVertexIterator<T>::AdjacentVertexIterator()
    : vertices_(nullptr), indices_(nullptr), pos_(0) {
}

// Параметризованный конструктор
template <typename T>
AdjacentVertexIterator<T>::AdjacentVertexIterator(std::vector<T>* vertices,
                                                 std::shared_ptr<std::vector<std::size_t>> indices,
                                                 std::size_t pos)
    : vertices_(vertices), indices_(indices), pos_(pos) {
}

// Разыменование
template <typename T>
typename AdjacentVertexIterator<T>::reference AdjacentVertexIterator<T>::operator*() const {
    if (!vertices_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Разыменование недействительного итератора смежной вершины");
    }
    std::size_t v_idx = (*indices_)[pos_];
    if (v_idx >= vertices_->size()) {
        throw GraphException("Индекс смежной вершины выходит за границы контейнера");
    }
    return (*vertices_)[v_idx];
}

// Оператор стрелка
template <typename T>
typename AdjacentVertexIterator<T>::pointer AdjacentVertexIterator<T>::operator->() const {
    if (!vertices_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Доступ по недействительному итератору смежной вершины");
    }
    std::size_t v_idx = (*indices_)[pos_];
    if (v_idx >= vertices_->size()) {
        throw GraphException("Индекс смежной вершины выходит за границы контейнера");
    }
    return &(*vertices_)[v_idx];
}

// Префиксный инкремент
template <typename T>
AdjacentVertexIterator<T>& AdjacentVertexIterator<T>::operator++() {
    ++pos_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
AdjacentVertexIterator<T> AdjacentVertexIterator<T>::operator++(int) {
    AdjacentVertexIterator temp = *this;
    ++pos_;
    return temp;
}

// Префиксный декремент
template <typename T>
AdjacentVertexIterator<T>& AdjacentVertexIterator<T>::operator--() {
    if (pos_ == 0) {
        throw GraphException("Выход за левую границу диапазона итератора смежной вершины");
    }
    --pos_;
    return *this;
}

// Постфиксный декремент
template <typename T>
AdjacentVertexIterator<T> AdjacentVertexIterator<T>::operator--(int) {
    AdjacentVertexIterator temp = *this;
    --(*this);
    return temp;
}

// Проверка равенства
template <typename T>
bool AdjacentVertexIterator<T>::operator==(const AdjacentVertexIterator& other) const {
    if (vertices_ != other.vertices_) {
        return false;
    }
    if (pos_ != other.pos_) {
        return false;
    }
    if (indices_ == other.indices_) {
        return true;
    }
    if (!indices_ || !other.indices_) {
        return (!indices_ && !other.indices_);
    }
    return *indices_ == *other.indices_;
}

// Проверка неравенства
template <typename T>
bool AdjacentVertexIterator<T>::operator!=(const AdjacentVertexIterator& other) const {
    return !(*this == other);
}

// Позиция в списке смежных вершин
template <typename T>
std::size_t AdjacentVertexIterator<T>::getPosition() const {
    return pos_;
}

// Индекс вершины в общем векторе
template <typename T>
std::size_t AdjacentVertexIterator<T>::getVertexIndex() const {
    if (!indices_ || pos_ >= indices_->size()) {
        throw GraphException("Позиция итератора не указывает на допустимую вершину");
    }
    return (*indices_)[pos_];
}

// Контейнер вершин
template <typename T>
const std::vector<T>* AdjacentVertexIterator<T>::getContainer() const {
    return vertices_;
}

template <typename T>
std::vector<T>* AdjacentVertexIterator<T>::getContainer() {
    return vertices_;
}

// Разделяемый список индексов
template <typename T>
std::shared_ptr<std::vector<std::size_t>> AdjacentVertexIterator<T>::getIndices() const {
    return indices_;
}

// Проверка валидности
template <typename T>
bool AdjacentVertexIterator<T>::isValid() const {
    return vertices_ != nullptr && indices_ != nullptr && pos_ < indices_->size();
}

#endif // ADJACENT_VERTEX_ITERATOR_CPP
