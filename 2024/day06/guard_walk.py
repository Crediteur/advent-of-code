import copy


def read_input():
    data = []
    # separate data
    with open("input.txt") as file:
        for line in file:
            data.append(line.rstrip("\r\n"))

    return data


# check given position (x,y) indices is
# within given dimensions (len(height), len(length))
def within_bounds(pos, dimensions) -> bool:
    pos_y, pos_x = pos
    height, length = dimensions  # len() function number
    contained = False

    if pos_y >= 0 and pos_y < height and pos_x >= 0 and pos_x < length:
        contained = True

    return contained


# part 1 and pt2
# note: pos(x,y) is the starting location of the guard
#       and next(x,y) is the position being incremented to track steps
def walk_guard_path(data) -> int:
    height = len(data)
    length = len(data[0])
    print(height, length)

    spaces = set()  # all unique spaces
    spaces_d = set()  # all unique spaces with direction
    blocks = set()  # all unique blocks placed

    pos = (0, 0)
    #       up,      right,  down,   left
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_i = 0

    # find starting guard position
    for i, r in enumerate(data):
        for j, c in enumerate(r):
            if c == "^":
                pos = (i, j)

    # add starting position to set
    pos_y, pos_x = pos
    spaces.add((pos_y, pos_x))

    # get direction and calculate next position
    dir_y, dir_x = dir[dir_i]
    next_y = pos_y + dir_y
    next_x = pos_x + dir_x

    # walk direction while within bounds
    while within_bounds((next_y, next_x), (height, length)):

        # check if next step is a . or #
        if data[next_y][next_x] == "#":
            # reset dir_i to 0 or increment dir_i
            dir_i += 1
            if dir_i == 4:
                dir_i = 0

            next_y -= dir_y
            next_x -= dir_x
            dir_y, dir_x = dir[dir_i]

            # print(f"dir change to {dir[dir_i]}")  # debug

        # increment position (next_y, next_x) and record to sets
        else:

            # pt2 (original function condensed here)
            # place a block at every location and check if new matrix contains a loop
            if (next_y, next_x) != pos and (next_y, next_x) not in blocks:
                mod_data = copy.deepcopy(data)
                temp_row = list(mod_data[next_y])
                temp_row[next_x] = "#"
                mod_data[next_y] = "".join(temp_row)
                # inefficency: can improve speed by updating new pos
                if contains_loop(mod_data, pos):
                    blocks.add((next_y, next_x))
                    # print(f"block placed at: {next_y, next_x}")  # debug

            spaces_d.add((next_y, next_x, dir_i))
            spaces.add((next_y, next_x))

        # increment next spot to check
        next_y += dir_y
        next_x += dir_x

    # return set of answers for p1 and p2
    return (len(spaces), len(blocks))


# helper function for p2
# checks a modifed version of the input matrix for loops
# same as p1, except with modified data matrix
# returns True/False early if loop is found
def contains_loop(mod_data, start_pos, dir_i=0) -> bool:
    has_loop = False

    height = len(mod_data)
    length = len(mod_data[0])

    spaces_d = set()

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    pos_y, pos_x = start_pos
    spaces_d.add((pos_y, pos_x, dir_i))

    dir_y, dir_x = dir[dir_i]
    next_y = pos_y + dir_y
    next_x = pos_x + dir_x

    while within_bounds((next_y, next_x), (height, length)):

        if mod_data[next_y][next_x] == "#":
            # reset dir_i to 0 or increment dir_i
            dir_i += 1
            if dir_i == 4:
                dir_i = 0

            next_y -= dir_y
            next_x -= dir_x
            dir_y, dir_x = dir[dir_i]

        else:
            if (next_y, next_x, dir_i) in spaces_d:
                return True
            spaces_d.add((next_y, next_x, dir_i))

        next_y += dir_y
        next_x += dir_x

    return has_loop


# part 2 notes:
# brute force approach, place block at every step and see if new data contains a loop
# change from intial approach: there can be blocks placed that formed closed loops on its own

# initial failed approach to p2:
# record all traversed positions with direction
# if walking over same space with next sequencial direction,
# can form a loop by placing an obstruction
# every step: check linear path of next dir to see if loop can be made
#    case 1: (pos, next_dir) exists in traversed spaces
#    case 2: check possible spaces in perpendicular next direction
#    note: found that case 2 includes case 1, therefore only case 2 was necessary


data = read_input()
print(f"total unique spaces traversed: {walk_guard_path(data)[0]}")
print(f"number of obstructions that form a loop: {walk_guard_path(data)[1]}")
