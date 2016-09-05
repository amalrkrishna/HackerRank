#!/bin/python3

__author__ = "Amal Krishna R"


def gcd_ext(a, b):
    s = 0
    t = 1
    while b:
        q, r = divmod(a, b)
        s, t = t, s - q * t
        a, b = b, r
    return s

def cache_factorials(n, p):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[-1] * i % p)
    inv_factorials = [gcd_ext(p, factorials[n])]
    for i in range(n, 0, -1):
        inv_factorials.append(inv_factorials[-1] * i % p)
    inv_factorials.reverse()
    return factorials, inv_factorials

def main():
    p = 10 ** 9 + 7
    f, inv_f = cache_factorials(200002, p)
    for i in range(int(input())):
        m, a = map(int, input().split())
        result = f[a + m + 1] * f[a + m + 2] * inv_f[a + 1] * inv_f[a + 2]
        result *= gcd_ext(p, pow(2, m, p))
        print(result % p)
        
main()
