#!/bin/python

__author__ = "Amal Krishna R"

import sys


s = list(raw_input().strip())
count = 0
for i in range(len(s)):
    if s[i] == '_':
        count = count + 1
print count+1
