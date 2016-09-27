#!/bin/python

__author__ = "Amal Krishna R"

q = int(raw_input())
n = []
for i in range(q):
    n.append(int(raw_input()))
    
for i in range(q):
    if n[i] % 2 == 0:
        print "Yes"
    else:
        print "No"
