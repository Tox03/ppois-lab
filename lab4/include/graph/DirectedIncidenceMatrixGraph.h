#pragma once

#include <cstddef>
#include <vector>
#include <memory>
#include <iostream>
#include <algorithm>
#include <iterator>

#include "graph/GraphException.h"
#include "graph/Edge.h"
#include "graph/VertexIterator.h"
#include "graph/ConstVertexIterator.h"
#include "graph/EdgeIterator.h"
#include "graph/ConstEdgeIterator.h"
#include "graph/IncidentEdgeIterator.h"
#include "graph/ConstIncidentEdgeIterator.h"
#include "graph/AdjacentVertexIterator.h"
#include "graph/ConstAdjacentVertexIterator.h"

/**
 * @brief Обобщённый класс ориентированного графа на основе матрицы инцидентности.
 * Контейнер скрывает внутреннее представление и предоставляет доступ исключительно
 * через методы и специализированные двунаправленные итераторы.
 * 
 * В матрице инцидентности размера N x M (N - вершины, M - рёбра):
 *   -1 : ребро исходит из вершины (источник);
 *   +1 : ребро входит в вершину (приёмник);
 *    2 : петля (ребро исходит из вершины и заходит в неё же);
 *    0 : вершина не инцидентна ребру.
 * 
 * @tparam T Тип данных, хранимых в вершинах графа.
 */
template <typename T>
class DirectedIncidenceMatrixGraph {
public:
    // Псевдонимы типов STL
    using value_type = T;
    using size_type = std::size_t;
    using difference_type = std::ptrdiff_t;
    using reference = T&;
    using const_reference = const T&;
    using pointer = T*;
    using const_pointer = const T*;

    using edge_type = Edge<T>;

    // Итераторы вершин
    using vertex_iterator = VertexIterator<T>;
    using const_vertex_iterator = ConstVertexIterator<T>;
    using reverse_vertex_iterator = std::reverse_iterator<vertex_iterator>;
    using const_reverse_vertex_iterator = std::reverse_iterator<const_vertex_iterator>;

    // Итераторы рёбер
    using edge_iterator = EdgeIterator<T>;
    using const_edge_iterator = ConstEdgeIterator<T>;
    using reverse_edge_iterator = std::reverse_iterator<edge_iterator>;
    using const_reverse_edge_iterator = std::reverse_iterator<const_edge_iterator>;

    // Итераторы инцидентных рёбер
    using incident_edge_iterator = IncidentEdgeIterator<T>;
    using const_incident_edge_iterator = ConstIncidentEdgeIterator<T>;
    using reverse_incident_edge_iterator = std::reverse_iterator<incident_edge_iterator>;
    using const_reverse_incident_edge_iterator = std::reverse_iterator<const_incident_edge_iterator>;

    // Итераторы смежных вершин
    using adjacent_vertex_iterator = AdjacentVertexIterator<T>;
    using const_adjacent_vertex_iterator = ConstAdjacentVertexIterator<T>;
    using reverse_adjacent_vertex_iterator = std::reverse_iterator<adjacent_vertex_iterator>;
    using const_reverse_adjacent_vertex_iterator = std::reverse_iterator<const_adjacent_vertex_iterator>;

    // Стандартные синонимы итераторов контейнера
    using iterator = vertex_iterator;
    using const_iterator = const_vertex_iterator;
    using reverse_iterator = reverse_vertex_iterator;
    using const_reverse_iterator = const_reverse_vertex_iterator;

    /// Константы матрицы инцидентности
    static constexpr int INCIDENCE_OUTGOING = -1; ///< Ребро исходит из вершины (источник)
    static constexpr int INCIDENCE_INCOMING = 1;  ///< Ребро входит в вершину (приёмник)
    static constexpr int INCIDENCE_LOOP = 2;      ///< Петля (ребро исходит и входит в одну вершину)
    static constexpr int INCIDENCE_NONE = 0;      ///< Вершина не инцидентна ребру

    /**
     * @brief Конструктор по умолчанию (создаёт пустой граф).
     */
    DirectedIncidenceMatrixGraph();

    /**
     * @brief Конструктор копирования (глубокое копирование).
     */
    DirectedIncidenceMatrixGraph(const DirectedIncidenceMatrixGraph& other);

