#!/usr/bin/env python3

from pprint import pprint
from typing import Dict, List, NamedTuple, Tuple

import helper


class Point(NamedTuple):
    x: int
    y: int
    z: int


class Cube:
    def __init__(self, lines: List[str]) -> None:
        self.d: Dict[Point, bool] = {}    # key: point in 3D, value: active (true) / inactive (false)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                self.d[Point(x, y, 0)] = (c == '#')
            #
        #
        self.add_inactive_neighbors()

    def add_inactive_neighbors(self) -> None:
        inactive_neighbors = []

        for point in self.d.keys():
            for neighbor, active in self.get_neighbors(point):
                if not active:
                    inactive_neighbors.append(neighbor)
                #
            #
        #
        for p in inactive_neighbors:
            self.d[p] = False

    def show(self) -> None:
        pprint(self.d)

    def get_neighbors(self, center: Point) -> List[Tuple[Point, bool]]:
        x, y, z = center
        neighbors: List[Point] = [
            Point(x-1, y-1, z),
            Point(x, y-1, z),
            Point(x+1, y-1, z),
            Point(x-1, y, z),
            Point(x+1, y, z),
            Point(x-1, y+1, z),
            Point(x, y+1, z),
            Point(x+1, y+1, z),
            #
            Point(x-1, y-1, z-1),
            Point(x, y-1, z-1),
            Point(x+1, y-1, z-1),
            Point(x-1, y, z-1),
            Point(x, y, z-1),
            Point(x+1, y, z-1),
            Point(x-1, y+1, z-1),
            Point(x, y+1, z-1),
            Point(x+1, y+1, z-1),
            #
            Point(x-1, y-1, z+1),
            Point(x, y-1, z+1),
            Point(x+1, y-1, z+1),
            Point(x-1, y, z+1),
            Point(x, y, z+1),
            Point(x+1, y, z+1),
            Point(x-1, y+1, z+1),
            Point(x, y+1, z+1),
            Point(x+1, y+1, z+1)
        ]
        #
        result: List[Tuple[Point, bool]] = []
        for p in neighbors:
            if self.d.get(p):
                result.append((p, True))
            else:
                result.append((p, False))
        #
        return result

    def get_number_of_active_cubes(self) -> int:
        return sum(1 for status in self.d.values() if status == True)

    def evolve(self) -> None:
        new_d: Dict[Point, bool] = {}

        for point, status in self.d.items():
            neighbors: List[Tuple[Point, bool]] = self.get_neighbors(point)
            assert len(neighbors) == 26    # (3 * 3 * 3) - 1
            number_of_active_neighbors = sum(1 for p, active in neighbors if active)
            if status == True:    # active
                if number_of_active_neighbors in (2, 3):
                    new_d[point] = True    # remains active
                else:
                    new_d[point] = False    # becomes inactive
            else:    # inactive
                if number_of_active_neighbors == 3:
                    new_d[point] = True    # becomes active
                else:
                    new_d[point] = False    # remains inactive
            #
        #
        self.d = new_d
        #
        self.add_inactive_neighbors()


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    cube = Cube(lines)

    for i in range(0, 6+1):
        # cube.show()
        print("Cycle:", i)
        print(cube.get_number_of_active_cubes())
        print("------------")
        cube.evolve()

##############################################################################

if __name__ == "__main__":
    main()
