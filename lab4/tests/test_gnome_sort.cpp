#include <gtest/gtest.h>
#include <vector>
#include <string>
#include "sort/GnomeSort.h"
#include "model/Student.h"

TEST(GnomeSortTest, EmptyAndSingleElementVector) {
    std::vector<int> empty_vec;
    GnomeSort::sort(empty_vec);
    EXPECT_TRUE(empty_vec.empty());

    std::vector<int> single_vec = {42};
    GnomeSort::sort(single_vec);
    ASSERT_EQ(single_vec.size(), 1u);
    EXPECT_EQ(single_vec[0], 42);
}

TEST(GnomeSortTest, AlreadySortedAndReverseSorted) {
    std::vector<int> sorted = {1, 2, 3, 4, 5};
    GnomeSort::sort(sorted);
    std::vector<int> expected = {1, 2, 3, 4, 5};
    EXPECT_EQ(sorted, expected);

    std::vector<int> reverse = {5, 4, 3, 2, 1};
    GnomeSort::sort(reverse);
    EXPECT_EQ(reverse, expected);
}

TEST(GnomeSortTest, DuplicatesAndNegativeNumbers) {
    std::vector<int> data = {3, -1, 4, -1, 5, 9, 2, 6, 5, -5};
    GnomeSort::sort(data);
    std::vector<int> expected = {-5, -1, -1, 2, 3, 4, 5, 5, 6, 9};
    EXPECT_EQ(data, expected);
}

TEST(GnomeSortTest, RawArraySorting) {
    int arr[] = {9, 7, 5, 3, 1, 8, 6, 4, 2, 0};
    std::size_t size = sizeof(arr) / sizeof(arr[0]);
    GnomeSort::sort(arr, size);
    for (std::size_t i = 0; i < size; ++i) {
        EXPECT_EQ(arr[i], static_cast<int>(i));
    }

    // Проверка нулевого указателя или размера 0
    GnomeSort::sort(static_cast<int*>(nullptr), 0);
}

TEST(GnomeSortTest, CustomComparator) {
    std::vector<int> data = {10, 50, 20, 40, 30};
    // Сортировка по убыванию
    GnomeSort::sort(data, std::greater<int>());
    std::vector<int> expected = {50, 40, 30, 20, 10};
    EXPECT_EQ(data, expected);
}

TEST(GnomeSortTest, StringsSorting) {
    std::vector<std::string> words = {"banana", "apple", "cherry", "date"};
    GnomeSort::sort(words);
    std::vector<std::string> expected = {"apple", "banana", "cherry", "date"};
    EXPECT_EQ(words, expected);
}

TEST(GnomeSortTest, UserDefinedObjectsSorting) {
    std::vector<Student> students = {
        Student(103, "Иванов Иван", 4.2, 20),
        Student(101, "Петров Петр", 4.8, 19),
        Student(104, "Сидоров Сидор", 3.9, 21),
        Student(102, "Алексеев Алексей", 5.0, 18)
    };

    // Сортировка по умолчанию (по ID)
    GnomeSort::sort(students);
    EXPECT_EQ(students[0].getId(), 101);
    EXPECT_EQ(students[1].getId(), 102);
    EXPECT_EQ(students[2].getId(), 103);
    EXPECT_EQ(students[3].getId(), 104);

    // Сортировка по среднему баллу GPA (по возрастанию)
    GnomeSort::sort(students, [](const Student& a, const Student& b) {
        return a.getGpa() < b.getGpa();
    });
    EXPECT_DOUBLE_EQ(students[0].getGpa(), 3.9);
    EXPECT_DOUBLE_EQ(students[1].getGpa(), 4.2);
    EXPECT_DOUBLE_EQ(students[2].getGpa(), 4.8);
    EXPECT_DOUBLE_EQ(students[3].getGpa(), 5.0);

    // Сортировка массива студентов по возрасту
    Student arr_s[] = {
        Student(1, "A", 4.0, 25),
        Student(2, "B", 4.0, 19),
        Student(3, "C", 4.0, 22)
    };
    GnomeSort::sort(arr_s, 3, [](const Student& a, const Student& b) {
        return a.getAge() < b.getAge();
    });
    EXPECT_EQ(arr_s[0].getAge(), 19);
    EXPECT_EQ(arr_s[1].getAge(), 22);
    EXPECT_EQ(arr_s[2].getAge(), 25);
}
