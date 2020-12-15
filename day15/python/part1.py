#!/usr/bin/env python3

from typing import List, Tuple


class Sequence:
    def __init__(self, numbers: Tuple[int, ...]) -> None:
        self.numbers = [-1] + list(numbers)

    def get_positions(self, value: int) -> List[int]:
        result = []
        for idx, elem in enumerate(self.numbers):
            if elem == value:
                result.append(idx)
            #
        #
        return result

    def step(self) -> None:
        last = self.numbers[-1]
        occurences = self.numbers.count(last)
        if occurences == 1:
            self.numbers.append(0)
        else:    # present twice or more
            last_two_positions = self.get_positions(last)[-2:]
            a, b = last_two_positions
            self.numbers.append(b - a)

    def __str__(self) -> str:
        return str(self.numbers)


def main() -> None:
    # example = "0,3,6"    # 2020th elem: 436
    # example = "1,3,2"    # 2020th elem: 1
    # example = "2,1,3"    # 2020th elem: 10
    # example = "1,2,3"    # 2020th elem: 27
    # example = "2,3,1"    # 2020th elem: 78
    # example = "3,2,1"    # 2020th elem: 438
    # example = "3,1,2"    # 2020th elem: 1836
    input_seq = "16,1,0,18,12,14,19"

    # to_process = example
    to_process = input_seq

    numbers = tuple(int(x) for x in to_process.split(","))
    # print(numbers)

    seq = Sequence(numbers)
    for i in range(2020 - len(seq.numbers) + 1):
        seq.step()

    # print(seq)
    # print()

    print("result:", seq.numbers[-1])

##############################################################################

if __name__ == "__main__":
    main()
