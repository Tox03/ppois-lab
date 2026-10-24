#pragma once
#include <string>
#include <iostream>

/**
 * @class MarkovRule
 * @brief Представляет одно правило подстановки в алгоритме Маркова.
 * 
 * Правило Маркова состоит из искомой подстроки (from), подстроки замены (to)
 * и флага завершающего (терминального) правила,
 * останавливающего работу алгоритма.
 */
class MarkovRule {
private:
    std::string from;        ///< Искомый образец
    std::string to;          ///< Образец для замены
    bool is_terminal;        ///< Флаг терминального правила

public:
    /** @brief Конструктор по умолчанию. */
    MarkovRule();

    /** 
     * @brief Конструктор правила подстановки.
     * @param from Искомая подстрока.
     * @param to Подстрока для замены.
     * @param is_terminal Является ли правило терминальным (по умолчанию false).
     */
    MarkovRule(const std::string& from, const std::string& to, bool is_terminal = false);
    
    /** @brief Конструктор копирования. */
    MarkovRule(const MarkovRule& other);

    /** @brief Оператор присваивания копированием. */
    MarkovRule& operator=(const MarkovRule& other);

    /** @brief Возвращает искомую подстроку. */
    std::string getFrom() const;

    /** @brief Возвращает подстроку для замены. */
    std::string getTo() const;

    /** @brief Проверяет, является ли правило терминальным. */
    bool isTerminal() const;

    /** @brief Оператор проверки на равенство правил. */
    bool operator==(const MarkovRule& other) const;

    /** @brief Оператор проверки на неравенство правил. */
    bool operator!=(const MarkovRule& other) const;

    /** @brief Запись правила в поток в формате: from -> to (или ->.) */
    friend std::ostream& operator<<(std::ostream& os, const MarkovRule& rule);

    /** @brief Чтение правила из потока. */
    friend std::istream& operator>>(std::istream& is, MarkovRule& rule);
};
