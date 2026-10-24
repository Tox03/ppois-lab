# Лабораторная работа №4: Обобщённое программирование (Сортировка и Графы)

## Вариант 4

- **Задание 1. Алгоритмы сортировки:**
  - **Gnome sort** (Гномья сортировка) — симметричные варианты сортировки по возрастанию и убыванию, поддержка произвольных итераторов, `std::vector` и встроенных массивов C++, пользовательские компараторы.
  - **Pigeonhole sort** (Голубиная сортировка) — симметричные варианты сортировки по возрастанию и убыванию для числовых типов и пользовательских объектов с функцией извлечения целочисленного ключа.
  - **Пользовательский класс:** `Student` (демонстрация сортировки объектов по рейтингу, имени и идентификатору).

- **Задание 2. Обобщённый контейнер графа:**
  - **Ориентированный граф на основе матрицы инцидентности** (`DirectedIncidenceMatrixGraph<T>`).
  - Полное сокрытие внутреннего представления.
  - Двунаправленные и обратные итераторы:
    - Итераторы вершин (`vertex_iterator`, `const_vertex_iterator`, `reverse_vertex_iterator`, `const_reverse_vertex_iterator`)
    - Итераторы рёбер (`edge_iterator`, `const_edge_iterator`, `reverse_edge_iterator`, `const_reverse_edge_iterator`)
    - Итераторы инцидентных рёбер (`incident_edge_iterator`, `const_incident_edge_iterator`, `reverse_incident_edge_iterator`, `const_reverse_incident_edge_iterator`)
    - Итераторы смежных вершин (`adjacent_vertex_iterator`, `const_adjacent_vertex_iterator`, `reverse_adjacent_vertex_iterator`, `const_reverse_adjacent_vertex_iterator`)
  - Симметричные операции:
    - Добавление / удаление вершин (`insertVertex` / `eraseVertex`)
    - Добавление / удаление рёбер (`insertEdge` / `eraseEdge`)
    - Проверка наличия (`hasVertex`, `hasEdge`)
    - Очистка и проверка на пустоту (`clear`, `empty`)
    - Прямой и обратный обход
    - Вычисление степеней (полустепень захода `inDegree`, исхода `outDegree`, общая степень `degree`)
    - Операции сравнения (`==`, `!=`, `<`, `<=`, `>`, `>=`)
    - Вывод матрицы инцидентности (`printIncidenceMatrix`)

---

## Архитектура и структура проекта

В соответствии с требованиями чеклиста и задания:
- Каждый класс вынесен в **отдельный .h и .cpp файл** (ни в одном файле нет двух классов).
- Все комментарии в коде написаны на русском языке.
- Отсутствуют магические числа (все константы явно именованы).
- Соблюдена строгая симметрия всех операций интерфейса и классов.

```
lab4/
├── CMakeLists.txt
├── README.md
├── include/
│   ├── graph/
│   │   ├── AdjacentVertexIterator.h
│   │   ├── ConstAdjacentVertexIterator.h
│   │   ├── ConstEdgeIterator.h
│   │   ├── ConstIncidentEdgeIterator.h
│   │   ├── ConstVertexIterator.h
│   │   ├── DirectedIncidenceMatrixGraph.h
│   │   ├── Edge.h
│   │   ├── EdgeIterator.h
│   │   ├── GraphException.h
│   │   ├── IncidentEdgeIterator.h
│   │   └── VertexIterator.h
│   ├── model/
│   │   └── Student.h
│   ├── sort/
│   │   ├── GnomeSort.h
│   │   └── PigeonholeSort.h
│   └── ui/
│       └── ConsoleMenu.h
├── src/
│   ├── graph/
│   │   ├── AdjacentVertexIterator.cpp
│   │   ├── ConstAdjacentVertexIterator.cpp
│   │   ├── ConstEdgeIterator.cpp
│   │   ├── ConstIncidentEdgeIterator.cpp
│   │   ├── ConstVertexIterator.cpp
│   │   ├── DirectedIncidenceMatrixGraph.cpp
│   │   ├── Edge.cpp
│   │   ├── EdgeIterator.cpp
│   │   ├── GraphException.cpp
│   │   ├── IncidentEdgeIterator.cpp
│   │   └── VertexIterator.cpp
│   ├── model/
│   │   └── Student.cpp
│   ├── sort/
│   │   ├── GnomeSort.cpp
│   │   └── PigeonholeSort.cpp
│   ├── ui/
│   │   └── ConsoleMenu.cpp
│   └── main.cpp
└── tests/
    ├── test_console_menu.cpp
    ├── test_edge.cpp
    ├── test_exceptions.cpp
    ├── test_gnome_sort.cpp
    ├── test_graph_core.cpp
    ├── test_graph_iterators.cpp
    ├── test_pigeonhole_sort.cpp
    └── test_student.cpp
```

---

## Сборка и запуск

### 1. Сборка через CMake

```bash
cmake -S lab4 -B lab4/build -DCMAKE_BUILD_TYPE=Release
cmake --build lab4/build --config Release --parallel
```

### 2. Запуск модульных тестов

```bash
# Windows
.\lab4\build\Release\AllTests.exe

# Linux / macOS
./lab4/build/AllTests
```

### 3. Запуск интерактивного консольного меню

```bash
.\lab4\build\Release\ppois-lab4.exe
```

### 4. Запуск автоматической демонстрации (--demo)

```bash
.\lab4\build\Release\ppois-lab4.exe --demo
```
