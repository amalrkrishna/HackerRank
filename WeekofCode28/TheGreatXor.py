#!/bin/python

__author__ = "Amal Krishna R"

import sys

q = int(raw_input().strip())
for a0 in xrange(q):
    x = long(raw_input().strip())
    # your code goes here
    i = 1
    a = 0
    while x > 1:
        if x & 1 == 0:
            a += i
        x >>= 1
        i *= 2
    print a


