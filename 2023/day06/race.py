def read_input():
    with open("input.txt", "r") as file:
        data = file.read()
    return data.split("\n")


def organize_data(data):
    t = data[0].split()[1:]
    r = data[1].split()[1:]
    return t, r


# part one
def power_sum_metrics(t, r):
    """
    iterate and check when time remaining beats record
    """
    metrics = [(int(t[i]), int(r[i])) for i in range(len(t))]

    total = 1
    for time, recd in metrics:
        count = 0
        for t in range(1, time):  # ignore t=0 and t=max
            meters = (time - t) * t
            if meters > recd:
                count += 1
        total *= count

    return total


# part two
def sum_long_race(t, r):
    """
    check edge boundaries for when you WONT win the race
    left and right should be the same, so *2 total
    """
    time = int(("").join(t))
    recd = int(("").join(r))

    # iterate from left until meters > dist
    count = 0
    for t in range(0, time // 2):
        meters = (time - t) * t
        if meters < recd:
            count += 1
        if meters > recd:
            break

    return time - count * 2 + 1


if __name__ == "__main__":
    t, r = organize_data(read_input())
    print(f"{power_sum_metrics(t, r)}")
    print(f"{sum_long_race(t, r)}")
