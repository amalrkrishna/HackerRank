#!/bin/python3

__author__ = "Amal Krishna R"

q = int(input())

for query in range(q):
    n = int(input())
    points = list()
    max_x, max_y = -99999, -99999
    min_x, min_y = 99999, 99999 

    for point in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    on_rectangle = True

    for point in points:
        if point[0] in (max_x, min_x):
            pass
        elif point[1] in (max_y, min_y):
            pass
        else: 
            on_rectangle = False
            break
    if on_rectangle:
        print("YES")
    else:
        print("NO")
