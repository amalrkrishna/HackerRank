#!/bin/python3

__author__ = "Amal Krishna R"

import sys

def fillMat(n, k, mat, array):
    for i in range(1, n):
        iLnum = int(array[i])
        for j in range(k):
            mat[i][j] = mat[i-1][j]
        for j in range(k):
            nj = ((j*10) + iLnum) % k
            mat[i][nj] = modAdd(a=mat[i][nj],b=mat[i-1][j],mod=1000000007)
        if i-2 >= 0:
            mat[i-2] = None 
    return mat

def buildMat(n, k, array):
    mat = []
    for _ in range(n):
        mat.append([0] * k)
    mat[0][0] += 1
    mat[0][int(array[0]) % k] += 1
    return mat

def modAdd(a, b, mod) -> int:
    return ((a % mod) + (b % mod)) % mod

n = int(input())
lucky_num = input()
k = 8
mat = buildMat(n,k, lucky_num)
filledMat = fillMat(n, k, mat, lucky_num)
finalAns = filledMat[-1][0] - 1 
if finalAns < 0:
	finalAns = 0
print(finalAns % 1000000007)

