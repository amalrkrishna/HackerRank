#!/bin/python

__author__ = "Amal Krishna R"

from itertools import groupby

n = int(raw_input())
A = raw_input().strip().split(' ')
A = map(int, A)
As = sorted(A)
B = [len(list(group)) for key, group in groupby(As)]

print len(As)-max(B)


