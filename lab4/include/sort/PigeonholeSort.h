#pragma once

#include <cstddef>
#include <vector>
#include <iterator>
#include <stdexcept>
#include <utility>

/**
 * @brief Класс, реализующий обобщённый алгоритм голубиной сортировки (Pigeonhole Sort).
 * Подходит для элементов с целочисленными ключами или объектов, для которых
 * задана функция извлечения целочисленного ключа (KeyExtractor).
 */
class PigeonholeSort {
public:
    /// Максимально допустимый диапазон ключей для предотвращения чрезмерного выделения памяти
    static constexpr long long MAX_ALLOWED_RANGE = 50000000LL;

    /**
     * @brief Сортировка диапазона с использованием пользовательской функции извлечения ключа.
     * @tparam RandomIt Тип итератора.
     * @tparam KeyExtractor Функция/лямбда, принимающая элемент и возвращающая целочисленный ключ (long long).
     * @param first Начало диапазона.
     * @param last Конец диапазона.
     * @param key_extractor Функция извлечения ключа.
     */
    template <typename RandomIt, typename KeyExtractor>
    static void sort(RandomIt first, RandomIt last, KeyExtractor key_extractor);

    /**
     * @brief Сортировка диапазона целочисленных элементов (ключом является само значение).
     * @tparam RandomIt Тип итератора.
     * @param first Начало диапазона.
     * @param last Конец диапазона.
     */
    template <typename RandomIt>
    static void sort(RandomIt first, RandomIt last);

    /**
     * @brief Сортировка вектора с функцией извлечения ключа.
     */
    template <typename T, typename KeyExtractor>
    static void sort(std::vector<T>& vec, KeyExtractor key_extractor);

    /**
     * @brief Сортировка вектора целочисленных значений.
     */
    template <typename T>
    static void sort(std::vector<T>& vec);

    /**
     * @brief Сортировка массива с функцией извлечения ключа.
     */
    template <typename T, typename KeyExtractor>
    static void sort(T arr[], std::size_t size, KeyExtractor key_extractor);

    /**
     * @brief Сортировка массива целочисленных значений.
     */
    template <typename T>
    static void sort(T arr[], std::size_t size);
};

#include "sort/PigeonholeSort.cpp"
