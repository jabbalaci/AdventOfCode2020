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

    def get_result(self) -> int:
        return sum(1 for v in self.d.values() if v == BLACK)

    def start(self) -> None:
        self.fill_dictionary()


def main() -> None:
    # lines = helper.read_lines("example0.txt")
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    hexa = Hexa(lines)
    # hexa.show_directions()
    hexa.start()
    # pprint(hexa.d)
    print(hexa.get_result())

##############################################################################

if __name__ == "__main__":
    main()
