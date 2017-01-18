#!/bin/python3

__author__ = "Amal Krishna R"

import sys

n,p = input().strip().split(' ')
n,p = [int(n),int(p)]

arr={}
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count=0
for item in a:
    val=int(item/p) + (item % p!=0)
    o=val
    while val in arr:
        val=arr[val]+1
    arr[o]=val
    if o!=val:
        arr[val]=o-1
    count=count+val

print(count)



