#include "markov/MarkovProgram.h"
#include <stdexcept>

MarkovProgram::MarkovProgram() {}

MarkovProgram::MarkovProgram(const MarkovProgram& other) : rules(other.rules) {}

MarkovProgram& MarkovProgram::operator=(const MarkovProgram& other) {
    if (this != &other) {
        rules = other.rules;
    }
    return *this;
}

void MarkovProgram::addRule(const MarkovRule& rule) {
    rules.push_back(rule);
}

void MarkovProgram::removeRule(size_t index) {
    if (index < rules.size()) {
        rules.erase(rules.begin() + index);
    } else {
        throw std::out_of_range("Индекс правила выходит за пределы диапазона");
    }
}

const MarkovRule& MarkovProgram::getRule(size_t index) const {
    if (index < rules.size()) {
        return rules[index];
    }
    throw std::out_of_range("Индекс правила выходит за пределы диапазона");
}

size_t MarkovProgram::getRuleCount() const {
    return rules.size();
}

bool MarkovProgram::operator==(const MarkovProgram& other) const {
    if (rules.size() != other.rules.size()) return false;
    for (size_t i = 0; i < rules.size(); ++i) {
        if (rules[i] != other.rules[i]) return false;
    }
    return true;
}

bool MarkovProgram::operator!=(const MarkovProgram& other) const {
    return !(*this == other);
}

std::ostream& operator<<(std::ostream& os, const MarkovProgram& program) {
    for (size_t i = 0; i < program.rules.size(); ++i) {
        os << program.rules[i] << "\n";
    }
    return os;
}

std::istream& operator>>(std::istream& is, MarkovProgram& program) {
    MarkovRule rule;
    while (is >> rule) {
        program.addRule(rule);
    }
    return is;
}
