#!/usr/bin/env python3

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

    def use_mask(self, bin_value: str) -> str:
        result = ""
        for mask, value in zip(self.mask, bin_value):
            if mask == 'X':
                result += value
            else:
                result += mask
            #
        #
        return result

    def set_value_in_memory(self, address: int, value: int) -> None:
        bin_value = self.to_bin(value)
        after_mask = self.use_mask(bin_value)
        new_decimal = int(after_mask, 2)
        # print(after_mask)
        # print(new_decimal)
        self.mem[address] = new_decimal

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
                self.set_value_in_memory(address, value)


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    prg = Program(lines)
    prg.start()

    print(prg.get_result())

##############################################################################

if __name__ == "__main__":
    main()
