#!/usr/bin/env python3

"""
Let's do it properly with a double ring.

Update: it turned out to be very slow for Part 2.

However, the double ring implementation could be re-used.
"""

from typing import List, Optional, Tuple


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.prev_node: Optional[Node] = None
        self.next_node: Optional[Node] = None

# endclass Node


class DoubleRing:
    def __init__(self) -> None:
        self.curr: Optional[Node] = None
        self._number_of_elems = 0

    def append(self, value):
        node = Node(value)

        if self.curr is None:
            self.curr = node
            node.prev_node = node
            node.next_node = node
        else:
            node.next_node = self.curr.next_node
            self.curr.next_node.prev_node = node    # type: ignore
            self.curr.next_node = node
            node.prev_node = self.curr
        #
        self.curr = self.curr.next_node
        #
        self._number_of_elems += 1

    def empty(self) -> int:
        return self._number_of_elems == 0

    def pop(self) -> int:
        assert not self.empty()
        #
        result = self.curr.value    # type: ignore

        if self._number_of_elems == 1:
            self.curr = None
        else:
            prev_node = self.curr.prev_node    # type: ignore
            next_node = self.curr.next_node    # type: ignore

            prev_node.next_node = next_node    # type: ignore
            next_node.prev_node = prev_node    # type: ignore
            self.curr = next_node
        #
        self._number_of_elems -= 1
        return result

    def _rotate_right(self, steps=1):
        assert not self.empty()
        #
        for _ in range(steps):
            self.curr = self.curr.prev_node    # type: ignore

    def _rotate_left(self, steps=1):
        assert not self.empty()
        #
        for _ in range(steps):
            self.curr = self.curr.next_node    # type: ignore

    def rotate(self, steps=1) -> None:
        if steps > 0:
            self._rotate_right(steps)
        elif steps < 0:
            steps = abs(steps)
            self._rotate_left(steps)

    def min_max(self) -> Tuple[int, int]:
        """
        Return the min and max elements in a tuple.
        """
        assert not self.empty()
        #
        p = self.curr
        mini = maxi = p.value    # type: ignore
        for _ in range(self._number_of_elems - 1):
            p = p.next_node    # type: ignore
            if p.value < mini:    # type: ignore
                mini = p.value    # type: ignore
            if p.value > maxi:    # type: ignore
                maxi = p.value    # type: ignore
        #
        return (mini, maxi)

    def get_elems_as_list(self) -> List[int]:
        elems = []
        p = self.curr
        for _ in range(self._number_of_elems):
            elems.append(p.value)    # type: ignore
            p = p.next_node    # type: ignore
        #
        return elems

    def __str__(self) -> str:
        elems = []
        p = self.curr
        for _ in range(self._number_of_elems):
            elems.append(p.value)    # type: ignore
            p = p.next_node    # type: ignore
        #
        return f"ring({elems})"

# endclass DoubleRing


class Rotator:
    def __init__(self, digits: str) -> None:
        self.d: DoubleRing = self.create_ring(digits)
        self.MIN, self.MAX = self.d.min_max()
        # self.NUMBER_OF_MOVES = 10    # test
        self.NUMBER_OF_MOVES = 100    # the real thing
        self.curr: int = self.d.curr.value    # type: ignore

    def create_ring(self, digits: str):
        ring = DoubleRing()
        for x in digits:
            ring.append(int(x))
        #
        ring.rotate(-1)
        #
        return ring

    def rotate_to(self, value: int) -> None:
        """
        Rotate the deque left until the given value is at the beginning.
        """
        while self.d.curr.value != value:    # type: ignore
            self.d.rotate(-1)    # rotate left

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
        # self.rotate_to(self.curr)
        # print(self)
        # print("current:", self.curr)
        three = [
            self.d.curr.next_node.value,    # type: ignore
            self.d.curr.next_node.next_node.value,    # type: ignore
            self.d.curr.next_node.next_node.next_node.value    # type: ignore
        ]
        # print("pick up:", three)
        # start: remove the three elements
        self.d.rotate(-1)
        # print("after rotate left:", self)
        self.d.pop(); self.d.pop(); self.d.pop()
        # print("after removing first three:", self)
        self.d.rotate()
        # print("after rotate right:", self)
        # end: remove the three elements
        dest = self.find_destination(self.curr, three)
        # print("destination:", dest)
        self.rotate_to(dest)
        # print("after rotating to destination:", self)
        # start: insert the three elements
        # self.d.rotate(-1)
        # print("after rotate left:", self)
        for n in three:
            self.d.append(n)
            # print("    after appending the three elems:", self)
        # self.d.rotate()
        # print("after rotate right:", self)
        # end: insert the three elements
        self.rotate_to(self.curr)
        # print("after rotating to current:", self)
        self.d.rotate(-1)
        self.curr = self.d.curr.value    # type: ignore
        # print("current:", self.curr)

    def start(self) -> None:
        for i in range(self.NUMBER_OF_MOVES):
            step = i + 1
            # print("Move", step)
            self.move()
            # print()

    def get_result(self) -> str:
        self.rotate_to(1)
        elems = self.d.get_elems_as_list()[1:]
        return "".join(str(x) for x in elems)

    def __str__(self) -> str:
        return str(self.d)


def main():
    example = "389125467"
    input = "394618527"

    # rot = Rotator(example)
    rot = Rotator(input)

    # print(rot)

    rot.start()
    # print(rot.d)
    print(rot.get_result())

##############################################################################

if __name__ == "__main__":
    main()
