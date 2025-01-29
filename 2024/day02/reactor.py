def read_input():
    data = []
    with open("input.txt") as file:
        for line in file:
            new_line = line.rstrip("\r\n").split()  # split spaces
            new_line = list(map(int, new_line))  # map str into numbers
            data.append(new_line)
    return data


# determine if a sequence of numbers is generally decreasing
# count total increases vs decreases
def decrease_seq(nums: list[int]) -> bool:
    inc = 0
    dec = 0

    for i, _ in enumerate(nums[1:], start=1):
        diff = nums[i] - nums[i - 1]
        if diff > 0:
            inc += 1
        elif diff < 0:
            dec += 1

    return dec > inc


# function to determine if a list of nums is all increasing or decreasing
# and within differences of 1-3
# returns [bool, int] where int is the index the safe variable became False
def safety_check(report: list[int]) -> bool:

    safe = True
    fail_index = -1
    increasing = True

    # check if report is increasing or decreasing
    if decrease_seq(report):
        increasing = False

    # determine if report is within safe range
    for i, _ in enumerate(report[1:], start=1):

        # set safe to False if increase/decrease conditions fail
        diff = report[i] - report[i - 1]
        if increasing and (diff < 1 or diff > 3):
            safe = False
            fail_index = i
            break
        elif not increasing and (diff > -1 or diff < -3):
            safe = False
            fail_index = i
            break

    return [safe, fail_index]


# part 1
def report_check(data: list[str]) -> int:

    safe_count = 0

    for report in data:  # line
        if safety_check(report)[0]:
            safe_count += 1

    return safe_count


# part 2
# problem edge case: 55 52 53 54 56 57
def tolerance_check(data: list[str]) -> int:
    tole_count = 0

    for report in data:

        # [bool, int]
        safe, f_i = safety_check(report)

        if safe:
            tole_count += 1
        else:
            # use index where check failed to check new concatenated lists
            report_B = report[:f_i] + report[f_i + 1 :]  # i
            report_A = report[: f_i - 1] + report[f_i:]  # i-1

            # this approach is less computationally expensive
            if safety_check(report_B)[0]:
                tole_count += 1
            elif safety_check(report_A)[0]:
                tole_count += 1

            # print(report, report_A, report_B, tolerance_worked)  # debug

    return tole_count


data = read_input()
print(f"total safe reports: {report_check(data)}")
print(f"total safe reports with tolerance: {tolerance_check(data)}")