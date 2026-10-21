#include "ui/ConsoleMenu.h"
#include "sort/GnomeSort.h"
#include "sort/PigeonholeSort.h"
#include "model/Student.h"
#include <vector>
#include <limits>

ConsoleMenu::ConsoleMenu()
    : graph_() {
}

void ConsoleMenu::printMenu(std::ostream& out) const {
    out << "\n================= МЕНЮ УПРАВЛЕНИЯ ЛАБОРАТОРНОЙ РАБОТОЙ №4 =================\n"
        << "--- Вершины графа (симметричные операции) ---\n"
        << " 1. Добавить вершину\n"
        << " 2. Удалить вершину\n"
        << " 3. Проверить наличие вершины\n"
        << "--- Рёбра графа (симметричные операции) ---\n"
        << " 4. Добавить ребро\n"
        << " 5. Удалить ребро\n"
        << " 6. Проверить наличие ребра\n"
        << "--- Состояние графа ---\n"
        << " 7. Очистить граф\n"
        << " 8. Заполнить демонстрационным графом\n"
        << " 9. Вывести матрицу инцидентности\n"
        << "10. Вывести сводку о графе (степени вершин, количество рёбер)\n"
        << "11. Продемонстрировать обход итераторами\n"
        << "--- Сортировка (симметричные операции по возрастанию и убыванию) ---\n"
        << "12. Сортировка чисел по возрастанию (Gnome Sort и Pigeonhole Sort)\n"
        << "13. Сортировка чисел по убыванию (Gnome Sort и Pigeonhole Sort)\n"
        << "14. Сортировка студентов по возрастанию (по рейтингу)\n"
        << "15. Сортировка студентов по убыванию (по рейтингу)\n"
        << "--- Демонстрация и выход ---\n"
        << "16. Запустить полный демонстрационный сценарий\n"
        << " 0. Выход\n"
        << "===========================================================================\n"
        << "Выберите команду: ";
}

void ConsoleMenu::clearGraph() {
    graph_.clear();
}

void ConsoleMenu::populateDemoGraph() {
    graph_.clear();
    graph_.insertVertex("A");
    graph_.insertVertex("B");
    graph_.insertVertex("C");
    graph_.insertVertex("D");

    graph_.insertEdge("A", "B");
    graph_.insertEdge("B", "C");
    graph_.insertEdge("C", "A");
    graph_.insertEdge("C", "D");
    graph_.insertEdge("D", "D"); // петля
}

void ConsoleMenu::handleAddVertex(std::istream& in, std::ostream& out) {
    out << "Введите имя вершины для добавления: ";
    std::string name;
    if (in >> name) {
        try {
            graph_.insertVertex(name);
            out << "Вершина '" << name << "' успешно добавлена.\n";
        } catch (const std::exception& ex) {
            out << "Ошибка при добавлении вершины: " << ex.what() << "\n";
        }
    }
}

void ConsoleMenu::handleRemoveVertex(std::istream& in, std::ostream& out) {
    out << "Введите имя вершины для удаления: ";
    std::string name;
    if (in >> name) {
        try {
            graph_.eraseVertex(name);
            out << "Вершина '" << name << "' успешно удалена.\n";
        } catch (const std::exception& ex) {
            out << "Ошибка при удалении вершины: " << ex.what() << "\n";
        }
    }
}

void ConsoleMenu::handleCheckVertex(std::istream& in, std::ostream& out) {
    out << "Введите имя вершины для проверки: ";
    std::string name;
    if (in >> name) {
        bool exists = graph_.hasVertex(name);
        out << "Вершина '" << name << "' " << (exists ? "присутствует" : "отсутствует") << " в графе.\n";
    }
}

void ConsoleMenu::handleAddEdge(std::istream& in, std::ostream& out) {
    out << "Введите начальную и конечную вершины ребра через пробел: ";
    std::string from;
    std::string to;
    if (in >> from >> to) {
        try {
            graph_.insertEdge(from, to);
            out << "Ребро (" << from << " -> " << to << ") успешно добавлено.\n";
        } catch (const std::exception& ex) {
            out << "Ошибка при добавлении ребра: " << ex.what() << "\n";
        }
    }
}

