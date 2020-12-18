#!/usr/bin/env python3

from typing import List

import helper


class Homework:
    def __init__(self, line: str) -> None:
        self.line = line

    def my_split(self, line: str) -> List[str]:
        result = []
        parts = line.split()
        cnt = 0
        tmp = []
        for part in parts:
            tmp.append(part)
            cnt += part.count("(")
            cnt -= part.count(")")
            if cnt == 0:
                result.append(" ".join(tmp))
                tmp = []
            #
        #
        return result

    def evaluate(self, expression: str) -> int:
        parts = self.my_split(expression)
        # print(parts)
        # return

        if len(parts) == 1:
            value = parts[0]
            if value.isdigit():
                return int(value)
            elif value.startswith("("):
                value = value[1:-1]
                return self.evaluate(value)
            else:
                raise Exception()    # we should never get here
        # else
        while ("+" in parts):
            pos = parts.index("+")
            a = self.evaluate(parts[pos - 1])
            b = self.evaluate(parts[pos + 1])
            parts[(pos-1):(pos+1+1)] = [str(a + b)]

        while ("*" in parts):
            pos = parts.index("*")
            a = self.evaluate(parts[pos - 1])
            b = self.evaluate(parts[pos + 1])
            parts[(pos-1):(pos+1+1)] = [str(a * b)]

        return self.evaluate(" ".join(parts))

    def get_value(self) -> int:
        result = self.evaluate(self.line)
        return result

    def __str__(self) -> str:
        return self.line


def main() -> None:
    # line = "2 + 3"    # 5
    # line = "2 * 4"    # 8
    # line = "1 + 2 * 3 + 4 * 5 + 6"    # 231
    # line = "1 + (2 * 3) + (4 * (5 + 6))"    # 51
    # line = "2 * 3 + (4 * 5)"    # 46
    # line = "5 + (8 * 3 + 9 + 3 * 4 * 3)"    # 1445
    # line = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"    # 669060
    # line = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"    # 23340

    # hw = Homework(line)
    # print(hw)
    # print(hw.get_value())

    lines: List[str] = helper.read_lines("input.txt")
    total = 0
    for line in lines:
        hw = Homework(line)
        total += hw.get_value()
    #
    print(total)

##############################################################################

if __name__ == "__main__":
    main()
