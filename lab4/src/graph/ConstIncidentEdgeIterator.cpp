#ifndef CONST_INCIDENT_EDGE_ITERATOR_CPP
#define CONST_INCIDENT_EDGE_ITERATOR_CPP

#include "graph/ConstIncidentEdgeIterator.h"
#include "graph/IncidentEdgeIterator.h"
#include "graph/Edge.h"
#include "graph/GraphException.h"

// Конструктор по умолчанию
template <typename T>
ConstIncidentEdgeIterator<T>::ConstIncidentEdgeIterator()
    : edges_(nullptr), indices_(nullptr), pos_(0) {
}

// Параметризованный конструктор
template <typename T>
ConstIncidentEdgeIterator<T>::ConstIncidentEdgeIterator(const std::vector<Edge<T>>* edges,
                                                       std::shared_ptr<std::vector<std::size_t>> indices,
                                                       std::size_t pos)
    : edges_(edges), indices_(indices), pos_(pos) {
}

// Конструктор преобразования
template <typename T>
ConstIncidentEdgeIterator<T>::ConstIncidentEdgeIterator(const IncidentEdgeIterator<T>& other)
    : edges_(other.getContainer()), indices_(other.getIndices()), pos_(other.getPosition()) {
}

// Разыменование
template <typename T>
typename ConstIncidentEdgeIterator<T>::reference ConstIncidentEdgeIterator<T>::operator*() const {
    if (!edges_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Разыменование недействительного константного итератора инцидентного ребра");
    }
    std::size_t edge_idx = (*indices_)[pos_];
    if (edge_idx >= edges_->size()) {
        throw GraphException("Индекс инцидентного ребра выходит за границы контейнера");
    }
    return (*edges_)[edge_idx];
}

// Оператор стрелка
template <typename T>
typename ConstIncidentEdgeIterator<T>::pointer ConstIncidentEdgeIterator<T>::operator->() const {
    if (!edges_ || !indices_ || pos_ >= indices_->size()) {
        throw GraphException("Доступ по недействительному константному итератору инцидентного ребра");
    }
    std::size_t edge_idx = (*indices_)[pos_];
    if (edge_idx >= edges_->size()) {
        throw GraphException("Индекс инцидентного ребра выходит за границы контейнера");
    }
    return &(*edges_)[edge_idx];
}

// Префиксный инкремент
template <typename T>
ConstIncidentEdgeIterator<T>& ConstIncidentEdgeIterator<T>::operator++() {
    ++pos_;
    return *this;
}

// Постфиксный инкремент
template <typename T>
ConstIncidentEdgeIterator<T> ConstIncidentEdgeIterator<T>::operator++(int) {
    ConstIncidentEdgeIterator temp = *this;
    ++pos_;
    return temp;
}

// Префиксный декремент
template <typename T>
ConstIncidentEdgeIterator<T>& ConstIncidentEdgeIterator<T>::operator--() {
    if (pos_ == 0) {
        throw GraphException("Выход за левую границу диапазона константного итератора инцидентного ребра");
    }
    --pos_;
    return *this;
}

// Постфиксный декремент
template <typename T>
ConstIncidentEdgeIterator<T> ConstIncidentEdgeIterator<T>::operator--(int) {
    ConstIncidentEdgeIterator temp = *this;
    --(*this);
    return temp;
}

// Проверка равенства
template <typename T>
bool ConstIncidentEdgeIterator<T>::operator==(const ConstIncidentEdgeIterator& other) const {
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
bool ConstIncidentEdgeIterator<T>::operator!=(const ConstIncidentEdgeIterator& other) const {
    return !(*this == other);
}

// Текущая позиция
template <typename T>
std::size_t ConstIncidentEdgeIterator<T>::getPosition() const {
    return pos_;
}

// Индекс ребра
template <typename T>
std::size_t ConstIncidentEdgeIterator<T>::getEdgeIndex() const {
    if (!indices_ || pos_ >= indices_->size()) {
        throw GraphException("Позиция итератора не указывает на допустимое ребро");
    }
    return (*indices_)[pos_];
}

// Проверка валидности
template <typename T>
bool ConstIncidentEdgeIterator<T>::isValid() const {
    return edges_ != nullptr && indices_ != nullptr && pos_ < indices_->size();
}

#endif // CONST_INCIDENT_EDGE_ITERATOR_CPP
