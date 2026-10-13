#include <gtest/gtest.h>
#include <string>
#include <sstream>
#include "graph/DirectedIncidenceMatrixGraph.h"
#include "graph/GraphException.h"
#include "model/Student.h"

TEST(GraphCoreTest, DefaultConstructorAndEmptyState) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    EXPECT_TRUE(graph.empty());
    EXPECT_TRUE(graph.is_empty());
    EXPECT_EQ(graph.vertex_count(), 0u);
    EXPECT_EQ(graph.size(), 0u);
    EXPECT_EQ(graph.edge_count(), 0u);
    EXPECT_FALSE(graph.has_vertex("A"));
}

TEST(GraphCoreTest, AddVertexAndDuplicateHandling) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("A");
    graph.add_vertex("B");
    graph.add_vertex("C");

    EXPECT_FALSE(graph.empty());
    EXPECT_EQ(graph.vertex_count(), 3u);
    EXPECT_TRUE(graph.has_vertex("A"));
    EXPECT_TRUE(graph.has_vertex("B"));
    EXPECT_TRUE(graph.has_vertex("C"));
    EXPECT_FALSE(graph.has_vertex("D"));

    EXPECT_THROW(graph.add_vertex("A"), GraphException);
}

TEST(GraphCoreTest, AddEdgeAndEdgePresence) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("A");
    graph.add_vertex("B");
    graph.add_vertex("C");

    graph.add_edge("A", "B");
    graph.add_edge("B", "C");

    EXPECT_EQ(graph.edge_count(), 2u);
    EXPECT_TRUE(graph.has_edge("A", "B"));
    EXPECT_TRUE(graph.has_edge("B", "C"));
    EXPECT_FALSE(graph.has_edge("B", "A"));
    EXPECT_FALSE(graph.has_edge("A", "C"));

    // Проверка через Edge<T>
    Edge<std::string> edge_ab("A", "B");
    EXPECT_TRUE(graph.has_edge(edge_ab));

    // Попытка добавить ребро с несуществующими вершинами
    EXPECT_THROW(graph.add_edge("A", "Z"), GraphException);
    EXPECT_THROW(graph.add_edge("Z", "A"), GraphException);

    // Попытка добавить дубликат ребра
    EXPECT_THROW(graph.add_edge("A", "B"), GraphException);
}

TEST(GraphCoreTest, SelfLoopEdge) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.add_vertex(1);
    graph.add_vertex(2);

    graph.add_edge(1, 1); // петля
    EXPECT_TRUE(graph.has_edge(1, 1));
    EXPECT_EQ(graph.edge_count(), 1u);

    // Проверка матрицы инцидентности: петля имеет значение INCIDENCE_LOOP
    const auto& matrix = graph.getIncidenceMatrix();
    EXPECT_EQ(matrix[0][0], DirectedIncidenceMatrixGraph<int>::INCIDENCE_LOOP);
    EXPECT_EQ(matrix[1][0], DirectedIncidenceMatrixGraph<int>::INCIDENCE_NONE);

    // Петля добавляет 1 к полустепени исхода и 1 к полустепени захода (всего 2)
    EXPECT_EQ(graph.vertex_in_degree(1), 1u);
    EXPECT_EQ(graph.vertex_out_degree(1), 1u);
    EXPECT_EQ(graph.vertex_degree(1), 2u);
}

TEST(GraphCoreTest, VertexDegrees) {
    DirectedIncidenceMatrixGraph<char> graph;
    graph.add_vertex('A');
    graph.add_vertex('B');
    graph.add_vertex('C');

    // A -> B, A -> C, B -> C, C -> C (петля)
    graph.add_edge('A', 'B');
    graph.add_edge('A', 'C');
    graph.add_edge('B', 'C');
    graph.add_edge('C', 'C');

    EXPECT_EQ(graph.vertex_out_degree('A'), 2u);
    EXPECT_EQ(graph.vertex_in_degree('A'), 0u);
    EXPECT_EQ(graph.vertex_degree('A'), 2u);

    EXPECT_EQ(graph.vertex_out_degree('B'), 1u);
    EXPECT_EQ(graph.vertex_in_degree('B'), 1u);
    EXPECT_EQ(graph.vertex_degree('B'), 2u);

    // C имеет входящие от A и B (+2), и петлю (in +1, out +1): in = 3, out = 1, total = 4
    EXPECT_EQ(graph.vertex_in_degree('C'), 3u);
    EXPECT_EQ(graph.vertex_out_degree('C'), 1u);
    EXPECT_EQ(graph.vertex_degree('C'), 4u);

    EXPECT_THROW(graph.vertex_degree('Z'), GraphException);
}

TEST(GraphCoreTest, EdgeDegree) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.add_vertex(1);
    graph.add_vertex(2);
    graph.add_vertex(3);
    graph.add_vertex(4);

    // 1 -> 2, 2 -> 3, 3 -> 4, 1 -> 3
    graph.add_edge(1, 2);
    graph.add_edge(2, 3);
    graph.add_edge(3, 4);
    graph.add_edge(1, 3);

    // Ребро (1 -> 2): смежно с (2 -> 3) и (1 -> 3). Итого степень = 2
    EXPECT_EQ(graph.edge_degree(1, 2), 2u);

    // Ребро (2 -> 3): смежно с (1 -> 2), (3 -> 4), (1 -> 3). Итого степень = 3
    EXPECT_EQ(graph.edge_degree(2, 3), 3u);

    Edge<int> e_missing(1, 4);
    EXPECT_THROW(graph.edge_degree(e_missing), GraphException);
    EXPECT_THROW(graph.edge_degree(1, 4), GraphException);
}

