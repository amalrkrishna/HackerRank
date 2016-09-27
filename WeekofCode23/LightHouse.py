#!/bin/python

__author__ = "Amal Krishna R"

def circle(r):
    if r == 0:
        return [[1]]
    grid = []
    for x in xrange(-r, r+1):
        for y in xrange(-r, r+1):
            if (x*x+y*y)<=(r*r):
                grid.append((x,y))
    return grid

def search(n, grid):
    maxr = (n-1)/2
    for k in xrange(maxr, 0, -1):
        kk = k*2+1
        cgrid = circle(k)
        for x in xrange(k, n-k):
            for y in xrange(k, n-k):
                gg = [ (a+x, b+y) for a,b in cgrid ]
                if all( grid[a][b] == '.' for a,b in gg ):
                    return k
    return 0

n = input()
grid = []
for nn in xrange(n):
    grid.append( raw_input().strip() )
print search(n,grid)

