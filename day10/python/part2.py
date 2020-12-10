#!/usr/bin/env python3

import helper
import math


def main():
    # lines = helper.read_lines_as_ints("example1.txt")
    # lines = helper.read_lines_as_ints("example2.txt")
    lines = helper.read_lines_as_ints("input.txt")
    numbers = sorted(lines)
    numbers = [0] + numbers + [numbers[-1] + 3]
    clusters = []

    print(numbers)
    print("length:", len(numbers))
    print()

    for i in range(0, len(numbers)-2):
        left_elem = numbers[i]
        cl = []
        j = i + 2
        while True:
            right_elem = numbers[j]
            if right_elem - left_elem > 3:
                break
            # else
            middle_elem = numbers[j - 1]    # just to the left of the j^th element
            cl.append(middle_elem)
            j += 1
        #
        if len(cl) > 0:
            clusters.append(cl)
    #
    print("clusters:           ", clusters)
    clusters = join_clusters(clusters)
    print("joined clusters:    ", clusters)

    d = {
        3: 7,
        2: 4,
        1: 2
    }

    multipliers = [d[len(cl)] for cl in clusters]
    print("numbers to multiply:", multipliers)

    result = math.prod(multipliers)
    print()
    print("result:", result)


def join_clusters(clusters):
    result = []
    curr = clusters[0]
    for cl in clusters[1:]:
        if curr[-1] == cl[0]:
            curr.extend(cl)
        else:
            distinct = sorted(set(curr))
            result.append(distinct)
            curr = cl
    #
    distinct = sorted(set(curr))
    result.append(distinct)

    return result

##############################################################################

if __name__ == "__main__":
    main()
