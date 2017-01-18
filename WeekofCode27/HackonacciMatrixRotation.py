#!/bin/python3

__author__ = "Amal Krishna R"

def hackonacci(n) :
    return [1,0,1,0,0,1,1][(n-1)%7]

def solve(n,A) :
    M = [[hackonacci((i*j)**2) for j in range(1,n+1)] for i in range(1,n+1)]
    count = {0:0,90:0,180:0,270:0}
    for i in range(n) :
        for j in range(n) :
            count[90] += M[i][j]^M[j][n-1-i]
            count[180] += M[i][j]^M[n-1-i][n-1-j]
            count[270] += M[i][j]^M[n-1-j][i]
    return list(count[a%360] for a in A)

n,q = map(int,input().split())
A = list(int(input()) for _ in range(q))
print("\n".join(map(str,solve(n,A))))



