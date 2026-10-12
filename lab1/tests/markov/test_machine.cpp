#include <gtest/gtest.h>
#include "markov/MarkovMachine.h"
#include <sstream>

TEST(MarkovMachineTest, ConstructorsAndSetters) {
    MarkovMachine machine;
    EXPECT_FALSE(machine.isHalted());
    EXPECT_FALSE(machine.isLogEnabled());

    machine.setLogEnabled(true);
    EXPECT_TRUE(machine.isLogEnabled());

    MarkovString tape("111");
    machine.setTape(tape);
    EXPECT_EQ(machine.getTape().getValue(), "111");

    MarkovProgram prog;
    prog.addRule(MarkovRule("1", "0", false));
    machine.setProgram(prog);
    EXPECT_EQ(machine.getProgram().getRuleCount(), 1);

    machine.addRule(MarkovRule("0", "2", true));
    EXPECT_EQ(machine.getProgram().getRuleCount(), 2);

    machine.removeRule(1);
    EXPECT_EQ(machine.getProgram().getRuleCount(), 1);

    MarkovMachine m2(machine);
    EXPECT_EQ(m2.getTape().getValue(), "111");

    MarkovMachine m3;
    m3 = machine;
    EXPECT_EQ(m3.getTape().getValue(), "111");
}

TEST(MarkovMachineTest, StepAndRun) {
    MarkovMachine machine;
    MarkovProgram prog;
    // rule 1: "11" -> "0"
    prog.addRule(MarkovRule("11", "0", false));
    // rule 2: "0" -> "1" (terminal)
    prog.addRule(MarkovRule("0", "1", true));
    
    machine.setProgram(prog);
    machine.setTape(MarkovString("111"));
    machine.setLogEnabled(true);

    bool res = machine.step();
    EXPECT_TRUE(res);
    EXPECT_EQ(machine.getTape().getValue(), "01");
    EXPECT_FALSE(machine.isHalted());

    res = machine.step();
    EXPECT_TRUE(res);
    EXPECT_EQ(machine.getTape().getValue(), "11");
    EXPECT_TRUE(machine.isHalted());

    res = machine.step();
    EXPECT_FALSE(res);
    EXPECT_EQ(machine.getTape().getValue(), "11");
}

TEST(MarkovMachineTest, RunToCompletion) {
    MarkovMachine machine;
    MarkovProgram prog;
    prog.addRule(MarkovRule("ab", "ba", false));
    prog.addRule(MarkovRule("ba", "", true));
    
    machine.setProgram(prog);
    machine.setTape(MarkovString("aab"));
    machine.run();
    
    EXPECT_EQ(machine.getTape().getValue(), "a");
    EXPECT_TRUE(machine.isHalted());
}

TEST(MarkovMachineTest, ResetAndHalt) {
    MarkovMachine machine;
    machine.step();
    EXPECT_TRUE(machine.isHalted());
    machine.reset();
    EXPECT_FALSE(machine.isHalted());
}

TEST(MarkovMachineTest, LoadStreams) {
    MarkovMachine machine;
    std::stringstream tape_ss("hello");
    machine.loadTapeFromStream(tape_ss);
    EXPECT_EQ(machine.getTape().getValue(), "hello");

    std::stringstream prog_ss("h -> H\no -> O\n");
    machine.loadProgramFromStream(prog_ss);
    
    machine.run();
    EXPECT_EQ(machine.getTape().getValue(), "HellO");
}

TEST(MarkovMachineTest, StreamOperators) {
    MarkovMachine machine;
    std::stringstream input("input_tape\ni -> I\n");
    input >> machine;
    EXPECT_EQ(machine.getTape().getValue(), "input_tape");
    EXPECT_EQ(machine.getProgram().getRuleCount(), 1);

    std::stringstream out;
    out << machine;
    EXPECT_FALSE(out.str().empty());
}

TEST(MarkovMachineTest, Equality) {
    MarkovMachine m1, m2;
    EXPECT_TRUE(m1 == m2);
    m1.setLogEnabled(true);
    EXPECT_FALSE(m1 == m2);
    EXPECT_TRUE(m1 != m2);
}
