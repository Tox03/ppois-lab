#include <gtest/gtest.h>
#include "markov/MarkovRule.h"
#include <sstream>

TEST(MarkovRuleTest, ConstructorAndGetters) {
    MarkovRule rule1;
    EXPECT_EQ(rule1.getFrom(), "");
    EXPECT_EQ(rule1.getTo(), "");
    EXPECT_FALSE(rule1.isTerminal());

    MarkovRule rule2("A", "B", true);
    EXPECT_EQ(rule2.getFrom(), "A");
    EXPECT_EQ(rule2.getTo(), "B");
    EXPECT_TRUE(rule2.isTerminal());
}

TEST(MarkovRuleTest, CopyConstructorAndAssignment) {
    MarkovRule rule1("A", "B", true);
    MarkovRule rule2(rule1);
    EXPECT_EQ(rule2.getFrom(), "A");
    EXPECT_TRUE(rule2.isTerminal());

    MarkovRule rule3;
    rule3 = rule1;
    EXPECT_EQ(rule3.getFrom(), "A");
    EXPECT_TRUE(rule3.isTerminal());
    
    // self assignment
    rule3 = rule3;
    EXPECT_EQ(rule3.getFrom(), "A");
}

TEST(MarkovRuleTest, EqualityOperators) {
    MarkovRule rule1("A", "B", false);
    MarkovRule rule2("A", "B", false);
    MarkovRule rule3("A", "C", false);

    EXPECT_TRUE(rule1 == rule2);
    EXPECT_FALSE(rule1 == rule3);
    EXPECT_TRUE(rule1 != rule3);
}

TEST(MarkovRuleTest, IOStream) {
    MarkovRule rule1("A", "B", false);
    std::stringstream ss;
    ss << rule1;
    EXPECT_EQ(ss.str(), "A -> B");

    MarkovRule rule2("C", "D", true);
    std::stringstream ss2;
    ss2 << rule2;
    EXPECT_EQ(ss2.str(), "C ->. D");

    MarkovRule read_rule;
    std::stringstream ss3("X ->. Y");
    ss3 >> read_rule;
    EXPECT_EQ(read_rule.getFrom(), "X");
    EXPECT_EQ(read_rule.getTo(), "Y");
    EXPECT_TRUE(read_rule.isTerminal());

    MarkovRule read_rule2;
    std::stringstream ss4("X -> Y");
    ss4 >> read_rule2;
    EXPECT_EQ(read_rule2.getFrom(), "X");
    EXPECT_EQ(read_rule2.getTo(), "Y");
    EXPECT_FALSE(read_rule2.isTerminal());
}
