#!/usr/bin/env python3

from functools import lru_cache
from typing import Dict, List

import helper


class Program:
    def __init__(self, lines: List[str]) -> None:
        self.lines = lines
        self.length = 36
        self.mask = ""    # will be set later
        self.mem: Dict[int, int] = {}

    def to_bin(self, decimal: int) -> str:
        s = bin(decimal)[2:]
        return "{0}{1}".format("0" * (self.length - len(s)), s)

    def use_mask(self, bin_address: str) -> str:
        result = ""
        for mask, value in zip(self.mask, bin_address):
            if mask in ('1', 'X'):
                result += mask
            elif mask == '0':
                result += value
            else:
                raise Exception()    # we should never get here
            #
        #
        return result

    @lru_cache
    def get_combinations(self, value):
        value = 2 ** value
        length = len(bin(value-1)[2:])
        return [bin(i)[2:].zfill(length) for i in range(value)]

    def set_value_in_memories(self, address: int, value: int) -> None:
        bin_address = self.to_bin(address)
        template_after_mask = self.use_mask(bin_address)
        # print(template_after_mask)
        # print()
        combinations = self.get_combinations(template_after_mask.count('X'))
        # print(combinations)
        for combo in combinations:
            template = list(template_after_mask)
            j = 0
            for i in range(len(template)):
                if template[i] == 'X':
                    template[i] = combo[j]
                    j += 1
                #
            #
            mem_address = int("".join(template), 2)
            self.mem[mem_address] = value
        #

    def get_result(self) -> int:
        return sum(self.mem.values())

    def start(self) -> None:
        for line in self.lines:
            if line.startswith("mask"):
                parts = line.split()
                self.mask = parts[-1]
            elif line.startswith("mem"):
                parts = line.replace("mem[", "").replace("]", "").split("=")
                address = int(parts[0].strip())
                value = int(parts[1].strip())
                self.set_value_in_memories(address, value)
            #
        #


def main() -> None:
    # lines = helper.read_lines("example2.txt")
    lines = helper.read_lines("input.txt")

    prg = Program(lines)
    prg.start()

    print(prg.get_result())

##############################################################################

if __name__ == "__main__":
    main()
