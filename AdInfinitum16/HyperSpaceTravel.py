#!/bin/python3

__author__ = "Amal Krishna R"

from statistics import median
n, m = map(int, input().split())

points=[]
for _ in range(n):
    points.append(list(map(int, input().split())))
    
for i in range(m):
    vals = sorted(point[i] for point in points)
    if len(vals) % 2 == 0:
        vals.pop(len(vals) - 1)
    print(median(vals), end=" ")
