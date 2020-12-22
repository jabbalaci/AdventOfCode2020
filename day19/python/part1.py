#!/usr/bin/env python3

import re
from pprint import pprint
from typing import Dict, Any, Union
import helper


class RegExp:
    def __init__(self, rules: str) -> None:
        self.d: Dict[int, Any] = self.parse_rules(rules)
        self.regexp: str = self.build_regexp()

    def process(self, param: Union[int, tuple]) -> str:
        if isinstance(param, tuple):
            value = param
        else:
            n = param
            value = self.d[n]

        result = ""
        if isinstance(value, str):
            result = value
        elif isinstance(value, list):
            result = "("
            #
            lst = []
            for t in value:
                lst.append(self.process(t))
            #
            result += "|".join(lst)
            #
            result += ")"
        elif isinstance(value, tuple):
            result = "("
            for e in value:
                result += self.process(e)
            result += ")"
        else:
            raise Exception()    # we should never get here

        # print(result)
        return result

    def build_regexp(self) -> str:
        return "^" + self.process(self.d[0][0]) + "$"

    def parse_rules(self, rules: str) -> Dict[int, Any]:
        d: Dict[int, Any] = {}
        for line in rules.splitlines():
            l, right = line.split(": ")
            left = int(l)
            if '"' in right:
                d[left] = right.replace('"', "")
            else:
                parts = right.split(" | ")
                lst = []
                for part in parts:
                    numbers = [int(x) for x in part.split()]
                    lst.append(tuple(numbers))
                #
                d[left] = lst
        #
        return d


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    rules, lines = helper.read(fname).split("\n\n")

    reg = RegExp(rules)
    # pprint(reg.d)
    # pprint(reg.regexp)

    result = sum(1 for line in lines.splitlines() if re.match(reg.regexp, line))
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
