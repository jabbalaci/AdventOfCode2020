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
        stack = []
        for part in parts:
            if part.startswith("("):
                part = part[1:-1]
                part = str(self.evaluate(part))
            #
            stack.append(part)
            if len(stack) == 3:
                b = int(stack.pop())
                op = stack.pop()
                a = int(stack.pop())
                if op == '+':
                    stack.append(str(a + b))
                elif op == '*':
                    stack.append(str(a * b))
                else:
                    raise Exception()    # we should never get here
                #
            #
        #
        return int(stack.pop())

    def get_value(self) -> int:
        result = self.evaluate(self.line)
        return result

    def __str__(self) -> str:
        return self.line


def main() -> None:
    # line = "1 + 2 * 3 + 4 * 5 + 6"    # 71
    # line = "1 + (2 * 3) + (4 * (5 + 6))"    # 51
    # line = "2 * 3 + (4 * 5)"    # 26
    # line = "5 + (8 * 3 + 9 + 3 * 4 * 3)"    # 437
    # line = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"    # 12240
    # line = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"    # 13632

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
