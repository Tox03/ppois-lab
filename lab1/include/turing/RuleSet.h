#pragma once
#include <iostream>
#include <string>
#include <map>

/**
 * @brief Структура, описывающая одно правило (инструкцию) для Машины Тьюринга.
 * 
 * Содержит текущее состояние, читаемый символ и действия, которые 
 * машина должна выполнить: новое состояние, записываемый символ и направление сдвига.
 */
struct Rule {
    std::string current_state; ///< Текущее состояние машины
    char        read_symbol;   ///< Символ, который машина считывает с ленты
    std::string next_state;    ///< Состояние, в которое переходит машина
    char        write_symbol;  ///< Символ, который машина запишет на ленту
    char        direction;     ///< Направление сдвига головки ('R', 'L', 'N')

    /**
     * @brief Оператор сравнения правил на равенство.
     * @param other Правило для сравнения.
     * @return true, если все поля совпадают.
     */
    bool operator==(const Rule& other) const {
        return current_state == other.current_state &&
               read_symbol == other.read_symbol &&
               next_state == other.next_state &&
               write_symbol == other.write_symbol &&
               direction == other.direction;
    }

    /**
     * @brief Оператор сравнения правил на неравенство.
     * @param other Правило для сравнения.
     * @return true, если правила отличаются.
     */
    bool operator!=(const Rule& other) const {
        return !(*this == other);
    }
};

/**
 * @brief Класс, представляющий набор правил для Машины Тьюринга.
 * 
 * Хранит правила в словаре (map) для быстрого поиска по комбинации 
 * "текущее состояние + считанный символ".
 */
class RuleSet {
private:
    /// Словарь правил. Ключ - пара (состояние, символ), значение - само правило.
    std::map<std::pair<std::string, char>, Rule> rules;

public:
    /**
     * @brief Конструктор по умолчанию.
     */
    RuleSet() = default;

    /**
     * @brief Добавляет новое правило или заменяет существующее.
     * @param rule Правило для добавления.
     */
    void add_rule(const Rule& rule);

    /**
     * @brief Удаляет правило из набора.
     * @param state Текущее состояние удаляемого правила.
     * @param symbol Считываемый символ удаляемого правила.
     */
    void remove_rule(const std::string& state, char symbol);
    
    /**
     * @brief Добавляет правило к текущему набору.
     * @param rule Правило для добавления.
     * @return Ссылка на текущий измененный объект.
     */
    RuleSet& operator+=(const Rule& rule);

    /**
     * @brief Создает новый набор правил с добавленным правилом.
     * @param rule Правило для добавления.
     * @return Новый объект RuleSet.
     */
    RuleSet operator+(const Rule& rule) const;

    /**
     * @brief Удаляет правило из текущего набора.
     * @param rule Правило, которое нужно удалить.
     * @return Ссылка на текущий измененный объект.
     */
    RuleSet& operator-=(const Rule& rule);

    /**
     * @brief Создает новый набор правил без указанного правила.
     * @param rule Правило, которое нужно удалить.
     * @return Новый объект RuleSet.
     */
    RuleSet operator-(const Rule& rule) const;

    /**
     * @brief Ищет правило для заданного состояния и символа.
     * @param state Текущее состояние машины.
     * @param symbol Символ, считанный с ленты.
     * @param out Ссылка, куда будет записано найденное правило.
     * @return true, если правило найдено, иначе false.
     */
    bool find_rule(const std::string& state, char symbol, Rule& out) const;

    /**
     * @brief Считывает правила из потока до конца ввода.
     * @param is Входной поток.
     */
    void load_from_stream(std::istream& is);

    /**
     * @brief Возвращает количество правил в наборе.
     * @return Число правил.
     */
    size_t size() const { return rules.size(); }

    /**
     * @brief Проверяет, пуст ли набор правил.
     * @return true, если набор пуст.
     */
    bool empty() const { return rules.empty(); }

    /**
     * @brief Очищает все правила.
     */
    void clear() { rules.clear(); }

    /**
     * @brief Возвращает константную ссылку на словарь всех правил.
     */
    const std::map<std::pair<std::string, char>, Rule>& get_all_rules() const { return rules; }

    /**
     * @brief Выводит все правила в поток.
     * @param os Выходной поток.
     * @param rs Набор правил.
     * @return Ссылка на выходной поток.
     */
    friend std::ostream& operator<<(std::ostream& os, const RuleSet& rs);

    /**
     * @brief Считывает правила из потока.
     * @param is Входной поток.
     * @param rs Набор правил.
     * @return Ссылка на входной поток.
     */
    friend std::istream& operator>>(std::istream& is, RuleSet& rs);

    /**
     * @brief Сравнивает два набора правил на равенство.
     * @param other Другой набор правил.
     * @return true, если правила идентичны.
     */
    bool operator==(const RuleSet& other) const;

    /**
     * @brief Сравнивает два набора правил на неравенство.
     * @param other Другой набор правил.
     * @return true, если наборы отличаются.
     */
    bool operator!=(const RuleSet& other) const;
};
