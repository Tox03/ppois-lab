#pragma once

#include <string>
#include <iostream>

/**
 * @brief Пользовательский класс студента для демонстрации сортировки
 * и работы обобщённого графа с пользовательскими типами данных.
 */
class Student {
public:
    /**
     * @brief Конструктор по умолчанию.
     */
    Student();

    /**
     * @brief Параметризованный конструктор.
     * @param id Уникальный идентификатор студента.
     * @param name Имя студента.
     * @param rating Рейтинг (баллы) студента.
     */
    Student(int id, const std::string& name, int rating);

    /**
     * @brief Получить идентификатор студента.
     * @return Идентификатор.
     */
    int getId() const;

    /**
     * @brief Установить идентификатор студента.
     * @param id Новый идентификатор.
     */
    void setId(int id);

    /**
     * @brief Получить имя студента.
     * @return Имя студента.
     */
    const std::string& getName() const;

    /**
     * @brief Установить имя студента.
     * @param name Новое имя студента.
     */
    void setName(const std::string& name);

    /**
     * @brief Получить рейтинг студента.
     * @return Рейтинг студента.
     */
    int getRating() const;

    /**
     * @brief Установить рейтинг студента.
     * @param rating Новый рейтинг студента.
     */
    void setRating(int rating);

    bool operator==(const Student& other) const;
    bool operator!=(const Student& other) const;
    bool operator<(const Student& other) const;
    bool operator<=(const Student& other) const;
    bool operator>(const Student& other) const;
    bool operator>=(const Student& other) const;

    friend std::ostream& operator<<(std::ostream& os, const Student& student);

private:
    int id_;              ///< Идентификатор студента
    std::string name_;    ///< Имя студента
    int rating_;          ///< Рейтинг студента
};
