#include <gtest/gtest.h>
#include <sstream>
#include <string>
#include "graph/Edge.h"

TEST(EdgeTest, DefaultAndParameterizedConstructors) {
    Edge<int> e_def;
    EXPECT_EQ(e_def.getSource(), 0);
    EXPECT_EQ(e_def.getTarget(), 0);
    EXPECT_EQ(e_def.getId(), 0u);

    Edge<std::string> e("A", "B", 1);
    EXPECT_EQ(e.getSource(), "A");
    EXPECT_EQ(e.getTarget(), "B");
    EXPECT_EQ(e.getId(), 1u);
    EXPECT_FALSE(e.isLoop());

    Edge<std::string> loop("A", "A", 2);
    EXPECT_TRUE(loop.isLoop());
}

TEST(EdgeTest, Setters) {
    Edge<int> e;
    e.setSource(10);
    e.setTarget(20);
    e.setId(5);

    EXPECT_EQ(e.getSource(), 10);
    EXPECT_EQ(e.getTarget(), 20);
    EXPECT_EQ(e.getId(), 5u);
}

TEST(EdgeTest, ComparisonOperators) {
    Edge<int> e1(1, 2, 1);
    Edge<int> e2(1, 2, 2); // id не влияет на топологическое равенство
    Edge<int> e3(1, 3, 1);
    Edge<int> e4(2, 1, 1);

    EXPECT_TRUE(e1 == e2);
    EXPECT_FALSE(e1 != e2);
    EXPECT_TRUE(e1 != e3);

    EXPECT_TRUE(e1 < e3);
    EXPECT_TRUE(e1 <= e3);
    EXPECT_TRUE(e1 <= e2);
    EXPECT_TRUE(e3 > e1);
    EXPECT_TRUE(e3 >= e1);
    EXPECT_TRUE(e1 >= e2);
    EXPECT_TRUE(e1 < e4);
}

TEST(EdgeTest, StreamOutput) {
    Edge<std::string> e("U", "V", 1);
    std::stringstream ss;
    ss << e;
    EXPECT_EQ(ss.str(), "(U -> V)");

    Edge<std::string> loop("U", "U", 2);
    std::stringstream ss_loop;
    ss_loop << loop;
    EXPECT_EQ(ss_loop.str(), "(U -> U [петля])");
}
