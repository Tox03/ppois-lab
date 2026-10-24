#include "turing/RuleSet.h"

void RuleSet::add_rule(const Rule& rule) {
    rules[{rule.current_state, rule.read_symbol}] = rule;
}

void RuleSet::remove_rule(const std::string& state, char symbol) {
    rules.erase({state, symbol});
}

RuleSet& RuleSet::operator+=(const Rule& rule) {
    add_rule(rule);
    return *this;
}

RuleSet RuleSet::operator+(const Rule& rule) const {
    RuleSet result = *this;
    result += rule;
    return result;
}

RuleSet& RuleSet::operator-=(const Rule& rule) {
    remove_rule(rule.current_state, rule.read_symbol);
    return *this;
}

RuleSet RuleSet::operator-(const Rule& rule) const {
    RuleSet result = *this;
    result -= rule;
    return result;
}

bool RuleSet::find_rule(const std::string& state, char symbol, Rule& out) const {
    auto it = rules.find({state, symbol});
    if (it != rules.end()) {
        out = it->second;
        return true;
    }
    return false;
}

void RuleSet::load_from_stream(std::istream& is) {
    std::string cur_state, read_sym_str, token;
    while (is >> cur_state >> read_sym_str) {
        if (read_sym_str.empty()) break;
        char read_sym = read_sym_str[0];
        if (!(is >> token)) break;
        
        // Пропуск стрелки "->" или "->.", если она присутствует
        if (token == "->" || token == "->.") {
            if (!(is >> token)) break;
        }
        std::string next_state = token;
        std::string write_str, dir_str;
        if (is >> write_str >> dir_str) {
            char write_sym = write_str.empty() ? '_' : write_str[0];
            char dir = dir_str.empty() ? 'N' : dir_str[0];
            add_rule({cur_state, read_sym, next_state, write_sym, dir});
        }
    }
}

std::ostream& operator<<(std::ostream& os, const RuleSet& rs) {
    for (const auto& pair : rs.rules) {
        const Rule& r = pair.second;
        os << r.current_state << " " << r.read_symbol << " -> "
           << r.next_state << " " << r.write_symbol << " " << r.direction << "\n";
    }
    return os;
}

std::istream& operator>>(std::istream& is, RuleSet& rs) {
    rs.load_from_stream(is);
    return is;
}

bool RuleSet::operator==(const RuleSet& other) const {
    return rules == other.rules;
}

bool RuleSet::operator!=(const RuleSet& other) const {
    return !(*this == other);
}
