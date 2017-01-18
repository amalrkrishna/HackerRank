#!/bin/python

__author__ = "Amal Krishna R"

import sys
import heapq as h

n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here
scores = list(set(scores))

h.heapify(scores)
for ai in alice:
    if scores != []:
        while ai >= scores[0]:
            h.heappop(scores)
            if scores == []:
                break
    print len(scores)+1

