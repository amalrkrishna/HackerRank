#!/bin/python

__author__ = "Amal Krishna R"

x,y=map(float, raw_input().split())
a,b=map(float, raw_input().split())
div=a**2+b**2
print "%.12f" % ((a*x+b*y)/div)
print "%.12f" % ((a*y-b*x)/div)
