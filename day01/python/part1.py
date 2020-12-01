#!/usr/bin/env python3

import helper
from itertools import combinations

GOAL = 2020

def main():
    # fname = "example.txt"
    fname = "input.txt"
    numbers = helper.read_lines_as_ints(fname)

    for a, b in combinations(numbers, 2):
        if a + b == GOAL:
            print(f"# {a}, {b}")
            print()
            result = a * b
            print(result)
            break

##############################################################################

if __name__ == "__main__":
    main()