void ConsoleMenu::handleRemoveEdge(std::istream& in, std::ostream& out) {
    out << "Введите начальную и конечную вершины ребра для удаления: ";
    std::string from;
    std::string to;
    if (in >> from >> to) {
        try {
            graph_.eraseEdge(from, to);
            out << "Ребро (" << from << " -> " << to << ") успешно удалено.\n";
        } catch (const std::exception& ex) {
            out << "Ошибка при удалении ребра: " << ex.what() << "\n";
        }
    }
}

void ConsoleMenu::handleCheckEdge(std::istream& in, std::ostream& out) {
    out << "Введите начальную и конечную вершины для проверки: ";
    std::string from;
    std::string to;
    if (in >> from >> to) {
        bool exists = graph_.hasEdge(from, to);
        out << "Ребро (" << from << " -> " << to << ") "
            << (exists ? "присутствует" : "отсутствует") << " в графе.\n";
    }
}

void ConsoleMenu::handlePrintMatrix(std::ostream& out) {
    out << "\n--- Матрица инцидентности графа ---\n";
    graph_.printIncidenceMatrix(out);
}

void ConsoleMenu::handlePrintSummary(std::ostream& out) {
    out << "\n--- Сводка о графе ---\n"
        << "Количество вершин: " << graph_.vertexCount() << "\n"
        << "Количество рёбер: " << graph_.edgeCount() << "\n"
        << "Граф пуст: " << (graph_.empty() ? "Да" : "Нет") << "\n";

    for (auto it = graph_.verticesBegin(); it != graph_.verticesEnd(); ++it) {
        const std::string& v = *it;
        out << "Вершина '" << v << "': полустепень исхода = " << graph_.outDegree(v)
            << ", полустепень захода = " << graph_.inDegree(v)
            << ", общая степень = " << graph_.degree(v) << "\n";
    }
}

void ConsoleMenu::handlePrintIterators(std::ostream& out) {
    out << "\n--- Прямой обход вершин ---\n";
    for (auto it = graph_.verticesBegin(); it != graph_.verticesEnd(); ++it) {
        out << *it << " ";
    }
    out << "\n--- Обратный обход вершин ---\n";
    for (auto it = graph_.verticesRBegin(); it != graph_.verticesREnd(); ++it) {
        out << *it << " ";
    }
    out << "\n--- Все рёбра графа ---\n";
    for (auto it = graph_.edgesBegin(); it != graph_.edgesEnd(); ++it) {
        out << *it << "\n";
    }
}

void ConsoleMenu::handleSortNumbersAscending(std::ostream& out) {
    std::vector<int> data = {42, 17, 88, 3, 25, 64, 12, 99, 5};
    out << "\nИсходный массив: ";
    for (int n : data) out << n << " ";
    out << "\n";

    std::vector<int> gnome_data = data;
    GnomeSort::sort(gnome_data);
    out << "GnomeSort (по возрастанию): ";
    for (int n : gnome_data) out << n << " ";
    out << "\n";

    std::vector<int> pigeon_data = data;
    PigeonholeSort::sort(pigeon_data);
    out << "PigeonholeSort (по возрастанию): ";
    for (int n : pigeon_data) out << n << " ";
    out << "\n";
}

void ConsoleMenu::handleSortNumbersDescending(std::ostream& out) {
    std::vector<int> data = {42, 17, 88, 3, 25, 64, 12, 99, 5};
    out << "\nИсходный массив: ";
    for (int n : data) out << n << " ";
    out << "\n";

    std::vector<int> gnome_data = data;
    GnomeSort::sort_descending(gnome_data);
    out << "GnomeSort (по убыванию): ";
    for (int n : gnome_data) out << n << " ";
    out << "\n";

    std::vector<int> pigeon_data = data;
    PigeonholeSort::sort_descending(pigeon_data);
    out << "PigeonholeSort (по убыванию): ";
    for (int n : pigeon_data) out << n << " ";
    out << "\n";
}

