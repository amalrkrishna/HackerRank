#!/bin/python3

__author__ = "Amal Krishna R"

import sys

t = int(input().strip())
for _ in range(t):
    n,m = map(int,input().strip().split(' '))
    ilst = [i for i in range(n)]
    vlst = [0 for i in range(n)]
    total = 0
    inc = 0
    redun = 0
    for _ in range(m):
        x,y = map(int,input().strip().split(' '))
        x -= 1
        y -= 1
        while ilst[x] != x:
            x = ilst[x]
        while ilst[y] != y:
            y = ilst[y]
        if ilst[x] != ilst[y]:
            vlst[y] += vlst[x] + 1
            vlst[x] = 0
            ilst[x] = y
        else:
            redun += 1
    mlst = [el for el in vlst if el != 0]
    mlst.sort(reverse = True)
    for el in mlst:
        total += inc * el  + (el * (el + 1) * (el + 2)) // 3
        inc += el * (el + 1)
    total += redun * inc
    print(total)

