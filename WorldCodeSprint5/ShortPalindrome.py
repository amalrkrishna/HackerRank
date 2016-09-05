#!/bin/python

__author__ = "Amal Krishna R"

mod = 10**9 + 7
s = raw_input().strip()

ccounts = [0]*26
for c in s:
    ccounts[ord(c)-97] += 1
tot = 0
pair_counts = [[0]*26 for i in xrange(26)]
behind_char_counts = [0]*26
for c in s:
    c = ord(c) - 97
    ccounts[c] -= 1
    for x in xrange(26):
        tot += pair_counts[x][c] * ccounts[x]
    for j in xrange(26):
        pair_counts[j][c] += behind_char_counts[j]
    behind_char_counts[c] += 1

print tot % mod
