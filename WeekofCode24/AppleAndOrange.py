#!/bin/python3

__author__ = "Amal Krishna R"

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
a_dist_list = [a + appd for appd in apple]
o_dist_list = [b + od for od in orange]
a_c = 0
o_c = 0

for apple_temp in a_dist_list:
    if s <= apple_temp <= t:
        a_c += 1
for orange_temp in o_dist_list:
    if s <= orange_temp <= t:
        o_c += 1
print(a_c)
print(o_c)
