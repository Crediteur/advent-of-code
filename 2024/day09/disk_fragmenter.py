def read_input() -> str:
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.rstrip("\r\n"))

    return data[0]


# p1
# convert a string of numbers into used space and empty spaces
#    represent alternating numbers as indices and spaces as '.'
# use two pointers to swap last file index and eariler space index
# until 2nd pointer is less than the first pointer so all free space is at the end
# compute and sum the file number with the product of element position for each digit
def filesystem_checksum(data) -> int:
    total = 0

    # create the expanded data, with each element preserved
    # (because the file size can be multiple digits)
    expanded_data = []

    for i, c in enumerate(list(data)):
        if i % 2 == 1:
            # free space
            for _ in range(int(c)):
                expanded_data.append(".")
        elif i % 2 == 0:
            # files
            for _ in range(int(c)):
                expanded_data.append(str(i // 2))

    # swap starting spaces and ending file elements
    p1_i = 0
    p2_i = len(expanded_data) - 1
    # print(expanded_data)

    while p2_i > p1_i:
        # increment pointers until desired elements found
        # assumption: there are more numbers than '.'s
        if expanded_data[p1_i] != ".":
            p1_i += 1
            continue
        if expanded_data[p2_i] == ".":
            p2_i -= 1
            continue

        # else: swap elements
        expanded_data[p1_i], expanded_data[p2_i] = (
            expanded_data[p2_i],
            expanded_data[p1_i],
        )

    print(len(expanded_data))

    # sum the product of the files with its index
    for i, c in enumerate(expanded_data):
        if c == ".":
            break
        total += i * int(c)

    return total


# p2
# create the expanded list like p1
# save each set of files or space as blocks
# preserve each file element as their own element due to multi digits
# swap spaces and blocks based on length:
#   directly mutate the element based on min common length difference
#   eg. ['.','.','.'] swap ['9','9'] -> ['9','9','.'] iterate and swap index positions


def compact_checksum(data) -> int:
    total = 0

    block_data = []

    for i, c in enumerate(list(data)):
        if i % 2 == 1:
            # space block
            block_data.append([".", int(c)])
        elif i % 2 == 0:
            # file block
            block_data.append([str(i // 2), int(c)])

    # print(block_data)

    for i, block in enumerate(reversed(block_data)):
        i = len(block_data) - 1 - i
        if block[0] == ".":
            continue
        for j, space in enumerate(block_data):
            if space[0] != ".":
                continue
            block_id, block_len = block
            _, space_len = space
            # important to recalculate new indices after list changes length
            block_i = block_data.index(block)
            space_j = block_data.index(space)

            # check if block swap is possible
            if block_len <= space_len and space_j < block_i:
                if block_len == space_len:
                    block_i = block_data.index(block)
                    space_j = block_data.index(space)
                    block_data[space_j], block_data[block_i] = (
                        block_data[block_i],
                        block_data[space_j],
                    )
                elif block_len < space_len:
                    diff = space_len - block_len
                    new_space = [".", space_len - diff]
                    diff_space = [".", diff]
                    # convert file block into spaces
                    removed_file = block_data.pop(block_i)
                    removed_space = block_data.pop(space_j)
                    block_data.insert(space_j, diff_space)
                    block_data.insert(space_j, removed_file)
                    block_data.insert(block_i, new_space)
                    # convert spaces into file indices
                    # check and connect surrounding spaces
                
                # print(block_data)
                # print(f"swapping {space, block}")
                break

    # calculate checksum
    count = 0
    for block in block_data:
        # print(count, block, total)
        block_type, block_size = block
        if block_type == ".":
            count += block_size
            continue
        for _ in range(block_size):
            total += int(block_type) * count
            count += 1

    return total


data = read_input()
print(f"resulting file checksum: {filesystem_checksum(data)}")
print(f"total compact checksum: {compact_checksum(data)}")
