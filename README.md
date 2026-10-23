# Лабораторные работы по дисциплине ППОИС

Репозиторий для выполнения лабораторных работ по курсу «Проектирование программного обеспечения интеллектуальных систем».

---

## Модель ветвления репозитория

В соответствии с регламентом дисциплины:
* Ветка **`main`** содержит общую сводную документацию, регламент и каталог проектов.
* Исходный код каждой лабораторной работы разрабатывается в собственной изолированной feature-ветке:
  * Лабораторная работа №1: **`feature/lab1-abstract-machines`**
  * Лабораторная работа №2: **`feature/lab2-car-parts-plant`**
  * Лабораторная работа №3: **`feature/lab3-social-network`**
  * Лабораторная работа №4: **`feature/lab4-sorting-graph`**
* Сдача и защита лабораторных работ проводятся через Pull Request из соответствующей feature-ветки в `main`.

---

## Структура репозитория

* **[`lab1/`](lab1/)** — **Лабораторная работа №1. Основы ООП: разработка класса** (ветка `feature/lab1-abstract-machines`)
  * Язык программирования: **C++17**.
  * Реализация двух абстрактных машин:
    1. **Машина Тьюринга** (вариант 1.8.2).
    2. **Нормальные алгорифмы Маркова** (вариант 1.8.3).
  * Консольный интерфейс (меню и CLI с флагом `-log`).
  * Модульные unit-тесты (GoogleTest, покрытие >90%).
  * Документация классов Doxygen.

* **[`lab2/`](lab2/)** — **Лабораторная работа №2. Объектно-ориентированное проектирование: Завод автодеталей** (ветка `feature/lab2-car-parts-plant`)
  * Язык программирования: **Python 3**.
  * Вариант 19: предметная область **«Завод автодеталей» (Car Parts Plant)**.
  * Комплексная объектно-ориентированная модель машиностроительного предприятия по производству автокомпонентов и узлов (поршни ДВС, тормозные диски, коленвалы, топливные форсунки, выпускные коллекторы).
  * **Архитектурные особенности:**
    * **60 классов предметной области**, сгруппированных по 11 модулям:
      * `core`: базовые сущности (адреса, контакты, спецификации, серийные номера, габариты).
      * `equipment`: оборудование и станки (ЧПУ фрезеры, лазерная резка, печи ТО, роботы, прессы).
      * `logistics`: клиенты, заказы клиентов, транспорт, ТТН, маршрутные листы.
      * `materials`: сырье (сплавы, пластик, резина, СОЖ), ячейки хранения, склады сырья.
      * `personnel`: персонал (директор, операторы станков, инженеры ТО, ОТК, начальники смен).
      * `plant`: центральный агрегат завода (`AutomotivePlant`).
      * `production`: производственные линии, смены, наряды-заказы, технологические карты.
      * `products`: номенклатура готовых автокомпонентов.
      * `quality`: служба ОТК, стандарты качества (IATF 16949), измерители шероховатости, КИМ-сканеры.
      * `safety`: охрана труда, датчики безопасности, журналы инцидентов.
      * `storage`: сериализация и персистентность состояния завода в JSON (`data/plant_state.json`).
    * **12 кастомных исключений** (`exceptions/`) для моделирования аварийных и нештатных ситуаций (перегрев, износ резца, превышение емкости складов, брак ОТК и др.).
    * Строго **1 класс на 1 файл** (`.py`), соблюдение стандартов PEP 8.
  * **Пользовательский интерфейс и функционал:**
    * Интерактивный CLI с 12 сценариями (суточное производство, наряды, склады, отгрузка по ТТН, плановое ТО, персонал и бюджет, ОТК, симуляция нештатных ситуаций, экспорт паспорта завода).
    * Автоматическое сохранение изменений в JSON и восстановление данных между запусками.
    * Защита от сбоев: валидация ввода, обработка пустых/некорректных значений, поддержка перезапуска аварийно остановленных линий.
  * **Тестирование и контроль качества:**
    * **92 модульных unit-теста** (`unittest`), суммарное покрытие **99%** (CLI — **98%**).
    * Автоматизированный CI (GitHub Actions): статический анализ (`flake8`), запуск тестов, порог покрытия >= 90%.
    * Поддержка создания standalone исполняемого файла `.exe` через PyInstaller.

