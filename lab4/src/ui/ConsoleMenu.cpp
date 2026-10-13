#include "ui/ConsoleMenu.h"

#include <vector>
#include <sstream>
#include <algorithm>

#include "sort/GnomeSort.h"
#include "sort/PigeonholeSort.h"
#include "model/Student.h"
#include "graph/DirectedIncidenceMatrixGraph.h"

// Конструктор по умолчанию
ConsoleMenu::ConsoleMenu() = default;

// Отображение главного меню
void ConsoleMenu::showMainMenu(std::ostream& out) const {
    out << "\n=======================================================\n";
    out << "   ЛАБОРАТОРНАЯ РАБОТА №4 (ВАРИАНТ 4)\n";
    out << "   1. Gnome sort & Pigeonhole sort\n";
    out << "   2. Ориентированный граф (матрица инцидентности)\n";
    out << "   3. Запуск автоматической демонстрации (--demo)\n";
    out << "   0. Выход\n";
    out << "=======================================================\n";
    out << "Выберите пункт меню: ";
}

// Запуск интерактивного цикла
void ConsoleMenu::run(std::istream& in, std::ostream& out) {
    int choice = -1;
    while (choice != 0) {
        showMainMenu(out);
        if (!(in >> choice)) {
            break;
        }

        switch (choice) {
            case 1: {
                out << "\n--- Сортировки ---\n";
                out << "1. Демонстрация Gnome sort\n";
                out << "2. Демонстрация Pigeonhole sort\n";
                out << "Выберите алгоритм: ";
                int sort_choice = 0;
                if (in >> sort_choice) {
                    if (sort_choice == 1) {
                        handleGnomeSortMenu(in, out);
                    } else if (sort_choice == 2) {
                        handlePigeonholeSortMenu(in, out);
                    } else {
                        out << "Неверный выбор алгоритма.\n";
                    }
                }
                break;
            }
            case 2:
                handleGraphMenu(in, out);
                break;
            case 3:
                runDemo(out);
                break;
            case 0:
                out << "Завершение работы программы.\n";
                break;
            default:
                out << "Неизвестный пункт меню. Повторите ввод.\n";
                break;
        }
    }
}

// Меню Gnome Sort
void ConsoleMenu::handleGnomeSortMenu(std::istream& in, std::ostream& out) {
    out << "\n[Gnome Sort] 1. Числа (std::vector) | 2. Массив int[] | 3. Студенты: ";
    int mode = 0;
    if (!(in >> mode)) return;

    if (mode == 1) {
        std::vector<int> numbers = {64, 34, 25, 12, 22, 11, 90, 5};
        out << "Исходный вектор: ";
        for (int x : numbers) out << x << " ";
        out << "\n";
        GnomeSort::sort(numbers);
        out << "Отсортированный вектор: ";
        for (int x : numbers) out << x << " ";
        out << "\n";
    } else if (mode == 2) {
        int arr[] = {42, 17, 89, 3, 23, 7};
        std::size_t sz = sizeof(arr) / sizeof(arr[0]);
        out << "Исходный массив: ";
        for (std::size_t i = 0; i < sz; ++i) out << arr[i] << " ";
        out << "\n";
        GnomeSort::sort(arr, sz);
        out << "Отсортированный массив: ";
        for (std::size_t i = 0; i < sz; ++i) out << arr[i] << " ";
        out << "\n";
    } else if (mode == 3) {
        std::vector<Student> students = {
            Student(103, "Иванов Иван", 4.2, 20),
            Student(101, "Петров Петр", 4.8, 19),
            Student(105, "Сидоров Сидор", 3.9, 21),
            Student(102, "Алексеев Алексей", 5.0, 18)
        };
        out << "Студенты до сортировки:\n";
        for (const auto& s : students) out << "  " << s << "\n";

        GnomeSort::sort(students);
        out << "Студенты после сортировки по умолчанию (по ID):\n";
        for (const auto& s : students) out << "  " << s << "\n";

        // Сортировка по GPA (убывание) с лямбда-компаратором
        GnomeSort::sort(students, [](const Student& a, const Student& b) {
            return a.getGpa() > b.getGpa();
        });
        out << "Студенты после сортировки по GPA (убывание):\n";
        for (const auto& s : students) out << "  " << s << "\n";
    }
}

