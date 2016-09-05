#!/bin/python

__author__ = "Amal Krishna R"

n = int(raw_input())
X = [int(i) for i in raw_input().split(' ')]
Y = [int(i) for i in raw_input().split(' ')]

X.sort()
Y.sort()

Z = [x - y for x, y in zip(X, Y)]

if sum(Z) != 0:
    print -1
else:
    print sum([abs(z) for z in Z]) / 2
