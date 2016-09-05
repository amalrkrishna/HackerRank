#!/bin/python

__author__ = "Amal Krishna R"

n=map(int,str(raw_input('')).split(' '))
m=map(int,str(raw_input('')).split(' '))
ans=0
from math import sqrt
for i in range(0,5):
    ans+=min(int(sqrt((n[i]-m[i])**2)),10-int(sqrt((n[i]-m[i])**2)))
print ans
