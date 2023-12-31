def read_input():
    with open("input.txt", "r") as file:
        data = file.read()
    return data.split("\n")


def parse_data(data):
    seq = data[0]
    map_data = data[2:]

    # slice and append each mapping into a dictionary
    map = {}
    for node in map_data:
        node_data = node.split("=")
        map_key = node_data[0].strip()
        map_val = (node_data[1].strip()[1:4], node_data[1].strip()[6:9])
        map[map_key] = map_val

    return seq, map


# part 1
# start at "AAA", traverse network to find 'ZZZ'
def walk_network(seq, map) -> int:
    direction = {"L": 0, "R": 1}

    count = 0
    seq_key = "AAA"  # start
    seq_ind = 0  # iterate through indices

    while True:
        # check if key at end
        if seq_key == "ZZZ":
            break

        # next key is determined by direction index
        dir_index = direction[seq[seq_ind]]  # map 'L' or 'R' to 0 or 1
        seq_key = map[seq_key][dir_index]  # update new key

        # iterate through each char index or reset to 0
        seq_ind += 1
        if seq_ind == len(seq):
            seq_ind = 0

        # count number of loops
        count += 1

    return count


# find all nodes that end with the letter 'A'
def get_starting_nodes(map) -> list[str]:
    starting_nodes = []
    for node in map:
        if node[2] == "A":
            starting_nodes.append(node)

    return starting_nodes


# return True only if all nodes end in 'Z'
def all_nodes_ended(nodes) -> bool:
    for node in nodes:
        if node[2] != "Z":
            return False
    return True


# part 2
# get list of all nodes that end with 'A'
# make a copy/mutate this list of nodes and walk them based on the sequence
# end when all nodes end with 'Z'
# count number of loops required


# only check all nodes when single node ended in 'Z'?
# find repeating count of each node loop and calculate LCM
def spooky_walk(seq, map, starting_nodes) -> int:
    direction = {"L": 0, "R": 1}

    count = 0
    seq_ind = 0

    N = len(starting_nodes)

    while True:
        if all_nodes_ended(starting_nodes):
            break

        # debug
        # print(f"{starting_nodes}, {seq_ind}, {seq[seq_ind]}")

        # walk each node in starting list
        for i in range(N):
            starting_nodes[i] = map[starting_nodes[i]][direction[seq[seq_ind]]]

        # iterate through each char index or reset to 0
        seq_ind += 1
        if seq_ind == len(seq):
            seq_ind = 0

        # count number of loops
        count += 1

    print(count)
    print(starting_nodes)
    return count


seq, map = parse_data(read_input())
# print(walk_network(seq, map))
print(spooky_walk(seq, map, get_starting_nodes(map)))
