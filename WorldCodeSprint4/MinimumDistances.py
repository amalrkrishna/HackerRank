#!/bin/python

__author__ = "Amal Krishna R"

import sys

n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
r=n+1
for i in range(n):
    for j in range(i+1,n):
        if A[j]==A[i]:
            r=min(j-i,r)
if r<=n:
    print r
else:
    print -1
