#!/usr/bin/env python3

from collections import deque
from typing import Deque, Dict, Tuple

"""
Part 2

optimized version of Part 1
"""


class Sequence:
    def __init__(self, numbers: Tuple[int, ...]) -> None:
        self.d: Dict[int, Deque[int]] = {}
        self.numbers = [-1]
        for n in numbers:
            self.register(n)

    def register(self, n: int) -> None:
        idx = len(self.numbers)
        if n not in self.d:
            self.d[n] = deque([idx], maxlen=2)
        else:
            self.d[n].append(idx)
        #
        self.numbers.append(n)

    def step(self) -> None:
        last = self.numbers[-1]
        positions = self.d.get(last, deque())
        if len(positions) == 1:
            self.register(0)
        else:    # present twice or more
            a, b = positions
            self.register(b - a)

    def __str__(self) -> str:
        return str(self.numbers)


def main() -> None:
    # example = "0,3,6"    # 30_000_000th elem: 175594
    # example = "1,3,2"    # 30_000_000th elem: 2578
    # example = "2,1,3"    # 30_000_000th elem: 3544142
    # example = "1,2,3"    # 30_000_000th elem: 261214
    # example = "2,3,1"    # 30_000_000th elem: 6895259
    # example = "3,2,1"    # 30_000_000th elem: 18
    # example = "3,1,2"    # 30_000_000th elem: 362
    input_seq = "16,1,0,18,12,14,19"

    # to_process = example
    to_process = input_seq

    numbers = tuple(int(x) for x in to_process.split(","))
    # print(numbers)

    seq = Sequence(numbers)
    # print(seq)

    N = 30_000_000

    for i in range(N - len(seq.numbers) + 1):
        seq.step()

    print()
    print("result:", seq.numbers[-1])

##############################################################################

if __name__ == "__main__":
    main()
