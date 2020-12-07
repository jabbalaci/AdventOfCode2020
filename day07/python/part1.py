#!/usr/bin/env python3

import reader
from pprint import pprint


class Search:
    def __init__(self, d, start="shiny_gold"):
        self.d = d
        self.start = start
        self.collect = set()

    def traverse(self, colored_bag):
        for key, lst in self.d.items():
            for cnt, bag in lst:
                if bag == colored_bag:
                    self.collect.add(key)
                    self.traverse(key)

    def go(self):
        self.traverse(self.start)


def main():
    # fname = "example.txt"
    fname = "input.txt"
    d = reader.process(fname)
    # pprint(d)

    search = Search(d)
    search.go()
    # print(search.collect)
    # print()
    print("result: {}".format(len(search.collect)))

##############################################################################

if __name__ == "__main__":
    main()
