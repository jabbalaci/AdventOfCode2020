#!/usr/bin/env python3

from helper import (rotate90, flip,
                    top_row, bottom_row,
                    left_column, right_column)


def rotate_and_flip_in_every_possible_way(matrix):
    result = []

    m = matrix
    for i in range(4):
        result.append(m)
        m = rotate90(m)
    #
    m = flip(m)
    for i in range(4):
        result.append(m)
        m = rotate90(m)
    #
    return result


def main():
    m = (
        (1, 2),
        (3, 4)
    )

    variations = rotate_and_flip_in_every_possible_way(m)
    for idx, v in enumerate(variations, start=1):
        print(idx, v)

    print("-" * 20)

    m2 = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    )
    print(m2)
    print(top_row(m2))
    print(bottom_row(m2))
    print(left_column(m2))
    print(right_column(m2))

    print("-" * 20)

    m3 = ("123", "456", "789")
    print(m3)
    print(top_row(m3))
    print(left_column(m3))
    variations = rotate_and_flip_in_every_possible_way(m3)
    for idx, v in enumerate(variations, start=1):
        print(idx, v)

##############################################################################

if __name__ == "__main__":
    main()
