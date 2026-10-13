#ifndef CONST_ADJACENT_VERTEX_ITERATOR_CPP
#define CONST_ADJACENT_VERTEX_ITERATOR_CPP

#include "graph/ConstAdjacentVertexIterator.h"
#include "graph/AdjacentVertexIterator.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
ConstAdjacentVertexIterator<T>::ConstAdjacentVertexIterator()
    : vertices_(nullptr), indices_(nullptr), pos_(0) {
}

// Параметризованный конструктор
template <typename T>
ConstAdjacentVertexIterator<T>::ConstAdjacentVertexIterator(const std::vector<T>* vertices,
                                                           std::shared_ptr<std::vector<std::size_t>> indices,
                                                           std::size_t pos)
    : vertices_(vertices), indices_(indices), pos_(pos) {
}

// Конструктор преобразования
template <typename T>
ConstAdjacentVertexIterator<T>::ConstAdjacentVertexIterator(const AdjacentVertexIterator<T>& other)
    : vertices_(other.getContainer()), indices_(other.getIndices()), pos_(other.getPosition()) {
}

// Разыменование
template <typename T>
typename ConstAdjacentVertexIterator<T>::reference ConstAdjacentVertexIterator<T>::operator*() const {
    if (!vertices_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Разыменование недействительного константного итератора смежной вершины");
    }
    std::size_t v_idx = (*indices_)[pos_];
    if (v_idx >= vertices_->size()) {
        throw GraphException("Индекс смежной вершины выходит за границы контейнера");
    }
    return (*vertices_)[v_idx];
}

// Оператор стрелка
template <typename T>
typename ConstAdjacentVertexIterator<T>::pointer ConstAdjacentVertexIterator<T>::operator->() const {
    if (!vertices_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Доступ по недействительному константному итератору смежной вершины");
    }
    std::size_t v_idx = (*indices_)[pos_];
    if (v_idx >= vertices_->size()) {
        throw GraphException("Индекс смежной вершины выходит за границы контейнера");
    }
    return &(*vertices_)[v_idx];
}

// Префиксный инкремент
template <typename T>
ConstAdjacentVertexIterator<T>& ConstAdjacentVertexIterator<T>::operator++() {
    ++pos_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
ConstAdjacentVertexIterator<T> ConstAdjacentVertexIterator<T>::operator++(int) {
    ConstAdjacentVertexIterator temp = *this;
    ++pos_;
    return temp;
}

// Префиксный декремент
template <typename T>
ConstAdjacentVertexIterator<T>& ConstAdjacentVertexIterator<T>::operator--() {
    if (pos_ == 0) {
        throw GraphException("Выход за левую границу диапазона константного итератора смежной вершины");
    }
    --pos_;
    return *this;
}

// Постфиксный декремент
template <typename T>
ConstAdjacentVertexIterator<T> ConstAdjacentVertexIterator<T>::operator--(int) {
    ConstAdjacentVertexIterator temp = *this;
    --(*this);
    return temp;
}

// Проверка равенства
template <typename T>
bool ConstAdjacentVertexIterator<T>::operator==(const ConstAdjacentVertexIterator& other) const {
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
bool ConstAdjacentVertexIterator<T>::operator!=(const ConstAdjacentVertexIterator& other) const {
    return !(*this == other);
}

// Текущая позиция
template <typename T>
std::size_t ConstAdjacentVertexIterator<T>::getPosition() const {
    return pos_;
}

// Индекс вершины
template <typename T>
std::size_t ConstAdjacentVertexIterator<T>::getVertexIndex() const {
    if (!indices_ || pos_ >= indices_->size()) {
        throw GraphException("Позиция итератора не указывает на допустимую вершину");
    }
    return (*indices_)[pos_];
}

// Проверка валидности
template <typename T>
bool ConstAdjacentVertexIterator<T>::isValid() const {
    return vertices_ != nullptr && indices_ != nullptr && pos_ < indices_->size();
}

#endif // CONST_ADJACENT_VERTEX_ITERATOR_CPP
