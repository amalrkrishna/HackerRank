#!/bin/python3

__author__ = "Amal Krishna R"

import sys

s = input().strip()
count = 0
for i in range(0,len(s)):
    if s[i].isupper() == 1:
        count = count+1  

print(count+1)
