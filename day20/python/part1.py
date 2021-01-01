#!/usr/bin/env python3

import math
from pprint import pprint
from typing import Dict, List, NamedTuple, Optional, Set, Tuple

import helper
from helper import (Point, bottom_row, flip, left_column, right_column,
                    rotate90, top_row)

Matrix = Tuple[Tuple[str, ...], ...]

TILE_WIDTH = TILE_HEIGHT = 10


def rotate_and_flip_in_every_possible_way(matrix: Matrix) -> List[Matrix]:
    """
    It will make a list of 8 variations of the received matrix.
    """
    result: List[Matrix] = []

    m = matrix
    for _ in range(4):
        result.append(m)
        m = rotate90(m)
    #
    m = flip(m)
    for _ in range(4):
        result.append(m)
        m = rotate90(m)
    #
    return result


class Tile:
    def __init__(self, _id: int, matrix: List[Tuple[str, ...]]) -> None:
        self._id: int = _id
        self._original: Matrix = tuple(matrix)
        self.variations: List[Matrix] = rotate_and_flip_in_every_possible_way(self._original)
        # the indices of the variations go from 0 to 7 (incl.)
        # self.index_of_selected_variation contains the index of the variation that was inserted in the puzzle
        # -1 means that this tile was not yet inserted in the puzzle
        self.index_of_selected_variation = -1

    @staticmethod
    def empty(width):
        """
        Used for debug purposes. When the puzzle was not complete, it returned
        an empty tile. It served as a placeholder when visualizing the puzzle.
        """
        s = "." * width
        matrix = []
        for i in range(width):
            matrix.append(tuple(list(s)))
        #
        tile = Tile(-1, matrix)
        tile.index_of_selected_variation = 0
        return tile

    def get_selected_variation(self) -> Matrix:
        idx = self.index_of_selected_variation
        assert 0 <= idx <= 7
        return self.variations[idx]

    def get_tile_without_margins(self):
        """
        Required for Part 2.
        """
        return tuple([row[1:-1] for row in self.get_selected_variation()[1:-1]])

    def __str__(self) -> str:
        return str(self._id)

# endclass Tile


class Tiles:
    def __init__(self, parts: List[str]) -> None:
        self.list_of_tiles: List[Tile] = self.extract_tiles(parts)

    def to_tile(self, part: str) -> Tile:
        lines = part.splitlines()
        first, rest = lines[0], lines[1:]
        _id = int(first.split()[-1].replace(":", ""))
        matrix = []
        for row in rest:
            matrix.append(tuple(list(row)))
        #
        return Tile(_id, matrix)

    def extract_tiles(self, parts: List[str]) -> List[Tile]:
        result: List[Tile] = []
        for part in parts:
            result.append(self.to_tile(part))
        #
        return result

    def get_unused_tiles(self) -> List[Tile]:
        """
        Return the tiles that are not yet inserted in the puzzle.
        """
        return [tile for tile in self.list_of_tiles if tile.index_of_selected_variation == -1]

    # def __str__(self) -> str:
    #     sb = []
    #     for tile in self.list_of_tiles:
    #         sb.append(str(tile))
    #         sb.append("---")
    #     #
    #     return "\n".join(sb)

# endclass Tiles


