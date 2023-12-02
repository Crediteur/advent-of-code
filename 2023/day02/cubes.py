def read_input():
    with open("input.txt", "r") as file:
        data = file.read()
    return data.split("\n")


# helper that cleans the str of each line
# returns id of the game and cubes and colours of each game, ignoring round
def parse_line(line) -> list[int, list[int, int]]:
    line = line.split(":")
    id = int(line[0].split(" ")[-1])  # get id of game

    pulls = line[1].replace(";", ",").split(",")  # get list of cube pulls
    pulls = [p.strip().split(" ") for p in pulls]  # clean string
    for pull in pulls:
        pull[0] = int(pull[0])

    return [id, pulls]


# part one
# bag only contains 12 red cubes, 13 green cubes, and 14 blue cubes
def possible_cubes(data) -> int:
    bag = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for line in data:
        possible = True  # flag to allow summation

        id, pulls = parse_line(line)

        # check cubes and colour of every pull
        for pull in pulls:
            cubes, colour = pull
            if bag[colour] < cubes:  # check if each pull is possible
                possible = False

        if possible:  # if possible, add game id to sum
            sum += id
    return sum


# part two
# find the max occurence of each colour and sum the powers
def power_cubes(data) -> int:
    sum = 0
    for line in data:
        # initilize empty bag
        max_bag = {"red": -1, "green": -1, "blue": -1}

        _, pulls = parse_line(line)

        # check if cubes is greater than in the bag
        for pull in pulls:
            cubes, colour = pull
            if max_bag[colour] < cubes:
                max_bag[colour] = cubes

        # sum the power of each colour in bag
        power_cubes = 1
        for cubes in max_bag.values():
            power_cubes *= cubes
        sum += power_cubes

    return sum


data = read_input()
print(f"id sum of possible games: {possible_cubes(data)}")
print(f"power sum of fewest cubes: {power_cubes(data)}")
