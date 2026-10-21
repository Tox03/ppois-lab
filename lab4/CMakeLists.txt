cmake_minimum_required(VERSION 3.15)
project(ppois-lab4 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if (MSVC)
    add_compile_options(/W4 /permissive- /EHsc)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Исходные файлы основной библиотеки
set(CORE_SOURCES
    src/graph/GraphException.cpp
    src/graph/Edge.cpp
    src/graph/VertexIterator.cpp
    src/graph/ConstVertexIterator.cpp
    src/graph/EdgeIterator.cpp
    src/graph/ConstEdgeIterator.cpp
    src/graph/IncidentEdgeIterator.cpp
    src/graph/ConstIncidentEdgeIterator.cpp
    src/graph/AdjacentVertexIterator.cpp
    src/graph/ConstAdjacentVertexIterator.cpp
    src/graph/DirectedIncidenceMatrixGraph.cpp
    src/sort/GnomeSort.cpp
    src/sort/PigeonholeSort.cpp
    src/model/Student.cpp
    src/ui/ConsoleMenu.cpp
)

add_library(Lab4Core STATIC ${CORE_SOURCES})
target_include_directories(Lab4Core PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

# Исполняемый файл приложения
add_executable(ppois-lab4 src/main.cpp)
target_link_libraries(ppois-lab4 PRIVATE Lab4Core)

# Модульное тестирование (GoogleTest)
include(FetchContent)
FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
# Для MSVC в Windows: согласование CRT с динамической библиотекой
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

set(TEST_SOURCES
    tests/test_gnome_sort.cpp
    tests/test_pigeonhole_sort.cpp
    tests/test_student.cpp
    tests/test_edge.cpp
    tests/test_graph_core.cpp
    tests/test_graph_iterators.cpp
    tests/test_exceptions.cpp
    tests/test_console_menu.cpp
)

add_executable(AllTests ${TEST_SOURCES})
target_link_libraries(AllTests PRIVATE Lab4Core gtest_main gtest)
target_include_directories(AllTests PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

include(GoogleTest)
gtest_discover_tests(AllTests)
