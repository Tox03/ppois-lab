#include "model/Student.h"
#include <tuple>

// Конструктор по умолчанию
Student::Student()
    : id_(0), name_(""), gpa_(0.0), age_(0) {
}

// Параметризованный конструктор
Student::Student(int id, const std::string& name, double gpa, int age)
    : id_(id), name_(name), gpa_(gpa), age_(age) {
}

// Геттеры
int Student::getId() const {
    return id_;
}

const std::string& Student::getName() const {
    return name_;
}

double Student::getGpa() const {
    return gpa_;
}

int Student::getAge() const {
    return age_;
}

// Сеттеры
void Student::setId(int id) {
    id_ = id;
}

void Student::setName(const std::string& name) {
    name_ = name;
}

void Student::setGpa(double gpa) {
    gpa_ = gpa;
}

void Student::setAge(int age) {
    age_ = age;
}

// Операторы сравнения
bool Student::operator==(const Student& other) const {
    return id_ == other.id_ &&
           name_ == other.name_ &&
           gpa_ == other.gpa_ &&
           age_ == other.age_;
}

bool Student::operator!=(const Student& other) const {
    return !(*this == other);
}

bool Student::operator<(const Student& other) const {
    return id_ < other.id_;
}

bool Student::operator<=(const Student& other) const {
    return (*this < other) || (*this == other);
}

bool Student::operator>(const Student& other) const {
    return other < *this;
}

bool Student::operator>=(const Student& other) const {
    return !(*this < other);
}

// Оператор вывода в поток
std::ostream& operator<<(std::ostream& os, const Student& student) {
    os << "Student{ID=" << student.id_
       << ", Name=\"" << student.name_ << "\""
       << ", GPA=" << student.gpa_
       << ", Age=" << student.age_ << "}";
    return os;
}

// Оператор ввода из потока
std::istream& operator>>(std::istream& is, Student& student) {
    is >> student.id_ >> student.name_ >> student.gpa_ >> student.age_;
    return is;
}
