#ifndef DIRECTED_INCIDENCE_MATRIX_GRAPH_CPP
#define DIRECTED_INCIDENCE_MATRIX_GRAPH_CPP

#include "graph/DirectedIncidenceMatrixGraph.h"
#include <iomanip>

// Конструктор по умолчанию
template <typename T>
DirectedIncidenceMatrixGraph<T>::DirectedIncidenceMatrixGraph()
    : vertices_(), edges_(), matrix_() {
}

// Конструктор копирования
template <typename T>
DirectedIncidenceMatrixGraph<T>::DirectedIncidenceMatrixGraph(const DirectedIncidenceMatrixGraph& other)
    : vertices_(other.vertices_), edges_(other.edges_), matrix_(other.matrix_) {
}

// Конструктор перемещения
template <typename T>
DirectedIncidenceMatrixGraph<T>::DirectedIncidenceMatrixGraph(DirectedIncidenceMatrixGraph&& other) noexcept
    : vertices_(std::move(other.vertices_)),
      edges_(std::move(other.edges_)),
      matrix_(std::move(other.matrix_)) {
}

// Оператор присваивания копированием
template <typename T>
DirectedIncidenceMatrixGraph<T>& DirectedIncidenceMatrixGraph<T>::operator=(const DirectedIncidenceMatrixGraph& other) {
    if (this != &other) {
        vertices_ = other.vertices_;
        edges_ = other.edges_;
        matrix_ = other.matrix_;
    }
    return *this;
}

// Оператор присваивания перемещением
template <typename T>
DirectedIncidenceMatrixGraph<T>& DirectedIncidenceMatrixGraph<T>::operator=(DirectedIncidenceMatrixGraph&& other) noexcept {
    if (this != &other) {
        vertices_ = std::move(other.vertices_);
        edges_ = std::move(other.edges_);
        matrix_ = std::move(other.matrix_);
    }
    return *this;
}

// Проверка на пустоту
template <typename T>
bool DirectedIncidenceMatrixGraph<T>::empty() const noexcept {
    return vertices_.empty();
}

template <typename T>
bool DirectedIncidenceMatrixGraph<T>::is_empty() const noexcept {
    return empty();
}

