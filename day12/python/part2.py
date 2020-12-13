#!/usr/bin/env python3

from typing import List, Tuple

import helper


class Ship:
    def __init__(self, lines: List[str]) -> None:
        self.instructions: Tuple[Tuple[str, int], ...] = self.parse(lines)
        self.x = 0          # ship's position
        self.y = 0          # ship's position
        self.wp_x = 10      # waypoint's relative position to the ship
        self.wp_y = 1       # waypoint's relative position to the ship

    def get_result(self) -> int:
        return abs(self.x) + abs(self.y)

    def parse(self, lines: List[str]) -> Tuple[Tuple[str, int], ...]:
        return tuple((line[0], int(line[1:])) for line in lines)

    def move_waypoint_north(self, value: int) -> None:
        self.wp_y += value

    def move_waypoint_south(self, value: int) -> None:
        self.wp_y -= value

    def move_waypoint_east(self, value: int) -> None:
        self.wp_x += value

    def move_waypoint_west(self, value: int) -> None:
        self.wp_x -= value

    def rotate_waypoint_right(self, degrees: int) -> None:
        if degrees == 90:
            self.wp_x, self.wp_y = (self.wp_y, -self.wp_x)
        elif degrees == 180:
            self.wp_x, self.wp_y = (-self.wp_x, -self.wp_y)
        elif degrees == 270:
            self.wp_x, self.wp_y = (-self.wp_y, self.wp_x)
        else:
            raise Exception()    # we should never get here

    def rotate_waypoint_left(self, degrees: int) -> None:
        self.rotate_waypoint_right(360 - degrees)

    def go_forward_to_waypoint(self, value: int) -> None:
        self.x += self.wp_x * value
        self.y += self.wp_y * value

    def start(self) -> None:
        for cmd, value in self.instructions:
            if cmd == 'N':
                self.move_waypoint_north(value)
            elif cmd == 'S':
                self.move_waypoint_south(value)
            elif cmd == 'E':
                self.move_waypoint_east(value)
            elif cmd == 'W':
                self.move_waypoint_west(value)
            elif cmd == 'L':
                self.rotate_waypoint_left(value)
            elif cmd == 'R':
                self.rotate_waypoint_right(value)
            elif cmd == 'F':
                self.go_forward_to_waypoint(value)
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
