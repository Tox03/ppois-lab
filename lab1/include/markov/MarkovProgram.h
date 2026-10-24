#pragma once
#include <vector>
#include <iostream>
#include "markov/MarkovRule.h"

/**
 * @class MarkovProgram
 * @brief Представляет упорядоченный набор правил (программу) для алгоритма Маркова.
 */
class MarkovProgram {
private:
    std::vector<MarkovRule> rules; ///< Список правил подстановки

public:
    /** @brief Конструктор по умолчанию. */
    MarkovProgram();
    
    /** @brief Конструктор копирования. */
    MarkovProgram(const MarkovProgram& other);

    /** @brief Оператор присваивания копированием. */
    MarkovProgram& operator=(const MarkovProgram& other);

    /** 
     * @brief Добавляет новое правило в конец программы.
     * @param rule Добавляемое правило.
     */
    void addRule(const MarkovRule& rule);

    /** 
     * @brief Удаляет правило по указанному индексу.
     * @param index Индекс удаляемого правила.
     */
    void removeRule(size_t index);

    /** 
     * @brief Возвращает константную ссылку на правило по индексу.
     * @param index Индекс правила.
     * @return Ссылка на правило.
     */
    const MarkovRule& getRule(size_t index) const;

    /** @brief Возвращает общее количество правил в программе. */
    size_t getRuleCount() const;

    /** @brief Проверяет, пуста ли программа. */
    bool empty() const { return rules.empty(); }

    /** @brief Очищает все правила в программе. */
    void clear() { rules.clear(); }

    /** @brief Оператор проверки программ на равенство. */
    bool operator==(const MarkovProgram& other) const;

    /** @brief Оператор проверки программ на неравенство. */
    bool operator!=(const MarkovProgram& other) const;

    /** @brief Выводит все правила в поток, по одному на строку. */
    friend std::ostream& operator<<(std::ostream& os, const MarkovProgram& program);

    /** @brief Считывает список правил из потока до конца ввода. */
    friend std::istream& operator>>(std::istream& is, MarkovProgram& program);
};
