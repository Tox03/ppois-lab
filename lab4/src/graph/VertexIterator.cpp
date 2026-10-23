#ifndef VERTEX_ITERATOR_CPP
#define VERTEX_ITERATOR_CPP

#include "graph/VertexIterator.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
VertexIterator<T>::VertexIterator()
    : vertices_(nullptr), index_(0) {
}

// Параметризованный конструктор
template <typename T>
VertexIterator<T>::VertexIterator(std::vector<T>* vertices, std::size_t index)
    : vertices_(vertices), index_(index) {
}

// Разыменование
template <typename T>
typename VertexIterator<T>::reference VertexIterator<T>::operator*() const {
    if (!vertices_ || index_ >= vertices_->size()) {
        throw GraphException("Разыменование недействительного итератора вершины");
    }
    return (*vertices_)[index_];
}

// Оператор стрелка
template <typename T>
typename VertexIterator<T>::pointer VertexIterator<T>::operator->() const {
    if (!vertices_ || index_ >= vertices_->size()) {
        throw GraphException("Доступ по недействительному итератору вершины");
    }
    return &(*vertices_)[index_];
}

// Префиксный инкремент
template <typename T>
VertexIterator<T>& VertexIterator<T>::operator++() {
    ++index_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
VertexIterator<T> VertexIterator<T>::operator++(int) {
    VertexIterator previous_state = *this;
    ++index_;
    return previous_state;
}

// Префиксный декремент
template <typename T>
VertexIterator<T>& VertexIterator<T>::operator--() {
    if (index_ == 0) {
        throw GraphException("Выход за левую границу диапазона итератора вершины");
    }
    --index_;
    return *this;
}

// Постфиксный декремент
template <typename T>
VertexIterator<T> VertexIterator<T>::operator--(int) {
    VertexIterator previous_state = *this;
    --(*this);
    return previous_state;
}

// Проверка равенства
template <typename T>
bool VertexIterator<T>::operator==(const VertexIterator& other) const {
    return vertices_ == other.vertices_ && index_ == other.index_;
}

// Проверка неравенства
template <typename T>
bool VertexIterator<T>::operator!=(const VertexIterator& other) const {
    return !(*this == other);
}

// Получение индекса
template <typename T>
std::size_t VertexIterator<T>::getIndex() const {
    return index_;
}

// Получение указателя на контейнер
template <typename T>
const std::vector<T>* VertexIterator<T>::getContainer() const {
    return vertices_;
}

template <typename T>
std::vector<T>* VertexIterator<T>::getContainer() {
    return vertices_;
}

// Проверка валидности
template <typename T>
bool VertexIterator<T>::isValid() const {
    return vertices_ != nullptr && index_ < vertices_->size();
}

#endif // VERTEX_ITERATOR_CPP
