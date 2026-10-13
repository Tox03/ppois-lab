#pragma once

#include <string>
#include <iostream>

/**
 * @brief Пользовательский класс «Студент» для демонстрации сортировок и контейнера.
 * Содержит идентификатор, ФИО, средний балл и возраст.
 */
class Student {
public:
    /**
     * @brief Конструктор по умолчанию.
     */
    Student();

    /**
     * @brief Параметризованный конструктор.
     * @param id Идентификатор студента.
     * @param name ФИО студента.
     * @param gpa Средний балл (GPA).
     * @param age Возраст студента.
     */
    Student(int id, const std::string& name, double gpa, int age);

    /**
     * @brief Получить идентификатор студента.
     */
    int getId() const;

    /**
     * @brief Получить ФИО студента.
     */
    const std::string& getName() const;

    /**
     * @brief Получить средний балл студента.
     */
    double getGpa() const;

    /**
     * @brief Получить возраст студента.
     */
    int getAge() const;

    /**
     * @brief Установить идентификатор студента.
     */
    void setId(int id);

    /**
     * @brief Установить ФИО студента.
     */
    void setName(const std::string& name);

    /**
     * @brief Установить средний балл.
     */
    void setGpa(double gpa);

    /**
     * @brief Установить возраст.
     */
    void setAge(int age);

    /**
     * @brief Операторы сравнения (по умолчанию сравнивают по id).
     */
    bool operator==(const Student& other) const;
    bool operator!=(const Student& other) const;
    bool operator<(const Student& other) const;
    bool operator<=(const Student& other) const;
    bool operator>(const Student& other) const;
    bool operator>=(const Student& other) const;

    /**
     * @brief Оператор вывода в поток.
     */
    friend std::ostream& operator<<(std::ostream& os, const Student& student);

    /**
     * @brief Оператор ввода из потока.
     */
    friend std::istream& operator>>(std::istream& is, Student& student);

private:
    int id_{0};                 ///< Идентификатор студента
    std::string name_{};        ///< ФИО студента
    double gpa_{0.0};           ///< Средний балл
    int age_{0};                ///< Возраст студента
};
