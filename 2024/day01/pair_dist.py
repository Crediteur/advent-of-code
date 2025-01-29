import os


def read_input():
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.rstrip("\r\n"))
    return data


# clean and return data as two lists
def split_data(data):
    left = []
    right = []
    for d in data:
        a, b = d.split()
        left.append(int(a))
        right.append(int(b))
    return [left, right]


# part 1
def total_lowest_distance(data):
    left, right = data
    total = 0

    # sort lists in descending order
    left.sort()
    right.sort()

    # calculate distances
    for i, _ in enumerate(left):
        total += abs(left[i] - right[i])

    return total


# part 2
def similarity_score(data):
    left, right = data
    score = 0
    right_dict = {}

    # populate right into dictionary
    for num in right:
        if num in right_dict:
            right_dict[num] += 1
        else:
            right_dict[num] = 1

    # calculate similarity score by checking key in dictionary
    for n in left:
        if n in right_dict:
            score += n * right_dict[n]

    return score


data = split_data(read_input())
print(f"total lowest distance of lists: {total_lowest_distance(data)}")
print(f"similarity score: {similarity_score(data)}")
