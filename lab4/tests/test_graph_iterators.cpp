#include <gtest/gtest.h>
#include "graph/DirectedIncidenceMatrixGraph.h"
#include <string>
#include <vector>

TEST(DirectedGraphIteratorsTest, VertexIteratorsForwardAndReverse) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    graph.insertVertex("B");
    graph.insertVertex("C");

    std::vector<std::string> forward_result;
    for (auto it = graph.verticesBegin(); it != graph.verticesEnd(); ++it) {
        forward_result.push_back(*it);
    }
    EXPECT_EQ(forward_result.size(), 3u);
    EXPECT_EQ(forward_result[0], "A");
    EXPECT_EQ(forward_result[1], "B");
    EXPECT_EQ(forward_result[2], "C");

    std::vector<std::string> reverse_result;
    for (auto it = graph.verticesRBegin(); it != graph.verticesREnd(); ++it) {
        reverse_result.push_back(*it);
    }
    EXPECT_EQ(reverse_result.size(), 3u);
    EXPECT_EQ(reverse_result[0], "C");
    EXPECT_EQ(reverse_result[1], "B");
    EXPECT_EQ(reverse_result[2], "A");

    // Const iterators
    const auto& const_graph = graph;
    std::vector<std::string> const_forward;
    for (auto it = const_graph.verticesBegin(); it != const_graph.verticesEnd(); ++it) {
        const_forward.push_back(*it);
    }
    EXPECT_EQ(const_forward, forward_result);

    std::vector<std::string> const_reverse;
    for (auto it = const_graph.verticesRBegin(); it != const_graph.verticesREnd(); ++it) {
        const_reverse.push_back(*it);
    }
    EXPECT_EQ(const_reverse, reverse_result);
}

TEST(DirectedGraphIteratorsTest, EdgeIteratorsForwardAndReverse) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.insertVertex(1);
    graph.insertVertex(2);
    graph.insertVertex(3);

    graph.insertEdge(1, 2);
    graph.insertEdge(2, 3);

    std::vector<Edge<int>> edges;
    for (auto it = graph.edgesBegin(); it != graph.edgesEnd(); ++it) {
        edges.push_back(*it);
    }
    ASSERT_EQ(edges.size(), 2u);
    EXPECT_EQ(edges[0].getSource(), 1);
    EXPECT_EQ(edges[0].getTarget(), 2);
    EXPECT_EQ(edges[1].getSource(), 2);
    EXPECT_EQ(edges[1].getTarget(), 3);

    // Reverse edge iterator
    std::vector<Edge<int>> reverse_edges;
    for (auto it = graph.edgesRBegin(); it != graph.edgesREnd(); ++it) {
        reverse_edges.push_back(*it);
    }
    ASSERT_EQ(reverse_edges.size(), 2u);
    EXPECT_EQ(reverse_edges[0].getSource(), 2);
    EXPECT_EQ(reverse_edges[0].getTarget(), 3);
    EXPECT_EQ(reverse_edges[1].getSource(), 1);
    EXPECT_EQ(reverse_edges[1].getTarget(), 2);
}

TEST(DirectedGraphIteratorsTest, IncidentEdgeIterators) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    graph.insertVertex("B");
    graph.insertVertex("C");

    graph.insertEdge("A", "B");
    graph.insertEdge("C", "A");

    std::vector<Edge<std::string>> incident_a;
    for (auto it = graph.incidentEdgesBegin("A"); it != graph.incidentEdgesEnd("A"); ++it) {
        incident_a.push_back(*it);
    }
    ASSERT_EQ(incident_a.size(), 2u);

    // Reverse incident edge iterator
    std::vector<Edge<std::string>> rev_incident_a;
    for (auto it = graph.incidentEdgesRBegin("A"); it != graph.incidentEdgesREnd("A"); ++it) {
        rev_incident_a.push_back(*it);
    }
    ASSERT_EQ(rev_incident_a.size(), 2u);
    EXPECT_EQ(rev_incident_a[0], incident_a[1]);
    EXPECT_EQ(rev_incident_a[1], incident_a[0]);
}

TEST(DirectedGraphIteratorsTest, AdjacentVertexIterators) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.insertVertex("A");
    graph.insertVertex("B");
    graph.insertVertex("C");
    graph.insertVertex("D");

    graph.insertEdge("A", "B");
    graph.insertEdge("A", "C");

    std::vector<std::string> adj;
    for (auto it = graph.adjacentVerticesBegin("A"); it != graph.adjacentVerticesEnd("A"); ++it) {
        adj.push_back(*it);
    }
    ASSERT_EQ(adj.size(), 2u);
    EXPECT_EQ(adj[0], "B");
    EXPECT_EQ(adj[1], "C");

    // Reverse adjacent iterator
    std::vector<std::string> rev_adj;
    for (auto it = graph.adjacentVerticesRBegin("A"); it != graph.adjacentVerticesREnd("A"); ++it) {
        rev_adj.push_back(*it);
    }
    ASSERT_EQ(rev_adj.size(), 2u);
    EXPECT_EQ(rev_adj[0], "C");
    EXPECT_EQ(rev_adj[1], "B");
}

TEST(DirectedGraphIteratorsTest, IteratorIncrementDecrementOperators) {
    DirectedIncidenceMatrixGraph<int> graph;
    graph.insertVertex(10);
    graph.insertVertex(20);

    auto it = graph.verticesBegin();
    EXPECT_EQ(*it, 10);
    auto it_post = it++;
    EXPECT_EQ(*it_post, 10);
    EXPECT_EQ(*it, 20);

    auto it_dec = it--;
    EXPECT_EQ(*it_dec, 20);
    EXPECT_EQ(*it, 10);

    auto it_pre = ++it;
    EXPECT_EQ(*it_pre, 20);
    EXPECT_EQ(*it, 20);

    auto it_pre_dec = --it;
    EXPECT_EQ(*it_pre_dec, 10);
    EXPECT_EQ(*it, 10);
}
