from Hand import Hand


def read_input():
    with open("input.txt", "r") as file:
        data = file.read()
    return data.split("\n")


def parse_data(data):
    """
    return a list of tuples containing
    the string cards and int bid
    """
    parsed = [(h, int(b)) for h, b in [d.split() for d in data]]
    return parsed


def create_hands(data, part=1):
    """
    create and populate a bunch of Hand objects
    sets Hand.card, Hand.bid, Hand.order, Hand.type
    returns a list of created Hands
    """
    hands = []
    for h, b in data:
        hand = Hand(cards=h, bid=b)
        hand.setOrder(part=part)
        hand.setType(part=part)
        hands.append(hand)

    return hands


def sort_hands(hands):
    """
    order by type then order by cards
    also update global rank
    """
    # beefy sort
    sorted_hands = sorted(hands, key=lambda h: (h.type, h.order))

    # update hand rank
    for i in range(1, len(sorted_hands) + 1):
        sorted_hands[i - 1].rank = i

    return sorted_hands


# part one
def sum_bids(hands):
    """
    sum bids multiplied by rank
    """
    total = 0
    for h in hands:
        total += h.rank * h.bid

    return total


if __name__ == "__main__":
    data = parse_data(read_input())
    sorted_hands = sort_hands(create_hands(data))
    print(f"ranked bid of every hand: {sum_bids(sorted_hands)}")
    sorted_hands = sort_hands(create_hands(data, part=2))
    print(f"ranked bid of joker as wildcards: {sum_bids(sorted_hands)}")

# p1 setup pseudo:
# put each hand into its own object
# put each hande in a dict and count the number of matching cards to find strength,
#   give each hand a strength class label
# in each strength class, organize by highest card,
#   and give a rank number to each hand based on global hand position
#   find an easier hack to represent card order?
# finally sum total by multiplying hand rank by bid
