#pragma once
#include <iostream>
#include <map>
#include <string>

/**
 * @brief Класс, эмулирующий бесконечную ленту Машины Тьюринга.
 * 
 * Лента реализована в виде разреженного массива на основе std::map.
 * Это позволяет ленте быть бесконечной в обе стороны, не занимая 
 * память под пробельные символы.
 */
class Tape {
private:
    std::map<int, char> tape; ///< Внутреннее хранилище непустых ячеек ленты
    int head_position;        ///< Текущий индекс головки чтения/записи
    char blank_symbol;        ///< Символ, считающийся "пустым" (обычно '_')

public:
    /**
     * @brief Конструктор ленты.
     * @param blank Символ, который считается пустым (пробелом). По умолчанию '_'.
     */
    Tape(char blank = '_');

    /**
     * @brief Считывает символ, находящийся под головкой.
     * @return Считанный символ или пробельный символ, если ячейка пуста.
     */
    char read_symbol() const;

    /**
     * @brief Записывает символ в ячейку под головкой.
     * Если записывается пробельный символ, ячейка удаляется из памяти.
     * @param symbol Символ для записи.
     */
    void write_symbol(char symbol);

    /**
     * @brief Сдвигает головку ленты.
     * @param direction 'R' - вправо, 'L' - влево. Остальные символы - стоять на месте.
     */
    void move_head(char direction);

    /**
     * @brief Загружает начальное состояние ленты из потока.
     * @param is Входной поток, содержащий строку символов.
     */
    void load_from_stream(std::istream& is);

    /**
     * @brief Читает символ по произвольному индексу без смещения головки.
     * @param index Индекс ячейки на ленте.
     * @return Считанный символ.
     */
    char read_at(int index) const;

    /**
     * @brief Записывает символ по произвольному индексу без смещения головки.
     * @param index Индекс ячейки на ленте.
     * @param symbol Символ для записи.
     */
    void write_at(int index, char symbol);

    /**
     * @brief Получить позицию каретки (головки).
     * @return Текущий индекс головки.
     */
    int get_head_position() const { return head_position; }

    /**
     * @brief Установить позицию каретки (головки).
     * @param pos Новый индекс головки.
     */
    void set_head_position(int pos) { head_position = pos; }

    /**
     * @brief Вспомогательный класс (Паттерн Proxy) для безопасной работы с оператором [].
     * Позволяет перехватывать операцию присваивания к ячейке ленты.
     */
    class Proxy {
    private:
        Tape& parent_tape;
        int index;
    public:
        Proxy(Tape& t, int idx) : parent_tape(t), index(idx) {}
        
        /** @brief Неявное преобразование к char для чтения. */
        operator char() const { return parent_tape.read_at(index); }
        
        /** @brief Перехват операции присваивания для записи. */
        Proxy& operator=(char symbol) {
            parent_tape.write_at(index, symbol);
            return *this;
        }
    };

    /**
     * @brief Оператор индексации для прямого доступа к ячейкам ленты.
     * @param index Индекс ячейки.
     * @return Объект-посредник Proxy для безопасного чтения/записи.
     */
    Proxy operator[](int index);

    /**
     * @brief Выводит заполненную часть ленты и положение головки в поток.
     * @param os Выходной поток.
     * @param t Лента для вывода.
     * @return Ссылка на выходной поток.
     */
    friend std::ostream& operator<<(std::ostream& os, const Tape& t);

    /**
     * @brief Считывает начальное состояние ленты из потока.
     * @param is Входной поток.
     * @param t Лента для записи.
     * @return Ссылка на входной поток.
     */
    friend std::istream& operator>>(std::istream& is, Tape& t);

    /**
     * @brief Сравнивает две ленты на равенство.
     * @param other Другая лента.
     * @return true, если содержимое лент, позиция головки и пустой символ совпадают.
     */
    bool operator==(const Tape& other) const;

    /**
     * @brief Сравнивает две ленты на неравенство.
     * @param other Другая лента.
     * @return true, если ленты различаются.
     */
    bool operator!=(const Tape& other) const;
};
