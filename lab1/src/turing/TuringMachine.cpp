#include "turing/TuringMachine.h"

TuringMachine::TuringMachine(const std::string& start_state) {
    current_state = start_state;
    halted = false;
}

Tape& TuringMachine::get_tape() { return tape; }
const Tape& TuringMachine::get_tape() const { return tape; }

RuleSet& TuringMachine::get_rules() { return rules; }
const RuleSet& TuringMachine::get_rules() const { return rules; }

void TuringMachine::set_state(const std::string& state) {
    current_state = state;
    halted = false;
}

bool TuringMachine::is_halted() const { return halted; }

bool TuringMachine::step() {
    if (halted) return false;

    char current_symbol = tape.read_symbol();
    Rule rule;
    
    if (rules.find_rule(current_state, current_symbol, rule)) {
        tape.write_symbol(rule.write_symbol);
        tape.move_head(rule.direction);
        current_state = rule.next_state;
        return true;
    } else {
        halted = true;
        return false;
    }
}

void TuringMachine::run(bool log_steps) {
    if (log_steps) {
        std::cout << "--- Initial State ---\n" << *this << "\n";
    }
    
    while (!halted) {
        if (step() && log_steps) {
            std::cout << "--- Step ---\n" << *this << "\n";
        }
    }
    
    if (log_steps) {
        std::cout << "--- Machine Halted ---\n";
    }
}

void TuringMachine::load_from_stream(std::istream& is) {
    is >> tape;
    is >> rules;
    halted = false;
}

bool TuringMachine::operator==(const TuringMachine& other) const {
    return current_state == other.current_state &&
           halted == other.halted &&
           tape == other.tape &&
           rules == other.rules;
}

bool TuringMachine::operator!=(const TuringMachine& other) const {
    return !(*this == other);
}

std::ostream& operator<<(std::ostream& os, const TuringMachine& tm) {
    os << "State: " << tm.current_state;
    if (tm.halted) os << " (HALTED)";
    os << "\n";
    os << tm.tape;
    return os;
}

std::istream& operator>>(std::istream& is, TuringMachine& tm) {
    tm.load_from_stream(is);
    return is;
}
