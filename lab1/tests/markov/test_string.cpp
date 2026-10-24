#include <gtest/gtest.h>
#include "markov/MarkovString.h"
#include <sstream>

TEST(MarkovStringTest, Constructors) {
    MarkovString str1;
    EXPECT_EQ(str1.getValue(), "");
    EXPECT_EQ(str1.getCaretPos(), 0);

    MarkovString str2("abc");
    EXPECT_EQ(str2.getValue(), "abc");
    EXPECT_EQ(str2.getCaretPos(), 0);

    MarkovString str3(str2);
    EXPECT_EQ(str3.getValue(), "abc");
}

TEST(MarkovStringTest, AssignmentAndSetters) {
    MarkovString str1("abc");
    MarkovString str2;
    str2 = str1;
    EXPECT_EQ(str2.getValue(), "abc");

    // self assignment
    str2 = str2;
    EXPECT_EQ(str2.getValue(), "abc");

    str2.setValue("def");
    EXPECT_EQ(str2.getValue(), "def");

    str2.setCaretPos(2);
    EXPECT_EQ(str2.getCaretPos(), 2);

    str2.setCaretPos(10);
    EXPECT_EQ(str2.getCaretPos(), 2);
    
    str2.setValue("d");
    EXPECT_EQ(str2.getCaretPos(), 1);
}

TEST(MarkovStringTest, IncrementDecrement) {
    MarkovString str("abc");
    ++str;
    EXPECT_EQ(str.getCaretPos(), 1);
    str++;
    EXPECT_EQ(str.getCaretPos(), 2);
    --str;
    EXPECT_EQ(str.getCaretPos(), 1);
    str--;
    EXPECT_EQ(str.getCaretPos(), 0);
    str--; // underflow check
    EXPECT_EQ(str.getCaretPos(), 0);

    str.setCaretPos(3);
    ++str; // overflow check
    EXPECT_EQ(str.getCaretPos(), 3);
}

TEST(MarkovStringTest, Equality) {
    MarkovString str1("abc");
    MarkovString str2("abc");
    MarkovString str3("def");
    
    EXPECT_TRUE(str1 == str2);
    EXPECT_FALSE(str1 == str3);
    EXPECT_TRUE(str1 != str3);
}

TEST(MarkovStringTest, IOStream) {
    MarkovString str1("hello");
    std::stringstream ss;
    ss << str1;
    EXPECT_EQ(ss.str(), "hello");

    MarkovString str2;
    std::stringstream ss2("world");
    ss2 >> str2;
    EXPECT_EQ(str2.getValue(), "world");
}
