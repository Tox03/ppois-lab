#include "turing/Tape.h"

Tape::Tape(char blank) : head_position(0), blank_symbol(blank) {}

char Tape::read_symbol() const {
    auto it = tape.find(head_position);
    if (it != tape.end()) {
        return it->second;
    }
    return blank_symbol;
}

void Tape::write_symbol(char symbol) {
    if (symbol == blank_symbol) {
        tape.erase(head_position);
    } else {
        tape[head_position] = symbol;
    }
}

void Tape::move_head(char direction) {
    if (direction == 'R' || direction == 'r') {
        head_position++;
    } else if (direction == 'L' || direction == 'l') {
        head_position--;
    }
}

void Tape::load_from_stream(std::istream& is) {
    tape.clear();
    head_position = 0;
    std::string initial_state;
    if (is >> initial_state) {
        for (size_t i = 0; i < initial_state.length(); ++i) {
            write_at(static_cast<int>(i), initial_state[i]);
        }
    }
}

char Tape::read_at(int index) const {
    auto it = tape.find(index);
    if (it != tape.end()) return it->second;
    return blank_symbol;
}

void Tape::write_at(int index, char symbol) {
    if (symbol == blank_symbol) {
        tape.erase(index);
    } else {
        tape[index] = symbol;
    }
}

Tape::Proxy Tape::operator[](int index) {
    return Proxy(*this, index);
}

std::ostream& operator<<(std::ostream& os, const Tape& t) {
    if (t.tape.empty()) {
        os << "[Empty Tape]\n^\n";
        return os;
    }

    int min_pos = t.tape.begin()->first;
    int max_pos = t.tape.rbegin()->first;
    
    if (t.head_position < min_pos) min_pos = t.head_position;
    if (t.head_position > max_pos) max_pos = t.head_position;

    for (int i = min_pos; i <= max_pos; ++i) {
        auto it = t.tape.find(i);
        os << (it != t.tape.end() ? it->second : t.blank_symbol);
    }
    os << "\n";
    
    for (int i = min_pos; i < t.head_position; ++i) {
        os << " ";
    }
    os << "^\n";
    
    return os;
}

std::istream& operator>>(std::istream& is, Tape& t) {
    t.load_from_stream(is);
    return is;
}

bool Tape::operator==(const Tape& other) const {
    return tape == other.tape && 
           head_position == other.head_position && 
           blank_symbol == other.blank_symbol;
}

bool Tape::operator!=(const Tape& other) const {
    return !(*this == other);
}
