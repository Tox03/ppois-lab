#include <gtest/gtest.h>
#include <sstream>
#include <string>
#include "ui/ConsoleMenu.h"

TEST(ConsoleMenuTest, RunDemoDirectly) {
    ConsoleMenu menu;
    std::stringstream out;
    menu.runDemo(out);
    std::string s = out.str();
    EXPECT_NE(s.find("GNOME SORT"), std::string::npos);
    EXPECT_NE(s.find("PIGEONHOLE SORT"), std::string::npos);
    EXPECT_NE(s.find("ОРИЕНТИРОВАННЫЙ ГРАФ"), std::string::npos);
}

TEST(ConsoleMenuTest, InteractiveExit) {
    ConsoleMenu menu;
    std::stringstream in("0\n");
    std::stringstream out;
    menu.run(in, out);
    EXPECT_NE(out.str().find("Завершение работы программы"), std::string::npos);
}

TEST(ConsoleMenuTest, InteractiveInvalidChoice) {
    ConsoleMenu menu;
    std::stringstream in("99\n0\n");
    std::stringstream out;
    menu.run(in, out);
    EXPECT_NE(out.str().find("Неизвестный пункт меню"), std::string::npos);
}

TEST(ConsoleMenuTest, InteractiveSortSubmenu) {
    ConsoleMenu menu;
    // 1 (сортировки) -> 1 (Gnome) -> 1 (вектор)
    // 1 (сортировки) -> 1 (Gnome) -> 2 (массив)
    // 1 (сортировки) -> 1 (Gnome) -> 3 (студенты)
    // 1 (сортировки) -> 2 (Pigeonhole) -> 1 (вектор)
    // 1 (сортировки) -> 2 (Pigeonhole) -> 2 (массив)
    // 1 (сортировки) -> 2 (Pigeonhole) -> 3 (студенты)
    // 1 (сортировки) -> 99 (неверный алгоритм)
    // 0 (выход)
    std::stringstream in(
        "1\n1\n1\n"
        "1\n1\n2\n"
        "1\n1\n3\n"
        "1\n2\n1\n"
        "1\n2\n2\n"
        "1\n2\n3\n"
        "1\n99\n"
        "0\n"
    );
    std::stringstream out;
    menu.run(in, out);
    EXPECT_NE(out.str().find("Отсортированный вектор"), std::string::npos);
    EXPECT_NE(out.str().find("Отсортированный массив"), std::string::npos);
    EXPECT_NE(out.str().find("Студенты после сортировки"), std::string::npos);
}

TEST(ConsoleMenuTest, InteractiveGraphSubmenu) {
    ConsoleMenu menu;
    // 2 (граф) ->
    // 13 (тестовый граф) ->
    // 5 A (степени) ->
    // 6 A B (степень ребра) ->
    // 7 (обход вершин) ->
    // 8 (обход рёбер) ->
    // 9 A (инцидентные рёбра) ->
    // 10 A (смежные вершины) ->
    // 11 (показать граф) ->
    // 12 (показать матрицу) ->
    // 1 X (добавить вершину) ->
    // 2 X A (добавить ребро) ->
    // 4 X A (удалить ребро) ->
    // 3 X (удалить вершину) ->
    // 99 (неверный пункт в меню графа) ->
    // 0 (выход из подменю графа) ->
    // 3 (автоматическая демонстрация) ->
    // 0 (выход из главного меню)
    std::stringstream in(
        "2\n"
        "13\n"
        "5\nA\n"
        "6\nA\nB\n"
        "7\n"
        "8\n"
        "9\nA\n"
        "10\nA\n"
        "11\n"
        "12\n"
        "1\nX\n"
        "2\nX\nA\n"
        "4\nX\nA\n"
        "3\nX\n"
        "99\n"
        "0\n"
        "3\n"
        "0\n"
    );
    std::stringstream out;
    menu.run(in, out);
    EXPECT_NE(out.str().find("Тестовый граф успешно загружен"), std::string::npos);
    EXPECT_NE(out.str().find("Прямой обход вершин"), std::string::npos);
    EXPECT_NE(out.str().find("Прямой обход рёбер"), std::string::npos);
    EXPECT_NE(out.str().find("Матрица инцидентности"), std::string::npos);
}
