#!/bin/python3

__author__ = "Amal Krishna R"

import sys
input=sys.stdin.readline

n,m=map(int,input().split())

c=list(map(int,input().split()))

g=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

# visit each connected component
a1=0
a2=1
vis=[0]*n
col=[0]*n   # temp colouring, 0 = not pick, 1 = pick
l1=[]
l2=[]

def getinfo(idx):
    # base case
    if idx==len(l1):
        # count
        out=0
        for i in l1:
            if col[i]:
                out+=c[i]
        return (out,1)
    # general case
    for i in g[l1[idx]]:
        if col[i]:
            return getinfo(idx+1)
    p1,p2=getinfo(idx+1)
    col[l1[idx]]=1
    q1,q2=getinfo(idx+1)
    col[l1[idx]]=0
    if p1==q1:
        return (p1,p2+q2)
    return max((p1,p2),(q1,q2))

for i in range(n):
    if not vis[i]:
        l1=[i]
        l2=[i]
        vis[i]=1
        while l2:
            u=l2.pop(-1)
            for v in g[u]:
                if not vis[v]:
                    l1.append(v)
                    l2.append(v)
                    vis[v]=1
        b1,b2=getinfo(0)
        a1+=b1
        a2*=b2

print("%s %s"%(a1,a2))

