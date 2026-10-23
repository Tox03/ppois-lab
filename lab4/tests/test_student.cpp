#include <gtest/gtest.h>
#include "model/Student.h"
#include <sstream>

TEST(StudentTest, DefaultAndParameterizedConstructors) {
    Student default_student;
    EXPECT_EQ(default_student.getId(), 0);
    EXPECT_EQ(default_student.getName(), "");
    EXPECT_EQ(default_student.getRating(), 0);

    Student s(1, "Иван", 90);
    EXPECT_EQ(s.getId(), 1);
    EXPECT_EQ(s.getName(), "Иван");
    EXPECT_EQ(s.getRating(), 90);
}

TEST(StudentTest, SettersAndGetters) {
    Student s;
    s.setId(10);
    s.setName("Петр");
    s.setRating(80);

    EXPECT_EQ(s.getId(), 10);
    EXPECT_EQ(s.getName(), "Петр");
    EXPECT_EQ(s.getRating(), 80);
}

TEST(StudentTest, ComparisonOperators) {
    Student s1(1, "Анна", 90);
    Student s2(1, "Анна", 90);
    Student s3(2, "Борис", 85);
    Student s4(3, "Анна", 90);

    EXPECT_TRUE(s1 == s2);
    EXPECT_FALSE(s1 != s2);

    EXPECT_TRUE(s3 < s1);
    EXPECT_TRUE(s3 <= s1);
    EXPECT_TRUE(s1 > s3);
    EXPECT_TRUE(s1 >= s3);

    EXPECT_TRUE(s1 <= s2);
    EXPECT_TRUE(s1 >= s2);

    EXPECT_TRUE(s1 < s4); // Одинаковый рейтинг, одинаковое имя, но id меньше
}

TEST(StudentTest, StreamOutput) {
    Student s(42, "Тест", 99);
    std::ostringstream oss;
    oss << s;
    std::string text = oss.str();
    EXPECT_NE(text.find("42"), std::string::npos);
    EXPECT_NE(text.find("Тест"), std::string::npos);
    EXPECT_NE(text.find("99"), std::string::npos);
}
