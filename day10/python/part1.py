#!/usr/bin/env python3

import helper


def main():
    # lines = helper.read_lines_as_ints("example1.txt")    # 7 (1 jolt) * 5 (3 jolts) = 35
    # lines = helper.read_lines_as_ints("example2.txt")    # 22 (1 jolt) * 10 (3 jolts) = 220
    lines = helper.read_lines_as_ints("input.txt")
    numbers = sorted(lines)
    numbers = [0] + numbers + [numbers[-1] + 3]

    one = 0
    three = 0
    for a, b in zip(numbers, numbers[1:]):
        diff = b - a
        if diff == 1:
            one += 1
        elif diff == 3:
            three += 1
    #
    print(one)
    print(three)
    print("result:", one * three)

##############################################################################

if __name__ == "__main__":
    main()