TEST(GraphCoreTest, RemoveEdge) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("X");
    graph.add_vertex("Y");
    graph.add_vertex("Z");
    graph.add_edge("X", "Y");
    graph.add_edge("Y", "Z");

    EXPECT_EQ(graph.edge_count(), 2u);
    EXPECT_TRUE(graph.remove_edge("X", "Y"));
    EXPECT_EQ(graph.edge_count(), 1u);
    EXPECT_FALSE(graph.has_edge("X", "Y"));
    EXPECT_TRUE(graph.has_edge("Y", "Z"));

    // Проверка удаления через объект Edge
    Edge<std::string> e_yz("Y", "Z");
    EXPECT_TRUE(graph.remove_edge(e_yz));
    EXPECT_EQ(graph.edge_count(), 0u);

    EXPECT_THROW(graph.remove_edge("X", "Y"), GraphException);
}

TEST(GraphCoreTest, RemoveVertexAndIncidentEdges) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("A");
    graph.add_vertex("B");
    graph.add_vertex("C");
    graph.add_edge("A", "B");
    graph.add_edge("B", "C");
    graph.add_edge("C", "A");

    EXPECT_EQ(graph.vertex_count(), 3u);
    EXPECT_EQ(graph.edge_count(), 3u);

    // Удаление вершины B должно также удалить рёбра (A->B) и (B->C)
    EXPECT_TRUE(graph.remove_vertex("B"));
    EXPECT_EQ(graph.vertex_count(), 2u);
    EXPECT_FALSE(graph.has_vertex("B"));
    EXPECT_EQ(graph.edge_count(), 1u);
    EXPECT_TRUE(graph.has_edge("C", "A"));

    EXPECT_THROW(graph.remove_vertex("B"), GraphException);
}

TEST(GraphCoreTest, ClearAndDeepCopy) {
    DirectedIncidenceMatrixGraph<int> g1;
    g1.add_vertex(10);
    g1.add_vertex(20);
    g1.add_edge(10, 20);

    DirectedIncidenceMatrixGraph<int> g2 = g1; // Конструктор копирования
    EXPECT_TRUE(g1 == g2);

    g2.add_vertex(30);
    g2.add_edge(20, 30);

    // Изменение копии не влияет на g1
    EXPECT_EQ(g1.vertex_count(), 2u);
    EXPECT_EQ(g2.vertex_count(), 3u);
    EXPECT_TRUE(g1 != g2);

    DirectedIncidenceMatrixGraph<int> g3;
    g3 = g2; // Оператор присваивания
    EXPECT_TRUE(g3 == g2);

    // Самоприсваивание
    g3 = g3;
    EXPECT_TRUE(g3 == g2);

    g1.clear();
    EXPECT_TRUE(g1.empty());
    EXPECT_EQ(g1.vertex_count(), 0u);
    EXPECT_EQ(g1.edge_count(), 0u);
}

TEST(GraphCoreTest, MoveSemantics) {
    DirectedIncidenceMatrixGraph<int> g1;
    g1.add_vertex(1);
    g1.add_vertex(2);
    g1.add_edge(1, 2);

    DirectedIncidenceMatrixGraph<int> g2(std::move(g1));
    EXPECT_EQ(g2.vertex_count(), 2u);
    EXPECT_EQ(g2.edge_count(), 1u);

    DirectedIncidenceMatrixGraph<int> g3;
    g3 = std::move(g2);
    EXPECT_EQ(g3.vertex_count(), 2u);
    EXPECT_EQ(g3.edge_count(), 1u);
}

TEST(GraphCoreTest, GraphComparisons) {
    DirectedIncidenceMatrixGraph<int> g1, g2;
    EXPECT_TRUE(g1 == g2);
    EXPECT_TRUE(g1 <= g2);
    EXPECT_TRUE(g1 >= g2);

    g1.add_vertex(1);
    EXPECT_TRUE(g2 < g1);
    EXPECT_TRUE(g2 <= g1);
    EXPECT_TRUE(g1 > g2);
    EXPECT_TRUE(g1 >= g2);

    g2.add_vertex(1);
    EXPECT_TRUE(g1 == g2);

    g1.add_vertex(2);
    g2.add_vertex(3);
    // При одинаковом числе вершин и рёбер сравниваются сами вершины (1, 2) < (1, 3)
    EXPECT_TRUE(g1 < g2);
}

TEST(GraphCoreTest, StreamOutputAndIncidenceMatrixPrinting) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    std::stringstream ss_empty;
    ss_empty << graph;
    EXPECT_FALSE(ss_empty.str().empty());

    graph.add_vertex("Alpha");
    graph.add_vertex("Beta");
    graph.add_edge("Alpha", "Beta");

    std::stringstream ss;
    ss << graph;
    std::string out_str = ss.str();
    EXPECT_NE(out_str.find("Alpha"), std::string::npos);
    EXPECT_NE(out_str.find("Beta"), std::string::npos);

    std::stringstream ss_matrix;
    graph.printIncidenceMatrix(ss_matrix);
    EXPECT_NE(ss_matrix.str().find("-1"), std::string::npos);
    EXPECT_NE(ss_matrix.str().find("1"), std::string::npos);
}

TEST(GraphCoreTest, UserDefinedObjectsInGraph) {
    DirectedIncidenceMatrixGraph<Student> student_graph;
    Student s1(1, "Иван", 4.5, 20);
    Student s2(2, "Петр", 4.9, 21);

    student_graph.add_vertex(s1);
    student_graph.add_vertex(s2);
    student_graph.add_edge(s1, s2);

    EXPECT_TRUE(student_graph.has_vertex(s1));
    EXPECT_TRUE(student_graph.has_edge(s1, s2));
    EXPECT_EQ(student_graph.vertex_degree(s1), 1u);
}
