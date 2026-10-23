#include <gtest/gtest.h>
#include "ui/ConsoleMenu.h"
#include <sstream>

TEST(ConsoleMenuTest, RunDemoExecutesCleanly) {
    ConsoleMenu menu;
    std::ostringstream oss;
    EXPECT_NO_THROW(menu.runDemo(oss));
    std::string output = oss.str();
    EXPECT_NE(output.find("ДЕМОНСТРАЦИОННЫЙ РЕЖИМ"), std::string::npos);
    EXPECT_NE(output.find("GnomeSort"), std::string::npos);
    EXPECT_NE(output.find("PigeonholeSort"), std::string::npos);
}

TEST(ConsoleMenuTest, InteractiveAddRemoveVerticesAndEdges) {
    ConsoleMenu menu;
    // Команды:
    // 1 V1      (добавить V1)
    // 1 V2      (добавить V2)
    // 3 V1      (проверить V1)
    // 4 V1 V2   (добавить ребро V1 -> V2)
    // 6 V1 V2   (проверить ребро V1 -> V2)
    // 5 V1 V2   (удалить ребро V1 -> V2)
    // 2 V1      (удалить V1)
    // 0         (выход)
    std::string input = "1 V1\n1 V2\n3 V1\n4 V1 V2\n6 V1 V2\n5 V1 V2\n2 V1\n0\n";
    std::istringstream iss(input);
    std::ostringstream oss;

    EXPECT_NO_THROW(menu.run(iss, oss));
    std::string output = oss.str();
    EXPECT_NE(output.find("Вершина 'V1' успешно добавлена"), std::string::npos);
    EXPECT_NE(output.find("Ребро (V1 -> V2) успешно добавлено"), std::string::npos);
    EXPECT_NE(output.find("Ребро (V1 -> V2) успешно удалено"), std::string::npos);
    EXPECT_NE(output.find("Вершина 'V1' успешно удалена"), std::string::npos);
}

TEST(ConsoleMenuTest, InteractiveSortingAndStateCommands) {
    ConsoleMenu menu;
    // 8 (заполнить демо)
    // 9 (вывести матрицу)
    // 10 (вывести сводку)
    // 11 (итераторы)
    // 12 (сортировка чисел asc)
    // 13 (сортировка чисел desc)
    // 14 (сортировка студентов asc)
    // 15 (сортировка студентов desc)
    // 7 (очистить)
    // 0 (выход)
    std::string input = "8\n9\n10\n11\n12\n13\n14\n15\n7\n0\n";
    std::istringstream iss(input);
    std::ostringstream oss;

    EXPECT_NO_THROW(menu.run(iss, oss));
    std::string output = oss.str();
    EXPECT_NE(output.find("Демо-граф загружен"), std::string::npos);
    EXPECT_NE(output.find("Матрица инцидентности"), std::string::npos);
    EXPECT_NE(output.find("Граф очищен"), std::string::npos);
}

TEST(ConsoleMenuTest, InvalidInputHandling) {
    ConsoleMenu menu;
    // Ошибочный ввод буквы вместо цифры, затем 0 для выхода
    std::string input = "invalid_choice\n999\n0\n";
    std::istringstream iss(input);
    std::ostringstream oss;

    EXPECT_NO_THROW(menu.run(iss, oss));
    std::string output = oss.str();
    EXPECT_NE(output.find("Неверный ввод"), std::string::npos);
    EXPECT_NE(output.find("Неизвестная команда"), std::string::npos);
    EXPECT_NE(output.find("Выход из программы"), std::string::npos);
}
