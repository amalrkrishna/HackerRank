#!/bin/python

__author__ = "Amal Krishna R"

import sys

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
if n==1:
    print 2
elif n==2:
    if a[0]==a[1]:
        print 2
    else:
        print 1
else:
    a.sort()
    if a[0]==a[-1]:
        print 0
    if sum(a)-a[-1]>a[-1]:
        print 0
    else:
        print 1
