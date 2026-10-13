#include <gtest/gtest.h>
#include <sstream>
#include "model/Student.h"

TEST(StudentTest, DefaultAndParameterizedConstructors) {
    Student def;
    EXPECT_EQ(def.getId(), 0);
    EXPECT_EQ(def.getName(), "");
    EXPECT_DOUBLE_EQ(def.getGpa(), 0.0);
    EXPECT_EQ(def.getAge(), 0);

    Student s(123, "Иван Иванов", 4.75, 20);
    EXPECT_EQ(s.getId(), 123);
    EXPECT_EQ(s.getName(), "Иван Иванов");
    EXPECT_DOUBLE_EQ(s.getGpa(), 4.75);
    EXPECT_EQ(s.getAge(), 20);
}

TEST(StudentTest, Setters) {
    Student s;
    s.setId(456);
    s.setName("Петр Петров");
    s.setGpa(3.8);
    s.setAge(22);

    EXPECT_EQ(s.getId(), 456);
    EXPECT_EQ(s.getName(), "Петр Петров");
    EXPECT_DOUBLE_EQ(s.getGpa(), 3.8);
    EXPECT_EQ(s.getAge(), 22);
}

TEST(StudentTest, ComparisonOperators) {
    Student s1(10, "A", 4.0, 20);
    Student s2(10, "A", 4.0, 20);
    Student s3(20, "B", 4.5, 21);

    EXPECT_TRUE(s1 == s2);
    EXPECT_FALSE(s1 != s2);
    EXPECT_TRUE(s1 != s3);

    EXPECT_TRUE(s1 < s3);
    EXPECT_TRUE(s1 <= s3);
    EXPECT_TRUE(s1 <= s2);
    EXPECT_FALSE(s3 < s1);

    EXPECT_TRUE(s3 > s1);
    EXPECT_TRUE(s3 >= s1);
    EXPECT_TRUE(s1 >= s2);
    EXPECT_FALSE(s1 > s3);
}

TEST(StudentTest, StreamOutputAndInput) {
    Student s(101, "Иванов", 4.5, 20);
    std::stringstream ss_out;
    ss_out << s;
    EXPECT_FALSE(ss_out.str().empty());

    std::stringstream ss_in("202 Сидоров 4.9 21");
    Student read_s;
    ss_in >> read_s;
    EXPECT_EQ(read_s.getId(), 202);
    EXPECT_EQ(read_s.getName(), "Сидоров");
    EXPECT_DOUBLE_EQ(read_s.getGpa(), 4.9);
    EXPECT_EQ(read_s.getAge(), 21);
}
