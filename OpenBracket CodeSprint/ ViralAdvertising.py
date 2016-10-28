#!/bin/python3

__author__ = "Amal Krishna R"

n = int(input())

k = 5
total = 0

for i in range(n):
	total += k // 2
	k = (k // 2) * 3

print(total)
	
