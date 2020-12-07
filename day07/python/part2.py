#!/usr/bin/env python3

import reader
from pprint import pprint


class Search:
    def __init__(self, d, start="shiny_gold"):
        self.d = d
        self.start = start
        self.total = 0

    def traverse(self, colored_bag, multiplier=1):
        lst = self.d[colored_bag]
        for cnt, bag in lst:
            self.total += multiplier * cnt
            self.traverse(bag, multiplier * cnt)

    def go(self):
        self.traverse(self.start)


def main():
    # fname = "example.txt"     # 32
    # fname = "example2.txt"    # 126
    fname = "input.txt"
    d = reader.process(fname)
    # pprint(d)

    search = Search(d)
    search.go()
    # print(search.collect)
    # print()
    print("result: {}".format(search.total))

##############################################################################

if __name__ == "__main__":
    main()
