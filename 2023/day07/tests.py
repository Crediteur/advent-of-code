import unittest

from Hand import Hand
from camelcards import parse_data, create_hands, sum_bids, sort_hands

str1 = ["AAAKK 222"]
data1 = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]


class TestPartOne(unittest.TestCase):
    def test_parse_data(self):
        h, b = parse_data(str1)[0]
        self.assertEqual(h, "AAAKK")
        self.assertEqual(b, 222)

    def test_Hand_class(self):
        h, b = parse_data(str1)[0]
        hand = Hand(cards=h, bid=b)
        hand.setOrder()
        hand.setType()
        self.assertEqual(hand.cards, "AAAKK")
        self.assertEqual(hand.bid, 222)
        self.assertEqual(hand.order, "MMMLL")
        self.assertEqual(hand.type, "5-house")

    def test_create_hands(self):
        data = create_hands(parse_data(data1))
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0].cards, "32T3K")
        self.assertEqual(data[0].bid, 765)
        self.assertEqual(data[0].order, "BAIBL")
        self.assertEqual(data[0].type, "2-onepair")

    def test_sum_bids(self):
        sorted_data = sort_hands(create_hands(parse_data(data1)))
        self.assertEqual(len(sorted_data), 5)
        self.assertTrue(sorted_data[0].type < sorted_data[1].type)
        self.assertTrue(sorted_data[0].rank < sorted_data[1].rank)
        self.assertTrue(sorted_data[0].order < sorted_data[1].order)

    def test_sort_hands(self):
        total = sum_bids(sort_hands(create_hands(parse_data(data1))))
        self.assertEqual(total, 6440)


class TestPartTwo(unittest.TestCase):
    def test_Hands_p2(self):
        data_p2 = create_hands(parse_data(data1), part=2)
        self.assertEqual(data_p2[4].order, "KKKAM")
        self.assertEqual(data_p2[4].type, "6-four")
        self.assertEqual(data_p2[4].caseJoker("1112", 1), "113")

    def test_sum_bids_p2(self):
        sorted_data_p2 = sort_hands(create_hands(parse_data(data1), part=2))
        total = sum_bids(sorted_data_p2)
        self.assertEqual(total, 5905)
