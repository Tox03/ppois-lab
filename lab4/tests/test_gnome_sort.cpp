#include <gtest/gtest.h>
#include "sort/GnomeSort.h"
#include "model/Student.h"
#include <vector>
#include <string>

TEST(GnomeSortTest, EmptyAndSingleElementVector) {
    std::vector<int> empty_vec;
    GnomeSort::sort(empty_vec);
    EXPECT_TRUE(empty_vec.empty());

    GnomeSort::sort_descending(empty_vec);
    EXPECT_TRUE(empty_vec.empty());

    std::vector<int> single_vec = {42};
    GnomeSort::sort(single_vec);
    ASSERT_EQ(single_vec.size(), 1u);
    EXPECT_EQ(single_vec[0], 42);

    GnomeSort::sort_descending(single_vec);
    ASSERT_EQ(single_vec.size(), 1u);
    EXPECT_EQ(single_vec[0], 42);
}

TEST(GnomeSortTest, SortIntegersAscendingAndDescending) {
    std::vector<int> numbers = {9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 2};
    std::vector<int> expected_asc = {1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9};
    std::vector<int> expected_desc = {9, 8, 7, 6, 5, 5, 4, 3, 2, 2, 1};

    GnomeSort::sort(numbers);
    EXPECT_EQ(numbers, expected_asc);

    GnomeSort::sort_descending(numbers);
    EXPECT_EQ(numbers, expected_desc);
}

TEST(GnomeSortTest, SortWithCustomComparator) {
    std::vector<std::string> words = {"banana", "apple", "cherry", "date"};
    
    // Сортировка по длине строки
    GnomeSort::sort(words, [](const std::string& a, const std::string& b) {
        return a.length() < b.length();
    });

    EXPECT_EQ(words[0], "date");
    EXPECT_EQ(words[1], "apple");
    EXPECT_EQ(words[2], "banana");
    EXPECT_EQ(words[3], "cherry");
}

TEST(GnomeSortTest, SortRawArrayAscendingAndDescending) {
    int arr[] = {30, 10, 50, 20, 40};
    const std::size_t size = 5;

    GnomeSort::sort(arr, size);
    EXPECT_EQ(arr[0], 10);
    EXPECT_EQ(arr[1], 20);
    EXPECT_EQ(arr[2], 30);
    EXPECT_EQ(arr[3], 40);
    EXPECT_EQ(arr[4], 50);

    GnomeSort::sort_descending(arr, size);
    EXPECT_EQ(arr[0], 50);
    EXPECT_EQ(arr[1], 40);
    EXPECT_EQ(arr[2], 30);
    EXPECT_EQ(arr[3], 20);
    EXPECT_EQ(arr[4], 10);

    // Граничный случай: nullptr и нулевой размер
    GnomeSort::sort<int>(nullptr, 0);
    GnomeSort::sort_descending<int>(nullptr, 0);
}

TEST(GnomeSortTest, SortStudentsByCustomClass) {
    std::vector<Student> students = {
        Student(1, "Alice", 85),
        Student(2, "Bob", 70),
        Student(3, "Charlie", 95),
        Student(4, "David", 70)
    };

    GnomeSort::sort(students);
    EXPECT_EQ(students[0].getName(), "Bob");
    EXPECT_EQ(students[1].getName(), "David");
    EXPECT_EQ(students[2].getName(), "Alice");
    EXPECT_EQ(students[3].getName(), "Charlie");

    GnomeSort::sort_descending(students);
    EXPECT_EQ(students[0].getName(), "Charlie");
    EXPECT_EQ(students[1].getName(), "Alice");
}
