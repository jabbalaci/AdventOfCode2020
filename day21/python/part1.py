#!/usr/bin/env python3

"""
Here I needed some help:

https://old.reddit.com/r/adventofcode/comments/kibpup/2020_day_21_part_1_i_dont_understand_how_to_solve/

The key idea is this:

    "The ingredient that is associated with an allergen
    must be in all recipes that contain that allergen.
    If the ingredient is not in all the recipes then remove it."
"""


import copy
from pprint import pprint
from typing import List, Set

import helper


class Food:
    def __init__(self, left: Set[str], right: Set[str]) -> None:
        self.left: Set[str] = left
        self.right: Set[str] = right

    def __str__(self) -> str:
        return f"{self.left} ({self.right})"


class Foods:
    def __init__(self, lines: List[str]) -> None:
        self.foods = self.parse(lines)
        self.backup_foods = copy.deepcopy(self.foods)
        self.has_allergen: Set[str] = set()

    def parse(self, lines: List[str]) -> List[Food]:
        result: List[Food] = []

        for line in lines:
            l, r = line.split(" (contains ")
            left = set(l.split())
            right = set(r.replace(")", "").split(", "))
            result.append(Food(left, right))

        return result

    def is_ingredient_everywhere_where_allergen_is_present(self, ingredient: str, allergen: str):
        result = []
        for food in self.foods:
            if allergen in food.right:
                result.append(ingredient in food.left)
            #
        #
        return all(result)

    def simplify(self) -> None:
        has_allergen = set()
        for food in self.foods:
            for ingredient in food.left:
                for allergen in food.right:
                    if self.is_ingredient_everywhere_where_allergen_is_present(ingredient, allergen):
                        has_allergen.add(ingredient)
                    #
                #
            #
        #
        self.has_allergen = has_allergen

    def get_result(self) -> int:
        total = 0
        for food in self.backup_foods:
            for ingredient in food.left:
                if ingredient not in self.has_allergen:
                    total += 1
                #
            #
        #
        return total

    def start(self) -> None:
        self.simplify()

    def __str__(self) -> str:
        sb = []
        for food in self.foods:
            sb.append(str(food))
        #
        return "\n".join(sb)


def main():
    # lines = helper.read_lines("example.txt")
    # lines = helper.read_lines("example2.txt")
    lines = helper.read_lines("input.txt")

    foods = Foods(lines)
    foods.start()
    # for f in foods.foods:
        # print(f)
    # print("-----------------")
    # for f in foods.backup_foods:
        # print(f)
    print(foods.get_result())

##############################################################################

if __name__ == "__main__":
    main()