// Меню Pigeonhole Sort
void ConsoleMenu::handlePigeonholeSortMenu(std::istream& in, std::ostream& out) {
    out << "\n[Pigeonhole Sort] 1. Числа (std::vector) | 2. Отрицательные числа | 3. Студенты: ";
    int mode = 0;
    if (!(in >> mode)) return;

    if (mode == 1) {
        std::vector<int> numbers = {8, 3, 2, 7, 4, 6, 8, 3, 1, 5};
        out << "Исходный вектор: ";
        for (int x : numbers) out << x << " ";
        out << "\n";
        PigeonholeSort::sort(numbers);
        out << "Отсортированный вектор: ";
        for (int x : numbers) out << x << " ";
        out << "\n";
    } else if (mode == 2) {
        int arr[] = {-5, 10, -2, 0, 7, -5, 3};
        std::size_t sz = sizeof(arr) / sizeof(arr[0]);
        out << "Исходный массив (с отрицательными числами): ";
        for (std::size_t i = 0; i < sz; ++i) out << arr[i] << " ";
        out << "\n";
        PigeonholeSort::sort(arr, sz);
        out << "Отсортированный массив: ";
        for (std::size_t i = 0; i < sz; ++i) out << arr[i] << " ";
        out << "\n";
    } else if (mode == 3) {
        std::vector<Student> students = {
            Student(104, "Васильев Василий", 4.1, 22),
            Student(101, "Петров Петр", 4.8, 19),
            Student(103, "Иванов Иван", 4.2, 20),
            Student(102, "Алексеев Алексей", 5.0, 18)
        };
        out << "Студенты до сортировки:\n";
        for (const auto& s : students) out << "  " << s << "\n";

        PigeonholeSort::sort(students, [](const Student& s) {
            return static_cast<long long>(s.getId());
        });
        out << "Студенты после голубиной сортировки по ID:\n";
        for (const auto& s : students) out << "  " << s << "\n";

        PigeonholeSort::sort(students, [](const Student& s) {
            return static_cast<long long>(s.getAge());
        });
        out << "Студенты после голубиной сортировки по возрасту:\n";
        for (const auto& s : students) out << "  " << s << "\n";
    }
}

