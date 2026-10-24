#include "graph/GraphException.h"

// Конструктор с параметром std::string
GraphException::GraphException(const std::string& message)
    : std::runtime_error(message) {
}

// Конструктор с параметром const char*
GraphException::GraphException(const char* message)
    : std::runtime_error(message) {
}
