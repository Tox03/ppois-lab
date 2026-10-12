#pragma once
#include "markov/MarkovProgram.h"
#include "markov/MarkovString.h"
#include <iostream>

/**
 * @class MarkovMachine
 * @brief Представляет абстрактную машину, выполняющую нормальный алгорифм Маркова.
 */
class MarkovMachine {
private:
    MarkovProgram program;   ///< Программа правил
    MarkovString tape;       ///< Обрабатываемая лента (строка)
    bool halted;             ///< Флаг завершения работы машины
    bool log_enabled;        ///< Флаг подробного логирования каждого шага

public:
    /** @brief Конструктор по умолчанию. */
    MarkovMachine();

    /** @brief Конструктор копирования. */
    MarkovMachine(const MarkovMachine& other);

    /** @brief Оператор присваивания копированием. */
    MarkovMachine& operator=(const MarkovMachine& other);

    /** 
     * @brief Устанавливает программу правил для машины.
     * @param prog Программа правил.
     */
    void setProgram(const MarkovProgram& prog);

    /** @brief Возвращает константную ссылку на программу правил. */
    const MarkovProgram& getProgram() const { return program; }

    /** @brief Возвращает ссылку на программу правил. */
    MarkovProgram& getProgram() { return program; }

    /** 
     * @brief Добавляет правило в программу машины.
     * @param rule Добавляемое правило.
     */
    void addRule(const MarkovRule& rule);

    /** 
     * @brief Удаляет правило из программы по индексу.
     * @param index Индекс удаляемого правила.
     */
    void removeRule(size_t index);

    /** 
     * @brief Задаёт ленту (строку данных) для машины.
     * @param tape_str Новая лента.
     */
    void setTape(const MarkovString& tape_str);

    /** @brief Возвращает текущее состояние ленты. */
    MarkovString getTape() const;

    /** 
     * @brief Включает или отключает пошаговое логирование.
     * @param enabled Флаг активности логирования.
     */
    void setLogEnabled(bool enabled);

    /** @brief Проверяет, включено ли пошаговое логирование. */
    bool isLogEnabled() const;

    /** @brief Проверяет, остановлена ли машина. */
    bool isHalted() const;

    /** @brief Сбрасывает флаг остановки машины. */
    void reset();

    /** 
     * @brief Выполняет один такт (шаг) алгоритма Маркова.
     * @return true, если правило было успешно применено; false, если машина остановлена.
     */
    bool step();

    /** @brief Интерпретирует всю программу до полной остановки. */
    void run();

    /** 
     * @brief Загружает правила программы из входного потока.
     * @param is Входной поток.
     */
    void loadProgramFromStream(std::istream& is);

    /** 
     * @brief Загружает начальное состояние ленты из входного потока.
     * @param is Входной поток.
     */
    void loadTapeFromStream(std::istream& is);

    /** 
     * @brief Загружает машину (ленту и правила) из входного потока.
     * @param is Входной поток.
     */
    void loadFromStream(std::istream& is);

    /** @brief Оператор проверки машин на равенство. */
    bool operator==(const MarkovMachine& other) const;

    /** @brief Оператор проверки машин на неравенство. */
    bool operator!=(const MarkovMachine& other) const;

    /** @brief Выводит ленту и статус остановки в поток. */
    friend std::ostream& operator<<(std::ostream& os, const MarkovMachine& machine);

    /** @brief Считывает состояние ленты и программу из потока. */
    friend std::istream& operator>>(std::istream& is, MarkovMachine& machine);
};
