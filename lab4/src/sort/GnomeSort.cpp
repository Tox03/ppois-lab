#ifndef GNOME_SORT_CPP
#define GNOME_SORT_CPP

#include "sort/GnomeSort.h"
#include <algorithm>

// Сортировка диапазона итераторов
template <typename RandomIt, typename Compare>
void GnomeSort::sort(RandomIt first, RandomIt last, Compare comp) {
    if (first == last) {
        return;
    }

    auto current = first;
    while (current != last) {
        if (current == first) {
            ++current;
        } else {
            auto prev = current;
            --prev;
            if (!comp(*current, *prev)) {
                // Элементы уже находятся в правильном порядке
                ++current;
            } else {
                // Меняем местами и делаем шаг назад
                std::iter_swap(current, prev);
                --current;
            }
        }
    }
}

// Сортировка вектора std::vector
template <typename T, typename Compare>
void GnomeSort::sort(std::vector<T>& vec, Compare comp) {
    sort(vec.begin(), vec.end(), comp);
}

// Сортировка обычного массива
template <typename T, typename Compare>
void GnomeSort::sort(T arr[], std::size_t size, Compare comp) {
    if (arr && size > 0) {
        sort(arr, arr + size, comp);
    }
}

#endif // GNOME_SORT_CPP
