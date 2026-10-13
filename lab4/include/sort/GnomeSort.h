#pragma once

#include <cstddef>
#include <vector>
#include <functional>
#include <iterator>
#include <utility>
#include <algorithm>

/**
 * @brief Класс, реализующий обобщённый алгоритм гномьей сортировки (Gnome Sort).
 * Поддерживает сортировку любых диапазонов с произвольным компаратором,
 * стандартных контейнеров (std::vector) и обычных массивов для любых типов данных.
 */
class GnomeSort {
public:
    /**
     * @brief Сортировка диапазона итераторов с использованием компаратора.
     * @tparam RandomIt Тип итератора произвольного доступа или двунаправленного итератора.
     * @tparam Compare Тип функции/функтора сравнения.
     * @param first Начало диапазона.
     * @param last Конец диапазона.
     * @param comp Компаратор (по умолчанию std::less).
     */
    template <typename RandomIt, typename Compare = std::less<typename std::iterator_traits<RandomIt>::value_type>>
    static void sort(RandomIt first, RandomIt last, Compare comp = Compare());

    /**
     * @brief Сортировка динамического вектора std::vector.
     * @tparam T Тип элементов вектора.
     * @tparam Compare Тип компаратора.
     * @param vec Вектор для сортировки.
     * @param comp Компаратор (по умолчанию std::less<T>).
     */
    template <typename T, typename Compare = std::less<T>>
    static void sort(std::vector<T>& vec, Compare comp = Compare());

    /**
     * @brief Сортировка обычного массива фиксированного размера.
     * @tparam T Тип элементов массива.
     * @tparam Compare Тип компаратора.
     * @param arr Указатель на массив.
     * @param size Размер массива.
     * @param comp Компаратор (по умолчанию std::less<T>).
     */
    template <typename T, typename Compare = std::less<T>>
    static void sort(T arr[], std::size_t size, Compare comp = Compare());
};

#include "sort/GnomeSort.cpp"
