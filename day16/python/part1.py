#!/usr/bin/env python3


def get_ranges(text):
    result = []
    for line in text.splitlines():
        part = line.split(": ")[1]
        ranges = part.split(" or ")
        for r in ranges:
            parts = r.split("-")
            a = int(parts[0])
            b = int(parts[1])
            result.append(range(a, b+1))
        #
    #
    return result


def get_numbers(text):
    result = []
    for line in text.splitlines()[1:]:
        result.extend([int(x) for x in line.split(",")])
    #
    return result


def contains(ranges, n):
    for r in ranges:
        if n in r:
            return True
        #
    #
    return False


def main():
    # fname = "example.txt"
    fname = "input.txt"

    with open(fname) as f:
        content = f.read()
    #
    parts = content.split("\n\n")

    ranges = get_ranges(parts[0])
    # print(ranges)
    numbers = get_numbers(parts[2])
    # print(numbers)

    total = 0
    for n in numbers:
        if not contains(ranges, n):
            total += n
        #
    #
    print(total)

##############################################################################

if __name__ == "__main__":
    main()
