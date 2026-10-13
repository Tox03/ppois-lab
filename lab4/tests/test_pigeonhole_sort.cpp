#include <gtest/gtest.h>
#include <vector>
#include "sort/PigeonholeSort.h"
#include "model/Student.h"

TEST(PigeonholeSortTest, EmptyAndSingleElementVector) {
    std::vector<int> empty_vec;
    PigeonholeSort::sort(empty_vec);
    EXPECT_TRUE(empty_vec.empty());

    std::vector<int> single_vec = {99};
    PigeonholeSort::sort(single_vec);
    ASSERT_EQ(single_vec.size(), 1u);
    EXPECT_EQ(single_vec[0], 99);
}

TEST(PigeonholeSortTest, IntegralNumbersSorting) {
    std::vector<int> data = {8, 3, 2, 7, 4, 6, 8, 3, 1, 5};
    PigeonholeSort::sort(data);
    std::vector<int> expected = {1, 2, 3, 3, 4, 5, 6, 7, 8, 8};
    EXPECT_EQ(data, expected);
}

TEST(PigeonholeSortTest, NegativeNumbersSorting) {
    std::vector<int> data = {-5, 10, -2, 0, 7, -5, 3};
    PigeonholeSort::sort(data);
    std::vector<int> expected = {-5, -5, -2, 0, 3, 7, 10};
    EXPECT_EQ(data, expected);
}

TEST(PigeonholeSortTest, RawArraySorting) {
    int arr[] = {20, 15, 10, 25, 10, 5};
    std::size_t size = sizeof(arr) / sizeof(arr[0]);
    PigeonholeSort::sort(arr, size);
    int expected[] = {5, 10, 10, 15, 20, 25};
    for (std::size_t i = 0; i < size; ++i) {
        EXPECT_EQ(arr[i], expected[i]);
    }

    PigeonholeSort::sort(static_cast<int*>(nullptr), 0);
}

TEST(PigeonholeSortTest, UserDefinedObjectsWithKeyExtractor) {
    std::vector<Student> students = {
        Student(104, "Васильев Василий", 4.1, 22),
        Student(101, "Петров Петр", 4.8, 19),
        Student(103, "Иванов Иван", 4.2, 20),
        Student(102, "Алексеев Алексей", 5.0, 18)
    };

    // Сортировка по ID
    PigeonholeSort::sort(students, [](const Student& s) {
        return static_cast<long long>(s.getId());
    });
    EXPECT_EQ(students[0].getId(), 101);
    EXPECT_EQ(students[1].getId(), 102);
    EXPECT_EQ(students[2].getId(), 103);
    EXPECT_EQ(students[3].getId(), 104);

    // Сортировка по возрасту
    PigeonholeSort::sort(students, [](const Student& s) {
        return static_cast<long long>(s.getAge());
    });
    EXPECT_EQ(students[0].getAge(), 18);
    EXPECT_EQ(students[1].getAge(), 19);
    EXPECT_EQ(students[2].getAge(), 20);
    EXPECT_EQ(students[3].getAge(), 22);

    // Сортировка массива студентов
    Student arr_s[] = {
        Student(50, "A", 3.0, 30),
        Student(20, "B", 4.0, 20),
        Student(40, "C", 5.0, 25)
    };
    PigeonholeSort::sort(arr_s, 3, [](const Student& s) {
        return static_cast<long long>(s.getId());
    });
    EXPECT_EQ(arr_s[0].getId(), 20);
    EXPECT_EQ(arr_s[1].getId(), 40);
    EXPECT_EQ(arr_s[2].getId(), 50);
}

TEST(PigeonholeSortTest, RangeTooLargeThrowsException) {
    std::vector<long long> extreme = {0LL, 100000000LL};
    EXPECT_THROW(PigeonholeSort::sort(extreme), std::invalid_argument);
}
