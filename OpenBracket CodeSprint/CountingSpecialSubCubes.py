#!/bin/python3

__author__ = "Amal Krishna R"

def findMax(arr, s, indices, n):
    largest = 1
    for i in indices:
        cur = arr[s+i]
        if cur > largest:
            largest = cur
        elif cur == n:
            largest = n
            break
    return largest

def findSpecial(arr, k, n):
    temp = arr
    if k > 1:
        temp = []
        m = n - k + 2
        m2 = m*m
        indices = [0, 1, m, m+1, m2, m2+1, m2+m, m2+m+1]
        for i in range(m-1):
            start = m2*i
            for j in range(m-1):
                for z in range(m-1):
                    largest = findMax(arr, start, indices, n)
                    temp.append(largest)
                    start += 1
                start += 1
    return temp    
               
q = int(input())

for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    for k in range(1, n+1):
        arr = findSpecial(arr, k, n)
        print(arr.count(k), end=' ')
    print('')
