cmake_minimum_required(VERSION 3.14)
project(PPOIS_Lab4 VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if(MSVC)
    add_compile_options(/utf-8)
    # Генерируем отладочную информацию для анализа покрытия OpenCppCoverage
    add_compile_options("$<$<CONFIG:Release>:/Zi>")
    add_link_options("$<$<CONFIG:Release>:/DEBUG>")
endif()

# Пути к заголовочным файлам и исходникам шаблонов
include_directories(include src)

# Статическая библиотека Lab4Core
add_library(Lab4Core STATIC
    src/graph/GraphException.cpp
    src/model/Student.cpp
    src/ui/ConsoleMenu.cpp
)
target_include_directories(Lab4Core PUBLIC include src)

# Главный исполняемый файл
add_executable(ppois-lab4 src/main.cpp)
target_link_libraries(ppois-lab4 PRIVATE Lab4Core)
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ppois-lab4)

# Модульное тестирование через GoogleTest
include(FetchContent)

# Проверяем наличие локального кэша googletest из lab1 для ускорения сборки
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/../lab1/build/_deps/googletest-src")
    FetchContent_Declare(
        googletest
        SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../lab1/build/_deps/googletest-src"
    )
else()
    FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
    )
endif()

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(AllTests
    tests/test_gnome_sort.cpp
    tests/test_pigeonhole_sort.cpp
    tests/test_student.cpp
    tests/test_edge.cpp
    tests/test_graph_core.cpp
    tests/test_graph_iterators.cpp
    tests/test_exceptions.cpp
    tests/test_console_menu.cpp
)

target_include_directories(AllTests PRIVATE include src)
target_link_libraries(AllTests PRIVATE
    Lab4Core
    gtest_main
)

include(GoogleTest)
gtest_discover_tests(AllTests)
