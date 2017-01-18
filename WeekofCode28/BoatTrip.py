#!/bin/python

__author__ = "Amal Krishna R"

import sys


n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))

if c*m >= max(p):
    print "Yes"
else:
    print "No"
