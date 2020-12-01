#!/usr/bin/env python3

import helper
from itertools import combinations

GOAL = 2020

def main():
    # fname = "example.txt"
    fname = "input.txt"
    numbers = helper.read_lines_as_ints(fname)

    for a, b, c in combinations(numbers, 3):
        if a + b + c == GOAL:
            print(f"# {a}, {b}, {c}")
            print()
            result = a * b * c
            print(result)
            break

##############################################################################

if __name__ == "__main__":
    main()
