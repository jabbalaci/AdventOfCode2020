#!/usr/bin/env python3

"""
not yet finished
"""

import copy
from pprint import pprint
from typing import List, Set

import helper
import part1

class Part2:
    def __init__(self, foods):
        self.foods = foods
        self.simple = []

    def start(self):
        self.simple = self.simplify(self.foods)
        for f in self.simple:
            print(f)

    def simplify(self, foods):
        lst = []
        for food in foods.foods:
            new_left = {ingr for ingr in food.left if ingr in foods.has_allergen}
            lst.append(part1.Food(new_left, food.right))
        #
        return lst


def main():
    # lines = helper.read_lines("example.txt")
    # lines = helper.read_lines("example2.txt")
    lines = helper.read_lines("input.txt")

    foods = part1.Foods(lines)
    foods.start()
    # print("Part 1:", foods.get_result())

    part2 = Part2(foods)
    part2.start()

##############################################################################

if __name__ == "__main__":
    main()
