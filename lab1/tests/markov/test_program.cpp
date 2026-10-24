#include <gtest/gtest.h>
#include "markov/MarkovProgram.h"
#include <sstream>

TEST(MarkovProgramTest, AddRemoveGet) {
    MarkovProgram prog;
    EXPECT_EQ(prog.getRuleCount(), 0);
    EXPECT_TRUE(prog.empty());

    prog.addRule(MarkovRule("A", "B", false));
    EXPECT_EQ(prog.getRuleCount(), 1);
    EXPECT_FALSE(prog.empty());
    EXPECT_EQ(prog.getRule(0).getFrom(), "A");

    prog.removeRule(0);
    EXPECT_EQ(prog.getRuleCount(), 0);
    EXPECT_TRUE(prog.empty());

    EXPECT_THROW(prog.getRule(0), std::out_of_range);
    EXPECT_THROW(prog.removeRule(0), std::out_of_range);
}

TEST(MarkovProgramTest, Clear) {
    MarkovProgram prog;
    prog.addRule(MarkovRule("A", "B", false));
    prog.addRule(MarkovRule("C", "D", true));
    EXPECT_EQ(prog.getRuleCount(), 2);
    prog.clear();
    EXPECT_TRUE(prog.empty());
    EXPECT_EQ(prog.getRuleCount(), 0);
}

TEST(MarkovProgramTest, CopyAssignmentEquality) {
    MarkovProgram prog1;
    prog1.addRule(MarkovRule("A", "B", false));

    MarkovProgram prog2(prog1);
    EXPECT_EQ(prog2.getRuleCount(), 1);

    MarkovProgram prog3;
    prog3 = prog1;
    EXPECT_EQ(prog3.getRuleCount(), 1);

    EXPECT_TRUE(prog1 == prog2);
    EXPECT_TRUE(prog1 == prog3);

    prog3.addRule(MarkovRule("C", "D", true));
    EXPECT_FALSE(prog1 == prog3);
    EXPECT_TRUE(prog1 != prog3);
    
    // self assignment
    prog3 = prog3;
    EXPECT_EQ(prog3.getRuleCount(), 2);
}

TEST(MarkovProgramTest, IOStream) {
    MarkovProgram prog;
    prog.addRule(MarkovRule("A", "B", false));
    prog.addRule(MarkovRule("C", "D", true));

    std::stringstream ss;
    ss << prog;
    EXPECT_EQ(ss.str(), "A -> B\nC ->. D\n");

    MarkovProgram prog_read;
    std::stringstream ss2("X -> Y\nZ ->. W\n");
    ss2 >> prog_read;
    EXPECT_EQ(prog_read.getRuleCount(), 2);
    EXPECT_EQ(prog_read.getRule(0).getFrom(), "X");
    EXPECT_EQ(prog_read.getRule(1).getTo(), "W");
    EXPECT_TRUE(prog_read.getRule(1).isTerminal());
}
