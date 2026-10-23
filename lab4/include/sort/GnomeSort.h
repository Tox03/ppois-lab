#pragma once

#include <cstddef>
#include <vector>
#include <functional>
#include <utility>
#include <iterator>
#include <algorithm>

/**
 * @brief Обобщённый класс гномьей сортировки (Gnome sort).
 * Поддерживает сортировку произвольных диапазонов через итераторы произвольного доступа,
 * стандартных контейнеров std::vector, а также встроенных массивов C++.
 * Предоставляет симметричные методы сортировки по возрастанию и по убыванию.
 */
class GnomeSort {
public:
    /**
     * @brief Сортировка диапазона [first, last) с заданным компаратором.
     * @tparam RandomIt Тип итератора произвольного доступа.
     * @tparam Compare Тип функции-компаратора.
     * @param first Начало диапазона.
     * @param last Конец диапазона.
     * @param comp Функция сравнения элементов.
     */
    template <typename RandomIt, typename Compare = std::less<typename std::iterator_traits<RandomIt>::value_type>>
    static void sort(RandomIt first, RandomIt last, Compare comp = Compare());

    /**
     * @brief Сортировка диапазона [first, last) по убыванию.
     * @tparam RandomIt Тип итератора произвольного доступа.
     * @param first Начало диапазона.
     * @param last Конец диапазона.
     */
    template <typename RandomIt>
    static void sort_descending(RandomIt first, RandomIt last);

    /**
     * @brief Сортировка вектора std::vector с заданным компаратором.
     * @tparam T Тип элементов вектора.
     * @tparam Compare Тип компаратора.
     * @param vec Ссылка на сортируемый вектор.
     * @param comp Функция сравнения элементов.
     */
    template <typename T, typename Compare = std::less<T>>
    static void sort(std::vector<T>& vec, Compare comp = Compare());

    /**
     * @brief Сортировка вектора std::vector по убыванию.
     * @tparam T Тип элементов вектора.
     * @param vec Ссылка на сортируемый вектор.
     */
    template <typename T>
    static void sort_descending(std::vector<T>& vec);

    /**
     * @brief Сортировка встроенного массива с заданным компаратором.
     * @tparam T Тип элементов массива.
     * @tparam Compare Тип компаратора.
     * @param arr Указатель на начало массива.
     * @param size Количество элементов в массиве.
     * @param comp Функция сравнения элементов.
     */
    template <typename T, typename Compare = std::less<T>>
    static void sort(T* arr, std::size_t size, Compare comp = Compare());

    /**
     * @brief Сортировка встроенного массива по убыванию.
     * @tparam T Тип элементов массива.
     * @param arr Указатель на начало массива.
     * @param size Количество элементов в массиве.
     */
    template <typename T>
    static void sort_descending(T* arr, std::size_t size);
};

#include "sort/GnomeSort.cpp"