    /**
     * @brief Конструктор перемещения.
     */
    DirectedIncidenceMatrixGraph(DirectedIncidenceMatrixGraph&& other) noexcept;

    /**
     * @brief Деструктор.
     */
    ~DirectedIncidenceMatrixGraph() = default;

    /**
     * @brief Оператор присваивания копированием.
     */
    DirectedIncidenceMatrixGraph& operator=(const DirectedIncidenceMatrixGraph& other);

    /**
     * @brief Оператор присваивания перемещением.
     */
    DirectedIncidenceMatrixGraph& operator=(DirectedIncidenceMatrixGraph&& other) noexcept;

    /**
     * @brief Проверка графа на пустоту.
     */
    bool empty() const noexcept;
    bool is_empty() const noexcept;

    /**
     * @brief Получить количество вершин в графе.
     */
    size_type vertex_count() const noexcept;
    size_type size() const noexcept;

    /**
     * @brief Получить количество рёбер в графе.
     */
    size_type edge_count() const noexcept;

    /**
     * @brief Полная очистка графа.
     */
    void clear() noexcept;

    /**
     * @brief Проверка присутствия вершины в графе.
     */
    bool has_vertex(const T& v) const;

    /**
     * @brief Проверка присутствия ориентированного ребра между вершинами.
     */
    bool has_edge(const T& from, const T& to) const;

    /**
     * @brief Проверка присутствия ребра.
     */
    bool has_edge(const Edge<T>& e) const;

    /**
     * @brief Доступ к вершине по индексу с проверкой границ.
     */
    reference at(size_type index);
    const_reference at(size_type index) const;

    /**
     * @brief Оператор доступа к вершине по индексу.
     */
    reference operator[](size_type index);
    const_reference operator[](size_type index) const;

    /**
     * @brief Найти вершину и вернуть итератор на неё.
     * @return vertex_iterator или end(), если не найдена.
     */
    vertex_iterator find_vertex(const T& v);
    const_vertex_iterator find_vertex(const T& v) const;

    /**
     * @brief Найти ребро и вернуть итератор на него.
     * @return edge_iterator или edges_end(), если не найдено.
     */
    edge_iterator find_edge(const T& from, const T& to);
    const_edge_iterator find_edge(const T& from, const T& to) const;

    /**
     * @brief Добавить вершину в граф.
     * @throws GraphException если вершина уже существует.
     */
    void add_vertex(const T& v);

    /**
     * @brief Добавить ориентированное ребро в граф.
     * @throws GraphException если вершины не найдены или ребро уже существует.
     */
    void add_edge(const T& from, const T& to);
    void add_edge(const Edge<T>& e);

    /**
     * @brief Удалить вершину из графа по значению (вместе со всеми инцидентными рёбрами).
     * @throws GraphException если вершина не найдена.
     */
    bool remove_vertex(const T& v);

    /**
     * @brief Удалить вершину по итератору.
     * @return Итератор на следующий элемент после удалённого.
     */
    vertex_iterator remove_vertex(vertex_iterator pos);
    vertex_iterator erase(vertex_iterator pos);

    /**
     * @brief Удалить ребро по начальной и конечной вершинам.
     * @throws GraphException если ребро не найдено.
     */
    bool remove_edge(const T& from, const T& to);
    bool remove_edge(const Edge<T>& e);

    /**
     * @brief Удалить ребро по итератору.
     * @return Итератор на следующее ребро после удалённого.
     */
    edge_iterator remove_edge(edge_iterator pos);
    edge_iterator erase(edge_iterator pos);

    /**
     * @brief Вычисление общей степени вершины (сумма полустепеней исхода и захода).
     */
    size_type vertex_degree(const T& v) const;

    /**
     * @brief Вычисление полустепени захода вершины (число входящих рёбер).
     */
    size_type vertex_in_degree(const T& v) const;

    /**
     * @brief Вычисление полустепени исхода вершины (число исходящих рёбер).
     */
    size_type vertex_out_degree(const T& v) const;

    /**
     * @brief Вычисление степени ребра (число смежных с ним рёбер).
     */
    size_type edge_degree(const Edge<T>& e) const;
    size_type edge_degree(const T& from, const T& to) const;

    // --- Итераторы вершин ---
    vertex_iterator begin();
    vertex_iterator end();
    const_vertex_iterator begin() const;
    const_vertex_iterator end() const;
    const_vertex_iterator cbegin() const;
    const_vertex_iterator cend() const;

