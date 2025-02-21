def read_input():
    data = []
    # separate data
    with open("input.txt") as file:
        for line in file:
            temp = line.rstrip("\r\n").split(":")
            temp = (int(temp[0]), [*map(int, temp[1].strip().split(" "))])
            data.append(temp)

    return data


# helper function for p2
# concatenates two numbers together
def concat_num(n, m) -> int:
    return int(str(n) + str(m))


# p1
# try to add and mult every number
# two branches of sequential numbers in a list, 2^4 possble size
# if number is bigger than target, break for efficiency
# for p2, same as p1 but with 3 branches of operations
def calibrate_results(data) -> list[int]:
    results = [0, 0]

    # two parts of the question with similar code
    for part in range(1, 3):
        total = 0
        for line in data:
            target, numbers = line
            workspace = [numbers[0]]  # start with first number

            for n in numbers[1:]:
                # for each conseqeutive num, add and mult
                temp_space = []
                for m in workspace:
                    # only add numbers if result is smaller than target
                    if n + m <= target:
                        temp_space.append(n + m)
                    if n * m <= target:
                        temp_space.append(n * m)
                    # new operation for p2 only
                    if part == 2:
                        if concat_num(m, n) <= target:
                            temp_space.append(concat_num(m, n))

                workspace = temp_space

            # add to total if target exists
            if target in workspace:
                total += target

        # sum total into results list
        results[part - 1] = total

    return results


data = read_input()
print(f"calibration with +,* operators: {calibrate_results(data)[0]}")
print(f"calibration with +,*,|| operators: {calibrate_results(data)[1]}")
