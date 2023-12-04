def read_input():
    with open("input.txt", "r") as file:
        data = file.read()
    return data.split("\n")


def parse_line(line) -> tuple[list[int], list[int]]:
    """
    separates the winning numbers from the picked numbers
    """
    split_line = line.replace(":", "|").split("|")
    # id = split_line[0][-1]
    win_n = [int(n) for n in split_line[1].strip().split(" ") if n]
    lot_n = [int(n) for n in split_line[2].strip().split(" ") if n]

    return win_n, lot_n


# part one
def sum_points(data) -> int:
    """
    sums total points of every matching number
    """

    total = 0
    for line in data:
        matches = 0
        win_n, lot_n = parse_line(line)

        for n in win_n:
            for m in lot_n:
                if n == m:
                    matches += 1

        if matches > 0:
            total += 2 ** (matches - 1)

    return int(total)


# part two
def sum_cards(data) -> int:
    """
    additively tracks card count if winnings propagate into more cards
    """

    # use an array to track the state of each card
    N = len(data)
    cards = [1] * N

    for i in range(N):
        matches = 0
        win_n, lot_n = parse_line(data[i])

        for n in win_n:
            for m in lot_n:
                if n == m:
                    matches += 1

        # increase card count for next m matches
        # multiplied by number of current cards
        if matches > 0:
            for m in range(matches):
                cards[i + m + 1] += 1 * cards[i]

    card_sum = sum(cards)
    return card_sum


if __name__ == "__main__":
    data = read_input()
    print(f"total poinits: {sum_points(data)}")
    print(f"total cards: {sum_cards(data)}")
