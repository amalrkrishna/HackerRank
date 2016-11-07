#!/bin/python3

__author__ = "Amal Krishna R"

import sys
import collections

n,m=map(int,input().split())
a=map(int,input().split())
b=map(int,input().split())

count=0
for i in xrange(max(a),min(b)+1):
    for j in a:
        if i%j!=0:
            break
    else:
        for k in b:
            if k%i!=0:
                break
        else:
            count+=1
print(count)
