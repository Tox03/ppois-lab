#include <gtest/gtest.h>
#include "graph/GraphException.h"
#include "graph/DirectedIncidenceMatrixGraph.h"
#include <string>

TEST(ExceptionTest, GraphExceptionConstructors) {
    GraphException ex1("Ошибка теста 1");
    EXPECT_STREQ(ex1.what(), "Ошибка теста 1");

    std::string str = "Ошибка теста 2";
    GraphException ex2(str);
    EXPECT_STREQ(ex2.what(), "Ошибка теста 2");
}

TEST(ExceptionTest, DuplicateVertexThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    EXPECT_THROW(graph.insertVertex("A"), GraphException);
}

TEST(ExceptionTest, ErasingNonExistentVertexThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    EXPECT_THROW(graph.eraseVertex("Ghost"), GraphException);
}

TEST(ExceptionTest, EdgeBetweenNonExistentVerticesThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    EXPECT_THROW(graph.insertEdge("A", "Ghost"), GraphException);
    EXPECT_THROW(graph.insertEdge("Ghost", "A"), GraphException);
    EXPECT_THROW(graph.insertEdge("Ghost1", "Ghost2"), GraphException);
}

TEST(ExceptionTest, DuplicateEdgeThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    graph.insertVertex("B");
    graph.insertEdge("A", "B");

    EXPECT_THROW(graph.insertEdge("A", "B"), GraphException);
}

TEST(ExceptionTest, ErasingNonExistentEdgeThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    graph.insertVertex("B");

    EXPECT_THROW(graph.eraseEdge("A", "B"), GraphException);
    EXPECT_THROW(graph.eraseEdge("A", "Ghost"), GraphException);
}

TEST(ExceptionTest, DegreesOfNonExistentVertexThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    EXPECT_THROW(graph.degree("Ghost"), GraphException);
    EXPECT_THROW(graph.inDegree("Ghost"), GraphException);
    EXPECT_THROW(graph.outDegree("Ghost"), GraphException);
    EXPECT_THROW(graph.incidentEdgesBegin("Ghost"), GraphException);
    EXPECT_THROW(graph.adjacentVerticesBegin("Ghost"), GraphException);
}

TEST(ExceptionTest, EdgeDegreeOfNonExistentEdgeThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("V1");
    graph.insertVertex("V2");

    EXPECT_THROW(graph.edge_degree("V1", "Ghost"), GraphException);
    EXPECT_THROW(graph.edge_degree(Edge<std::string>("Ghost1", "Ghost2")), GraphException);
}

TEST(ExceptionTest, InvalidIteratorEraseThrowsException) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");

    DirectedIncidenceMatrixGraph<std::string>::vertex_iterator default_v_it;
    EXPECT_THROW(graph.erase(default_v_it), GraphException);

    DirectedIncidenceMatrixGraph<std::string>::edge_iterator default_e_it;
    EXPECT_THROW(graph.erase(default_e_it), GraphException);

    DirectedIncidenceMatrixGraph<std::string> other_graph;
    other_graph.insertVertex("Other");
    EXPECT_THROW(graph.erase(other_graph.begin()), GraphException);
}