// Количество вершин
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type DirectedIncidenceMatrixGraph<T>::vertex_count() const noexcept {
    return vertices_.size();
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type DirectedIncidenceMatrixGraph<T>::size() const noexcept {
    return vertex_count();
}

// Количество рёбер
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type DirectedIncidenceMatrixGraph<T>::edge_count() const noexcept {
    return edges_.size();
}

// Очистка графа
template <typename T>
void DirectedIncidenceMatrixGraph<T>::clear() noexcept {
    vertices_.clear();
    edges_.clear();
    matrix_.clear();
}

// Поиск индекса вершины
template <typename T>
std::size_t DirectedIncidenceMatrixGraph<T>::findVertexIndex(const T& v) const {
    for (std::size_t i = 0; i < vertices_.size(); ++i) {
        if (vertices_[i] == v) {
            return i;
        }
    }
    throw GraphException("Вершина не найдена в графе");
}

// Поиск индекса ребра
template <typename T>
std::size_t DirectedIncidenceMatrixGraph<T>::findEdgeIndex(const T& from, const T& to) const {
    for (std::size_t i = 0; i < edges_.size(); ++i) {
        if (edges_[i].getSource() == from && edges_[i].getTarget() == to) {
            return i;
        }
    }
    throw GraphException("Ребро не найдено в графе");
}

// Проверка наличия вершины
template <typename T>
bool DirectedIncidenceMatrixGraph<T>::has_vertex(const T& v) const {
    for (const auto& vertex : vertices_) {
        if (vertex == v) {
            return true;
        }
    }
    return false;
}

// Проверка наличия ребра по вершинам
template <typename T>
bool DirectedIncidenceMatrixGraph<T>::has_edge(const T& from, const T& to) const {
    for (const auto& edge : edges_) {
        if (edge.getSource() == from && edge.getTarget() == to) {
            return true;
        }
    }
    return false;
}

// Проверка наличия ребра по объекту Edge
template <typename T>
bool DirectedIncidenceMatrixGraph<T>::has_edge(const Edge<T>& e) const {
    return has_edge(e.getSource(), e.getTarget());
}

// Доступ по индексу с проверкой границ
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reference
DirectedIncidenceMatrixGraph<T>::at(size_type index) {
    if (index >= vertices_.size()) {
        throw GraphException("Индекс вершины выходит за пределы диапазона");
    }
    return vertices_[index];
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reference
DirectedIncidenceMatrixGraph<T>::at(size_type index) const {
    if (index >= vertices_.size()) {
        throw GraphException("Индекс вершины выходит за пределы диапазона");
    }
    return vertices_[index];
}

// Оператор индексации
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reference
DirectedIncidenceMatrixGraph<T>::operator[](size_type index) {
    return vertices_[index];
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reference
DirectedIncidenceMatrixGraph<T>::operator[](size_type index) const {
    return vertices_[index];
}

// Поиск вершины с возвратом итератора
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::vertex_iterator
DirectedIncidenceMatrixGraph<T>::find_vertex(const T& v) {
    for (std::size_t i = 0; i < vertices_.size(); ++i) {
        if (vertices_[i] == v) {
            return vertex_iterator(&vertices_, i);
        }
    }
    return end();
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_vertex_iterator
DirectedIncidenceMatrixGraph<T>::find_vertex(const T& v) const {
    for (std::size_t i = 0; i < vertices_.size(); ++i) {
        if (vertices_[i] == v) {
            return const_vertex_iterator(&vertices_, i);
        }
    }
    return end();
}

// Поиск ребра с возвратом итератора
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::edge_iterator
DirectedIncidenceMatrixGraph<T>::find_edge(const T& from, const T& to) {
    for (std::size_t i = 0; i < edges_.size(); ++i) {
        if (edges_[i].getSource() == from && edges_[i].getTarget() == to) {
            return edge_iterator(&edges_, i);
        }
    }
    return edges_end();
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_edge_iterator
DirectedIncidenceMatrixGraph<T>::find_edge(const T& from, const T& to) const {
    for (std::size_t i = 0; i < edges_.size(); ++i) {
        if (edges_[i].getSource() == from && edges_[i].getTarget() == to) {
            return const_edge_iterator(&edges_, i);
        }
    }
    return edges_end();
}

// Добавление вершины
template <typename T>
void DirectedIncidenceMatrixGraph<T>::add_vertex(const T& v) {
    if (has_vertex(v)) {
        throw GraphException("Вершина уже существует в графе");
    }
    vertices_.push_back(v);
    matrix_.push_back(std::vector<int>(edges_.size(), INCIDENCE_NONE));
}

// Добавление ребра
template <typename T>
void DirectedIncidenceMatrixGraph<T>::add_edge(const T& from, const T& to) {
    std::size_t source_vertex_idx = findVertexIndex(from);
    std::size_t target_vertex_idx = findVertexIndex(to);

    if (has_edge(from, to)) {
        throw GraphException("Ребро между указанными вершинами уже существует");
    }

    std::size_t edge_id = edges_.size() + 1;
    edges_.emplace_back(from, to, edge_id);

    // Добавляем новый столбец в матрицу инцидентности
    for (std::size_t vertex_idx = 0; vertex_idx < vertices_.size(); ++vertex_idx) {
        if (source_vertex_idx == target_vertex_idx) {
            // Петля
            matrix_[vertex_idx].push_back(vertex_idx == source_vertex_idx ? INCIDENCE_LOOP : INCIDENCE_NONE);
        } else {
            if (vertex_idx == source_vertex_idx) {
                matrix_[vertex_idx].push_back(INCIDENCE_OUTGOING); // Исходное ребро
            } else if (vertex_idx == target_vertex_idx) {
                matrix_[vertex_idx].push_back(INCIDENCE_INCOMING);  // Входящее ребро
            } else {
                matrix_[vertex_idx].push_back(INCIDENCE_NONE);
            }
        }
    }
}

template <typename T>
void DirectedIncidenceMatrixGraph<T>::add_edge(const Edge<T>& e) {
    add_edge(e.getSource(), e.getTarget());
}

// Удаление ребра по вершинам
template <typename T>
bool DirectedIncidenceMatrixGraph<T>::remove_edge(const T& from, const T& to) {
    std::size_t column_idx = findEdgeIndex(from, to);
    edges_.erase(edges_.begin() + column_idx);

    for (std::size_t vertex_idx = 0; vertex_idx < vertices_.size(); ++vertex_idx) {
        matrix_[vertex_idx].erase(matrix_[vertex_idx].begin() + column_idx);
    }
    return true;
}

template <typename T>
bool DirectedIncidenceMatrixGraph<T>::remove_edge(const Edge<T>& e) {
    return remove_edge(e.getSource(), e.getTarget());
}

// Удаление ребра по итератору
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::edge_iterator
DirectedIncidenceMatrixGraph<T>::remove_edge(edge_iterator pos) {
    if (!pos.isValid() || pos.getContainer() != &edges_) {
        throw GraphException("Некорректный итератор ребра для удаления");
    }
    std::size_t column_idx = pos.getIndex();
    edges_.erase(edges_.begin() + column_idx);

    for (std::size_t vertex_idx = 0; vertex_idx < vertices_.size(); ++vertex_idx) {
        matrix_[vertex_idx].erase(matrix_[vertex_idx].begin() + column_idx);
    }
    return edge_iterator(&edges_, column_idx);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::edge_iterator
DirectedIncidenceMatrixGraph<T>::erase(edge_iterator pos) {
    return remove_edge(pos);
}

// Удаление вершины
template <typename T>
bool DirectedIncidenceMatrixGraph<T>::remove_vertex(const T& v) {
    std::size_t vertex_row_idx = findVertexIndex(v);

    // Находим все столбцы инцидентных рёбер
    std::vector<std::size_t> cols_to_remove;
    for (std::size_t column_idx = 0; column_idx < edges_.size(); ++column_idx) {
        if (matrix_[vertex_row_idx][column_idx] != INCIDENCE_NONE) {
            cols_to_remove.push_back(column_idx);
        }
    }

    // Удаляем рёбра в порядке убывания индексов столбцов
    std::sort(cols_to_remove.rbegin(), cols_to_remove.rend());
    for (std::size_t col_to_erase : cols_to_remove) {
        edges_.erase(edges_.begin() + col_to_erase);
        for (std::size_t vertex_idx = 0; vertex_idx < vertices_.size(); ++vertex_idx) {
            matrix_[vertex_idx].erase(matrix_[vertex_idx].begin() + col_to_erase);
        }
    }

    // Удаляем строку из матрицы и саму вершину
    matrix_.erase(matrix_.begin() + vertex_row_idx);
    vertices_.erase(vertices_.begin() + vertex_row_idx);

    return true;
}

// Удаление вершины по итератору
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::vertex_iterator
DirectedIncidenceMatrixGraph<T>::remove_vertex(vertex_iterator pos) {
    if (!pos.isValid() || pos.getContainer() != &vertices_) {
        throw GraphException("Некорректный итератор вершины для удаления");
    }
    std::size_t row = pos.getIndex();
    T val = vertices_[row];
    remove_vertex(val);
    return vertex_iterator(&vertices_, row);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::vertex_iterator
DirectedIncidenceMatrixGraph<T>::erase(vertex_iterator pos) {
    return remove_vertex(pos);
}

// Степень захода вершины
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type
DirectedIncidenceMatrixGraph<T>::vertex_in_degree(const T& v) const {
    std::size_t vertex_row_idx = findVertexIndex(v);
    size_type count = 0;
    for (std::size_t edge_col_idx = 0; edge_col_idx < edges_.size(); ++edge_col_idx) {
        if (matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_INCOMING ||
            matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_LOOP) {
            ++count;
        }
    }
    return count;
}

// Степень исхода вершины
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type
DirectedIncidenceMatrixGraph<T>::vertex_out_degree(const T& v) const {
    std::size_t vertex_row_idx = findVertexIndex(v);
    size_type count = 0;
    for (std::size_t edge_col_idx = 0; edge_col_idx < edges_.size(); ++edge_col_idx) {
        if (matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_OUTGOING ||
            matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_LOOP) {
            ++count;
        }
    }
    return count;
}

// Общая степень вершины
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type
DirectedIncidenceMatrixGraph<T>::vertex_degree(const T& v) const {
    std::size_t vertex_row_idx = findVertexIndex(v);
    size_type count = 0;
    for (std::size_t edge_col_idx = 0; edge_col_idx < edges_.size(); ++edge_col_idx) {
        if (matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_OUTGOING ||
            matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_INCOMING) {
            ++count;
        } else if (matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_LOOP) {
            count += 2;
        }
    }
    return count;
}

// Степень ребра
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type
DirectedIncidenceMatrixGraph<T>::edge_degree(const Edge<T>& e) const {
    std::size_t target_col = findEdgeIndex(e.getSource(), e.getTarget());
    std::size_t source_vertex_idx = findVertexIndex(e.getSource());
    std::size_t target_vertex_idx = findVertexIndex(e.getTarget());

    size_type count = 0;
    for (std::size_t edge_col_idx = 0; edge_col_idx < edges_.size(); ++edge_col_idx) {
        if (edge_col_idx == target_col) {
            continue;
        }
        if (matrix_[source_vertex_idx][edge_col_idx] != INCIDENCE_NONE ||
            matrix_[target_vertex_idx][edge_col_idx] != INCIDENCE_NONE) {
            ++count;
        }
    }
    return count;
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::size_type
DirectedIncidenceMatrixGraph<T>::edge_degree(const T& from, const T& to) const {
    std::size_t column_idx = findEdgeIndex(from, to);
    return edge_degree(edges_[column_idx]);
}

// Индексы инцидентных рёбер
template <typename T>
std::shared_ptr<std::vector<std::size_t>>
DirectedIncidenceMatrixGraph<T>::getIncidentEdgeIndices(const T& v) const {
    std::size_t vertex_row_idx = findVertexIndex(v);
    auto indices = std::make_shared<std::vector<std::size_t>>();
    for (std::size_t edge_col_idx = 0; edge_col_idx < edges_.size(); ++edge_col_idx) {
        if (matrix_[vertex_row_idx][edge_col_idx] != INCIDENCE_NONE) {
            indices->push_back(edge_col_idx);
        }
    }
    return indices;
}

// Индексы смежных вершин
template <typename T>
std::shared_ptr<std::vector<std::size_t>>
DirectedIncidenceMatrixGraph<T>::getAdjacentVertexIndices(const T& v) const {
    std::size_t vertex_row_idx = findVertexIndex(v);
    auto indices = std::make_shared<std::vector<std::size_t>>();
    for (std::size_t edge_col_idx = 0; edge_col_idx < edges_.size(); ++edge_col_idx) {
        if (matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_OUTGOING) {
            // Ищем приёмник (где INCIDENCE_INCOMING)
            for (std::size_t target_row_idx = 0; target_row_idx < vertices_.size(); ++target_row_idx) {
                if (matrix_[target_row_idx][edge_col_idx] == INCIDENCE_INCOMING) {
                    if (std::find(indices->begin(), indices->end(), target_row_idx) == indices->end()) {
                        indices->push_back(target_row_idx);
                    }
                    break;
                }
            }
        } else if (matrix_[vertex_row_idx][edge_col_idx] == INCIDENCE_LOOP) {
            // Петля
            if (std::find(indices->begin(), indices->end(), vertex_row_idx) == indices->end()) {
                indices->push_back(vertex_row_idx);
            }
        }
    }
    return indices;
}

// Итераторы вершин
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::vertex_iterator DirectedIncidenceMatrixGraph<T>::begin() {
    return vertex_iterator(&vertices_, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::vertex_iterator DirectedIncidenceMatrixGraph<T>::end() {
    return vertex_iterator(&vertices_, vertices_.size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_vertex_iterator DirectedIncidenceMatrixGraph<T>::begin() const {
    return const_vertex_iterator(&vertices_, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_vertex_iterator DirectedIncidenceMatrixGraph<T>::end() const {
    return const_vertex_iterator(&vertices_, vertices_.size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_vertex_iterator DirectedIncidenceMatrixGraph<T>::cbegin() const {
    return const_vertex_iterator(&vertices_, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_vertex_iterator DirectedIncidenceMatrixGraph<T>::cend() const {
    return const_vertex_iterator(&vertices_, vertices_.size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_vertex_iterator DirectedIncidenceMatrixGraph<T>::rbegin() {
    return reverse_vertex_iterator(end());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_vertex_iterator DirectedIncidenceMatrixGraph<T>::rend() {
    return reverse_vertex_iterator(begin());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_vertex_iterator DirectedIncidenceMatrixGraph<T>::rbegin() const {
    return const_reverse_vertex_iterator(end());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_vertex_iterator DirectedIncidenceMatrixGraph<T>::rend() const {
    return const_reverse_vertex_iterator(begin());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_vertex_iterator DirectedIncidenceMatrixGraph<T>::crbegin() const {
    return const_reverse_vertex_iterator(cend());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_vertex_iterator DirectedIncidenceMatrixGraph<T>::crend() const {
    return const_reverse_vertex_iterator(cbegin());
}

// Итераторы рёбер
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::edge_iterator DirectedIncidenceMatrixGraph<T>::edges_begin() {
    return edge_iterator(&edges_, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::edge_iterator DirectedIncidenceMatrixGraph<T>::edges_end() {
    return edge_iterator(&edges_, edges_.size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_begin() const {
    return const_edge_iterator(&edges_, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_end() const {
    return const_edge_iterator(&edges_, edges_.size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_cbegin() const {
    return const_edge_iterator(&edges_, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_cend() const {
    return const_edge_iterator(&edges_, edges_.size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_rbegin() {
    return reverse_edge_iterator(edges_end());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_rend() {
    return reverse_edge_iterator(edges_begin());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_rbegin() const {
    return const_reverse_edge_iterator(edges_end());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_rend() const {
    return const_reverse_edge_iterator(edges_begin());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_crbegin() const {
    return const_reverse_edge_iterator(edges_cend());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_edge_iterator DirectedIncidenceMatrixGraph<T>::edges_crend() const {
    return const_reverse_edge_iterator(edges_cbegin());
}

// Итераторы инцидентных рёбер
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_begin(const T& v) {
    auto indices = getIncidentEdgeIndices(v);
    return incident_edge_iterator(&edges_, indices, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_end(const T& v) {
    auto indices = getIncidentEdgeIndices(v);
    return incident_edge_iterator(&edges_, indices, indices->size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_begin(const T& v) const {
    return incident_edges_cbegin(v);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_end(const T& v) const {
    return incident_edges_cend(v);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_cbegin(const T& v) const {
    auto indices = getIncidentEdgeIndices(v);
    return const_incident_edge_iterator(&edges_, indices, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_cend(const T& v) const {
    auto indices = getIncidentEdgeIndices(v);
    return const_incident_edge_iterator(&edges_, indices, indices->size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_rbegin(const T& v) {
    return reverse_incident_edge_iterator(incident_edges_end(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_rend(const T& v) {
    return reverse_incident_edge_iterator(incident_edges_begin(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_rbegin(const T& v) const {
    return const_reverse_incident_edge_iterator(incident_edges_end(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_rend(const T& v) const {
    return const_reverse_incident_edge_iterator(incident_edges_begin(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_crbegin(const T& v) const {
    return const_reverse_incident_edge_iterator(incident_edges_cend(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_incident_edge_iterator
DirectedIncidenceMatrixGraph<T>::incident_edges_crend(const T& v) const {
    return const_reverse_incident_edge_iterator(incident_edges_cbegin(v));
}

// Итераторы смежных вершин
template <typename T>
typename DirectedIncidenceMatrixGraph<T>::adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_begin(const T& v) {
    auto indices = getAdjacentVertexIndices(v);
    return adjacent_vertex_iterator(&vertices_, indices, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_end(const T& v) {
    auto indices = getAdjacentVertexIndices(v);
    return adjacent_vertex_iterator(&vertices_, indices, indices->size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_begin(const T& v) const {
    return adjacent_vertices_cbegin(v);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_end(const T& v) const {
    return adjacent_vertices_cend(v);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_cbegin(const T& v) const {
    auto indices = getAdjacentVertexIndices(v);
    return const_adjacent_vertex_iterator(&vertices_, indices, 0);
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_cend(const T& v) const {
    auto indices = getAdjacentVertexIndices(v);
    return const_adjacent_vertex_iterator(&vertices_, indices, indices->size());
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_rbegin(const T& v) {
    return reverse_adjacent_vertex_iterator(adjacent_vertices_end(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::reverse_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_rend(const T& v) {
    return reverse_adjacent_vertex_iterator(adjacent_vertices_begin(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_rbegin(const T& v) const {
    return const_reverse_adjacent_vertex_iterator(adjacent_vertices_end(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_rend(const T& v) const {
    return const_reverse_adjacent_vertex_iterator(adjacent_vertices_begin(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_crbegin(const T& v) const {
    return const_reverse_adjacent_vertex_iterator(adjacent_vertices_cend(v));
}

template <typename T>
typename DirectedIncidenceMatrixGraph<T>::const_reverse_adjacent_vertex_iterator
DirectedIncidenceMatrixGraph<T>::adjacent_vertices_crend(const T& v) const {
    return const_reverse_adjacent_vertex_iterator(adjacent_vertices_cbegin(v));
}

// Сравнение графов
template <typename T>
bool DirectedIncidenceMatrixGraph<T>::operator==(const DirectedIncidenceMatrixGraph& other) const {
    return vertices_ == other.vertices_ &&
           edges_ == other.edges_ &&
           matrix_ == other.matrix_;
}

template <typename T>
bool DirectedIncidenceMatrixGraph<T>::operator!=(const DirectedIncidenceMatrixGraph& other) const {
    return !(*this == other);
}

template <typename T>
bool DirectedIncidenceMatrixGraph<T>::operator<(const DirectedIncidenceMatrixGraph& other) const {
    if (vertices_.size() != other.vertices_.size()) {
        return vertices_.size() < other.vertices_.size();
    }
    if (edges_.size() != other.edges_.size()) {
        return edges_.size() < other.edges_.size();
    }
    if (vertices_ != other.vertices_) {
        return vertices_ < other.vertices_;
    }
    if (edges_ != other.edges_) {
        return edges_ < other.edges_;
    }
    return matrix_ < other.matrix_;
}

template <typename T>
bool DirectedIncidenceMatrixGraph<T>::operator<=(const DirectedIncidenceMatrixGraph& other) const {
    return (*this < other) || (*this == other);
}

template <typename T>
bool DirectedIncidenceMatrixGraph<T>::operator>(const DirectedIncidenceMatrixGraph& other) const {
    return other < *this;
}

template <typename T>
bool DirectedIncidenceMatrixGraph<T>::operator>=(const DirectedIncidenceMatrixGraph& other) const {
    return !(*this < other);
}

// Получение матрицы инцидентности
template <typename T>
const std::vector<std::vector<int>>& DirectedIncidenceMatrixGraph<T>::getIncidenceMatrix() const {
    return matrix_;
}

// Печать матрицы инцидентности
template <typename T>
void DirectedIncidenceMatrixGraph<T>::printIncidenceMatrix(std::ostream& os) const {
    os << "Матрица инцидентности (" << vertices_.size() << " вершин x " << edges_.size() << " рёбер):\n";
    if (vertices_.empty() || edges_.empty()) {
        os << "  (матрица пуста)\n";
        return;
    }

    // Заголовок столбцов (рёбра)
    os << std::setw(12) << "Вершина \\ Ребро";
    for (std::size_t j = 0; j < edges_.size(); ++j) {
        os << std::setw(6) << ("e" + std::to_string(j + 1));
    }
    os << "\n";

    // Строки (вершины)
    for (std::size_t i = 0; i < vertices_.size(); ++i) {
        os << std::setw(12) << vertices_[i];
        for (std::size_t j = 0; j < edges_.size(); ++j) {
            os << std::setw(6) << matrix_[i][j];
        }
        os << "\n";
    }
}

// Текстовое представление с использованием итераторов и std::for_each
template <typename U>
std::ostream& operator<<(std::ostream& os, const DirectedIncidenceMatrixGraph<U>& graph) {
    os << "Ориентированный граф (матрица инцидентности) [Вершин: "
       << graph.vertex_count() << ", Рёбер: " << graph.edge_count() << "]:\n";
    os << "  Вершины: [";
    bool first_v = true;
    std::for_each(graph.cbegin(), graph.cend(), [&](const U& v) {
        if (!first_v) {
            os << ", ";
        }
        os << v;
        first_v = false;
    });
    os << "]\n  Рёбра:\n";
    if (graph.edge_count() == 0) {
        os << "    (нет рёбер)\n";
    } else {
        std::for_each(graph.edges_cbegin(), graph.edges_cend(), [&](const Edge<U>& e) {
            os << "    " << e << "\n";
        });
    }
    return os;
}

#endif // DIRECTED_INCIDENCE_MATRIX_GRAPH_CPP
