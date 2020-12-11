#!/usr/bin/env python3

from typing import Dict, List, Tuple

import helper

DIRECTIONS: Dict[str, Tuple[int, int]] = {
    'NW': (-1, -1),
    'N':  (-1,  0),
    'NE': (-1, +1),
    'E':  ( 0, +1),
    'SE': (+1, +1),
    'S':  (+1,  0),
    'SW': (+1, -1),
    'W':  ( 0, -1)
}

class Layout:
    def __init__(self, lst: List[str]) -> None:
        self.grid: Tuple[str, ...] = tuple(lst)

    def scan(self, direction: str, i: int, j: int) -> str:
        result = "."
        new_i = i
        new_j = j
        t = DIRECTIONS[direction]

        try:
            while True:
                new_i += t[0]
                new_j += t[1]
                if (new_i < 0) or (new_j < 0):
                    raise IndexError
                if (value := self.grid[new_i][new_j]) != '.':
                    result = value
                    break
                #
            #
        except IndexError:
            pass
        #
        return result

    def get_neighbors(self, i: int, j: int) -> str:
        result = ""

        result += self.scan('NW', i, j)
        result += self.scan('N',  i, j)
        result += self.scan('NE', i, j)
        result += self.scan('E',  i, j)
        result += self.scan('SE', i, j)
        result += self.scan('S',  i, j)
        result += self.scan('SW', i, j)
        result += self.scan('W',  i, j)

        return result

    def evolve(self) -> bool:
        """
        Returns True if the grid changed. Otherwise, returns False.
        """
        result = []
        for i, row in enumerate(self.grid):
            line = []
            for j, seat in enumerate(row):
                neighbors = self.get_neighbors(i, j)
                line.append(seat)
                if seat == 'L':
                    if neighbors.count('#') == 0:
                        line[-1] = '#'
                    #
                elif seat == '#':
                    if neighbors.count('#') >= 5:
                        line[-1] = 'L';
                    #
                #
            #
            result.append("".join(line))
        #
        new_grid = tuple(result)
        if new_grid != self.grid:
            self.grid = new_grid
            return True
        #
        return False

    def number_of_seats(self) -> int:
        return sum(row.count('#') for row in self.grid)

    def __str__(self) -> str:
        return "\n".join(self.grid) + "\n" + str(self.number_of_seats())


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    grid = Layout(lines)

    while grid.evolve():
        pass
    #
    print(grid.number_of_seats())

##############################################################################

if __name__ == "__main__":
    main()
