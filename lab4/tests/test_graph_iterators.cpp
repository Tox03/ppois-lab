#include <gtest/gtest.h>
#include <string>
#include <vector>
#include "graph/DirectedIncidenceMatrixGraph.h"
#include "graph/GraphException.h"

TEST(GraphIteratorsTest, VertexIteratorsForwardAndBackward) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("A");
    graph.add_vertex("B");
    graph.add_vertex("C");

    // Прямой обход
    std::vector<std::string> forward_vertices;
    for (auto it = graph.begin(); it != graph.end(); ++it) {
        forward_vertices.push_back(*it);
    }
    std::vector<std::string> expected = {"A", "B", "C"};
    EXPECT_EQ(forward_vertices, expected);

    // Доступ через стрелку ->
    auto it = graph.begin();
    EXPECT_EQ(it->length(), 1u);

    // Постфиксный инкремент
    auto it_post = it++;
    EXPECT_EQ(*it_post, "A");
    EXPECT_EQ(*it, "B");

    // Декремент
    auto it_dec = it;
    --it_dec;
    EXPECT_EQ(*it_dec, "A");
    auto it_post_dec = it--;
    EXPECT_EQ(*it_post_dec, "B");
    EXPECT_EQ(*it, "A");

    // Выход за границы (левая граница)
    EXPECT_THROW(--it, GraphException);

    // Разыменование end()
    EXPECT_THROW(*graph.end(), GraphException);
    EXPECT_THROW(graph.end().operator->(), GraphException);
}

TEST(GraphIteratorsTest, ReverseAndConstVertexIterators) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.add_vertex(10);
    graph.add_vertex(20);
    graph.add_vertex(30);

    // Обратный обход
    std::vector<int> reverse_vertices;
    for (auto rit = graph.rbegin(); rit != graph.rend(); ++rit) {
        reverse_vertices.push_back(*rit);
    }
    std::vector<int> expected_rev = {30, 20, 10};
    EXPECT_EQ(reverse_vertices, expected_rev);

    // Константные обратные итераторы
    std::vector<int> const_rev_vertices;
    for (auto crit = graph.crbegin(); crit != graph.crend(); ++crit) {
        const_rev_vertices.push_back(*crit);
    }
    EXPECT_EQ(const_rev_vertices, expected_rev);

    // Константный прямой обход
    const auto& cgraph = graph;
    std::vector<int> const_vertices;
    for (auto cit = cgraph.cbegin(); cit != cgraph.cend(); ++cit) {
        const_vertices.push_back(*cit);
    }
    std::vector<int> expected = {10, 20, 30};
    EXPECT_EQ(const_vertices, expected);

    // Преобразование неконстантного в константный
    DirectedIncidenceMatrixGraph<int>::const_vertex_iterator cit_converted = graph.begin();
    EXPECT_EQ(*cit_converted, 10);
}

TEST(GraphIteratorsTest, EdgeIteratorsForwardAndBackward) {
    DirectedIncidenceMatrixGraph<char> graph;
    graph.add_vertex('A');
    graph.add_vertex('B');
    graph.add_vertex('C');
    graph.add_edge('A', 'B');
    graph.add_edge('B', 'C');

    std::vector<Edge<char>> edges;
    for (auto it = graph.edges_begin(); it != graph.edges_end(); ++it) {
        edges.push_back(*it);
    }
    ASSERT_EQ(edges.size(), 2u);
    EXPECT_EQ(edges[0].getSource(), 'A');
    EXPECT_EQ(edges[0].getTarget(), 'B');
    EXPECT_EQ(edges[1].getSource(), 'B');
    EXPECT_EQ(edges[1].getTarget(), 'C');

    // Стрелка ->
    auto it = graph.edges_begin();
    EXPECT_EQ(it->getSource(), 'A');

    // Постфиксные операции
    auto it_copy = it++;
    EXPECT_EQ(it_copy->getSource(), 'A');
    EXPECT_EQ(it->getSource(), 'B');

    // Обратный обход рёбер
    std::vector<char> rev_sources;
    for (auto rit = graph.edges_rbegin(); rit != graph.edges_rend(); ++rit) {
        rev_sources.push_back(rit->getSource());
    }
    std::vector<char> expected_rev = {'B', 'A'};
    EXPECT_EQ(rev_sources, expected_rev);

    // Исключения выхода за границы
    EXPECT_THROW(*graph.edges_end(), GraphException);
    EXPECT_THROW(graph.edges_end().operator->(), GraphException);
    auto it_start = graph.edges_begin();
    EXPECT_THROW(--it_start, GraphException);
}

