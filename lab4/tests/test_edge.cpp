#include <gtest/gtest.h>
#include "graph/Edge.h"
#include <sstream>
#include <string>

TEST(EdgeTest, DefaultAndParameterizedConstructors) {
    Edge<std::string> default_edge;
    EXPECT_EQ(default_edge.getSource(), "");
    EXPECT_EQ(default_edge.getTarget(), "");
    EXPECT_EQ(default_edge.getId(), 0u);

    Edge<std::string> edge("A", "B", 42);
    EXPECT_EQ(edge.getSource(), "A");
    EXPECT_EQ(edge.getTarget(), "B");
    EXPECT_EQ(edge.getId(), 42u);
}

TEST(EdgeTest, SettersAndGetters) {
    Edge<int> edge;
    edge.setSource(1);
    edge.setTarget(2);
    edge.setId(100);

    EXPECT_EQ(edge.getSource(), 1);
    EXPECT_EQ(edge.getTarget(), 2);
    EXPECT_EQ(edge.getId(), 100u);
}

TEST(EdgeTest, EqualityAndOrderingOperators) {
    Edge<std::string> e1("A", "B", 1);
    Edge<std::string> e2("A", "B", 2); // Равенство рёбер проверяется по источнику и приёмнику
    Edge<std::string> e3("A", "C", 1);

    EXPECT_TRUE(e1 == e2);
    EXPECT_FALSE(e1 != e2);
    EXPECT_TRUE(e1 != e3);
    EXPECT_TRUE(e1 < e3);
}

TEST(EdgeTest, StreamOutput) {
    Edge<std::string> edge("X", "Y", 5);
    std::ostringstream oss;
    oss << edge;
    EXPECT_EQ(oss.str(), "(X -> Y)");
}
