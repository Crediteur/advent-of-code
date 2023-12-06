import unittest
from race import organize_data, power_sum_metrics, sum_long_race

data1 = ["Time:      7  15   30", "Distance:  9  40  200"]


class TestPartOne(unittest.TestCase):
    def test_organize_data(self):
        t, r = organize_data(data1)
        self.assertEqual(len(t), 3)
        self.assertEqual(len(r), 3)
        self.assertEqual(t, ["7", "15", "30"])
        self.assertEqual(r, ["9", "40", "200"])

    def test_power_metrics(self):
        t, r = organize_data(data1)
        total = power_sum_metrics(t, r)
        self.assertEqual(total, 288)


class TestPartTwo(unittest.TestCase):
    def test_long_race(self):
        t, r = organize_data(data1)
        self.assertEqual(sum_long_race(t, r), 71503)
