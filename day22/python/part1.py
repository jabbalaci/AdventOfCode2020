#!/usr/bin/env python3

from collections import deque
from typing import Deque, List, Tuple

import helper


def start(player1: Deque[int], player2: Deque[int]):
    p1 = player1.copy()
    p2 = player2.copy()

    while p1 and p2:
        a = p1.popleft()
        b = p2.popleft()
        tmp = p1 if a > b else p2
        two = sorted([a, b], reverse=True)
        tmp.append(two[0])
        tmp.append(two[1])
    #
    return p1 if p1 else p2


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    part1, part2 = parse(fname)
    p1 = deque(part1)
    p2 = deque(part2)

    q = start(p1, p2)
    # print(q)
    values = range(1, len(q)+1)[::-1]
    result = sum(a * b for a, b in zip(q, values))
    print(result)


def parse(fname: str) -> Tuple[List[int], List[int]]:
    content = helper.read(fname)
    part1, part2 = content.split("\n\n")
    p1 = [int(x) for x in part1.splitlines()[1:]]
    p2 = [int(x) for x in part2.splitlines()[1:]]

    return p1, p2

##############################################################################

if __name__ == "__main__":
    main()
