#!/bin/python3

__author__ = "Amal Krishna R"

import sys

n = int(input().strip())
array = map(int, input().split(" "))

waya = 0
sama = 0
samc = 0

for i in range(n):
    waya = waya + 1
    sama = array[i]
    if sama != waya:
        samc = samc + 1
        waya = sama
   
print(samc)