// Меню графа
void ConsoleMenu::handleGraphMenu(std::istream& in, std::ostream& out) {
    DirectedIncidenceMatrixGraph<std::string> graph;
    int g_choice = -1;

    while (g_choice != 0) {
        out << "\n--- Управление ориентированным графом ---\n";
        out << "1. Добавить вершину\n";
        out << "2. Добавить ребро\n";
        out << "3. Удалить вершину\n";
        out << "4. Удалить ребро\n";
        out << "5. Степени вершины\n";
        out << "6. Степень ребра\n";
        out << "7. Обход вершин (прямой и обратный итераторы)\n";
        out << "8. Обход рёбер (прямой и обратный итераторы)\n";
        out << "9. Инцидентные рёбра вершины\n";
        out << "10. Смежные вершины\n";
        out << "11. Показать граф (operator<<)\n";
        out << "12. Показать матрицу инцидентности\n";
        out << "13. Загрузить тестовый демонстрационный граф\n";
        out << "0. Назад в главное меню\n";
        out << "Выберите действие: ";

        if (!(in >> g_choice)) break;

        try {
            switch (g_choice) {
                case 1: {
                    out << "Введите имя вершины: ";
                    std::string v;
                    in >> v;
                    graph.add_vertex(v);
                    out << "Вершина '" << v << "' успешно добавлена.\n";
                    break;
                }
                case 2: {
                    out << "Введите начальную и конечную вершины ребра (from to): ";
                    std::string u, v;
                    in >> u >> v;
                    graph.add_edge(u, v);
                    out << "Ребро (" << u << " -> " << v << ") успешно добавлено.\n";
                    break;
                }
                case 3: {
                    out << "Введите имя вершины для удаления: ";
                    std::string v;
                    in >> v;
                    graph.remove_vertex(v);
                    out << "Вершина '" << v << "' успешно удалена.\n";
                    break;
                }
                case 4: {
                    out << "Введите вершины ребра для удаления (from to): ";
                    std::string u, v;
                    in >> u >> v;
                    graph.remove_edge(u, v);
                    out << "Ребро (" << u << " -> " << v << ") успешно удалено.\n";
                    break;
                }
                case 5: {
                    out << "Введите имя вершины: ";
                    std::string v;
                    in >> v;
                    out << "Степень захода in-degree(" << v << ") = " << graph.vertex_in_degree(v) << "\n";
                    out << "Степень исхода out-degree(" << v << ") = " << graph.vertex_out_degree(v) << "\n";
                    out << "Общая степень degree(" << v << ") = " << graph.vertex_degree(v) << "\n";
                    break;
                }
                case 6: {
                    out << "Введите вершины ребра (from to): ";
                    std::string u, v;
                    in >> u >> v;
                    out << "Степень ребра (" << u << " -> " << v << ") = "
                        << graph.edge_degree(u, v) << "\n";
                    break;
                }
                case 7: {
                    out << "Прямой обход вершин: [";
                    for (auto it = graph.cbegin(); it != graph.cend(); ++it) {
                        out << *it << " ";
                    }
                    out << "]\nОбратный обход вершин (reverse iterator): [";
                    for (auto rit = graph.crbegin(); rit != graph.crend(); ++rit) {
                        out << *rit << " ";
                    }
                    out << "]\n";
                    break;
                }
                case 8: {
                    out << "Прямой обход рёбер:\n";
                    for (auto it = graph.edges_cbegin(); it != graph.edges_cend(); ++it) {
                        out << "  " << *it << "\n";
                    }
                    out << "Обратный обход рёбер:\n";
                    for (auto rit = graph.edges_crbegin(); rit != graph.edges_crend(); ++rit) {
                        out << "  " << *rit << "\n";
                    }
                    break;
                }
                case 9: {
                    out << "Введите имя вершины: ";
                    std::string v;
                    in >> v;
                    out << "Рёбра, инцидентные вершине '" << v << "':\n";
                    for (auto it = graph.incident_edges_cbegin(v); it != graph.incident_edges_cend(v); ++it) {
                        out << "  " << *it << "\n";
                    }
                    break;
                }
                case 10: {
                    out << "Введите имя вершины: ";
                    std::string v;
                    in >> v;
                    out << "Вершины, смежные с вершиной '" << v << "': [";
                    for (auto it = graph.adjacent_vertices_cbegin(v); it != graph.adjacent_vertices_cend(v); ++it) {
                        out << *it << " ";
                    }
                    out << "]\n";
                    break;
                }
                case 11:
                    out << graph;
                    break;
                case 12:
                    graph.printIncidenceMatrix(out);
                    break;
                case 13: {
                    graph.clear();
                    graph.add_vertex("A");
                    graph.add_vertex("B");
                    graph.add_vertex("C");
                    graph.add_vertex("D");
                    graph.add_edge("A", "B");
                    graph.add_edge("B", "C");
                    graph.add_edge("C", "A");
                    graph.add_edge("C", "D");
                    graph.add_edge("A", "A"); // петля
                    out << "Тестовый граф успешно загружен!\n";
                    out << graph;
                    graph.printIncidenceMatrix(out);
                    break;
                }
                case 0:
                    break;
                default:
                    out << "Неверный пункт меню.\n";
                    break;
            }
        } catch (const std::exception& ex) {
            out << "[ОШИБКА]: " << ex.what() << "\n";
        }
    }
}

