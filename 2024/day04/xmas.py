def read_input():
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.rstrip("\r\n"))
    return data


# part 1
def find_xmas(data: list[list[str]]) -> int:
    total = 0
    height = len(data)
    length = len(data[0])

    # (y,x) or (row,col), top left to bottom right: 1-8 directions
    matrix = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    letters = ["M", "A", "S"]

    xmas_x = []
    xmas_m = []

    # find all X's
    for i, r in enumerate(data):  # row
        for j, c in enumerate(r):  # col
            if c == "X":
                xmas_x.append((i, j))

    # search: record the direction and position of M
    for i, j in xmas_x:
        for m_i, coord in enumerate(matrix):
            y, x = coord
            i_y = i + y
            j_x = j + x
            if i_y >= 0 and i_y < height and j_x >= 0 and j_x < length:
                if data[i_y][j_x] == "M":
                    xmas_m.append((i, j, m_i))

    # check validity of letters
    for i, j, m_i in xmas_m:
        y, x = matrix[m_i]
        i_y = i + y
        j_x = j + x
        letter_match = 0

        for l in letters:
            if i_y >= 0 and i_y < height and j_x >= 0 and j_x < length:
                if data[i_y][j_x] == l:
                    # increment i_y and j_x
                    i_y += y
                    j_x += x
                    letter_match += 1
            else:
                break

        if letter_match == 3:
            total += 1

    return total


# part 2
def find_x_mas(data: list[list[str]]) -> int:
    total = 0
    height = len(data)
    length = len(data[0])

    # matrix to check corners only
    matrix = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    xmas_a = []

    # find all A's
    for i, r in enumerate(data):  # row
        for j, c in enumerate(r):  # col
            # skip letters on the perimeter
            if i > 0 and i < height - 1 and j > 0 and j < length - 1:
                if c == "A":
                    xmas_a.append((i, j))

    # check for X-shaped cross originating from the A
    for i, j in xmas_a:
        s_count = 0
        m_count = 0
        pos = []
        for y, x in matrix:
            i_y = i + y
            j_x = j + x
            pos.append((i_y, j_x))
            if data[i_y][j_x] == "S":
                s_count += 1
            elif data[i_y][j_x] == "M":
                m_count += 1

        # make sure diag letters are NOT the same
        letter_top = data[pos[0][0]][pos[0][1]]
        letter_bot = data[pos[3][0]][pos[3][1]]

        if s_count == 2 and m_count == 2 and letter_top != letter_bot:
            total += 1

    return total


data = read_input()
print(f"total XMAS: {find_xmas(data)}")
print(f"total X-MAS: {find_x_mas(data)}")
