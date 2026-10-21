#include <gtest/gtest.h>
#include "graph/DirectedIncidenceMatrixGraph.h"
#include "model/Student.h"
#include <sstream>
#include <string>

TEST(DirectedGraphCoreTest, DefaultStateAndClear) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    EXPECT_TRUE(graph.empty());
    EXPECT_EQ(graph.vertexCount(), 0u);
    EXPECT_EQ(graph.edgeCount(), 0u);

    graph.insertVertex("V1");
    EXPECT_FALSE(graph.empty());
    EXPECT_EQ(graph.vertexCount(), 1u);

    graph.clear();
    EXPECT_TRUE(graph.empty());
    EXPECT_EQ(graph.vertexCount(), 0u);
    EXPECT_EQ(graph.edgeCount(), 0u);
}

TEST(DirectedGraphCoreTest, CopyAndMoveSemantics) {
    DirectedIncidenceMatrixGraph<std::string> g1;
    g1.insertVertex("A");
    g1.insertVertex("B");
    g1.insertEdge("A", "B");

    // Конструктор копирования
    DirectedIncidenceMatrixGraph<std::string> g2 = g1;
    EXPECT_EQ(g2.vertexCount(), 2u);
    EXPECT_EQ(g2.edgeCount(), 1u);
    EXPECT_TRUE(g2.hasEdge("A", "B"));
    EXPECT_TRUE(g1 == g2);

    // Оператор присваивания копированием
    DirectedIncidenceMatrixGraph<std::string> g3;
    g3 = g1;
    EXPECT_TRUE(g3 == g1);

    // Конструктор перемещения
    DirectedIncidenceMatrixGraph<std::string> g4 = std::move(g2);
    EXPECT_EQ(g4.vertexCount(), 2u);
    EXPECT_TRUE(g4.hasEdge("A", "B"));

    // Оператор присваивания перемещением
    DirectedIncidenceMatrixGraph<std::string> g5;
    g5 = std::move(g3);
    EXPECT_EQ(g5.vertexCount(), 2u);
    EXPECT_TRUE(g5.hasEdge("A", "B"));
}

TEST(DirectedGraphCoreTest, VertexOperations) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.insertVertex(10);
    graph.insertVertex(20);

    EXPECT_TRUE(graph.hasVertex(10));
    EXPECT_TRUE(graph.hasVertex(20));
    EXPECT_FALSE(graph.hasVertex(30));

    EXPECT_NO_THROW(graph.eraseVertex(10));
    EXPECT_FALSE(graph.hasVertex(10));
    EXPECT_EQ(graph.vertexCount(), 1u);
}

TEST(DirectedGraphCoreTest, EdgeOperationsAndLoops) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    graph.insertVertex("B");
    graph.insertVertex("C");

    graph.insertEdge("A", "B");
    graph.insertEdge("B", "C");
    graph.insertEdge("C", "C"); // петля

    EXPECT_TRUE(graph.hasEdge("A", "B"));
    EXPECT_TRUE(graph.hasEdge("B", "C"));
    EXPECT_TRUE(graph.hasEdge("C", "C"));
    EXPECT_FALSE(graph.hasEdge("B", "A"));

    EXPECT_EQ(graph.edgeCount(), 3u);

    // Удаление вершины каскадно удаляет связанные рёбра
    graph.eraseVertex("B");
    EXPECT_EQ(graph.vertexCount(), 2u);
    EXPECT_EQ(graph.edgeCount(), 1u); // Осталась только петля C -> C
    EXPECT_FALSE(graph.hasEdge("A", "B"));
    EXPECT_FALSE(graph.hasEdge("B", "C"));
    EXPECT_TRUE(graph.hasEdge("C", "C"));

    // Удаление оставшегося ребра
    graph.eraseEdge("C", "C");
    EXPECT_EQ(graph.edgeCount(), 0u);
}

TEST(DirectedGraphCoreTest, DegreesCalculations) {
    DirectedIncidenceMatrixGraph<char> graph;
    graph.insertVertex('X');
    graph.insertVertex('Y');
    graph.insertVertex('Z');

    graph.insertEdge('X', 'Y');
    graph.insertEdge('X', 'Z');
    graph.insertEdge('Z', 'X');
    graph.insertEdge('X', 'X'); // петля на X

    // Для X:
    // Исходящие: X->Y, X->Z, X->X (3)
    // Входящие: Z->X, X->X (2)
    // Степень: 3 + 2 = 5
    EXPECT_EQ(graph.outDegree('X'), 3u);
    EXPECT_EQ(graph.inDegree('X'), 2u);
    EXPECT_EQ(graph.degree('X'), 5u);

    // Для Y:
    // Исходящие: 0
    // Входящие: X->Y (1)
    // Степень: 1
    EXPECT_EQ(graph.outDegree('Y'), 0u);
    EXPECT_EQ(graph.inDegree('Y'), 1u);
    EXPECT_EQ(graph.degree('Y'), 1u);
}

TEST(DirectedGraphCoreTest, IncidenceMatrixValidation) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    graph.insertVertex("B");
    graph.insertEdge("A", "B");

    const auto& matrix = graph.getIncidenceMatrix();
    ASSERT_EQ(matrix.size(), 2u); // 2 строки (A, B)
    ASSERT_EQ(matrix[0].size(), 1u); // 1 столбец (ребро A->B)
    EXPECT_EQ(matrix[0][0], -1); // A - источник
    EXPECT_EQ(matrix[1][0], 1);  // B - сток

    std::ostringstream oss;
    graph.printIncidenceMatrix(oss);
    EXPECT_FALSE(oss.str().empty());
}

TEST(DirectedGraphCoreTest, GraphWithCustomStudentClass) {
    DirectedIncidenceMatrixGraph<Student> student_graph;
    Student s1(1, "Alice", 90);
    Student s2(2, "Bob", 80);

    student_graph.insertVertex(s1);
    student_graph.insertVertex(s2);
    student_graph.insertEdge(s1, s2);

    EXPECT_EQ(student_graph.vertexCount(), 2u);
    EXPECT_EQ(student_graph.edgeCount(), 1u);
    EXPECT_TRUE(student_graph.hasEdge(s1, s2));

    std::ostringstream oss;
    oss << student_graph;
    EXPECT_FALSE(oss.str().empty());
}

TEST(DirectedGraphCoreTest, ComparisonOperators) {
    DirectedIncidenceMatrixGraph<int> g1;
    g1.insertVertex(1);
    g1.insertVertex(2);

    DirectedIncidenceMatrixGraph<int> g2;
    g2.insertVertex(1);
    g2.insertVertex(2);

    EXPECT_TRUE(g1 == g2);
    EXPECT_FALSE(g1 != g2);
    EXPECT_FALSE(g1 < g2);
    EXPECT_TRUE(g1 <= g2);
    EXPECT_FALSE(g1 > g2);
    EXPECT_TRUE(g1 >= g2);

    g2.insertVertex(3);
    EXPECT_TRUE(g1 < g2);
    EXPECT_TRUE(g1 <= g2);
    EXPECT_FALSE(g1 > g2);
    EXPECT_FALSE(g1 >= g2);
}
