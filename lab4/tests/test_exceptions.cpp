#include <gtest/gtest.h>
#include <string>
#include "graph/GraphException.h"

TEST(ExceptionsTest, StringAndCStringConstructors) {
    GraphException ex1("Текст ошибки");
    EXPECT_STREQ(ex1.what(), "Текст ошибки");

    GraphException ex2(std::string("Другая ошибка"));
    EXPECT_STREQ(ex2.what(), "Другая ошибка");

    // Проверка, что GraphException наследуется от std::runtime_error
    try {
        throw GraphException("Проверка наследования");
    } catch (const std::runtime_error& err) {
        EXPECT_STREQ(err.what(), "Проверка наследования");
    }
}