class Puzzle:
    def __init__(self, tiles: Tiles) -> None:
        self.tiles: Tiles = tiles
        self.d: Dict[Point, Tile] = {}
        self.number_of_rows = int(math.sqrt(len(tiles.list_of_tiles)))
        self.number_of_columns = self.number_of_rows

    def insert_first_puzzle(self) -> None:
        tile = self.tiles.list_of_tiles[0]
        tile.index_of_selected_variation = 0
        self.d[Point(0, 0)] = tile
        # self.show_dictionary()

    def get_four_neighbor_positions(self, x: int, y: int):
        """
        Order: N, E, S, W
        """
        return [
            (x, y-1),   # north
            (x+1, y),   # east
            (x, y+1),   # south
            (x-1, y),   # west
        ]

    def find_empty_places(self) -> List[Point]:
        places: List[Point] = []
        bag: Set[Point] = set()

        for key in self.d.keys():
            x, y = key
            neighbors = self.get_four_neighbor_positions(x, y)
            for x, y in neighbors:
                if (x, y) not in self.d:
                    if (x, y) not in bag:
                        places.append(Point(x, y))
                        bag.add(Point(x, y))
                    #
                #
            #
        #
        return places

    def get_unused_tiles(self) -> List[Tile]:
        return self.tiles.get_unused_tiles()

    def matches(self, matrix: Matrix,
                      neighbors: List[Optional[Tile]]) -> bool:
        top_neighbor, right_neighbor, bottom_neighbor, left_neighbor = neighbors
        result = []
        if top_neighbor:
            nb = top_neighbor
            result.append(top_row(matrix) == bottom_row(nb.get_selected_variation()))
        if right_neighbor:
            nb = right_neighbor
            result.append(right_column(matrix) == left_column(nb.get_selected_variation()))
        if bottom_neighbor:
            nb = bottom_neighbor
            result.append(bottom_row(matrix) == top_row(nb.get_selected_variation()))
        if left_neighbor:
            nb = left_neighbor
            result.append(left_column(matrix) == right_column(nb.get_selected_variation()))
        #
        return all(result)

    def find_matching_tile(self, x: int, y: int,
                                 neighbor_positions: List[Point]) -> Optional[Tile]:
        """
        x, y: position of an empty place. It has at least one neighbor with a found puzzle.
        """
        top_neighbor: Optional[Tile] = self.d.get(neighbor_positions[0])
        right_neighbor: Optional[Tile] = self.d.get(neighbor_positions[1])
        bottom_neighbor: Optional[Tile] = self.d.get(neighbor_positions[2])
        left_neighbor: Optional[Tile] = self.d.get(neighbor_positions[3])
        neighbors: List[Optional[Tile]] = [
            top_neighbor,
            right_neighbor,
            bottom_neighbor,
            left_neighbor
        ]

        unused_tiles: List[Tile] = self.get_unused_tiles()
        # print("# unused tiles:", len(unused_tiles))
        for tile in unused_tiles:
            # print("# current tile:", tile)
            for idx, v in enumerate(tile.variations):
                if self.matches(v, neighbors):
                    # print("# matching tile:", tile)
                    tile.index_of_selected_variation = idx
                    return tile
                #
            #
        #
        return None

    def finished(self) -> bool:
        """
        Finished if all tiles have been inserted in the puzzle.
        That is, if there is no unused tiles left.
        """
        return len(self.get_unused_tiles()) == 0

    # def show_dictionary(self) -> None:
        # for key, tile in self.d.items():
            # print('#', key, "->", tile, f"({tile.index_of_selected_variation})")

    def start(self) -> None:
        self.insert_first_puzzle()

        # cnt = 0

        while not self.finished():

            # cnt += 1
            # if cnt == 2:
            #     self.debug()
            #     exit(1)

            empty_places: List[Point] = self.find_empty_places()
            for empty_place in empty_places:
                x, y = empty_place
                neighbor_positions = self.get_four_neighbor_positions(x, y)
                tile = self.find_matching_tile(x, y, neighbor_positions)
                if tile:
                    self.d[Point(x, y)] = tile
                    # self.show_dictionary()
                    break
                #
            #
        #

    def show_ids(self):
        topleft_x = min(x for x, y in self.d.keys())
        topleft_y = min(y for x, y in self.d.keys())
        for row in range(topleft_y, topleft_y + self.number_of_rows):
            for col in range(topleft_x, topleft_x + self.number_of_columns):
                tile = self.d[Point(x=col, y=row)]
                print(tile._id, end=" ")
            #
            print()
        #

    def show_content(self) -> None:
        topleft_x = min(x for x, y in self.d.keys())
        topleft_y = min(y for x, y in self.d.keys())
        for row in range(topleft_y, topleft_y + self.number_of_rows):
            tiles_in_row = []
            for col in range(topleft_x, topleft_x + self.number_of_columns):
                tile = self.d.get(Point(x=col, y=row), Tile.empty(TILE_WIDTH))
                matrix = tile.get_selected_variation()
                # matrix = tile.get_tile_without_margins()
                tiles_in_row.append(matrix)
                # print(tile._id, end="; ")
            #
            for i in range(len(tiles_in_row[0])):
                line = ""
                for j in range(len(tiles_in_row)):
                    curr_row = tiles_in_row[j][i]
                    line += "".join(curr_row)
                    line += " "
                #
                # full_map.append(tuple(list(line)))
                print(line)
            #
            print()
        #

    def get_input_for_part2(self) -> str:
        """
        Transform each tile: remove the borders.
        Leave no gap between the tiles.
        """
        result = ""
        topleft_x = min(x for x, y in self.d.keys())
        topleft_y = min(y for x, y in self.d.keys())
        for row in range(topleft_y, topleft_y + self.number_of_rows):
            tiles_in_row = []
            for col in range(topleft_x, topleft_x + self.number_of_columns):
                tile = self.d.get(Point(x=col, y=row), Tile.empty(TILE_WIDTH))
                # matrix = tile.get_selected_variation()
                matrix = tile.get_tile_without_margins()
                tiles_in_row.append(matrix)
                # print(tile._id, end="; ")
            #
            for i in range(len(tiles_in_row[0])):
                line = ""
                for j in range(len(tiles_in_row)):
                    curr_row = tiles_in_row[j][i]
                    line += "".join(curr_row)
                    # line += " "
                #
                # full_map.append(tuple(list(line)))
                result += line.rstrip()
                result += "\n"
            #
            # result += "\n"
        #
        return result.rstrip()

    def get_result(self) -> int:
        topleft_x = min(x for x, y in self.d.keys())
        topleft_y = min(y for x, y in self.d.keys())
        offset = self.number_of_rows - 1    # number_of_rows == number_of_columns

        topleft = self.d[Point(topleft_x, topleft_y)]
        topright = self.d[Point(topleft_x + offset, topleft_y)]
        bottomleft = self.d[Point(topleft_x, topleft_y + offset)]
        bottomright = self.d[Point(topleft_x + offset, topleft_y + offset)]

        return topleft._id * topright._id * bottomleft._id * bottomright._id

# endclass Puzzle


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    parts: List[str] = parse(fname)

    tiles = Tiles(parts)

    puzzle = Puzzle(tiles)
    puzzle.start()
    puzzle.show_ids()
    print()
    print("Part 1:", puzzle.get_result())
    print()
    puzzle.show_content()

    # for Part 2
    if True:
        matrix: str = puzzle.get_input_for_part2()

        with open("input_for_part2.txt", "w") as f:
            print(matrix, file=f)
            print("input_for_part2.txt was created successfully")


def parse(fname: str) -> List[str]:
    content: str = helper.read(fname).strip()
    return content.split("\n\n")

##############################################################################

if __name__ == "__main__":
    main()
