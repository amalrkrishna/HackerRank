#!/bin/python3

__author__ = "Amal Krishna R"

import sys
import math
s1=[]
s2=[]
n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    s1.append(s)
for i in range(n):
    s2.append(''.join(set(s1[i])))
for i in range(len(s2)):    
    print(len(s2[i]))
