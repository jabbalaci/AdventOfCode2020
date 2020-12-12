#!/usr/bin/env python3

import helper
from typing import List, Tuple

DIRECTIONS = "NESWNES"    # north, east, south, west, north, east, south

class Ship:
    def __init__(self, lines: List[str]) -> None:
        self.instructions: Tuple[Tuple[str, int], ...] = self.parse(lines)
        self.face = 'E'    # the ship faces this direction
        self.x = 0
        self.y = 0

    def get_result(self) -> int:
        return abs(self.x) + abs(self.y)

    def parse(self, lines: List[str]) -> Tuple[Tuple[str, int], ...]:
        return tuple((line[0], int(line[1:])) for line in lines)

    def go_north(self, value) -> None:
        self.y += value

    def go_south(self, value) -> None:
        self.y -= value

    def go_east(self, value) -> None:
        self.x += value

    def go_west(self, value) -> None:
        self.x -= value

    def turn_right(self, degrees: int) -> None:
        turns = degrees // 90
        pos = DIRECTIONS.find(self.face)
        self.face = DIRECTIONS[pos + turns]

    def turn_left(self, degrees: int) -> None:
        self.turn_right(360 - degrees)

    def go_forward(self, value: int) -> None:
        if self.face == 'N':
            self.go_north(value)
        elif self.face == 'E':
            self.go_east(value)
        elif self.face == 'S':
            self.go_south(value)
        elif self.face == 'W':
            self.go_west(value)
        else:
            raise Exception()    # we should never get here

    def start(self) -> None:
        for cmd, value in self.instructions:
            if cmd == 'F':
                self.go_forward(value)
            elif cmd == 'N':
                self.go_north(value)
            elif cmd == 'S':
                self.go_south(value)
            elif cmd == 'E':
                self.go_east(value)
            elif cmd == 'W':
                self.go_west(value)
            elif cmd == 'L':
                self.turn_left(value)
            elif cmd == 'R':
                self.turn_right(value)
            else:
                raise Exception()    # we should never get here


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    ship = Ship(lines)
    ship.start()

    print(ship.get_result())

##############################################################################

if __name__ == "__main__":
    main()
