#include "model/Student.h"

// Конструктор по умолчанию
Student::Student()
    : id_(0), name_(""), rating_(0) {
}

// Параметризованный конструктор
Student::Student(int id, const std::string& name, int rating)
    : id_(id), name_(name), rating_(rating) {
}

// Получить идентификатор
int Student::getId() const {
    return id_;
}

// Установить идентификатор
void Student::setId(int id) {
    id_ = id;
}

// Получить имя
const std::string& Student::getName() const {
    return name_;
}

// Установить имя
void Student::setName(const std::string& name) {
    name_ = name;
}

// Получить рейтинг
int Student::getRating() const {
    return rating_;
}

// Установить рейтинг
void Student::setRating(int rating) {
    rating_ = rating;
}

// Оператор равенства
bool Student::operator==(const Student& other) const {
    return id_ == other.id_ && name_ == other.name_ && rating_ == other.rating_;
}

// Оператор неравенства
bool Student::operator!=(const Student& other) const {
    return !(*this == other);
}

// Оператор меньше (сравнение по рейтингу, затем по имени, затем по id)
bool Student::operator<(const Student& other) const {
    if (rating_ != other.rating_) {
        return rating_ < other.rating_;
    }
    if (name_ != other.name_) {
        return name_ < other.name_;
    }
    return id_ < other.id_;
}

// Оператор меньше или равно
bool Student::operator<=(const Student& other) const {
    return !(other < *this);
}

// Оператор больше
bool Student::operator>(const Student& other) const {
    return other < *this;
}

// Оператор больше или равно
bool Student::operator>=(const Student& other) const {
    return !(*this < other);
}

// Оператор вывода в поток
std::ostream& operator<<(std::ostream& os, const Student& student) {
    os << "Student(ID: " << student.id_ << ", Name: " << student.name_
       << ", Rating: " << student.rating_ << ")";
    return os;
}
