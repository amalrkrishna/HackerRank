#!/bin/python3

__author__ = "Amal Krishna R"

n, count = map(int, input().split())
sgn = 1
rot = 0
for i in range(count):
    t, k = map(int, input().split())
    t = 3 - 2 * t
    sgn *= t
    rot = k + t * rot
print((3 - sgn) // 2, (-sgn * rot) % n)