* **[`lab3/`](lab3/)** — **Лабораторная работа №3. Крупный ООП-проект: Социальная сеть** (ветка `feature/lab3-social-network`)
  * Язык программирования: **Python 3**.
  * Комплексная объектно-ориентированная модель крупномасштабной платформы социальной сети (профили пользователей, публикации, групповые и личные диалоги, звонки, сообщества, многоуровневая модерация, монетизация, рекомендательные алгоритмы, аналитика и безопасность).
  * **Архитектурные особенности:**
    * **61 класс предметной области и 16 кастомных исключений**, распределённых по 11 подсистемам:
      * `core`: управление аккаунтом (`UserAccount`), профилем (`UserProfile`), настройками приватности (`UserPrivacy`), контактами (`ContactInfo`), параметрами интерфейса (`UserSettings`), активностью (`UserActivity`) и репутацией (`UserReputation`).
      * `content`: публикации (`Post`, `TextPost`, `MediaPost`, `PollPost`, `PollOption`), исчезающие истории (`Story`, `StoryViewer`), альбомы (`Album`), вложения (`MediaAttachment`), комментарии (`Comment`), реакции (`Reaction`) и хэштеги (`Hashtag`).
      * `communication`: диалоги (`DirectMessage`), групповые чаты (`GroupChat`, `ChatMember`), сообщения (`ChatMessage`), аудиосообщения (`AudioMessage`) и сессии звонков (`CallSession`).
      * `relations`: дружба (`Friendship`), заявки в друзья (`FriendRequest`), подписки (`Follow`), сообщества (`UserGroup`), членство в группах (`GroupMembership`), мероприятия (`GroupEvent`), черный список (`BlockRecord`).
      * `moderation`: служба модерации (`Moderator`), отчеты о нарушениях (`ModerationReport`), санкции (`Sanction`), апелляции (`Appeal`), контент-фильтры (`ContentFilter`), стоп-слова (`BannedWordFilter`), журнал аудита (`AuditLog`).
      * `monetization`: кошельки (`Wallet`), транзакции (`Transaction`), подписки (`Subscription`, `SubscriptionTier`), подарки (`VirtualGift`), рекламные кампании (`AdCampaign`) и объявления (`Advertisement`).
      * `analytics`: новостная лента (`Feed`, `FeedItem`), алгоритм рекомендаций (`RecommendationEngine`), тренды (`TrendAnalyzer`), метрики (`EngagementMetrics`), статистика (`UserStatistic`).
      * `notification`: уведомления (`Notification`), пакетная группировка (`NotificationBatch`), каналы доставки (`NotificationChannel`).
      * `security`: двухфакторная аутентификация (`TwoFactorAuth`), токены веб-сессий (`SessionToken`), журнал безопасности (`SecurityLog`).
      * `system`: фасад системы (`SocialNetworkSystem`), поисковый индекс (`SearchService`), резервное копирование (`DataBackup`).
      * `exceptions`: 16 специализированных классов исключений для обработки бизнес-правил (`UserNotFoundException`, `AccessDeniedException`, `AuthenticationException`, `ContentBlockedException` и др.).
    * Строго **1 класс на 1 файл** (`.py`), полное соответствие стандарту PEP 8.
    * Все комментарии, документация и docstring написаны на **русском языке**.
    * Полная симметрия всех операций (добавление / удаление, блокировка / разблокировка, подписка / отписка, включение / отключение режима обслуживания и др.).
  * **Пользовательский интерфейс и функционал:**
    * Интерактивное консольное приложение (`NetworkCLI`) для управления всеми подсистемами.
    * Строгая валидация входных данных, информативные сообщения об ошибках.
  * **Тестирование и контроль качества:**
    * **104 модульных unit-теста** (`unittest`), суммарное покрытие кода **>95%** (порог CI >= 90%).
    * Статический анализ кода линтером `flake8` (0 предупреждений).
    * Автоматизированная сборка standalone исполняемого файла `.exe` через PyInstaller.

