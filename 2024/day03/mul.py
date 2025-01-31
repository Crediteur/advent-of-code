import re


def read_input():
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.rstrip("\r\n"))
    return "".join(data)


# use regex to find all mul instructions
# in the string form of 'num,num'
def re_find_num(string: str) -> str:
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    matches = re.findall(pattern, string)
    return matches


# part 1
def mul_match(data: str) -> int:
    total = 0

    # use re_find_num func to find all mul instructions
    matches = re_find_num(data)

    for m in matches:
        x, y = m.split(",")
        total += int(x) * int(y)

    return total


# part 2
def mul_match_alter(data: str) -> int:
    total = 0
    mult_enabled = True

    # use regex to find matching all instructions
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, data)

    # parse mul instructions into numbers only
    parsed_matches = []
    for m in matches:
        if m[0] == "m":
            m = re_find_num(m)[0]
        parsed_matches.append(m)

    # sum up mul instructions
    for string in parsed_matches:
        match string:
            case "do()":
                mult_enabled = True
            case "don't()":
                mult_enabled = False
            case _ if mult_enabled:
                x, y = string.split(",")
                total += int(x) * int(y)

    return total


data = read_input()
print(f"total of mul operations: {mul_match(data)}")
print(f"total with alterations: {mul_match_alter(data)}")
