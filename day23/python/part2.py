#!/usr/bin/env python3

"""
Part 2 was extremely slow.

On Reddit I found a good tip: use a dictionary.

"Each key is a cup number, and the corresponding value is the next cup.
Moving cups is just a matter of relinking them."

This version (with dictionary) is fast.
"""

from typing import Dict, List


class CrabGame:
    def __init__(self, digits: str) -> None:
        self.NUMBER_OF_CUPS = 1_000_000
        self.curr = int(digits[0])
        self.d: Dict[int, int] = self.create_dict(digits, self.NUMBER_OF_CUPS)
        self.MIN = min(self.d.keys())
        self.MAX = max(self.d.keys())
        self.NUMBER_OF_MOVES = 10_000_000

    def create_dict(self, digits: str, number_of_cups: int) -> Dict[int, int]:
        lst = [int(x) for x in digits]
        n = max(lst) + 1
        loops = number_of_cups - len(lst)
        for _ in range(loops):
            lst.append(n)
            n += 1
        #
        assert len(lst) == number_of_cups
        #
        shifted = lst[1:] + [lst[0]]
        return dict(zip(lst, shifted))

    def find_destination(self, curr: int, three: List[int]) -> int:
        value = curr
        while True:
            value -= 1
            if value < self.MIN:
                value = self.MAX
            #
            if value not in three:
                return value
            #
        #

    def get_next_three(self, value: int) -> List[int]:
        lst = []
        for _ in range(3):
            key = value
            value = self.d[key]
            lst.append(value)
        #
        return lst

    def move(self) -> None:
        # print("cups:", self)
        # print("current:", self.curr)
        three = self.get_next_three(self.curr)
        # print("pick up:", three)
        dest = self.find_destination(self.curr, three)
        # print("destination:", dest)
        # re-linking
        three_first = three[0]
        three_last = three[-1]
        after_three = self.d[three_last]
        after_dest = self.d[dest]

        self.d[self.curr] = after_three
        self.d[dest] = three_first
        self.d[three_last] = after_dest
        #
        self.curr = self.d[self.curr]
        # print("new curr:", self.curr)

    def start(self) -> None:
        for i in range(self.NUMBER_OF_MOVES):
            # if i % 100_000 == 0:
                # print(i)
            step = i + 1
            # print("Move", step)
            self.move()
            # print()

    def _get_elems_as_list(self, value: int) -> List[int]:
        start_value = value
        lst = []
        while True:
            key = value
            lst.append(key)
            value = self.d[key]
            if value == start_value:
                break
            #
        #
        return lst

    def get_result(self) -> int:
        a = self.d[1]
        b = self.d[a]
        print("Cup 1:", a)
        print("Cup 2:", b)
        print()
        return a * b

    def __str__(self) -> str:
        return " ".join([str(x) for x in self._get_elems_as_list(self.curr)])


def main():
    example = "389125467"
    input = "394618527"

    # game = CrabGame(example)
    game = CrabGame(input)

    game.start()
    print("Result:", game.get_result())

##############################################################################

if __name__ == "__main__":
    main()
