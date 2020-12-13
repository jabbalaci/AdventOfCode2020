#!/usr/bin/env python3

from typing import List, Tuple

import helper


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines: List[str] = helper.read_lines("input.txt")

    timestamp: int = int(lines[0])
    buses: Tuple[int, ...] = tuple(int(item) for item in lines[1].split(",") if item != 'x')

    print(timestamp)
    print(buses)
    print("----------")

    can_go = True
    counter = timestamp
    while can_go:
        for n in buses:
            if counter % n == 0:
                print(counter)
                print(n)
                print("----------")
                result = (counter - timestamp) * n
                print("result:", result)
                can_go = False
                break
            #
        #
        counter += 1
    #

##############################################################################

if __name__ == "__main__":
    main()