    reverse_vertex_iterator rbegin();
    reverse_vertex_iterator rend();
    const_reverse_vertex_iterator rbegin() const;
    const_reverse_vertex_iterator rend() const;
    const_reverse_vertex_iterator crbegin() const;
    const_reverse_vertex_iterator crend() const;

    // --- Итераторы рёбер ---
    edge_iterator edges_begin();
    edge_iterator edges_end();
    const_edge_iterator edges_begin() const;
    const_edge_iterator edges_end() const;
    const_edge_iterator edges_cbegin() const;
    const_edge_iterator edges_cend() const;

    reverse_edge_iterator edges_rbegin();
    reverse_edge_iterator edges_rend();
    const_reverse_edge_iterator edges_rbegin() const;
    const_reverse_edge_iterator edges_rend() const;
    const_reverse_edge_iterator edges_crbegin() const;
    const_reverse_edge_iterator edges_crend() const;

    // --- Итераторы инцидентных рёбер для вершины ---
    incident_edge_iterator incident_edges_begin(const T& v);
    incident_edge_iterator incident_edges_end(const T& v);
    const_incident_edge_iterator incident_edges_begin(const T& v) const;
    const_incident_edge_iterator incident_edges_end(const T& v) const;
    const_incident_edge_iterator incident_edges_cbegin(const T& v) const;
    const_incident_edge_iterator incident_edges_cend(const T& v) const;

    reverse_incident_edge_iterator incident_edges_rbegin(const T& v);
    reverse_incident_edge_iterator incident_edges_rend(const T& v);
    const_reverse_incident_edge_iterator incident_edges_rbegin(const T& v) const;
    const_reverse_incident_edge_iterator incident_edges_rend(const T& v) const;
    const_reverse_incident_edge_iterator incident_edges_crbegin(const T& v) const;
    const_reverse_incident_edge_iterator incident_edges_crend(const T& v) const;

    // --- Итераторы смежных вершин для вершины ---
    adjacent_vertex_iterator adjacent_vertices_begin(const T& v);
    adjacent_vertex_iterator adjacent_vertices_end(const T& v);
    const_adjacent_vertex_iterator adjacent_vertices_begin(const T& v) const;
    const_adjacent_vertex_iterator adjacent_vertices_end(const T& v) const;
    const_adjacent_vertex_iterator adjacent_vertices_cbegin(const T& v) const;
    const_adjacent_vertex_iterator adjacent_vertices_cend(const T& v) const;

    reverse_adjacent_vertex_iterator adjacent_vertices_rbegin(const T& v);
    reverse_adjacent_vertex_iterator adjacent_vertices_rend(const T& v);
    const_reverse_adjacent_vertex_iterator adjacent_vertices_rbegin(const T& v) const;
    const_reverse_adjacent_vertex_iterator adjacent_vertices_rend(const T& v) const;
    const_reverse_adjacent_vertex_iterator adjacent_vertices_crbegin(const T& v) const;
    const_reverse_adjacent_vertex_iterator adjacent_vertices_crend(const T& v) const;

    // --- Операции сравнения графов ---
    bool operator==(const DirectedIncidenceMatrixGraph& other) const;
    bool operator!=(const DirectedIncidenceMatrixGraph& other) const;
    bool operator<(const DirectedIncidenceMatrixGraph& other) const;
    bool operator<=(const DirectedIncidenceMatrixGraph& other) const;
    bool operator>(const DirectedIncidenceMatrixGraph& other) const;
    bool operator>=(const DirectedIncidenceMatrixGraph& other) const;

    // --- Удобные псевдонимы методов (CamelCase) для расширенной совместимости ---
    void insertVertex(const T& v) { add_vertex(v); }
    bool eraseVertex(const T& v) { return remove_vertex(v); }
    void insertEdge(const T& from, const T& to) { add_edge(from, to); }
    bool eraseEdge(const T& from, const T& to) { return remove_edge(from, to); }
    bool hasVertex(const T& v) const { return has_vertex(v); }
    bool hasEdge(const T& from, const T& to) const { return has_edge(from, to); }
    size_type vertexCount() const noexcept { return vertex_count(); }
    size_type edgeCount() const noexcept { return edge_count(); }
    size_type degree(const T& v) const { return vertex_degree(v); }
    size_type inDegree(const T& v) const { return vertex_in_degree(v); }
    size_type outDegree(const T& v) const { return vertex_out_degree(v); }

