#!/usr/bin/env python3

from typing import List, Tuple

import helper


class Layout:
    def __init__(self, lst: List[str]) -> None:
        self.grid: Tuple[str, ...] = tuple(lst)

    def get_neighbors(self, i: int, j: int) -> str:
        result = ""
        try:
            if i - 1 < 0: raise IndexError
            if j - 1 < 0: raise IndexError
            result += self.grid[i-1][j-1]
        except IndexError:
            pass
        try:
            if i - 1 < 0: raise IndexError
            result += self.grid[i-1][j]
        except IndexError:
            pass
        try:
            if i - 1 < 0: raise IndexError
            result += self.grid[i-1][j+1]
        except IndexError:
            pass
        try:
            if j - 1 < 0: raise IndexError
            result += self.grid[i][j-1]
        except IndexError:
            pass
        try:
            result += self.grid[i][j+1]
        except IndexError:
            pass
        try:
            if j - 1 < 0: raise IndexError
            result += self.grid[i+1][j-1]
        except IndexError:
            pass
        try:
            result += self.grid[i+1][j]
        except IndexError:
            pass
        try:
            result += self.grid[i+1][j+1]
        except IndexError:
            pass
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
                    if neighbors.count('#') >= 4:
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
        return "\n".join(self.grid)


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    grid = Layout(lines)
    # print(grid)
    # print()
    while grid.evolve():
        pass
        # print(grid)
        # print()
    #
    print(grid.number_of_seats())

##############################################################################

if __name__ == "__main__":
    main()
