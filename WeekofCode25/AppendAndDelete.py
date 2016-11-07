#!/bin/python3

__author__ = "Amal Krishna R"

import sys
import collections

s = input().strip()
t = input().strip()
k = int(input().strip())

count = 0
for i in range(min(len(s),len(t))):
    if s[i] != t[i]:
        count = i
        break
    else:
        count = i+1
        
d = len(s)-lead+len(t)-count

if k >= len(s)+len(t):
    print("Yes")
elif d <= k and (d % 2) == (k % 2):
    print("Yes")
else:
    print("No")
