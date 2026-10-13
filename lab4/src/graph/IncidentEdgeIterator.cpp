#ifndef INCIDENT_EDGE_ITERATOR_CPP
#define INCIDENT_EDGE_ITERATOR_CPP

#include "graph/IncidentEdgeIterator.h"
#include "graph/Edge.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
IncidentEdgeIterator<T>::IncidentEdgeIterator()
    : edges_(nullptr), indices_(nullptr), pos_(0) {
}

// Параметризованный конструктор
template <typename T>
IncidentEdgeIterator<T>::IncidentEdgeIterator(std::vector<Edge<T>>* edges,
                                             std::shared_ptr<std::vector<std::size_t>> indices,
                                             std::size_t pos)
    : edges_(edges), indices_(indices), pos_(pos) {
}

// Разыменование
template <typename T>
typename IncidentEdgeIterator<T>::reference IncidentEdgeIterator<T>::operator*() const {
    if (!edges_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Разыменование недействительного итератора инцидентного ребра");
    }
    std::size_t edge_idx = (*indices_)[pos_];
    if (edge_idx >= edges_->size()) {
        throw GraphException("Индекс инцидентного ребра выходит за границы контейнера");
    }
    return (*edges_)[edge_idx];
}

// Оператор стрелка
template <typename T>
typename IncidentEdgeIterator<T>::pointer IncidentEdgeIterator<T>::operator->() const {
    if (!edges_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Доступ по недействительному итератору инцидентного ребра");
    }
    std::size_t edge_idx = (*indices_)[pos_];
    if (edge_idx >= edges_->size()) {
        throw GraphException("Индекс инцидентного ребра выходит за границы контейнера");
    }
    return &(*edges_)[edge_idx];
}

// Префиксный инкремент
template <typename T>
IncidentEdgeIterator<T>& IncidentEdgeIterator<T>::operator++() {
    ++pos_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
IncidentEdgeIterator<T> IncidentEdgeIterator<T>::operator++(int) {
    IncidentEdgeIterator temp = *this;
    ++pos_;
    return temp;
}

// Префиксный декремент
template <typename T>
IncidentEdgeIterator<T>& IncidentEdgeIterator<T>::operator--() {
    if (pos_ == 0) {
        throw GraphException("Выход за левую границу диапазона итератора инцидентного ребра");
    }
    --pos_;
    return *this;
}

// Постфиксный декремент
template <typename T>
IncidentEdgeIterator<T> IncidentEdgeIterator<T>::operator--(int) {
    IncidentEdgeIterator temp = *this;
    --(*this);
    return temp;
}

// Проверка равенства
template <typename T>
bool IncidentEdgeIterator<T>::operator==(const IncidentEdgeIterator& other) const {
    if (edges_ != other.edges_) {
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
bool IncidentEdgeIterator<T>::operator!=(const IncidentEdgeIterator& other) const {
    return !(*this == other);
}

// Текущая позиция в списке
template <typename T>
std::size_t IncidentEdgeIterator<T>::getPosition() const {
    return pos_;
}

// Индекс ребра в общем контейнере
template <typename T>
std::size_t IncidentEdgeIterator<T>::getEdgeIndex() const {
    if (!indices_ || pos_ >= indices_->size()) {
        throw GraphException("Позиция итератора не указывает на допустимое ребро");
    }
    return (*indices_)[pos_];
}

// Контейнер рёбер
template <typename T>
const std::vector<Edge<T>>* IncidentEdgeIterator<T>::getContainer() const {
    return edges_;
}

template <typename T>
std::vector<Edge<T>>* IncidentEdgeIterator<T>::getContainer() {
    return edges_;
}

// Разделяемый список индексов
template <typename T>
std::shared_ptr<std::vector<std::size_t>> IncidentEdgeIterator<T>::getIndices() const {
    return indices_;
}

// Проверка валидности
template <typename T>
bool IncidentEdgeIterator<T>::isValid() const {
    return edges_ != nullptr && indices_ != nullptr && pos_ < indices_->size();
}

#endif // INCIDENT_EDGE_ITERATOR_CPP
