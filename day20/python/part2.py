#!/usr/bin/env python3

"""
Before running it, execute `part1.py`.
`part1.py` will generate the necessary input file for Part 2.
"""

from typing import List, Tuple

import helper
from helper import flip, rotate90

Matrix = Tuple[Tuple[str, ...], ...]


def rotate_and_flip_in_every_possible_way(matrix: Matrix) -> List[Matrix]:
    """
    It will make a list of 8 variations of the received matrix.
    """
    result: List[Matrix] = []

    m = matrix
    for _ in range(4):
        result.append(m)
        m = rotate90(m)
    #
    m = flip(m)
    for _ in range(4):
        result.append(m)
        m = rotate90(m)
    #
    return result


class MatchFinder:
    """
    Having a base matrix, find all the occurrences of a sub-matrix in it.
    """
    def __init__(self, base: Matrix, sub: Matrix) -> None:
        self.base: Matrix = base
        self.sub: Matrix = sub
        self.base_width: int = len(self.base[0])
        self.base_height: int = len(self.base)
        self.sub_width: int = len(self.sub[0])
        self.sub_height: int = len(self.sub)

    def match_template(self, offset_down: int, offset_right: int) -> bool:
        for i in range(self.sub_height):
            for j in range(self.sub_width):
                if self.sub[i][j] == '#':
                    if self.base[i + offset_down][j + offset_right] != '#':
                        return False
                    #
                #
            #
        #
        return True

    def find_matches(self) -> int:
        total = 0
        for row in range(self.base_height - self.sub_height):
            for col in range(self.base_width - self.sub_width):
                offset_down, offset_right = row, col
                if self.match_template(offset_down, offset_right):
                    total += 1
                #
            #
        #
        return total

    def get_result(self) -> int:
        return self.find_matches()

# endclass MatchFinder


def read_matrix(fname: str) -> Matrix:
    lines: List[str] = helper.read_lines(fname)
    matrix = []
    for line in lines:
        matrix.append(tuple(list(line)))
    #
    return tuple(matrix)


def show(matrix: Matrix) -> None:
    for row in matrix:
        print("".join(row))


def number_of_hashes(m: Matrix) -> int:
    return sum(1 for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == '#')


def calculate_result(base_matrix: Matrix, sub_matrix: Matrix, monsters: int) -> int:
    a: int = number_of_hashes(base_matrix)
    b: int = number_of_hashes(sub_matrix)

    return a - (b * monsters)


def main() -> None:
    m: Matrix = read_matrix("input_for_part2.txt")
    variations: List[Matrix] = rotate_and_flip_in_every_possible_way(m)

    # for idx, v in enumerate(variations):
        # print(f"{idx}:")
        # show(v)
        # print("-" * 40)

    # base_matrix = variations[1]
    # show(base_matrix)

    # print("-" * 20)

    sub_matrix = read_matrix("monster_template.txt")
    # show(sub_matrix)

    # mf = MatchFinder(base_matrix, sub_matrix)
    # mf.start()

    # print("-" * 20)
    matches = []
    for v in variations:
        mf = MatchFinder(v, sub_matrix)
        matches.append(mf.get_result())
    #
    monsters = max(matches)
    # print(monsters)
    result = calculate_result(variations[0], sub_matrix, monsters)
    print("Part 2:", result)

##############################################################################

if __name__ == "__main__":
    main()
