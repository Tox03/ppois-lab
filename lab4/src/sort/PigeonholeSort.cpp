#ifndef PIGEONHOLE_SORT_CPP
#define PIGEONHOLE_SORT_CPP

#include "sort/PigeonholeSort.h"

// Сортировка диапазона с пользовательским экстрактором ключа
template <typename RandomIt, typename KeyExtractor>
void PigeonholeSort::sort(RandomIt first, RandomIt last, KeyExtractor key_extractor) {
    if (first == last) {
        return;
    }

    auto next = first;
    ++next;
    if (next == last) {
        return;
    }

    long long min_key = key_extractor(*first);
    long long max_key = min_key;

    for (auto it = next; it != last; ++it) {
        long long element_key = key_extractor(*it);
        if (element_key < min_key) {
            min_key = element_key;
        }
        if (element_key > max_key) {
            max_key = element_key;
        }
    }

    long long range = max_key - min_key + 1;
    if (range < 0 || range > MAX_ALLOWED_RANGE) {
        throw std::invalid_argument("Диапазон ключей слишком велик для голубиной сортировки");
    }

    using ValueType = typename std::iterator_traits<RandomIt>::value_type;
    std::vector<std::vector<ValueType>> holes(static_cast<std::size_t>(range));

    for (auto it = first; it != last; ++it) {
        long long element_key = key_extractor(*it);
        std::size_t hole_idx = static_cast<std::size_t>(element_key - min_key);
        holes[hole_idx].push_back(std::move(*it));
    }

    auto out_it = first;
    for (auto& hole : holes) {
        for (auto& elem : hole) {
            *out_it = std::move(elem);
            ++out_it;
        }
    }
}

// Сортировка диапазона целочисленных элементов
template <typename RandomIt>
void PigeonholeSort::sort(RandomIt first, RandomIt last) {
    sort(first, last, [](const auto& val) -> long long {
        return static_cast<long long>(val);
    });
}

// Сортировка вектора с экстрактором ключа
template <typename T, typename KeyExtractor>
void PigeonholeSort::sort(std::vector<T>& vec, KeyExtractor key_extractor) {
    sort(vec.begin(), vec.end(), key_extractor);
}

// Сортировка вектора целочисленных значений
template <typename T>
void PigeonholeSort::sort(std::vector<T>& vec) {
    sort(vec.begin(), vec.end());
}

// Сортировка массива с экстрактором ключа
template <typename T, typename KeyExtractor>
void PigeonholeSort::sort(T arr[], std::size_t size, KeyExtractor key_extractor) {
    if (arr && size > 0) {
        sort(arr, arr + size, key_extractor);
    }
}

// Сортировка массива целочисленных значений
template <typename T>
void PigeonholeSort::sort(T arr[], std::size_t size) {
    if (arr && size > 0) {
        sort(arr, arr + size);
    }
}

#endif // PIGEONHOLE_SORT_CPP
