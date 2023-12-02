import unittest
from cubes import parse_line, possible_cubes, power_cubes

str1 = "Game 1: 3 blue, 4 red"
data1 = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


class TestPartOne(unittest.TestCase):
    # str1 id
    def test_parse_line_id(self):
        actual = parse_line(str1)[0]
        expected = 1
        self.assertEqual(actual, expected)

    # str1 cubes and colours
    def test_parse_line_cube_colours(self):
        actual = parse_line(str1)[1]
        expected = [["3", "blue"], ["4", "red"]]
        self.assertEqual(actual, expected)

    # data1
    def test_possible_cubes(self):
        actual = possible_cubes(data1)
        expected = 8
        self.assertEqual(actual, expected)


class TestPartTwo(unittest.TestCase):
    # data1
    def test_power_cubes(self):
        actual = power_cubes(data1)
        expected = 2286
        self.assertEqual(actual, expected)
