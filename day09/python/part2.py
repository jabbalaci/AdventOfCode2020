#!/usr/bin/env python3

import helper
import part1

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


def find_sum(goal, numbers):
    i = -1

    while True:
        i += 1
        data = [numbers[i]]
        j = i
        while True:
            j += 1
            data.append(numbers[j])
            if len(data) >= 2:
                summa = sum(data)
                if summa == goal:
                    return data
                if summa > goal:
                    break
            #
        #
    #


def main():
    # settings = 'example'
    settings = 'input'

    fname = config[settings]['fname']
    window = config[settings]['WINDOW']

    lines = helper.read_lines_as_ints(fname)
    invalid_number = part1.get_result(fname, window)

    print("invalid_number:", invalid_number)
    data = find_sum(invalid_number, lines)
    print("contiguous sum makers:", data)
    result = min(data) + max(data)
    print()
    print(f"result: {result}")

##############################################################################

if __name__ == "__main__":
    main()
