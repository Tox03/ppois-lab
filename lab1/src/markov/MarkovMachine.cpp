#include "markov/MarkovMachine.h"

MarkovMachine::MarkovMachine() : halted(false), log_enabled(false) {}

MarkovMachine::MarkovMachine(const MarkovMachine& other) 
    : program(other.program), tape(other.tape), halted(other.halted), log_enabled(other.log_enabled) {}

MarkovMachine& MarkovMachine::operator=(const MarkovMachine& other) {
    if (this != &other) {
        program = other.program;
        tape = other.tape;
        halted = other.halted;
        log_enabled = other.log_enabled;
    }
    return *this;
}

void MarkovMachine::setProgram(const MarkovProgram& prog) {
    program = prog;
    halted = false;
}

void MarkovMachine::addRule(const MarkovRule& rule) {
    program.addRule(rule);
}

void MarkovMachine::removeRule(size_t index) {
    program.removeRule(index);
}

void MarkovMachine::setTape(const MarkovString& tape_str) {
    tape = tape_str;
    halted = false;
}

MarkovString MarkovMachine::getTape() const {
    return tape;
}

void MarkovMachine::setLogEnabled(bool enabled) {
    log_enabled = enabled;
}

bool MarkovMachine::isLogEnabled() const {
    return log_enabled;
}

bool MarkovMachine::isHalted() const {
    return halted;
}

void MarkovMachine::reset() {
    halted = false;
}

bool MarkovMachine::step() {
    if (halted) return false;

    std::string current_str = tape.getValue();
    for (size_t i = 0; i < program.getRuleCount(); ++i) {
        const MarkovRule& rule = program.getRule(i);
        size_t pos = current_str.find(rule.getFrom());
        if (pos != std::string::npos) {
            current_str.replace(pos, rule.getFrom().length(), rule.getTo());
            tape.setValue(current_str);
            tape.setCaretPos(pos); // Установка каретки на позицию замены
            
            if (log_enabled) {
                std::cout << "Применено правило: " << rule << " | Текущая строка: " << tape << "\n";
            }

            if (rule.isTerminal()) {
                halted = true;
            }
            return true;
        }
    }
    
    // Ни одно правило не подошло, остановка
    halted = true;
    return false;
}

void MarkovMachine::run() {
    while (step()) {
        // Цикл до остановки
    }
}

void MarkovMachine::loadProgramFromStream(std::istream& is) {
    is >> program;
}

void MarkovMachine::loadTapeFromStream(std::istream& is) {
    is >> tape;
}

void MarkovMachine::loadFromStream(std::istream& is) {
    std::string initial_tape;
    if (std::getline(is, initial_tape)) {
        tape = MarkovString(initial_tape);
    }
    is >> program;
    halted = false;
}

bool MarkovMachine::operator==(const MarkovMachine& other) const {
    return program == other.program && 
           tape == other.tape && 
           halted == other.halted && 
           log_enabled == other.log_enabled;
}

bool MarkovMachine::operator!=(const MarkovMachine& other) const {
    return !(*this == other);
}

std::ostream& operator<<(std::ostream& os, const MarkovMachine& machine) {
    os << "Tape: " << machine.tape;
    if (machine.halted) os << " (HALTED)";
    return os;
}

std::istream& operator>>(std::istream& is, MarkovMachine& machine) {
    machine.loadFromStream(is);
    return is;
}