void ConsoleMenu::handleSortStudentsAscending(std::ostream& out) {
    std::vector<Student> students = {
        Student(101, "Иван Иванов", 85),
        Student(102, "Петр Петров", 72),
        Student(103, "Анна Смирнова", 95),
        Student(104, "Ольга Кузнецова", 60)
    };

    out << "\nИсходный список студентов:\n";
    for (const auto& s : students) out << "  " << s << "\n";

    GnomeSort::sort(students);
    out << "После GnomeSort (по возрастанию рейтинга):\n";
    for (const auto& s : students) out << "  " << s << "\n";

    auto key_func = [](const Student& s) { return static_cast<std::int64_t>(s.getRating()); };
    PigeonholeSort::sort(students, key_func);
    out << "После PigeonholeSort (по возрастанию рейтинга):\n";
    for (const auto& s : students) out << "  " << s << "\n";
}

void ConsoleMenu::handleSortStudentsDescending(std::ostream& out) {
    std::vector<Student> students = {
        Student(101, "Иван Иванов", 85),
        Student(102, "Петр Петров", 72),
        Student(103, "Анна Смирнова", 95),
        Student(104, "Ольга Кузнецова", 60)
    };

    out << "\nИсходный список студентов:\n";
    for (const auto& s : students) out << "  " << s << "\n";

    GnomeSort::sort_descending(students);
    out << "После GnomeSort (по убыванию рейтинга):\n";
    for (const auto& s : students) out << "  " << s << "\n";

    auto key_func = [](const Student& s) { return static_cast<std::int64_t>(s.getRating()); };
    PigeonholeSort::sort_descending(students, key_func);
    out << "После PigeonholeSort (по убыванию рейтинга):\n";
    for (const auto& s : students) out << "  " << s << "\n";
}

void ConsoleMenu::runDemo(std::ostream& out) {
    out << "=======================================================\n"
        << "  ДЕМОНСТРАЦИОННЫЙ РЕЖИМ ЛАБОРАТОРНОЙ РАБОТЫ №4\n"
        << "=======================================================\n";

    out << "\n>>> 1. Сортировка чисел (GnomeSort и PigeonholeSort)\n";
    handleSortNumbersAscending(out);
    handleSortNumbersDescending(out);

    out << "\n>>> 2. Сортировка пользовательских объектов (Student)\n";
    handleSortStudentsAscending(out);
    handleSortStudentsDescending(out);

    out << "\n>>> 3. Построение ориентированного графа матрицей инцидентности\n";
    populateDemoGraph();
    handlePrintMatrix(out);
    handlePrintSummary(out);
    handlePrintIterators(out);

    out << "\n>>> 4. Удаление ребра (A -> B) и вершины (D)\n";
    graph_.eraseEdge("A", "B");
    graph_.eraseVertex("D");
    handlePrintMatrix(out);
    handlePrintSummary(out);

    out << "\n>>> 5. Очистка графа\n";
    clearGraph();
    out << "Граф очищен, пустота: " << (graph_.empty() ? "Да" : "Нет") << "\n";

    out << "\n================ ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА ================\n";
}

void ConsoleMenu::run(std::istream& in, std::ostream& out) {
    bool running = true;
    while (running) {
        printMenu(out);
        int choice = -1;
        if (!(in >> choice)) {
            in.clear();
            std::string dummy;
            if (!(in >> dummy)) {
                break;
            }
            out << "Неверный ввод, повторите попытку.\n";
            continue;
        }

        switch (choice) {
            case 1: handleAddVertex(in, out); break;
            case 2: handleRemoveVertex(in, out); break;
            case 3: handleCheckVertex(in, out); break;
            case 4: handleAddEdge(in, out); break;
            case 5: handleRemoveEdge(in, out); break;
            case 6: handleCheckEdge(in, out); break;
            case 7: clearGraph(); out << "Граф очищен.\n"; break;
            case 8: populateDemoGraph(); out << "Демо-граф загружен.\n"; break;
            case 9: handlePrintMatrix(out); break;
            case 10: handlePrintSummary(out); break;
            case 11: handlePrintIterators(out); break;
            case 12: handleSortNumbersAscending(out); break;
            case 13: handleSortNumbersDescending(out); break;
            case 14: handleSortStudentsAscending(out); break;
            case 15: handleSortStudentsDescending(out); break;
            case 16: runDemo(out); break;
            case 0:
                out << "Выход из программы.\n";
                running = false;
                break;
            default:
                out << "Неизвестная команда.\n";
                break;
        }
    }
}
