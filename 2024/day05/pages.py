def read_input():
    rules = []
    updates = []

    # separate data
    with open("input.txt") as file:
        for line in file:
            if "|" in line:
                rules.append(line.rstrip("\r\n").split("|"))
            elif "," in line:
                updates.append(line.rstrip("\r\n").split(","))

        rules = [[int(r) for r in rule] for rule in rules]
        updates = [[int(u) for u in update] for update in updates]

    return [rules, updates]


# part 1
# separates rules, correct update data, and incorrect update data
def ordering_rules(data: list[list[int], list[int]]) -> list[int, list[int]]:
    rules = data[0]
    updates = data[1]
    incorrect = []
    total = 0

    for update in updates:
        correct = True
        for rule in rules:
            # check rules are applicable in the update
            a = rule[0]
            b = rule[1]
            if a in update and b in update:
                # check indices for the two numbers
                a_i = update.index(a)
                b_i = update.index(b)
                if not a_i < b_i:
                    incorrect.append(update)
                    correct = False
                    break

        if correct:
            # get the middle index and number
            m_i = len(update) // 2
            total += update[m_i]

    return [total, incorrect]


# part 2
def incorrect_updates(data, incorrect) -> int:
    rules = data[0]
    total = 0
    swap = True
    cycles = 0

    # repeat swapping until no swaps are made, inefficient
    while swap is True:
        swap = False
        for inc in incorrect:
            for rule in rules[::-1]:
                a = rule[0]
                b = rule[1]
                if a in inc and b in inc:
                    a_i = inc.index(a)
                    b_i = inc.index(b)
                    if a_i > b_i:
                        # move (b) element in the list behind (a)
                        inc.insert(a_i, inc.pop(b_i))
                        swap = True
        cycles += 1

    for inc in incorrect:
        m_i = len(inc) // 2
        total += inc[m_i]

    # print(incorrect, cycles) # debug
    return total


data = read_input()
p1 = ordering_rules(data)
print(f"Total middle numbers of the correct updates: {p1[0]}")
print(f"Total corrected incorrect updates: {incorrect_updates(data, p1[1])}")
