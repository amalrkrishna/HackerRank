#!/bin/python3

__author__ = "Amal Krishna R"

import sys
import collections

np = int(input())

for prob in range(np):
    a,b,d = (int(x) for x in input().split())
    m = max(a,b)
    t = (d + m - 1)
    if t > 1:
        print(t)
    elif d == 0:
        print(0)
    elif d == a or d == b:
        print(1)
    else:
        print(2)

