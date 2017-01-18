#!/bin/python3

__author__ = "Amal Krishna R"

import sys

def f(x):
    return x + 1 if x % 2 == 1 else x - 1

g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    p = [int(p_temp) for p_temp in input().strip().split(' ')]
    xor = 0
    for x in p:
        xor ^= f(x)
    print('L' if xor == 0 else 'W')



