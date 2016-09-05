#!/bin/python

__author__ = "Amal Krishna R"

def factor_all(limit):
    ans = [None] + [dict() for i in xrange(limit)]
    for x in xrange(2,limit+1):
        if len(ans[x]) > 0:
            continue
        for y in xrange(x,limit+1,x):
            z, count = y,0
            while z % x == 0:
                z = z/x
                count += 1
            ans[y][x] = count
    
    return ans

def count(a):
    fac = factor_all(10**5)
    for i in xrange(len(a)-1, 1,-1):
        if a[i] == -1:
            continue
        
        for p,e in fac[i].iteritems():
            x = 1
            for j in xrange(1,e+1):
                x *= p
                if a[x] == -1:
                    a[x] = a[i] % x
                if a[x] != a[i] % x:
                    return 0
    ans = 1    
    for i in xrange(2,len(a)):
        if a[i] != -1 or len(fac[i]) > 1:
            continue

        p = fac[i].keys()[0]
        ans = (ans * p) % (10**9 + 7)

    return ans

n = int(raw_input())
a = [None] + map(int, raw_input().split())
print count(a)
