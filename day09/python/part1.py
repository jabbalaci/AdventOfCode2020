#!/usr/bin/env python3

from itertools import combinations

import helper

config = {
    'example': {
        'fname': 'example.txt',
        'WINDOW': 5
    },
    'input': {
        'fname': 'input.txt',
        'WINDOW': 25
    }
}


def check(summa, numbers):
    for a, b in combinations(numbers, 2):
        if (a + b == summa) and (a != b):
            return True
        #
    #
    return False


def get_result(fname, window):
    lines = helper.read_lines_as_ints(fname)
    for i in range(window, len(lines)):
        curr = lines[i]
        prev_window = lines[(i-window):i]
        # print(curr, prev_window)
        if not check(curr, prev_window):
            return curr


def main():
    # settings = 'example'
    settings = 'input'

    fname = config[settings]['fname']
    window = config[settings]['WINDOW']

    result = get_result(fname, window)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
