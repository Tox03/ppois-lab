#ifndef EDGE_ITERATOR_CPP
#define EDGE_ITERATOR_CPP

#include "graph/EdgeIterator.h"
#include "graph/Edge.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
EdgeIterator<T>::EdgeIterator()
    : edges_(nullptr), index_(0) {
}

// Параметризованный конструктор
template <typename T>
EdgeIterator<T>::EdgeIterator(std::vector<Edge<T>>* edges, std::size_t index)
    : edges_(edges), index_(index) {
}

// Разыменование
template <typename T>
typename EdgeIterator<T>::reference EdgeIterator<T>::operator*() const {
    if (!edges_ || index_ >= edges_->size()) {
        throw GraphException("Разыменование недействительного итератора ребра");
    }
    return (*edges_)[index_];
}

// Оператор стрелка
template <typename T>
typename EdgeIterator<T>::pointer EdgeIterator<T>::operator->() const {
    if (!edges_ || index_ >= edges_->size()) {
        throw GraphException("Доступ по недействительному итератору ребра");
    }
    return &(*edges_)[index_];
}

// Префиксный инкремент
template <typename T>
EdgeIterator<T>& EdgeIterator<T>::operator++() {
    ++index_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
EdgeIterator<T> EdgeIterator<T>::operator++(int) {
    EdgeIterator previous_state = *this;
    ++index_;
    return previous_state;
}

// Префиксный декремент
template <typename T>
EdgeIterator<T>& EdgeIterator<T>::operator--() {
    if (index_ == 0) {
        throw GraphException("Выход за левую границу диапазона итератора ребра");
    }
    --index_;
    return *this;
}

// Постфиксный декремент
template <typename T>
EdgeIterator<T> EdgeIterator<T>::operator--(int) {
    EdgeIterator previous_state = *this;
    --(*this);
    return previous_state;
}

// Проверка равенства
template <typename T>
bool EdgeIterator<T>::operator==(const EdgeIterator& other) const {
    return edges_ == other.edges_ && index_ == other.index_;
}

// Проверка неравенства
template <typename T>
bool EdgeIterator<T>::operator!=(const EdgeIterator& other) const {
    return !(*this == other);
}

// Получение индекса
template <typename T>
std::size_t EdgeIterator<T>::getIndex() const {
    return index_;
}

// Получение контейнера
template <typename T>
const std::vector<Edge<T>>* EdgeIterator<T>::getContainer() const {
    return edges_;
}

template <typename T>
std::vector<Edge<T>>* EdgeIterator<T>::getContainer() {
    return edges_;
}

// Проверка валидности
template <typename T>
bool EdgeIterator<T>::isValid() const {
    return edges_ != nullptr && index_ < edges_->size();
}

#endif // EDGE_ITERATOR_CPP
