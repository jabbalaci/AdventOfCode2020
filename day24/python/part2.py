#!/usr/bin/env python3

from pprint import pprint
from typing import Dict, List, Tuple

import helper

WHITE, BLACK = 0, 1    # default: everything is white


class Hexa:
    def __init__(self, lines: List[str]) -> None:
        self.dirs: List[Tuple[str, ...]] = [self.to_directions(line) for line in lines]
        self.d: Dict[Tuple[int, int], int] = {}

    def to_directions(self, line: str) -> Tuple[str, ...]:
        result = []
        i = 0
        while i < len(line):
            first = line[i]
            if first in ('w', 'e'):
                result.append(first)
                i += 1
            else:
                second = line[i+1]
                result.append(first + second)
                i += 2
            #
        #
        return tuple(result)

    def show_directions(self) -> None:
        for t in self.dirs:
            print(t)

    def fill_dictionary(self) -> None:
        for directions in self.dirs:
            x, y = 0, 0
            for dir in directions:
                if dir == 'ne':
                    if y % 2 == 1:
                        x, y = x+1, y-1
                    else:
                        x, y = x, y-1
                elif dir == 'e':    # OK
                    x, y = x+1, y
                elif dir == 'se':
                    if y % 2 == 1:
                        x, y = x+1, y+1
                    else:
                        x, y = x, y+1
                elif dir == 'sw':
                    if y % 2 == 1:
                        x, y = x, y+1
                    else:
                        x, y = x-1, y+1
                elif dir == 'w':    # OK
                    x, y = x-1, y
                elif dir == 'nw':
                    if y % 2 == 1:
                        x, y = x, y-1
                    else:
                        x, y = x-1, y-1
                else:
                    raise Exception()    # we should never get here
            #
            value = self.d.get((x, y), WHITE)
            flipped = BLACK if value == WHITE else WHITE
            self.d[(x, y)] = flipped
        #
        self.add_white_neighbors()    # NEW!

    def get_six_neighbors(self, point) -> List[Tuple[int, int]]:
        result = []
        x, y = point
        if y % 2 == 1:    # if y is odd
            result = [
                (x+1, y), (x+1, y+1), (x, y+1), (x-1, y), (x, y-1), (x+1, y-1)
            ]
        else:
            result = [
                (x+1, y), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1)
            ]
        #
        return result

    def add_white_neighbors(self) -> None:
        collect = []
        for point, color in self.d.items():
            if color == BLACK:
                six_neigbors = self.get_six_neighbors(point)
                for nb in six_neigbors:
                    if self.d.get(nb, WHITE) == WHITE:
                        collect.append(nb)
                    #
                #
            #
        #
        for p in collect:
            self.d[p] = WHITE

    def evolve(self) -> None:
        new_d: Dict[Tuple[int, int], int] = {}
        for point, color in self.d.items():
            new_d[point] = color
            six_neigbors = self.get_six_neighbors(point)
            num_of_white_neighbors = sum(1 for nb in six_neigbors if self.d.get(nb, WHITE) == WHITE)
            num_of_black_neighbors = 6 - num_of_white_neighbors
            if color == BLACK:
                if num_of_black_neighbors == 0 or num_of_black_neighbors > 2:
                    new_d[point] = WHITE
                #
            else:    # if color is WHITE
                if num_of_black_neighbors == 2:
                    new_d[point] = BLACK
            #
        #
        self.d = new_d
        self.add_white_neighbors()    # Important!

    def start(self) -> None:
        self.fill_dictionary()
        for i in range(100):
            day = i + 1
            self.evolve()
            print("Day {0}: {1}".format(day, self.get_result()))

    def get_result(self) -> int:
        return sum(1 for v in self.d.values() if v == BLACK)


def main() -> None:
    # lines = helper.read_lines("example0.txt")
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    hexa = Hexa(lines)
    # hexa.show_directions()
    hexa.start()
    # pprint(hexa.d)
    # print(hexa.get_result())

##############################################################################

if __name__ == "__main__":
    main()
