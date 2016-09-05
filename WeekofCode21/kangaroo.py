#!/bin/python

__author__ = "Amal Krishna R"

import sys
x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if x2>x1 and v2>v1:
    print "NO"
elif x1==x2:
    print "YES"
elif x1!=x2 and v1==v2:
    print "NO"
else:
    n=(x1-x2)/(float(v2-v1))
    if n>0 and int(n)==n:
        print "YES"
    else:
        print "NO"
