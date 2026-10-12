cmake_minimum_required(VERSION 3.14)
project(AbstractMachinesSuite VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if(MSVC)
    add_compile_options(/utf-8)
    # Генерируем PDB-файлы для анализа покрытия OpenCppCoverage
    add_compile_options("$<$<CONFIG:Release>:/Zi>")
    add_link_options("$<$<CONFIG:Release>:/DEBUG>")
endif()

# Include directories
include_directories(include)

# Turing Machine core library
add_library(TuringCore STATIC
    src/turing/Tape.cpp
    src/turing/RuleSet.cpp
    src/turing/TuringMachine.cpp
)
target_include_directories(TuringCore PUBLIC include)

# Markov Algorithms core library
add_library(MarkovCore STATIC
    src/markov/MarkovString.cpp
    src/markov/MarkovRule.cpp
    src/markov/MarkovProgram.cpp
    src/markov/MarkovMachine.cpp
)
target_include_directories(MarkovCore PUBLIC include)

# UI Library (isolated console interaction)
add_library(AppUI STATIC
    src/ui/TuringUI.cpp
    src/ui/MarkovUI.cpp
    src/ui/MenuManager.cpp
)
target_include_directories(AppUI PUBLIC include)
target_link_libraries(AppUI PUBLIC TuringCore MarkovCore)

# Main Executable
add_executable(ppois-lab1 src/main.cpp)
target_link_libraries(ppois-lab1 PRIVATE AppUI TuringCore MarkovCore)
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ppois-lab1)

# Unit Testing with GoogleTest
include(FetchContent)
FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(AllTests
    tests/turing/test_tape.cpp
    tests/turing/test_ruleset.cpp
    tests/turing/test_machine.cpp
    tests/markov/test_rule.cpp
    tests/markov/test_string.cpp
    tests/markov/test_program.cpp
    tests/markov/test_machine.cpp
)

target_include_directories(AllTests PRIVATE include)
target_link_libraries(AllTests PRIVATE
    TuringCore
    MarkovCore
    gtest_main
)

include(GoogleTest)
gtest_discover_tests(AllTests)
