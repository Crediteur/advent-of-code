import unittest
from seeds import clean_data, get_low_seed

data1 = ["seeds: 10", "50 98 2", "52 50 48"]
data2 = [
    "seeds: 79 14 55 13",
    " ",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    " ",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    " ",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    " ",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    " ",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    " ",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    " ",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]


class TestPartOne(unittest.TestCase):
    def test_clean_data(self):
        seeds1, sections1 = clean_data(data1)
        self.assertEqual(seeds1, [10])
        self.assertEqual(sections1, [[[50, 98, 2], [52, 50, 48]]])

        seeds2, sections2 = clean_data(data2)
        self.assertEqual(seeds2, [79, 14, 55, 13])
        self.assertEqual(len(sections2), 7)  # in total, there should be 7 sections
        self.assertEqual(len(sections2[2]), 4)  # fertilizer-to-map should have 4 maps

    def test_get_low_seed(self):
        seeds1, sections1 = clean_data(data1)
        self.assertEqual(get_low_seed(seeds1, sections1), 10)

        seeds2, sections2 = clean_data(data2)
        self.assertEqual(get_low_seed(seeds2, sections2), 35)


class TestPartTwo(unittest.TestCase):
    def test_seed_length_is_even(self):
        seeds2, sections2 = clean_data(data2)
        self.assertEqual(len(seeds2) % 2, 0)  # seeds length is even
