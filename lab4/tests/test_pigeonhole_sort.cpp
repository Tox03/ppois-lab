#include <gtest/gtest.h>
#include "sort/PigeonholeSort.h"
#include "model/Student.h"
#include <vector>

TEST(PigeonholeSortTest, EmptyAndSingleElementVector) {
    std::vector<int> empty_vec;
    PigeonholeSort::sort(empty_vec);
    EXPECT_TRUE(empty_vec.empty());

    PigeonholeSort::sort_descending(empty_vec);
    EXPECT_TRUE(empty_vec.empty());

    std::vector<int> single_vec = {100};
    PigeonholeSort::sort(single_vec);
    ASSERT_EQ(single_vec.size(), 1u);
    EXPECT_EQ(single_vec[0], 100);

    PigeonholeSort::sort_descending(single_vec);
    ASSERT_EQ(single_vec.size(), 1u);
    EXPECT_EQ(single_vec[0], 100);
}

TEST(PigeonholeSortTest, SortWithNegativeNumbersAndDuplicates) {
    std::vector<int> numbers = {-5, 12, -10, 0, 7, -5, 12, 3};
    std::vector<int> expected_asc = {-10, -5, -5, 0, 3, 7, 12, 12};
    std::vector<int> expected_desc = {12, 12, 7, 3, 0, -5, -5, -10};

    PigeonholeSort::sort(numbers);
    EXPECT_EQ(numbers, expected_asc);

    PigeonholeSort::sort_descending(numbers);
    EXPECT_EQ(numbers, expected_desc);
}

TEST(PigeonholeSortTest, SortRawArray) {
    int arr[] = {8, 3, 2, 7, 4, 6, 8};
    const std::size_t size = 7;

    PigeonholeSort::sort(arr, size);
    EXPECT_EQ(arr[0], 2);
    EXPECT_EQ(arr[1], 3);
    EXPECT_EQ(arr[2], 4);
    EXPECT_EQ(arr[3], 6);
    EXPECT_EQ(arr[4], 7);
    EXPECT_EQ(arr[5], 8);
    EXPECT_EQ(arr[6], 8);

    PigeonholeSort::sort_descending(arr, size);
    EXPECT_EQ(arr[0], 8);
    EXPECT_EQ(arr[1], 8);
    EXPECT_EQ(arr[2], 7);
    EXPECT_EQ(arr[3], 6);
    EXPECT_EQ(arr[4], 4);
    EXPECT_EQ(arr[5], 3);
    EXPECT_EQ(arr[6], 2);

    PigeonholeSort::sort<int>(nullptr, 0);
    PigeonholeSort::sort_descending<int>(nullptr, 0);
}

TEST(PigeonholeSortTest, SortStudentsWithKeyExtractor) {
    std::vector<Student> students = {
        Student(1, "Alice", 85),
        Student(2, "Bob", 70),
        Student(3, "Charlie", 95),
        Student(4, "Diana", 60)
    };

    auto extractor = [](const Student& s) {
        return static_cast<std::int64_t>(s.getRating());
    };

    PigeonholeSort::sort(students, extractor);
    EXPECT_EQ(students[0].getName(), "Diana");
    EXPECT_EQ(students[1].getName(), "Bob");
    EXPECT_EQ(students[2].getName(), "Alice");
    EXPECT_EQ(students[3].getName(), "Charlie");

    PigeonholeSort::sort_descending(students, extractor);
    EXPECT_EQ(students[0].getName(), "Charlie");
    EXPECT_EQ(students[1].getName(), "Alice");
    EXPECT_EQ(students[2].getName(), "Bob");
    EXPECT_EQ(students[3].getName(), "Diana");

    // Также проверка для raw array объектов Student
    Student s_arr[] = { Student(10, "S1", 90), Student(20, "S2", 50) };
    PigeonholeSort::sort(s_arr, 2, extractor);
    EXPECT_EQ(s_arr[0].getRating(), 50);
    EXPECT_EQ(s_arr[1].getRating(), 90);

    PigeonholeSort::sort_descending(s_arr, 2, extractor);
    EXPECT_EQ(s_arr[0].getRating(), 90);
    EXPECT_EQ(s_arr[1].getRating(), 50);
}

TEST(PigeonholeSortTest, RangeLimitExceededThrowsException) {
    std::vector<std::int64_t> huge_range = {0, 60000000LL};
    EXPECT_THROW(PigeonholeSort::sort(huge_range), std::invalid_argument);
    EXPECT_THROW(PigeonholeSort::sort_descending(huge_range), std::invalid_argument);
}
