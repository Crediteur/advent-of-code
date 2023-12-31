from multiprocessing import Process, Queue


def read_input():
    with open("input.txt", "r") as file:
        data = file.read()
    return data.split("\n")


def clean_data(data) -> tuple[list[int], list[list[int]]]:
    """
    parse each line in data
    get seed numbers from first line,
    get subsequent mappings from lines that start with a number
    """
    seeds = [int(s) for s in data[0].split()[1:]]

    sections = []
    maps = []
    for line in data[1:]:
        if line and line[0].isnumeric():
            maps.append([int(l) for l in line.split()])
        if line and line[0].isalpha() and maps:
            sections.append(maps)
            maps = []
    sections.append(maps)

    return seeds, sections


# part one
# pseudocode:
# for each seed:
#   for each section:
#       for each map:
#           if source < seed < source+range:
#               seed_map = seed - source + destination
#               break out of seciton
# seed_map.append(results)
def get_low_seed(seeds, sections) -> int:
    seed_maps = []
    for seed in seeds:
        for section in sections:
            for map in section:
                dest = map[0]  # map to
                srce = map[1]  # map from
                rnge = map[2]  # range of map to
                if srce <= seed <= srce + rnge - 1:
                    seed = seed - srce + dest
                    break
        seed_maps.append(seed)

    # print(seed_maps)
    return min(seed_maps)


# # part two
# def get_range_low_seed(seeds, sections) -> int:
#     table = {}
#     min_seed = float("inf")
#     for i in range(1, len(seeds), 2):
#         seed_start = seeds[i - 1]
#         seed_range = seeds[i]
#         for seed in range(seed_start, seed_start + seed_range):
#             if seed in table:
#                 continue
#             seed_initial = seed
#             for section in sections:
#                 for map in section:
#                     dest = map[0]  # map to
#                     srce = map[1]  # map from
#                     rnge = map[2]  # range of map to
#                     if srce <= seed <= srce + rnge - 1:
#                         seed = seed - srce + dest
#                         break
#             # cache results
#             table[seed_initial] = seed
#             if seed < min_seed:
#                 min_seed = seed
#     print(len(table))
#     print(min_seed)
#     return min_seed


# part two
def get_range_low_seed(seeds, sections) -> int:
    """
    reverse look up
    """
    # make seed ranges
    seed_ranges = [
        (seeds[i - 1], seeds[i] + seeds[i - 1]) for i in range(1, len(seeds), 2)
    ]

    max_seed = max(seed_ranges)[1]

    # map integer in reverse
    for i in range(max_seed):
        num = i
        for section in reversed(sections):
            for map in section:
                dest = map[0]  # map to
                srce = map[1]  # map from
                rnge = map[2]  # range of map to
                if dest <= num <= dest + rnge - 1:
                    num = num - dest + srce
                    break

            # print(i, num)  # i = location, num = seed

        # first number in a seed range, must be lowest
        for seed_range in seed_ranges:
            s, e = seed_range
            if num in range(s, e):
                print(f"found at: {i, num}")  # i = location, num = seed
                return i

    return -1


# split the seed ranges into more possible ranges through each transformation
# ie. if a map range splits a seed range, there is now an extra range for this seed
# return the range of the transformed ranges,
#   which are NOT the possible initial seeds, so we have to feed the number back to find the seed
# check the lowest number(s) in the smallest seed range (feed the range through part 1/2)

data2 = [
    "seeds: 79 14 55 13",
    " ",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    " ",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    " ",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    " ",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    " ",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    " ",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    " ",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]


if __name__ == "__main__":
    """
    assumptions: all seeds are mappable in each section
    """
    data = read_input()
    seeds, sections = clean_data(data)
    # print(f"lowest seed: {get_low_seed(seeds, sections)}")
    print(f"lowest range seed: {get_range_low_seed(seeds, sections)}")
