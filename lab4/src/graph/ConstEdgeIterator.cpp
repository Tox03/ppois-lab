#ifndef CONST_EDGE_ITERATOR_CPP
#define CONST_EDGE_ITERATOR_CPP

#include "graph/ConstEdgeIterator.h"
#include "graph/EdgeIterator.h"
#include "graph/Edge.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
ConstEdgeIterator<T>::ConstEdgeIterator()
    : edges_(nullptr), index_(0) {
}

// Параметризованный конструктор
template <typename T>
ConstEdgeIterator<T>::ConstEdgeIterator(const std::vector<Edge<T>>* edges, std::size_t index)
    : edges_(edges), index_(index) {
}

// Конструктор преобразования из неконстантного итератора
template <typename T>
ConstEdgeIterator<T>::ConstEdgeIterator(const EdgeIterator<T>& other)
    : edges_(other.getContainer()), index_(other.getIndex()) {
}

// Разыменование
template <typename T>
typename ConstEdgeIterator<T>::reference ConstEdgeIterator<T>::operator*() const {
    if (!edges_ || index_ >= edges_->size()) {
        throw GraphException("Разыменование недействительного константного итератора ребра");
    }
    return (*edges_)[index_];
}

// Оператор стрелка
template <typename T>
typename ConstEdgeIterator<T>::pointer ConstEdgeIterator<T>::operator->() const {
    if (!edges_ || index_ >= edges_->size()) {
        throw GraphException("Доступ по недействительному константному итератору ребра");
    }
    return &(*edges_)[index_];
}

// Префиксный инкремент
template <typename T>
ConstEdgeIterator<T>& ConstEdgeIterator<T>::operator++() {
    ++index_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
ConstEdgeIterator<T> ConstEdgeIterator<T>::operator++(int) {
    ConstEdgeIterator previous_state = *this;
    ++index_;
    return previous_state;
}

// Префиксный декремент
template <typename T>
ConstEdgeIterator<T>& ConstEdgeIterator<T>::operator--() {
    if (index_ == 0) {
        throw GraphException("Выход за левую границу диапазона константного итератора ребра");
    }
    --index_;
    return *this;
}

// Постфиксный декремент
template <typename T>
ConstEdgeIterator<T> ConstEdgeIterator<T>::operator--(int) {
    ConstEdgeIterator previous_state = *this;
    --(*this);
    return previous_state;
}

// Проверка равенства
template <typename T>
bool ConstEdgeIterator<T>::operator==(const ConstEdgeIterator& other) const {
    return edges_ == other.edges_ && index_ == other.index_;
}

// Проверка неравенства
template <typename T>
bool ConstEdgeIterator<T>::operator!=(const ConstEdgeIterator& other) const {
    return !(*this == other);
}

// Получение индекса
template <typename T>
std::size_t ConstEdgeIterator<T>::getIndex() const {
    return index_;
}

// Проверка валидности
template <typename T>
bool ConstEdgeIterator<T>::isValid() const {
    return edges_ != nullptr && index_ < edges_->size();
}

#endif // CONST_EDGE_ITERATOR_CPP
