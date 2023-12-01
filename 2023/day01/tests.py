import unittest
from trebuchet import (
    find_numbers,
    find_string_numbers,
    find_left_number,
    find_right_number,
)

# part 1
str1 = ["potato2apple3pineapple"]
data1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

# part 2
str2 = ["sevenine"]
data2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


class TestPartOne(unittest.TestCase):
    # "potato2apple3pineapple"
    def test_simple_string_with_digits(self):
        actual = find_numbers(str1)
        expected = 23
        self.assertEqual(actual, expected)

    # data1
    def test_longer_string_data(self):
        actual = find_numbers(data1)
        expected = 142  # 12+38+15+77
        self.assertEqual(actual, expected)


class TestPartTwo(unittest.TestCase):
    # "potato2apple3pineapple"
    def test_simple_left_digit(self):
        actual = find_left_number(str1[0])
        expected = "2"
        self.assertEqual(actual, expected)

    def test_simple_right_digit(self):
        actual = find_right_number(str1[0])
        expected = "3"
        self.assertEqual(actual, expected)

    # "sevenine"
    def test_simple_left_number(self):
        actual = find_left_number(str2[0])
        expected = "7"
        self.assertEqual(actual, expected)

    def test_simple_right_number(self):
        actual = find_right_number(str2[0])
        expected = "9"
        self.assertEqual(actual, expected)

    def test_simple_string_numbers(self):
        actual = find_string_numbers(str2)
        expected = 79
        self.assertEqual(actual, expected)

    # data2
    def test_simple_string_numbers(self):
        actual = find_string_numbers(data2)
        expected = 281
        self.assertEqual(actual, expected)
