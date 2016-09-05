#!/bin/python

__author__ = "Amal Krishna R"

n1, n2, n3 = map(int, raw_input().split())
a1 = map(int, raw_input().split())
a2 = map(int, raw_input().split())
a3 = map(int, raw_input().split())

a1.reverse()
a2.reverse()
a3.reverse()


x = dict()
s = 0
x[0] = 3
for i in xrange(n1):
    s += a1[i]
    if s in x:
        x[s] += 1
    else:
        x[s] = 1
s = 0
for i in xrange(n2):
    s += a2[i]
    if s in x:
        x[s] += 1

mx = 0

s = 0
for i in xrange(n3):
    s += a3[i]
    if s in x:
        x[s] += 1
        if x[s] == 3:
            mx = max(mx, s)

print(mx)
