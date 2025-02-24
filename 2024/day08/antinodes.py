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


# p1
# count each character into a dictionary with it's (y,x) coordinates
# go through each entry and calculate each coordinate pair with another
# to find the antinode on BOTH ends, check if these nodes are within bounds
#   valid antinodes can occur once at any unique location within bounds
# add valid antinode coordinates into a set, and count the set
# p2
# repeat rise/run addition while coordinates are still inbounds
def count_antinode(data) -> int:
    height, length = len(data), len(data[0])
    antennas = {}
    locations = set()
    cascaded_locations = set()

    # count unique chars into antennas
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char != ".":
                # count coordinates under their respective symbols
                if char in antennas:
                    antennas[char].append((y, x))
                else:
                    antennas[char] = [(y, x)]

    # create unique antinodes based on pairing locations
    for key, coord_list in antennas.items():
        # print(f"cycling antenna: {key}")
        unique_set = set()

        # compare each coordinate with each other
        for pair1 in coord_list:
            for pair2 in coord_list[1:]:
                # inefficincy: duplicate pair1/pair2 comparisons still occur here
                # maybe can be resolved by sorting the pairs in a set first
                if pair1 == pair2:
                    continue
                # create new antinode pairs
                new_pair1 = list(pair1)
                new_pair2 = list(pair2)
                y1, x1 = pair1
                y2, x2 = pair2
                # run/rise difference
                y_d = y2 - y1
                x_d = x2 - x1

                # calculate possible coordinates by adding diff
                new_pair1[0] -= y_d
                new_pair1[1] -= x_d
                new_pair2[0] += y_d
                new_pair2[1] += x_d

                # check new pairs are within bounds
                if within_bounds(new_pair1, (height, length)):
                    locations.add(tuple(new_pair1))
                    cascaded_locations.add(tuple(new_pair1))

                if within_bounds(new_pair2, (height, length)):
                    locations.add(tuple(new_pair2))
                    cascaded_locations.add(tuple(new_pair2))

                # p2
                # each pair of antennas are antinodes themselves
                # including ones from p1 and cascading ones outward
                cascaded_locations.add(pair1)
                cascaded_locations.add(pair2)
                cascade_pair1 = list(new_pair1)
                cascade_pair2 = list(new_pair2)

                # repeat coordinate addition from p1 in a loop
                while within_bounds(cascade_pair1, (height, length)) or within_bounds(
                    cascade_pair2, (height, length)
                ):
                    cascade_pair1[0] -= y_d
                    cascade_pair1[1] -= x_d
                    cascade_pair2[0] += y_d
                    cascade_pair2[1] += x_d

                    # check new pairs are within bounds
                    if within_bounds(cascade_pair1, (height, length)):
                        cascaded_locations.add(tuple(cascade_pair1))
                    if within_bounds(cascade_pair2, (height, length)):
                        cascaded_locations.add(tuple(cascade_pair2))

    return (len(locations), len(cascaded_locations))


data = read_input()
p1, p2 = count_antinode(data)
print(f"total unique antinode locations: {p1}")
print(f"total unique cascaded antinode locations: {p2}")
