def read_input():
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.rstrip("\r\n"))
    return data


# part one
def find_numbers(data) -> int:
    sum = 0
    for line in data:
        left = ""
        right = ""

        # first pointer finds first number from left
        for forward in line:
            if forward.isnumeric():
                left = forward
                break

        # second pointer finds first number from right
        for backward in reversed(line):
            if backward.isnumeric():
                right = backward
                break  # can also return early here

        # combine as strings before turning into number
        sum += int(left + right)

    return sum


# dictionary of strings to numbers
str_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# first pointer finds first number from left
def find_left_number(line: str) -> str:
    for i, forward in enumerate(line):
        if forward.isnumeric():
            left = forward
            return left
        # else check strings
        for j in range(3, 6):
            chunk = line[i : i + j]
            if chunk in str_numbers:
                left = str_numbers[chunk]
                return left


# second pointer finds first number from right
# [::-1] returns reversed sequence, reversed() returns reversed iterator only
def find_right_number(line: str) -> str:
    line = line[::-1]
    for i, backward in enumerate(line):
        if backward.isnumeric():
            right = backward
            return right
        # else check right strings by reversing chunk again
        for j in range(3, 6):
            chunk = line[i : i + j][::-1]
            if chunk in str_numbers:
                right = str_numbers[chunk]
                return right


# part two, this was a toughie
def find_string_numbers(data) -> int:
    sum = 0
    for line in data:
        left = ""
        right = ""

        left = find_left_number(line)

        right = find_right_number(line)

        # combine as strings before turning into number
        sum += int(left + right)

    return sum


data = read_input()
print(f"digits sums: {find_numbers(data)}")
print(f"string sums: {find_string_numbers(data)}")
