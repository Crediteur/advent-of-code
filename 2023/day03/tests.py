import unittest
from gear import find_symbols, parse_number, find_numbers, find_gears


class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.str1 = ["....$...%...4...823/..."]
        self.str2 = "abc342bca"
        self.str3 = "###00002"
        self.data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]

    def test_find_symbols(self):
        self.assertEqual(find_symbols(self.str1), {"$", "%", "/"})
        self.assertEqual(len(find_symbols(self.str1)), 3)

    def test_parse_number(self):
        self.assertEqual(parse_number(self.str2, 3), (342, "abc...bca"))
        self.assertEqual(parse_number(self.str2, 5), (342, "abc...bca"))
        self.assertEqual(parse_number(self.str3, 3), (2, "###....."))
        self.assertEqual(parse_number(self.str3, 7), (2, "###....."))

    def test_find_number(self):
        self.assertEqual(find_numbers(self.data, find_symbols(self.data)), 4361)


class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]

    def test_find_gears(self):
        self.assertEqual(find_gears(self.data), 467835)
