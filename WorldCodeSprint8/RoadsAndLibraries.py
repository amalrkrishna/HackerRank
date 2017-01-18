#!/bin/python

__author__ = "Amal Krishna R"

import sys

def dfs(node, conned, flag):
    if flag[node]: return 0
    flag[node] = 1
    num = 1
    for nextNode in conned[node]:
        num += dfs(nextNode, conned, flag) 
    return num        

q = int(raw_input().strip())
for a0 in xrange(q):
    n,m,x,y = map(int, raw_input().split())
    conned = [[] for _ in xrange(n+1)]
    flag = [0] * (n+1)
    
    for a1 in xrange(m):
        city_1,city_2 = map(int, raw_input().split())
        conned[city_1].append(city_2)
        conned[city_2].append(city_1)

    ans = 0        
    for i in xrange(1, n+1):        
        if flag[i] > 0: continue
        num = dfs(i, conned, flag)            
        ans += min(num * x, x + (num-1) * y) 
    print ans  
