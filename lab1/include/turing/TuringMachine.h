#pragma once
#include "turing/Tape.h"
#include "turing/RuleSet.h"
#include <string>
#include <iostream>

/**
 * @brief Главный класс, представляющий абстрактную Машину Тьюринга.
 * 
 * Связывает воедино бесконечную ленту (Tape) и набор правил переходов (RuleSet),
 * управляет состоянием машины и выполняет алгоритм.
 */
class TuringMachine {
private:
    Tape tape;                 ///< Лента машины
    RuleSet rules;             ///< Набор правил (таблица переходов)
    std::string current_state; ///< Текущее состояние машины
    bool halted;               ///< Флаг остановки (true, если машина завершила работу)

public:
    /**
     * @brief Конструктор машины Тьюринга.
     * @param start_state Стартовое состояние (по умолчанию "q0").
     */
    TuringMachine(const std::string& start_state = "q0");

    /**
     * @brief Возвращает ссылку на ленту для изменения её состояния.
     * @return Неконстантная ссылка на ленту.
     */
    Tape& get_tape();

    /**
     * @brief Возвращает константную ссылку на ленту (только для чтения).
     * @return Константная ссылка на ленту.
     */
    const Tape& get_tape() const;
    
    /**
     * @brief Возвращает ссылку на набор правил для добавления/удаления.
     * @return Неконстантная ссылка на правила.
     */
    RuleSet& get_rules();

    /**
     * @brief Возвращает константную ссылку на набор правил (только для чтения).
     * @return Константная ссылка на правила.
     */
    const RuleSet& get_rules() const;

    /**
     * @brief Получает текущее состояние машины.
     * @return Строка текущего состояния.
     */
    const std::string& get_state() const { return current_state; }

    /**
     * @brief Принудительно устанавливает новое состояние машины
     * и сбрасывает флаг остановки.
     * @param state Новое состояние.
     */
    void set_state(const std::string& state);

    /**
     * @brief Проверяет, остановлена ли машина.
     * @return true, если машина остановлена (нет подходящих правил), иначе false.
     */
    bool is_halted() const;

    /**
     * @brief Выполняет один такт (шаг) работы машины.
     * Считывает символ, находит правило, записывает новый символ,
     * сдвигает головку и меняет состояние.
     * @return true, если шаг успешно выполнен.
     * false, если машина остановилась (правило не найдено).
     */
    bool step();

    /**
     * @brief Запускает автоматическое выполнение алгоритма до остановки машины.
     * @param log_steps Если true, после каждого шага состояние
     * машины будет выводиться в консоль.
     */
    void run(bool log_steps = false);

    /**
     * @brief Загружает состояние ленты и правила из потока.
     * @param is Входной поток.
     */
    void load_from_stream(std::istream& is);

    /**
     * @brief Сравнивает две машины Тьюринга на равенство.
     */
    bool operator==(const TuringMachine& other) const;

    /**
     * @brief Сравнивает две машины Тьюринга на неравенство.
     */
    bool operator!=(const TuringMachine& other) const;

    /**
     * @brief Выводит текущее состояние машины и ленту в поток.
     * @param os Выходной поток.
     * @param tm Машина Тьюринга для вывода.
     * @return Ссылка на выходной поток.
     */
    friend std::ostream& operator<<(std::ostream& os, const TuringMachine& tm);

    /**
     * @brief Считывает состояние машины из потока.
     * @param is Входной поток.
     * @param tm Машина Тьюринга.
     * @return Ссылка на входной поток.
     */
    friend std::istream& operator>>(std::istream& is, TuringMachine& tm);
};
