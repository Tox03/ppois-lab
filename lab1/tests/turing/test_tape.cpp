#include <gtest/gtest.h>
#include "turing/Tape.h"
#include <sstream>

TEST(TapeTest, DefaultConstructorAndBlankSymbol) {
    Tape tape;
    EXPECT_EQ(tape.read_symbol(), '_');
    EXPECT_EQ(tape.get_head_position(), 0);

    Tape tape_star('*');
    EXPECT_EQ(tape_star.read_symbol(), '*');
}

TEST(TapeTest, WriteAndReadSymbol) {
    Tape tape;
    tape.write_symbol('1');
    EXPECT_EQ(tape.read_symbol(), '1');

    // Writing blank erases the cell
    tape.write_symbol('_');
    EXPECT_EQ(tape.read_symbol(), '_');
}

TEST(TapeTest, MoveHead) {
    Tape tape;
    tape.move_head('R');
    EXPECT_EQ(tape.get_head_position(), 1);
    tape.move_head('r');
    EXPECT_EQ(tape.get_head_position(), 2);
    tape.move_head('L');
    EXPECT_EQ(tape.get_head_position(), 1);
    tape.move_head('l');
    EXPECT_EQ(tape.get_head_position(), 0);
    tape.move_head('N');
    EXPECT_EQ(tape.get_head_position(), 0);

    tape.set_head_position(10);
    EXPECT_EQ(tape.get_head_position(), 10);
}

TEST(TapeTest, ReadWriteAtAndProxyOperator) {
    Tape tape;
    tape.write_at(5, 'A');
    EXPECT_EQ(tape.read_at(5), 'A');
    EXPECT_EQ(tape.read_at(3), '_');

    tape.write_at(5, '_');
    EXPECT_EQ(tape.read_at(5), '_');

    // Proxy operator[]
    tape[10] = 'Z';
    char val = tape[10];
    EXPECT_EQ(val, 'Z');
    EXPECT_EQ(tape.read_at(10), 'Z');
}

TEST(TapeTest, StreamsAndFormatting) {
    Tape empty_tape;
    std::stringstream ss_empty;
    ss_empty << empty_tape;
    EXPECT_NE(ss_empty.str().find("[Empty Tape]"), std::string::npos);

    Tape tape;
    std::stringstream input("1011");
    input >> tape;
    EXPECT_EQ(tape.read_at(0), '1');
    EXPECT_EQ(tape.read_at(1), '0');
    EXPECT_EQ(tape.read_at(2), '1');
    EXPECT_EQ(tape.read_at(3), '1');

    std::stringstream ss_out;
    ss_out << tape;
    EXPECT_NE(ss_out.str().find("1011"), std::string::npos);
    EXPECT_NE(ss_out.str().find("^"), std::string::npos);
}

TEST(TapeTest, EqualityOperators) {
    Tape t1, t2;
    EXPECT_TRUE(t1 == t2);

    t1.write_symbol('1');
    EXPECT_FALSE(t1 == t2);
    EXPECT_TRUE(t1 != t2);

    t2.write_symbol('1');
    EXPECT_TRUE(t1 == t2);

    t1.move_head('R');
    EXPECT_FALSE(t1 == t2);
}
