#!/bin/python

__author__ = "Amal Krishna R"

from __future__ import division
q = int(raw_input())
finmatrix = []
for i in range(q):
    matrix = []
    n = int(raw_input())
    for i in range(2*n):
        matrix.append(map(int, raw_input().split(' ')))
    finmatrix.append(matrix)    

summ = {}
for i in range(len(finmatrix)):
    summ[i] = 0
    ran = int(len(finmatrix[i])/2)
    for k in range(ran):
        for j in range(ran):
            summ[i] = summ[i] + max(finmatrix[i][k][j],finmatrix[i][k][2*ran-1-j],finmatrix[i][2*ran-1-k][j],finmatrix[i][2*ran-1-k][2*ran-1-j])

for k,v in summ.items():
    print v

