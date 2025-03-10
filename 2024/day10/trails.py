def read_input():
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.rstrip("\r\n"))

    return data


# check given position (y,x): check indices are
# within given dimensions (len(height), len(length))
def within_bounds(pos, dimensions) -> bool:
    pos_y, pos_x = pos
    height, length = dimensions
    contained = False

    if pos_y >= 0 and pos_y < height and pos_x >= 0 and pos_x < length:
        contained = True

    return contained


# p1 and p2
# find all starting location 0s
# check four directions to see if next number in sequence and within bounds
# incrementally check for next height number and append positions into a list
# finish loop at 9, count all unique positions
def walk_trails(data) -> dict[int, int]:
    H, L = len(data), len(data[0])
    starting_spots = []

    # find 0s
    for y, row in enumerate(data):
        for x, num in enumerate(row):
            if num == "0":
                starting_spots.append((y, x))

    #                up     right   down    left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    spots = [[] for _ in range(len(starting_spots))]

    # iterate through all starting spots and check cardinal directions
    # for viable incremental trail heights

    for i, pos in enumerate(starting_spots):
        spots[i].append(pos)
        trail_h = 1

        # 9 heights
        while trail_h < 10:
            new_spots = []
            # iterate through each updated list heights
            for y, x in spots[i]:
                # check each direction
                for d_y, d_x in directions:
                    y2 = y + d_y
                    x2 = x + d_x
                    # check pos is within bounds and next sequential num is correct
                    if within_bounds((y2, x2), (H, L)) and data[y2][x2] == str(trail_h):
                        new_spots.append((y2, x2))

                # mutate list to pos of new trail heights each itr
                spots[i] = new_spots
            trail_h += 1

    # sum total of each unique ending pos for each trail head
    score = 0
    rating = 0
    for endings in spots:
        score += len(set(endings))
        rating += len(endings)

    return {"score": score, "rating": rating}


data = read_input()
print(f"sum of unique hiking trail start/end spots: {walk_trails(data)['score']}")
print(f"sum of all different hiking trail paths: {walk_trails(data)['rating']}")
