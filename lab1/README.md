# Лабораторная работа №1. Основы ООП: Абстрактные машины

Объединенный проект, реализующий две абстрактные машины:
1. **Машина Тьюринга** (раздел 1.8.2)
2. **Нормальные алгорифмы Маркова** (раздел 1.8.3)

---

## Архитектура проекта

- **Инкапсуляция и разделение обязанностей**:
  - `include/turing/`, `src/turing/`: логика Машины Тьюринга (`Tape`, `RuleSet`, `TuringMachine`).
  - `include/markov/`, `src/markov/`: логика Нормальных алгорифмов Маркова (`MarkovString`, `MarkovRule`, `MarkovProgram`, `MarkovMachine`).
  - `include/ui/`, `src/ui/`: консольный интерфейс пользователя (`TuringUI`, `MarkovUI`, `MenuManager`), полностью изолированный от логики классов.
- **Единая точка входа**: `src/main.cpp`.
- **Модульное тестирование**: GoogleTest в `tests/` с покрытием более 90%.
- **Документация**: Doxygen (`Doxyfile`).

---

## Сборка проекта

### Сборка через CMake (Visual Studio / Ninja / MSBuild):
```powershell
cmake -B build -S .
cmake --build build --config Release
```

---

## Запуск

### 1. Интерактивный режим (меню)
Запуск без аргументов:
```powershell
./build/Release/ppois-lab1.exe
```
Открывает главное меню выбора машины:
```text
============================================
        КОМПЛЕКС АБСТРАКТНЫХ МАШИН (Лаб. 1) 
============================================
1. Машина Тьюринга
2. Нормальные алгорифмы Маркова
0. Выход
```

### 2. Запуск через аргументы командной строки

#### Машина Тьюринга:
```powershell
# Обычный запуск из файла
./build/Release/ppois-lab1.exe turing examples/turing_example.txt

# Запуск с пошаговым логированием (-log)
./build/Release/ppois-lab1.exe turing examples/turing_example.txt -log
```

#### Нормальные алгорифмы Маркова:
```powershell
# Обычный запуск из файла
./build/Release/ppois-lab1.exe markov examples/markov_example.txt

# Запуск с пошаговым логированием (-log)
./build/Release/ppois-lab1.exe markov examples/markov_example.txt -log
```

Также поддерживается синтаксис флагов:
```powershell
./build/Release/ppois-lab1.exe -m turing examples/turing_example.txt -log
./build/Release/ppois-lab1.exe -m markov examples/markov_example.txt -log
```

---

## Запуск тестов
```powershell
ctest --test-dir build -C Release --output-on-failure
# или прямой запуск бинарника тестов:
./build/Release/AllTests.exe
```