* **[`lab4/`](lab4/)** — **Лабораторная работа №4. Обобщённое программирование: сортировка и контейнеры** (ветка `feature/lab4-sorting-graph`)
  * Язык программирования: **C++17**.
  * **Вариант 4**:
    * **Задание 1. Обобщённые алгоритмы сортировки:**
      * **Gnome sort** (Гномья сортировка) — обобщённые функции сортировки по возрастанию (`sort`) и по убыванию (`sort_descending`) с поддержкой произвольных двунаправленных итераторов, `std::vector`, встроенных массивов C++ и пользовательских компараторов.
      * **Pigeonhole sort** (Голубиная сортировка) — обобщённые функции сортировки по возрастанию и по убыванию для целочисленных типов и пользовательских объектов с функцией проекции целочисленного ключа.
      * Пользовательский класс **`Student`** (ID, ФИО, рейтинг) — демонстрация сортировки пользовательских объектов по рейтингу (целочисленный ключ), имени и идентификатору; перегрузка операторов сравнения (`<`, `>`, `==`) и оператора вывода в поток (`<<`).
    * **Задание 2. Обобщённый контейнер: Ориентированный граф на матрице инцидентности:**
      * Шаблон класса **`DirectedIncidenceMatrixGraph<T>`** — контейнер ориентированного графа на базе динамической матрицы инцидентности $V \times E$ (коды: `-1` — исход, `+1` — заход, `+2` — петля).
      * Полное сокрытие внутреннего представления.
      * Семейство двунаправленных и обратных итераторов:
        * Итераторы вершин (`vertex_iterator`, `const_vertex_iterator`, `reverse_vertex_iterator`, `const_reverse_vertex_iterator`).
        * Итераторы рёбер (`edge_iterator`, `const_edge_iterator`, `reverse_edge_iterator`, `const_reverse_edge_iterator`).
        * Итераторы инцидентных рёбер (`incident_edge_iterator`, `const_incident_edge_iterator`, `reverse_incident_edge_iterator`, `const_reverse_incident_edge_iterator`).
        * Итераторы смежных вершин (`adjacent_vertex_iterator`, `const_adjacent_vertex_iterator`, `reverse_adjacent_vertex_iterator`, `const_reverse_adjacent_vertex_iterator`).
      * Публичные псевдонимы типов STL (`value_type`, `size_type`, `difference_type`, `reference`, `const_reference`, `iterator`, `const_iterator` и др.).
      * Полная симметрия операций:
        * Добавление / удаление вершин (`insertVertex` / `eraseVertex`).
        * Добавление / удаление рёбер (`insertEdge` / `eraseEdge`).
        * Проверка наличия (`hasVertex`, `hasEdge`).
        * Очистка и проверка на пустоту (`clear`, `empty`).
        * Степени вершин (полустепень захода `inDegree`, исхода `outDegree`, общая степень `degree`).
        * Индексация и безопасный доступ (`operator[]`, `at()`).
        * Поиск элементов (`find_vertex`, `find_edge`).
        * Сравнение графов (`==`, `!=`, `<`, `<=`, `>`, `>=`).
        * Форматированный вывод матрицы инцидентности (`printIncidenceMatrix`).
  * **Архитектурные требования:**
    * Строго **1 класс на 1 .h и .cpp файл** (ни в одном файле нет двух классов).
    * Все комментарии в коде написаны на **русском языке**.
    * Полное отсутствие магических чисел (все константы явно именованы).
    * Поддержка русского языка в консоли Windows (флаг компилятора `/utf-8`, функции `SetConsoleOutputCP(CP_UTF8)` и `SetConsoleCP(CP_UTF8)`).
  * **Пользовательский интерфейс и тестирование:**
    * Интерактивное консольное меню (`ConsoleMenu`) с 16 пунктами и автоматический демонстрационный режим (`--demo`).
    * **49 модульных unit-тестов** (GoogleTest), 100% успешное прохождение.
    * Анализ покрытия кода тестами через OpenCppCoverage (>90%).

---

## Быстрый старт (Лабораторная №1)

Переключение на ветку первой лабораторной:
```powershell
git checkout feature/lab1-abstract-machines
```

