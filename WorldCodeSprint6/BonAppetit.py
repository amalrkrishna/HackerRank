#!/bin/python

__author__ = "Amal Krishna R"

from __future__ import division
    
n, k = raw_input().strip().split(' ')
s = raw_input()
items = map(int, s.split())
c = raw_input()

del items[int(k)]
avg = sum(items)/2
if int(avg) < int(c):
    print int(c)-int(avg)
else:
    print "Bon Appetit"
