#include <gtest/gtest.h>
#include "turing/TuringMachine.h"
#include <sstream>

TEST(TuringMachineTest, ConstructorsAndState) {
    TuringMachine tm("start");
    EXPECT_EQ(tm.get_state(), "start");
    EXPECT_FALSE(tm.is_halted());

    tm.set_state("q1");
    EXPECT_EQ(tm.get_state(), "q1");

    const TuringMachine& const_tm = tm;
    EXPECT_EQ(const_tm.get_state(), "q1");
    EXPECT_EQ(const_tm.get_tape().read_symbol(), '_');
    EXPECT_EQ(const_tm.get_rules().size(), 0);
}

TEST(TuringMachineTest, StepAndRunBitInversion) {
    TuringMachine tm("q0");
    std::stringstream input("1011\nq0 1 q0 0 R\nq0 0 q0 1 R\nq0 _ q1 _ N\n");
    input >> tm;

    EXPECT_FALSE(tm.is_halted());

    // Run step by step
    // 1st step: reads '1', writes '0', moves R, stays q0
    EXPECT_TRUE(tm.step());
    EXPECT_EQ(tm.get_tape().read_at(0), '0');

    // Run to completion with logging enabled to exercise logging code
    tm.run(true);

    EXPECT_TRUE(tm.is_halted());
    EXPECT_EQ(tm.get_state(), "q1");
    EXPECT_EQ(tm.get_tape().read_at(0), '0');
    EXPECT_EQ(tm.get_tape().read_at(1), '1');
    EXPECT_EQ(tm.get_tape().read_at(2), '0');
    EXPECT_EQ(tm.get_tape().read_at(3), '0');

    // Further steps should return false
    EXPECT_FALSE(tm.step());
}

TEST(TuringMachineTest, NormalRunWithoutLog) {
    TuringMachine tm("q0");
    std::stringstream input("1\nq0 1 halt 0 N\n");
    input >> tm;

    tm.run(false);
    EXPECT_TRUE(tm.is_halted());
    EXPECT_EQ(tm.get_state(), "halt");
    EXPECT_EQ(tm.get_tape().read_at(0), '0');
}

TEST(TuringMachineTest, EqualityAndStreams) {
    TuringMachine tm1("q0");
    TuringMachine tm2("q0");
    EXPECT_TRUE(tm1 == tm2);

    tm1.set_state("q_diff");
    EXPECT_FALSE(tm1 == tm2);
    EXPECT_TRUE(tm1 != tm2);

    std::stringstream ss;
    ss << tm1;
    EXPECT_NE(ss.str().find("State: q_diff"), std::string::npos);
}