### Сборка через CMake:
```powershell
cd lab1
cmake -B build -S .
cmake --build build --config Release
```

### Запуск тестов:
```powershell
./lab1/build/Release/AllTests.exe
```

### Запуск программы:
```powershell
# Интерактивное меню:
./lab1/build/Release/ppois-lab1.exe

# Запуск Машины Тьюринга из файла с логированием:
./lab1/build/Release/ppois-lab1.exe turing lab1/examples/turing_example.txt -log

# Запуск Алгорифмов Маркова из файла с логированием:
./lab1/build/Release/ppois-lab1.exe markov lab1/examples/markov_example.txt -log
```

---

## Быстрый старт (Лабораторная №2)

Переключение на ветку второй лабораторной:
```powershell
git checkout feature/lab2-car-parts-plant
```

### Требования:
* Python 3.10 или выше
* Зависимости для разработки и тестов (опционально):
  ```powershell
  pip install coverage flake8 pyinstaller
  ```

### Запуск интерактивного консольного приложения (CLI):
```powershell
python lab2/main.py
```

### Запуск модульных тестов:
```powershell
cd lab2
python -m unittest discover -s tests -p "test_*.py" -v
```

### Проверка тестового покрытия (Coverage):
```powershell
cd lab2
coverage run -m unittest discover -s tests -p "test_*.py"
coverage report -m
```

### Проверка стиля кода (Flake8):
```powershell
flake8 lab2 --max-line-length=120
```

### Сборка автономного исполняемого файла (.exe):
```powershell
pyinstaller --onefile --name car_parts_plant lab2/main.py
```
Готовый исполняемый файл будет сформирован в каталоге `dist/car_parts_plant.exe`.

---

## Быстрый старт (Лабораторная №3)

Переключение на ветку третьей лабораторной:
```powershell
git checkout feature/lab3-social-network
```

### Требования:
* Python 3.9 или выше
* Зависимости для разработки и тестов:
  ```powershell
  pip install coverage flake8 pyinstaller
  ```

### Запуск интерактивного консольного приложения (CLI):
```powershell
python lab3/main.py
```

### Запуск модульных тестов:
```powershell
python -m unittest discover -s lab3/tests -p "test_*.py" -v
```

### Проверка тестового покрытия (Coverage >= 90%):
```powershell
python -m coverage run --source=lab3/network,lab3/cli -m unittest discover -s lab3/tests -p "test_*.py" -v
python -m coverage report -m
```

### Проверка стиля кода (Flake8):
```powershell
flake8 --config=lab3/.flake8 lab3
```

### Сборка автономного исполняемого файла (.exe):
```powershell
pyinstaller --name ppois-lab3 --onefile --paths . lab3/main.py --distpath lab3/dist
```
Готовый исполняемый файл будет создан в каталоге `lab3/dist/ppois-lab3.exe`.

---

## Быстрый старт (Лабораторная №4)

Переключение на ветку четвёртой лабораторной:
```powershell
git checkout feature/lab4-sorting-graph
```

### Требования:
* Компилятор C++17 (MSVC / GCC / Clang)
* CMake 3.20 или выше

### Сборка через CMake:
```powershell
cmake -S lab4 -B lab4/build -DCMAKE_BUILD_TYPE=Release
cmake --build lab4/build --config Release --parallel
```

### Запуск модульных тестов (GoogleTest):
```powershell
# Windows
.\lab4\build\Release\AllTests.exe

# Linux / macOS
./lab4/build/AllTests
```

### Запуск интерактивного консольного меню:
```powershell
.\lab4\build\Release\ppois-lab4.exe
```

### Запуск автоматической демонстрации (--demo):
```powershell
.\lab4\build\Release\ppois-lab4.exe --demo
```

### Анализ тестового покрытия (OpenCppCoverage на Windows):
```powershell
& "C:\Program Files\OpenCppCoverage\OpenCppCoverage.exe" --sources "$((Get-Location).Path)\lab4" --export_type html:lab4_coverage_report -- .\lab4\build\Release\AllTests.exe
```
HTML-отчёт формируется в папке `lab4_coverage_report/index.html`.
