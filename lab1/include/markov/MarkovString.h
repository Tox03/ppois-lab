#pragma once
#include <string>
#include <iostream>

/**
 * @class MarkovString
 * @brief Представляет ленту данных (строку) в алгоритме Маркова.
 */
class MarkovString {
private:
    std::string data;       ///< Содержимое строки
    size_t caret_pos;       ///< Текущая позиция каретки

public:
    /** @brief Конструктор по умолчанию. */
    MarkovString();

    /** 
     * @brief Конструктор с начальным значением строки.
     * @param data Начальное строковое значение.
     */
    explicit MarkovString(const std::string& data);
    
    /** @brief Конструктор копирования. */
    MarkovString(const MarkovString& other);

    /** @brief Оператор присваивания копированием. */
    MarkovString& operator=(const MarkovString& other);

    /** @brief Возвращает текущее значение строки. */
    std::string getValue() const;

    /** 
     * @brief Устанавливает новое значение строки.
     * @param value Новая строка.
     */
    void setValue(const std::string& value);

    /** @brief Возвращает текущую позицию каретки. */
    size_t getCaretPos() const;

    /** 
     * @brief Устанавливает позицию каретки.
     * @param pos Новая позиция каретки.
     */
    void setCaretPos(size_t pos);

    /** @brief Префиксный инкремент позиции каретки (++obj). */
    MarkovString& operator++(); 

    /** @brief Постфиксный инкремент позиции каретки (obj++). */
    MarkovString operator++(int); 

    /** @brief Префиксный декремент позиции каретки (--obj). */
    MarkovString& operator--(); 

    /** @brief Постфиксный декремент позиции каретки (obj--). */
    MarkovString operator--(int); 

    /** @brief Оператор проверки на равенство. */
    bool operator==(const MarkovString& other) const;

    /** @brief Оператор проверки на неравенство. */
    bool operator!=(const MarkovString& other) const;

    /** @brief Запись содержимого строки в поток вывода. */
    friend std::ostream& operator<<(std::ostream& os, const MarkovString& str);

    /** @brief Чтение содержимого строки из потока ввода. */
    friend std::istream& operator>>(std::istream& is, MarkovString& str);
};
