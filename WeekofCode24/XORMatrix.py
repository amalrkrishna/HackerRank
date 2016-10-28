#!/bin/python3

__author__ = "Amal Krishna R"

n, m = map(int, input().split())
ar = tuple(map(int, input().split()))
i = 1
m -= 1
while m:
    if m & 1:
        j = i % n
        ar = tuple(ar[pos] ^ ar[(pos + j) % n] for pos in range(n))
    m >>= 1
    i <<= 1
print(*ar)
