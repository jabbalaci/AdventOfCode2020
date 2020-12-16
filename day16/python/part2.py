#!/usr/bin/env python3

import math
from typing import Dict, List, Tuple


def rows_to_columns(rows: List[List[int]]) -> Dict[int, List[int]]:
    d: Dict[int, List[int]] = {}
    for i in range(len(rows[0])):
        lst = []
        for j in range(len(rows)):
            lst.append(rows[j][i])
        #
        d[i] = sorted(lst)
    #
    return d


class TrainStation:
    #
    def __init__(self, part1: str, part2: str, part3: str) -> None:
        self.d: Dict[str, List[Tuple[int, int]]] = self.extract_fields_with_ranges(part1)
        self.tickets = self.get_tickets(part2, part3)
        self.your_ticket = self.tickets[0].copy()
        self.columns: Dict[int, List[int]] = {}    # will be set later
        self.associations: Dict[int, str] = {}

    def start(self) -> None:
        self.delete_invalid_tickets()
        # print(len(self.tickets), self.tickets)
        self.columns = rows_to_columns(self.tickets)
        # print(self.columns)
        self.which_field_is_which()

    def which_field_is_which(self) -> None:
        stop = False

        while not stop:
            for col_id, col_values in self.columns.items():
                candidates = self.find_candidate_fields(col_values)
                occupied = self.associations.values()
                candidates = list(set(candidates).difference(set(occupied)))
                if len(self.associations) == len(self.d):
                    stop = True
                    break
                if len(candidates) == 1:
                    self.associations[col_id] = candidates[0]
                # print(col_values, candidates)
            #
        #
        print(self.associations)

    def is_in(self, numbers, ranges):
        # print(numbers)
        # print(ranges)

        result = []
        for n in numbers:
            tmp = []
            for a, b in ranges:
                tmp.append(a <= n <= b)
            #
            result.append(any(tmp))
        #
        res = all(result)
        # print(res)
        # print("--------")
        return res

    def find_candidate_fields(self, numbers: List[int]) -> List[str]:
        result: List[str] = []
        for name, ranges in self.d.items():
            if self.is_in(numbers, ranges):
                result.append(name)
            #
        #
        return result

    def get_tickets(self, your_ticket: str, nearby_tickets: str) -> List[List[int]]:
        line = your_ticket.splitlines()[1]
        lines = nearby_tickets.splitlines()[1:]
        #
        lines = [line] + lines
        result = []
        for line in lines:
            result.append([int(x) for x in line.split(",")])
        #
        return result

    def extract_fields_with_ranges(self, text: str) -> Dict[str, List[Tuple[int, int]]]:
        d: Dict[str, List[Tuple[int, int]]] = {}
        for line in text.splitlines():
            key, right = line.split(": ")
            ranges = right.split(" or ")
            lst = []
            for r in ranges:
                parts = r.split("-")
                a = int(parts[0])
                b = int(parts[1])
                lst.append((a, b))
            #
            key = key.replace(" ", "_")
            d[key] = lst
        #
        return d

    def contains(self, n: int) -> bool:
        for key, lst in self.d.items():
            for a, b in lst:
                if a <= n <= b:
                    return True
                #
            #
        #
        return False

    def get_part1_result(self) -> int:
        total = 0
        flat_list = (n for sublist in self.tickets for n in sublist)

        for n in flat_list:
            if not self.contains(n):
                total += n
            #
        #
        return total

    def get_part2_result(self) -> int:
        lst = []
        for idx, name in self.associations.items():
            if name.startswith("departure"):
                lst.append(self.your_ticket[idx])
            #
        #
        print(lst)
        print()
        return math.prod(lst)

    def all_numbers_valid(self, sublist: List[int]) -> bool:
        for n in sublist:
            if not self.contains(n):
                return False
            #
        #
        return True

    def delete_invalid_tickets(self) -> None:
        result = [lst for lst in self.tickets if self.all_numbers_valid(lst)]
        self.tickets = result
# endclass


def main() -> None:
    # fname = "example.txt"
    # fname = "example2.txt"
    fname = "input.txt"

    with open(fname) as f:
        content = f.read()
    #
    parts = content.split("\n\n")

    ts = TrainStation(parts[0], parts[1], parts[2])
    # print(ts.d)
    # print(len(ts.tickets), ts.tickets)
    print("Part 1:", ts.get_part1_result())
    print()
    ts.start()
    print()
    print("Part 2:", ts.get_part2_result())

##############################################################################

if __name__ == "__main__":
    main()
