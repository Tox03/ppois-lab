#ifndef PIGEONHOLE_SORT_CPP
#define PIGEONHOLE_SORT_CPP

#include "sort/PigeonholeSort.h"
#include <algorithm>
#include <utility>

// Сортировка диапазона с функцией извлечения ключа
template <typename RandomIt, typename KeyExtractor>
void PigeonholeSort::sort(RandomIt first, RandomIt last, KeyExtractor key_extractor) {
    if (first == last || std::next(first) == last) {
        return;
    }

    std::int64_t min_key = key_extractor(*first);
    std::int64_t max_key = min_key;
    for (RandomIt it = first; it != last; ++it) {
        std::int64_t key = key_extractor(*it);
        if (key < min_key) min_key = key;
        if (key > max_key) max_key = key;
    }

    std::int64_t range = max_key - min_key + 1;
    if (range > MAX_ALLOWED_RANGE) {
        throw std::invalid_argument("Диапазон ключей превышает максимально допустимый предел");
    }

    using ValueType = typename std::iterator_traits<RandomIt>::value_type;
    std::vector<std::vector<ValueType>> holes(static_cast<std::size_t>(range));
    for (RandomIt it = first; it != last; ++it) {
        std::size_t hole_index = static_cast<std::size_t>(key_extractor(*it) - min_key);
        holes[hole_index].push_back(std::move(*it));
    }

    RandomIt target = first;
    for (std::size_t i = 0; i < holes.size(); ++i) {
        for (std::size_t j = 0; j < holes[i].size(); ++j) {
            *target = std::move(holes[i][j]);
            ++target;
        }
    }
}

// Сортировка диапазона для чисел по возрастанию
template <typename RandomIt>
void PigeonholeSort::sort(RandomIt first, RandomIt last) {
    using ValueType = typename std::iterator_traits<RandomIt>::value_type;
    sort(first, last, [](const ValueType& item) -> std::int64_t {
        return static_cast<std::int64_t>(item);
    });
}

// Сортировка диапазона с функцией извлечения ключа по убыванию
template <typename RandomIt, typename KeyExtractor>
void PigeonholeSort::sort_descending(RandomIt first, RandomIt last, KeyExtractor key_extractor) {
    if (first == last || std::next(first) == last) {
        return;
    }

    std::int64_t min_key = key_extractor(*first);
    std::int64_t max_key = min_key;
    for (RandomIt it = first; it != last; ++it) {
        std::int64_t key = key_extractor(*it);
        if (key < min_key) min_key = key;
        if (key > max_key) max_key = key;
    }

    std::int64_t range = max_key - min_key + 1;
    if (range > MAX_ALLOWED_RANGE) {
        throw std::invalid_argument("Диапазон ключей превышает максимально допустимый предел");
    }

    using ValueType = typename std::iterator_traits<RandomIt>::value_type;
    std::vector<std::vector<ValueType>> holes(static_cast<std::size_t>(range));
    for (RandomIt it = first; it != last; ++it) {
        std::size_t hole_index = static_cast<std::size_t>(key_extractor(*it) - min_key);
        holes[hole_index].push_back(std::move(*it));
    }

    RandomIt target = first;
    for (std::size_t i = holes.size(); i > 0; --i) {
        std::size_t idx = i - 1;
        for (std::size_t j = 0; j < holes[idx].size(); ++j) {
            *target = std::move(holes[idx][j]);
            ++target;
        }
    }
}

// Сортировка диапазона для чисел по убыванию
template <typename RandomIt>
void PigeonholeSort::sort_descending(RandomIt first, RandomIt last) {
    using ValueType = typename std::iterator_traits<RandomIt>::value_type;
    sort_descending(first, last, [](const ValueType& item) -> std::int64_t {
        return static_cast<std::int64_t>(item);
    });
}

// Сортировка вектора с функцией извлечения ключа
template <typename T, typename KeyExtractor>
void PigeonholeSort::sort(std::vector<T>& vec, KeyExtractor key_extractor) {
    sort(vec.begin(), vec.end(), key_extractor);
}

// Сортировка вектора по возрастанию
template <typename T>
void PigeonholeSort::sort(std::vector<T>& vec) {
    sort(vec.begin(), vec.end());
}

// Сортировка вектора по убыванию с функцией извлечения ключа
template <typename T, typename KeyExtractor>
void PigeonholeSort::sort_descending(std::vector<T>& vec, KeyExtractor key_extractor) {
    sort_descending(vec.begin(), vec.end(), key_extractor);
}

// Сортировка вектора по убыванию
template <typename T>
void PigeonholeSort::sort_descending(std::vector<T>& vec) {
    sort_descending(vec.begin(), vec.end());
}

// Сортировка массива по возрастанию с функцией извлечения ключа
template <typename T, typename KeyExtractor>
void PigeonholeSort::sort(T* arr, std::size_t size, KeyExtractor key_extractor) {
    if (arr != nullptr && size > 0) {
        sort(arr, arr + size, key_extractor);
    }
}

// Сортировка массива по возрастанию
template <typename T>
void PigeonholeSort::sort(T* arr, std::size_t size) {
    if (arr != nullptr && size > 0) {
        sort(arr, arr + size);
    }
}

// Сортировка массива по убыванию с функцией извлечения ключа
template <typename T, typename KeyExtractor>
void PigeonholeSort::sort_descending(T* arr, std::size_t size, KeyExtractor key_extractor) {
    if (arr != nullptr && size > 0) {
        sort_descending(arr, arr + size, key_extractor);
    }
}

// Сортировка массива по убыванию
template <typename T>
void PigeonholeSort::sort_descending(T* arr, std::size_t size) {
    if (arr != nullptr && size > 0) {
        sort_descending(arr, arr + size);
    }
}

#endif // PIGEONHOLE_SORT_CPP
