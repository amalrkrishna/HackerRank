#!/bin/python3

__author__ = "Amal Krishna R"

import sys
import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


n = int(input().strip())
sumarray = []
array = list(divisorGenerator(n))
for i in range(len(array)):
    sumarray.append(sum(map(int,str(array[i]))))
print(array[sumarray.index(max(sumarray))])
