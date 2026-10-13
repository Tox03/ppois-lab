#ifndef CONST_VERTEX_ITERATOR_CPP
#define CONST_VERTEX_ITERATOR_CPP

#include "graph/ConstVertexIterator.h"
#include "graph/VertexIterator.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
ConstVertexIterator<T>::ConstVertexIterator()
    : vertices_(nullptr), index_(0) {
}

// Параметризованный конструктор
template <typename T>
ConstVertexIterator<T>::ConstVertexIterator(const std::vector<T>* vertices, std::size_t index)
    : vertices_(vertices), index_(index) {
}

// Конструктор преобразования из неконстантного итератора
template <typename T>
ConstVertexIterator<T>::ConstVertexIterator(const VertexIterator<T>& other)
    : vertices_(other.getContainer()), index_(other.getIndex()) {
}

// Разыменование
template <typename T>
typename ConstVertexIterator<T>::reference ConstVertexIterator<T>::operator*() const {
    if (!vertices_ || index_ >= vertices_->size()) {
        throw GraphException("Разыменование недействительного константного итератора вершины");
    }
    return (*vertices_)[index_];
}

// Оператор стрелка
template <typename T>
typename ConstVertexIterator<T>::pointer ConstVertexIterator<T>::operator->() const {
    if (!vertices_ || index_ >= vertices_->size()) {
        throw GraphException("Доступ по недействительному константному итератору вершины");
    }
    return &(*vertices_)[index_];
}

// Префиксный инкремент
template <typename T>
ConstVertexIterator<T>& ConstVertexIterator<T>::operator++() {
    ++index_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
ConstVertexIterator<T> ConstVertexIterator<T>::operator++(int) {
    ConstVertexIterator previous_state = *this;
    ++index_;
    return previous_state;
}

// Префиксный декремент
template <typename T>
ConstVertexIterator<T>& ConstVertexIterator<T>::operator--() {
    if (index_ == 0) {
        throw GraphException("Выход за левую границу диапазона константного итератора вершины");
    }
    --index_;
    return *this;
}

// Постфиксный декремент
template <typename T>
ConstVertexIterator<T> ConstVertexIterator<T>::operator--(int) {
    ConstVertexIterator previous_state = *this;
    --(*this);
    return previous_state;
}

// Проверка равенства
template <typename T>
bool ConstVertexIterator<T>::operator==(const ConstVertexIterator& other) const {
    return vertices_ == other.vertices_ && index_ == other.index_;
}

// Проверка неравенства
template <typename T>
bool ConstVertexIterator<T>::operator!=(const ConstVertexIterator& other) const {
    return !(*this == other);
}

// Получение индекса
template <typename T>
std::size_t ConstVertexIterator<T>::getIndex() const {
    return index_;
}

// Проверка валидности
template <typename T>
bool ConstVertexIterator<T>::isValid() const {
    return vertices_ != nullptr && index_ < vertices_->size();
}

#endif // CONST_VERTEX_ITERATOR_CPP