TEST(GraphIteratorsTest, IncidentEdgeIterators) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("U");
    graph.add_vertex("V");
    graph.add_vertex("W");
    graph.add_edge("U", "V");
    graph.add_edge("W", "U");
    graph.add_edge("U", "U"); // петля

    // Инцидентные рёбра для U (должны быть все три)
    std::vector<Edge<std::string>> incident_u;
    for (auto it = graph.incident_edges_begin("U"); it != graph.incident_edges_end("U"); ++it) {
        incident_u.push_back(*it);
        EXPECT_TRUE(it.isValid());
    }
    EXPECT_EQ(incident_u.size(), 3u);

    // Проверка доступа через стрелку и декремент
    auto it = graph.incident_edges_begin("U");
    EXPECT_FALSE(it->getSource().empty());
    auto it_next = it;
    ++it_next;
    auto it_prev = it_next;
    --it_prev;
    EXPECT_TRUE(it == it_prev);

    // Обратный обход инцидентных рёбер
    std::size_t rev_count = 0;
    for (auto rit = graph.incident_edges_rbegin("U"); rit != graph.incident_edges_rend("U"); ++rit) {
        ++rev_count;
    }
    EXPECT_EQ(rev_count, 3u);

    // Вершина без рёбер
    graph.add_vertex("Isolated");
    auto iso_begin = graph.incident_edges_begin("Isolated");
    auto iso_end = graph.incident_edges_end("Isolated");
    EXPECT_TRUE(iso_begin == iso_end);

    // Исключения
    EXPECT_THROW(*iso_begin, GraphException);
    EXPECT_THROW(--iso_begin, GraphException);
}

TEST(GraphIteratorsTest, AdjacentVertexIterators) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.add_vertex(1);
    graph.add_vertex(2);
    graph.add_vertex(3);
    graph.add_vertex(4);

    // 1 -> 2, 1 -> 3, 1 -> 1 (петля)
    graph.add_edge(1, 2);
    graph.add_edge(1, 3);
    graph.add_edge(1, 1);

    // Смежные вершины для 1 (приёмники исходящих рёбер: 2, 3, 1)
    std::vector<int> adj_1;
    for (auto it = graph.adjacent_vertices_begin(1); it != graph.adjacent_vertices_end(1); ++it) {
        adj_1.push_back(*it);
    }
    std::vector<int> expected_adj = {2, 3, 1};
    EXPECT_EQ(adj_1, expected_adj);

    // Обратный обход смежных вершин
    std::vector<int> rev_adj;
    for (auto rit = graph.adjacent_vertices_rbegin(1); rit != graph.adjacent_vertices_rend(1); ++rit) {
        rev_adj.push_back(*rit);
    }
    std::vector<int> expected_rev = {1, 3, 2};
    EXPECT_EQ(rev_adj, expected_rev);

    // Константный обход смежных вершин
    const auto& cgraph = graph;
    std::vector<int> const_adj;
    for (auto cit = cgraph.adjacent_vertices_cbegin(1); cit != cgraph.adjacent_vertices_cend(1); ++cit) {
        const_adj.push_back(*cit);
    }
    EXPECT_EQ(const_adj, expected_adj);

    // Вершина 4 не имеет исходящих рёбер
    auto adj_4_begin = graph.adjacent_vertices_begin(4);
    auto adj_4_end = graph.adjacent_vertices_end(4);
    EXPECT_TRUE(adj_4_begin == adj_4_end);

    EXPECT_THROW(*adj_4_begin, GraphException);
    EXPECT_THROW(--adj_4_begin, GraphException);
}

TEST(GraphIteratorsTest, RemoveVertexByIterator) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("A");
    graph.add_vertex("B");
    graph.add_vertex("C");

    // Удаляем вершину B через итератор
    auto it = graph.begin();
    ++it; // указывает на "B"
    auto next_it = graph.remove_vertex(it);

    EXPECT_EQ(graph.vertex_count(), 2u);
    EXPECT_FALSE(graph.has_vertex("B"));
    EXPECT_EQ(*next_it, "C");

    // Попытка удалить по недействительному итератору
    EXPECT_THROW(graph.remove_vertex(graph.end()), GraphException);
}

TEST(GraphIteratorsTest, RemoveEdgeByIterator) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.add_vertex(1);
    graph.add_vertex(2);
    graph.add_vertex(3);
    graph.add_edge(1, 2);
    graph.add_edge(2, 3);

    // Удаляем ребро (1 -> 2) через итератор
    auto it = graph.edges_begin();
    auto next_it = graph.erase(it);

    EXPECT_EQ(graph.edge_count(), 1u);
    EXPECT_FALSE(graph.has_edge(1, 2));
    EXPECT_EQ(next_it->getSource(), 2);
    EXPECT_EQ(next_it->getTarget(), 3);

    // Попытка удалить по недействительному итератору
    EXPECT_THROW(graph.erase(graph.edges_end()), GraphException);
}
