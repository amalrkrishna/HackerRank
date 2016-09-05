#!/bin/python

__author__ = "Amal Krishna R"

size,k = [int(x) for x in raw_input().split()]
tower = [int(x) for x in raw_input().split()]
power = [False for x in tower]

on = 0
okok = True
for i in range(size):
    if not power[i]:
        ok = False
        for j in range(max(0,i-k), min(size,i+k))[::-1]:
            if tower[j] == 1:
                for ii in range(max(0,j-k), min(size,j+k)):
                    power[ii] = True
                on += 1
                ok = True
                break
        if not ok:
            okok = False
            break
            
if okok:
    print on
else:
    print -1
