#include "markov/MarkovRule.h"
#include <sstream>

MarkovRule::MarkovRule() : from(""), to(""), is_terminal(false) {}

MarkovRule::MarkovRule(const std::string& from, const std::string& to, bool is_terminal)
    : from(from), to(to), is_terminal(is_terminal) {}

MarkovRule::MarkovRule(const MarkovRule& other)
    : from(other.from), to(other.to), is_terminal(other.is_terminal) {}

MarkovRule& MarkovRule::operator=(const MarkovRule& other) {
    if (this != &other) {
        from = other.from;
        to = other.to;
        is_terminal = other.is_terminal;
    }
    return *this;
}

std::string MarkovRule::getFrom() const { return from; }
std::string MarkovRule::getTo() const { return to; }
bool MarkovRule::isTerminal() const { return is_terminal; }

bool MarkovRule::operator==(const MarkovRule& other) const {
    return from == other.from && to == other.to && is_terminal == other.is_terminal;
}

bool MarkovRule::operator!=(const MarkovRule& other) const {
    return !(*this == other);
}

std::ostream& operator<<(std::ostream& os, const MarkovRule& rule) {
    os << rule.from << (rule.is_terminal ? " ->. " : " -> ") << rule.to;
    return os;
}

std::istream& operator>>(std::istream& is, MarkovRule& rule) {
    std::string line;
    if (std::getline(is, line)) {
        size_t pos = line.find(" ->. ");
        if (pos != std::string::npos) {
            rule.from = line.substr(0, pos);
            rule.to = line.substr(pos + 5);
            rule.is_terminal = true;
        } else {
            pos = line.find(" -> ");
            if (pos != std::string::npos) {
                rule.from = line.substr(0, pos);
                rule.to = line.substr(pos + 4);
                rule.is_terminal = false;
            } else {
                is.setstate(std::ios::failbit);
            }
        }
    }
    return is;
}
