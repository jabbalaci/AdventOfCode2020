#!/usr/bin/env python3

"""
This solution is specific to my input.
The solution is based on the Chinese Remainder Theorem.

Thanks to Mocsa and Szöszi.
Without their help I wouldn't have figured out how to solve this :)
"""


def main() -> None:
    line = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,379,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
    parts = line.split(",")

    # for idx, value in enumerate(parts):
        # if value != 'x':
            # print(f"(x + {idx}) % {value} = 0")

    original = 2_429_011    # 379 * 13 * 17 * 29
    i = 100_000_000_000_000 // 2_429_011

    while True:
        x = i * original - 41
        if (x + 0) % 41 == 0 and \
           (x + 35) % 37 == 0 and \
           (x + 41) % 379 == 0 and \
           (x + 49) % 23 == 0 and \
           (x + 54) % 13 == 0 and \
           (x + 58) % 17 == 0 and \
           (x + 70) % 29 == 0 and \
           (x + 72) % 557 == 0 and \
           (x + 91) % 19 == 0:
            print(x)
            break
        #
        i += 1

##############################################################################

if __name__ == "__main__":
    main()
