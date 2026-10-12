#include "markov/MarkovString.h"

MarkovString::MarkovString() : data(""), caret_pos(0) {}

MarkovString::MarkovString(const std::string& data) : data(data), caret_pos(0) {}

MarkovString::MarkovString(const MarkovString& other) : data(other.data), caret_pos(other.caret_pos) {}

MarkovString& MarkovString::operator=(const MarkovString& other) {
    if (this != &other) {
        data = other.data;
        caret_pos = other.caret_pos;
    }
    return *this;
}

std::string MarkovString::getValue() const { return data; }

void MarkovString::setValue(const std::string& value) { 
    data = value;
    if (caret_pos > data.length()) {
        caret_pos = data.length();
    }
}

size_t MarkovString::getCaretPos() const { return caret_pos; }

void MarkovString::setCaretPos(size_t pos) {
    if (pos <= data.length()) {
        caret_pos = pos;
    }
}

MarkovString& MarkovString::operator++() {
    if (caret_pos < data.length()) caret_pos++;
    return *this;
}

MarkovString MarkovString::operator++(int) {
    MarkovString previous_value(*this);
    ++(*this);
    return previous_value;
}

MarkovString& MarkovString::operator--() {
    if (caret_pos > 0) caret_pos--;
    return *this;
}

MarkovString MarkovString::operator--(int) {
    MarkovString previous_value(*this);
    --(*this);
    return previous_value;
}

bool MarkovString::operator==(const MarkovString& other) const {
    return data == other.data && caret_pos == other.caret_pos;
}

bool MarkovString::operator!=(const MarkovString& other) const {
    return !(*this == other);
}

std::ostream& operator<<(std::ostream& os, const MarkovString& str) {
    os << str.data;
    return os;
}

std::istream& operator>>(std::istream& is, MarkovString& str) {
    is >> str.data;
    str.caret_pos = 0;
    return is;
}
