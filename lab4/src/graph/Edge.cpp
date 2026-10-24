#ifndef EDGE_CPP
#define EDGE_CPP

#include "graph/Edge.h"

// Конструктор по умолчанию
template <typename T>
Edge<T>::Edge()
    : source_(), target_(), id_(0) {
}

// Параметризованный конструктор
template <typename T>
Edge<T>::Edge(const T& source, const T& target, std::size_t id)
    : source_(source), target_(target), id_(id) {
}

// Получение начальной вершины
template <typename T>
const T& Edge<T>::getSource() const {
    return source_;
}

// Получение конечной вершины
template <typename T>
const T& Edge<T>::getTarget() const {
    return target_;
}

// Получение идентификатора
template <typename T>
std::size_t Edge<T>::getId() const {
    return id_;
}

// Установка начальной вершины
template <typename T>
void Edge<T>::setSource(const T& source) {
    source_ = source;
}

// Установка конечной вершины
template <typename T>
void Edge<T>::setTarget(const T& target) {
    target_ = target;
}

// Установка идентификатора
template <typename T>
void Edge<T>::setId(std::size_t id) {
    id_ = id;
}

// Получение ребра в виде пары
template <typename T>
std::pair<T, T> Edge<T>::toPair() const {
    return {source_, target_};
}

// Проверка на петлю
template <typename T>
bool Edge<T>::isLoop() const {
    return source_ == target_;
}

// Оператор равенства
template <typename T>
bool Edge<T>::operator==(const Edge<T>& other) const {
    return source_ == other.source_ && target_ == other.target_;
}

// Оператор неравенства
template <typename T>
bool Edge<T>::operator!=(const Edge<T>& other) const {
    return !(*this == other);
}

// Оператор «меньше»
template <typename T>
bool Edge<T>::operator<(const Edge<T>& other) const {
    if (source_ != other.source_) {
        return source_ < other.source_;
    }
    return target_ < other.target_;
}

// Оператор «меньше или равно»
template <typename T>
bool Edge<T>::operator<=(const Edge<T>& other) const {
    return !(other < *this);
}

// Оператор «больше»
template <typename T>
bool Edge<T>::operator>(const Edge<T>& other) const {
    return other < *this;
}

// Оператор «больше или равно»
template <typename T>
bool Edge<T>::operator>=(const Edge<T>& other) const {
    return !(*this < other);
}

// Оператор вывода в поток
template <typename U>
std::ostream& operator<<(std::ostream& os, const Edge<U>& edge) {
    os << "(" << edge.source_ << " -> " << edge.target_ << ")";
    return os;
}

#endif // EDGE_CPP
