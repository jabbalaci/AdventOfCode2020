#!/usr/bin/env python3

"""
Refactored version of Part 1a.

It will serve as a starting point for Part 2.
"""

from collections import deque
from typing import Deque, List


class Rotator:
    def __init__(self, digits: str) -> None:
        self.d: Deque[int] = deque([int(x) for x in digits])
        self.MIN = min(self.d)
        self.MAX = max(self.d)
        # self.NUMBER_OF_MOVES = 10    # test
        self.NUMBER_OF_MOVES = 100    # the real thing
        self.curr: int = self.d[0]

    def rotate_to(self, value: int) -> None:
        """
        Rotate the deque left until the given value is at the beginning.
        """
        index = self.d.index(value)
        self.d.rotate(-index)    # rotate left `index` times

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

    def move(self) -> None:
        self.rotate_to(self.curr)
        # print(self)
        # print("current:", self.curr)
        three = [self.d[1], self.d[2], self.d[3]]
        # print("pick up:", three)
        # start: remove the three elements
        self.d.rotate(-1)
        self.d.popleft(); self.d.popleft(); self.d.popleft()
        self.d.rotate()
        # end: remove the three elements
        dest = self.find_destination(self.curr, three)
        # print("destination:", dest)
        self.rotate_to(dest)
        # start: insert the three elements
        self.d.rotate(-1)
        for n in reversed(three):
            self.d.appendleft(n)
        self.d.rotate()
        # end: insert the three elements
        self.rotate_to(self.curr)
        self.curr = self.d[1]

    def start(self) -> None:
        for i in range(self.NUMBER_OF_MOVES):
            step = i + 1
            # print("Move", step)
            self.move()
            # print()

    def get_result(self) -> str:
        copy = self.d.copy()
        while copy[0] != 1:
            copy.rotate(-1)
        copy.popleft()
        return "".join([str(x) for x in copy])

    def __str__(self) -> str:
        return str(self.d)


def main():
    example = "389125467"
    input = "394618527"

    # rot = Rotator(example)
    rot = Rotator(input)

    rot.start()
    # print(rot.d)
    print(rot.get_result())

##############################################################################

if __name__ == "__main__":
    main()
