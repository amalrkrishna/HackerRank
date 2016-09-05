#!/bin/python

__author__ = "Amal Krishna R"

import sys
import math

n, m = raw_input().strip().split(' ')
guests, cookies = [int(n), int(m)]

if guests >= cookies:
    print guests - cookies
else:
    print int((math.ceil(cookies / float(n)) * guests) - cookies)