// Автоматическая демонстрация всех возможностей
void ConsoleMenu::runDemo(std::ostream& out) {
    out << "\n=======================================================\n";
    out << "   АВТОМАТИЧЕСКАЯ ДЕМОНСТРАЦИЯ (ВАРИАНТ 4)\n";
    out << "=======================================================\n";

    out << "\n>>> 1. GNOME SORT (ГНОМЬЯ СОРТИРОВКА)\n";
    std::vector<int> numbers = {54, 26, 93, 17, 77, 31, 44, 55, 20};
    out << "Исходный вектор чисел: ";
    for (int x : numbers) out << x << " ";
    out << "\n";
    GnomeSort::sort(numbers);
    out << "Отсортированный вектор: ";
    for (int x : numbers) out << x << " ";
    out << "\n";

    double arr_d[] = {3.14, -1.5, 2.71, 0.0, -9.9, 100.2};
    std::size_t sz_d = sizeof(arr_d) / sizeof(arr_d[0]);
    out << "Исходный массив double[]: ";
    for (std::size_t i = 0; i < sz_d; ++i) out << arr_d[i] << " ";
    out << "\n";
    GnomeSort::sort(arr_d, sz_d);
    out << "Отсортированный массив double[]: ";
    for (std::size_t i = 0; i < sz_d; ++i) out << arr_d[i] << " ";
    out << "\n";

    std::vector<Student> students = {
        Student(104, "Сергеев Сергей", 3.8, 21),
        Student(101, "Иванов Иван", 4.9, 19),
        Student(103, "Алексеев Алексей", 4.5, 20),
        Student(102, "Дмитриев Дмитрий", 4.2, 18)
    };
    out << "\nСтуденты до сортировки:\n";
    for (const auto& s : students) out << "  " << s << "\n";
    GnomeSort::sort(students);
    out << "Студенты после Gnome Sort по умолчанию (по ID):\n";
    for (const auto& s : students) out << "  " << s << "\n";

    out << "\n>>> 2. PIGEONHOLE SORT (ГОЛУБИНАЯ СОРТИРОВКА)\n";
    std::vector<int> p_nums = {8, 3, 2, 7, 4, 6, 8, 3, 1, 5, -3, -1, 0};
    out << "Исходный вектор (с отрицательными числами и дубликатами): ";
    for (int x : p_nums) out << x << " ";
    out << "\n";
    PigeonholeSort::sort(p_nums);
    out << "Отсортированный вектор: ";
    for (int x : p_nums) out << x << " ";
    out << "\n";

    PigeonholeSort::sort(students, [](const Student& s) {
        return static_cast<long long>(s.getAge());
    });
    out << "Студенты после Pigeonhole Sort по возрасту:\n";
    for (const auto& s : students) out << "  " << s << "\n";

    out << "\n>>> 3. ОРИЕНТИРОВАННЫЙ ГРАФ (МАТРИЦА ИНЦИДЕНТНОСТИ)\n";
    DirectedIncidenceMatrixGraph<std::string> graph;
    graph.add_vertex("V1");
    graph.add_vertex("V2");
    graph.add_vertex("V3");
    graph.add_vertex("V4");

    graph.add_edge("V1", "V2");
    graph.add_edge("V2", "V3");
    graph.add_edge("V3", "V1");
    graph.add_edge("V3", "V4");
    graph.add_edge("V4", "V4"); // петля

    out << graph << "\n";
    graph.printIncidenceMatrix(out);

    out << "\nСтепени вершин:\n";
    for (auto it = graph.cbegin(); it != graph.cend(); ++it) {
        out << "  Вершина " << *it
            << ": in_degree=" << graph.vertex_in_degree(*it)
            << ", out_degree=" << graph.vertex_out_degree(*it)
            << ", total_degree=" << graph.vertex_degree(*it) << "\n";
    }

    out << "\nСтепени рёбер:\n";
    for (auto it = graph.edges_cbegin(); it != graph.edges_cend(); ++it) {
        out << "  Ребро " << *it << ": edge_degree=" << graph.edge_degree(*it) << "\n";
    }

    out << "\nИтерация смежных вершин для V3: [";
    for (auto it = graph.adjacent_vertices_cbegin("V3"); it != graph.adjacent_vertices_cend("V3"); ++it) {
        out << *it << " ";
    }
    out << "]\n";

    out << "Итерация инцидентных рёбер для V3:\n";
    for (auto it = graph.incident_edges_cbegin("V3"); it != graph.incident_edges_cend("V3"); ++it) {
        out << "  " << *it << "\n";
    }

    out << "\nДемонстрация глубокого копирования и сравнения:\n";
    DirectedIncidenceMatrixGraph<std::string> copyGraph = graph;
    out << "Копия равна оригиналу? " << (copyGraph == graph ? "ДА" : "НЕТ") << "\n";
    copyGraph.remove_vertex("V4");
    out << "После удаления V4 из копии:\n";
    out << "Оригинал вершин: " << graph.vertex_count() << ", рёбер: " << graph.edge_count() << "\n";
    out << "Копия вершин: " << copyGraph.vertex_count() << ", рёбер: " << copyGraph.edge_count() << "\n";
    out << "Копия равна оригиналу? " << (copyGraph == graph ? "ДА" : "НЕТ") << "\n";

    out << "\nДемонстрация завершена успешно!\n";
}
