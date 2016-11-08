#!/bin/python3

__author__ = "Amal Krishna R"

n, s = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

hist = {}

def sd(n, a):
    if n in hist.keys():
        return hist[n]
    for x in a:
        if n % x == 0:
            if x % 2 == 0:
                hist[n] = True
                return True
            nn = n // x
            if not foo(nn, a):
                hist[n] = True
                return True
    hist[n] = False
    return False

if sd(n,a):
    print("First")
else:
    print("Second")
