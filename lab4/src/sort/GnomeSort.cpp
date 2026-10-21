#ifndef GNOME_SORT_CPP
#define GNOME_SORT_CPP

#include "sort/GnomeSort.h"
#include <algorithm>

// Сортировка диапазона с компаратором
template <typename RandomIt, typename Compare>
void GnomeSort::sort(RandomIt first, RandomIt last, Compare comp) {
    if (first == last) {
        return;
    }

    RandomIt current = first;
    while (current != last) {
        if (current == first) {
            ++current;
        } else {
            RandomIt prev = current - 1;
            if (comp(*current, *prev)) {
                std::iter_swap(current, prev);
                --current;
            } else {
                ++current;
            }
        }
    }
}

// Сортировка диапазона по убыванию
template <typename RandomIt>
void GnomeSort::sort_descending(RandomIt first, RandomIt last) {
    using ValueType = typename std::iterator_traits<RandomIt>::value_type;
    sort(first, last, std::greater<ValueType>());
}

// Сортировка вектора с компаратором
template <typename T, typename Compare>
void GnomeSort::sort(std::vector<T>& vec, Compare comp) {
    sort(vec.begin(), vec.end(), comp);
}

// Сортировка вектора по убыванию
template <typename T>
void GnomeSort::sort_descending(std::vector<T>& vec) {
    sort(vec.begin(), vec.end(), std::greater<T>());
}

// Сортировка встроенного массива с компаратором
template <typename T, typename Compare>
void GnomeSort::sort(T* arr, std::size_t size, Compare comp) {
    if (arr != nullptr && size > 0) {
        sort(arr, arr + size, comp);
    }
}

// Сортировка встроенного массива по убыванию
template <typename T>
void GnomeSort::sort_descending(T* arr, std::size_t size) {
    if (arr != nullptr && size > 0) {
        sort(arr, arr + size, std::greater<T>());
    }
}

#endif // GNOME_SORT_CPP
