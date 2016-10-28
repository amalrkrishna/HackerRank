#!/bin/python3

__author__ = "Amal Krishna R"

import sys
import collections

def all_happy(ladybugs):
    """Assumes no empty cells."""
    for i, bug in enumerate(ladybugs):
        try:
            left = ladybugs[i - 1]
        except IndexError:
            left = None
        try:
            right = ladybugs[i + 1]
        except IndexError:
            right = None
        if bug not in (left, right):
            return False
    return True


Q = int(input().strip())

for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    
    counter = collections.Counter(b)
    empty_cells = counter["_"]
    del counter["_"]
    
    if 1 in counter.values():
        print("NO")
    elif empty_cells == 0 and not all_happy(b):
        print("NO")
    else:
        print("YES")

