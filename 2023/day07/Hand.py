class Hand:
    """
    object for storing each camelcards hand
    part two functionality enabled by passing part=2
    """

    def __init__(self, cards="", bid=-1):
        self.cards = cards  # "AAA32"
        self.type = ""  # 1-7, "triple"
        self.rank = -1  # global position
        self.bid = bid  # 321
        self.order = ""  # "MMMBA"
        # custom mapping of cards

    def setOrder(self, part=1):
        """
        create custom mapping of cards
        (easier to sort in one go)
        """
        order_map = {
            "2": "A",
            "3": "B",
            "4": "C",
            "5": "D",
            "6": "E",
            "7": "F",
            "8": "G",
            "9": "H",
            "T": "I",
            "J": "J",
            "Q": "K",
            "K": "L",
            "A": "M",
        }
        order_map_p2 = {
            "J": "A",
            "2": "B",
            "3": "C",
            "4": "D",
            "5": "E",
            "6": "F",
            "7": "G",
            "8": "H",
            "9": "I",
            "T": "J",
            "Q": "K",
            "K": "L",
            "A": "M",
        }
        new_order = ""
        for c in self.cards:
            if part == 1:
                new_order += order_map[c]
            else:
                new_order += order_map_p2[c]
        self.order = new_order

    def setType(self, part=1):
        """
        hash card counts and map to a hand type
        part two considers the joker wildcard
        """
        types_map = {
            "5": "7-five",
            "14": "6-four",
            "23": "5-house",
            "113": "4-triple",
            "122": "3-twopair",
            "1112": "2-onepair",
            "11111": "1-high",
        }

        # count cards
        count_map = {}
        joker = 0
        for card in self.cards:
            if card == "J":
                joker += 1
            if card not in count_map:
                count_map[card] = 0
            count_map[card] += 1

        # create string key
        count_list = sorted(count_map.values())
        count_str = "".join(map(str, count_list))

        if part == 2 and 0 < joker < 5:
            joker_type = self.caseJoker(count_str, joker)
            count_str = joker_type

        self.type = types_map[count_str]

    # part 2
    def caseJoker(self, count_str, joker):
        """
        case match hand type and
        upgrade type based on joker count_str
        """
        match count_str:
            case "14" | "23":
                return "5"
            case "113":
                return "14"
            case "122":
                match joker:
                    case 1:
                        return "23"
                    case 2:
                        return "14"
            case "1112":
                return "113"
            case "11111":
                return "1112"
            case _:
                return count_str
