#include <gtest/gtest.h>
#include "turing/RuleSet.h"
#include <sstream>

TEST(RuleTest, EqualityOperators) {
    Rule r1{"q0", '1', "q0", '0', 'R'};
    Rule r2{"q0", '1', "q0", '0', 'R'};
    Rule r3{"q0", '0', "q0", '1', 'R'};

    EXPECT_TRUE(r1 == r2);
    EXPECT_FALSE(r1 == r3);
    EXPECT_TRUE(r1 != r3);
}

TEST(RuleSetTest, AddAndFindRule) {
    RuleSet rs;
    EXPECT_TRUE(rs.empty());
    EXPECT_EQ(rs.size(), 0);

    Rule r1{"q0", '1', "q1", '0', 'R'};
    rs.add_rule(r1);

    EXPECT_FALSE(rs.empty());
    EXPECT_EQ(rs.size(), 1);

    Rule found;
    EXPECT_TRUE(rs.find_rule("q0", '1', found));
    EXPECT_EQ(found, r1);

    EXPECT_FALSE(rs.find_rule("q0", '0', found));
    EXPECT_FALSE(rs.find_rule("q1", '1', found));
}

TEST(RuleSetTest, RemoveAndClear) {
    RuleSet rs;
    Rule r1{"q0", '1', "q1", '0', 'R'};
    rs += r1;
    EXPECT_EQ(rs.size(), 1);

    rs.remove_rule("q0", '1');
    EXPECT_TRUE(rs.empty());

    rs += r1;
    rs.clear();
    EXPECT_TRUE(rs.empty());
}

TEST(RuleSetTest, OperatorsPlusMinus) {
    RuleSet rs;
    Rule r1{"q0", '1', "q0", '0', 'R'};
    Rule r2{"q0", '0', "q0", '1', 'R'};

    rs += r1;
    EXPECT_EQ(rs.size(), 1);

    RuleSet rs2 = rs + r2;
    EXPECT_EQ(rs2.size(), 2);
    EXPECT_EQ(rs.size(), 1);

    rs2 -= r1;
    EXPECT_EQ(rs2.size(), 1);

    RuleSet rs3 = rs2 - r2;
    EXPECT_TRUE(rs3.empty());
}

TEST(RuleSetTest, StreamsAndEquality) {
    RuleSet rs;
    std::stringstream input("q0 1 q0 0 R\nq0 0 q0 1 R\n");
    input >> rs;

    EXPECT_EQ(rs.size(), 2);

    std::stringstream output;
    output << rs;
    EXPECT_FALSE(output.str().empty());

    RuleSet rs2;
    output >> rs2;
    EXPECT_TRUE(rs == rs2);

    Rule r_diff{"q1", '_', "q2", '_', 'N'};
    rs2 += r_diff;
    EXPECT_FALSE(rs == rs2);
    EXPECT_TRUE(rs != rs2);
}