    vertex_iterator verticesBegin() { return begin(); }
    vertex_iterator verticesEnd() { return end(); }
    const_vertex_iterator verticesBegin() const { return begin(); }
    const_vertex_iterator verticesEnd() const { return end(); }
    reverse_vertex_iterator verticesRBegin() { return rbegin(); }
    reverse_vertex_iterator verticesREnd() { return rend(); }
    const_reverse_vertex_iterator verticesRBegin() const { return rbegin(); }
    const_reverse_vertex_iterator verticesREnd() const { return rend(); }

    edge_iterator edgesBegin() { return edges_begin(); }
    edge_iterator edgesEnd() { return edges_end(); }
    const_edge_iterator edgesBegin() const { return edges_begin(); }
    const_edge_iterator edgesEnd() const { return edges_end(); }
    reverse_edge_iterator edgesRBegin() { return edges_rbegin(); }
    reverse_edge_iterator edgesREnd() { return edges_rend(); }
    const_reverse_edge_iterator edgesRBegin() const { return edges_rbegin(); }
    const_reverse_edge_iterator edgesREnd() const { return edges_rend(); }

    incident_edge_iterator incidentEdgesBegin(const T& v) { return incident_edges_begin(v); }
    incident_edge_iterator incidentEdgesEnd(const T& v) { return incident_edges_end(v); }
    const_incident_edge_iterator incidentEdgesBegin(const T& v) const { return incident_edges_begin(v); }
    const_incident_edge_iterator incidentEdgesEnd(const T& v) const { return incident_edges_end(v); }
    reverse_incident_edge_iterator incidentEdgesRBegin(const T& v) { return incident_edges_rbegin(v); }
    reverse_incident_edge_iterator incidentEdgesREnd(const T& v) { return incident_edges_rend(v); }
    const_reverse_incident_edge_iterator incidentEdgesRBegin(const T& v) const { return incident_edges_rbegin(v); }
    const_reverse_incident_edge_iterator incidentEdgesREnd(const T& v) const { return incident_edges_rend(v); }

    adjacent_vertex_iterator adjacentVerticesBegin(const T& v) { return adjacent_vertices_begin(v); }
    adjacent_vertex_iterator adjacentVerticesEnd(const T& v) { return adjacent_vertices_end(v); }
    const_adjacent_vertex_iterator adjacentVerticesBegin(const T& v) const { return adjacent_vertices_begin(v); }
    const_adjacent_vertex_iterator adjacentVerticesEnd(const T& v) const { return adjacent_vertices_end(v); }
    reverse_adjacent_vertex_iterator adjacentVerticesRBegin(const T& v) { return adjacent_vertices_rbegin(v); }
    reverse_adjacent_vertex_iterator adjacentVerticesREnd(const T& v) { return adjacent_vertices_rend(v); }
    const_reverse_adjacent_vertex_iterator adjacentVerticesRBegin(const T& v) const { return adjacent_vertices_rbegin(v); }
    const_reverse_adjacent_vertex_iterator adjacentVerticesREnd(const T& v) const { return adjacent_vertices_rend(v); }

    // Вспомогательный метод для демонстрации матрицы
    const std::vector<std::vector<int>>& getIncidenceMatrix() const;
    void printIncidenceMatrix(std::ostream& os = std::cout) const;

    // Текстовое представление через итераторы и std::for_each
    template <typename U>
    friend std::ostream& operator<<(std::ostream& os, const DirectedIncidenceMatrixGraph<U>& graph);

private:
    std::size_t findVertexIndex(const T& v) const;
    std::size_t findEdgeIndex(const T& from, const T& to) const;
    std::shared_ptr<std::vector<std::size_t>> getIncidentEdgeIndices(const T& v) const;
    std::shared_ptr<std::vector<std::size_t>> getAdjacentVertexIndices(const T& v) const;

    std::vector<T> vertices_;                ///< Хранилище вершин
    std::vector<Edge<T>> edges_;             ///< Хранилище рёбер
    std::vector<std::vector<int>> matrix_;   ///< Матрица инцидентности: |V| строк x |E| столбцов
};

#include "graph/DirectedIncidenceMatrixGraph.cpp"
