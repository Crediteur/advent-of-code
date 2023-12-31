import unittest
from scratchcards import parse_line, sum_points, sum_cards

data = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.str1 = "Card   2: 15 53  2 |  4 15 98"
        self.data1 = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"]

    def test_parse_line(self):
        self.assertEqual(len(parse_line(self.str1)), 2)
        self.assertEqual(parse_line(self.str1), ([15, 53, 2], [4, 15, 98]))

    def test_sum_points(self):
        self.assertEqual(sum_points(self.data1), 8)
        self.assertEqual(sum_points(data), 13)


class TestPartOne(unittest.TestCase):
    def test_sum_cards(self):
        self.assertEqual(sum_cards(data), 30)
