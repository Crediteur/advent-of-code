def read_input():
    with open("input.txt", "r") as file:
        data = file.read()
    return data.split("\n")


def find_symbols(data) -> set[str]:
    """
    find the set of unique symbols in input
    """
    s = set()
    for line in data:
        for char in line:
            if not char.isnumeric() and char != ".":
                s.add(char)
    # print(f"unique symbols: {s}")
    return s


# takes the row (string) and index (int) of a number
def parse_number(chunk: str, x_pos: int) -> int:
    """
    finds the whole number given one index position in a string
    checks left and right of given index for more digits
    """

    # track char nums in an array for easier appends
    num_chars = [chunk[x_pos]]

    # check left side of pos for numbers
    left = x_pos - 1
    while left >= 0 and chunk[left].isnumeric():
        num_chars.insert(0, chunk[left])
        left -= 1

    # check right side of pos for numbers
    right = x_pos + 1
    while right < len(chunk) and chunk[right].isnumeric():
        num_chars.append(chunk[right])
        right += 1

    # replace found numbers with "."
    new_chunk = chunk[: left + 1] + (right - (left + 1)) * "." + chunk[right:]
    # print(f"old chunk: {chunk}")
    # print(f"new chunk: {new_chunk}")

    num = int("".join(num_chars))
    return num, new_chunk


# part one
# rough pseudocode:
# iterate to each character
# if symbol, look at adjacent indices in 2d grid
#   (append empty row to start and end to reduce vertical bounds checking)
# if char is a number, look forward and backward of index to parse number
# sum number and replace number with dot "."
def find_numbers(data, symbols: set[str]) -> int:
    """
    sum numbers found adjacent to symbols
    note: function mutates data
    """

    # positions of indices to search
    matrix = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

    # add extra rows at start and end for out of bounds buffer
    N = len(data[0])
    data.insert(0, "." * N)
    data.append("." * N)

    total = 0
    for i in range(1, len(data) - 1):
        # get a chunk of three sequential rows
        chunk = [data[i - 1], data[i], data[i + 1]]
        for j in range(N):
            char = chunk[1][j]
            if char in symbols:
                # check surrounding tiles for numbers
                for pos in matrix:
                    y, x = pos
                    if 0 <= j + x < N and chunk[1 + y][j + x].isnumeric():
                        # single digit found, extract whole number
                        num, new_chunk = parse_number(chunk[1 + y], j + x)
                        chunk[1 + y] = new_chunk
                        total += num

        # update data with parsed chunks
        # chunk needs to be updated every functional reference, because it is pass by value
        data[i - 1] = chunk[0]
        data[i] = chunk[1]
        data[i + 1] = chunk[2]

    # for row in data:
    #     print(row)
    return total


# part two
def find_gears(data):
    """
    sum powers of exactly two numbers adjacent to "*" symbol
    note: function mutates data
    """

    matrix = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    N = len(data[0])
    data.insert(0, "." * N)
    data.append("." * N)

    total = 0
    for i in range(1, len(data) - 1):
        # get a chunk of three sequential rows
        chunk = [data[i - 1], data[i], data[i + 1]]
        for j in range(N):
            char = chunk[1][j]
            if char == "*":
                # track part numbers found
                parts = []
                # check surrounding tiles for numbers
                for pos in matrix:
                    y, x = pos
                    if 0 <= j + x < N and chunk[1 + y][j + x].isnumeric():
                        num, new_chunk = parse_number(chunk[1 + y], j + x)
                        chunk[1 + y] = new_chunk
                        parts.append(num)
                # only sum if exactly two parts are found
                if len(parts) == 2:
                    total += parts[0] * parts[1]

        # update data with parsed chunks
        data[i - 1] = chunk[0]
        data[i] = chunk[1]
        data[i + 1] = chunk[2]

    return total


if __name__ == "__main__":
    data = read_input()
    symbols = find_symbols(data)
    print(f"sum adjacent to symbols: {find_numbers(data, symbols)}")
    data = read_input()
    print(f"sum of gear ratios: {find_gears(data)}")
