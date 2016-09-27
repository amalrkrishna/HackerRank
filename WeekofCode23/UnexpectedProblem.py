#!/bin/python

__author__ = "Amal Krishna R"

word = raw_input()
maxres = int(raw_input())

reslen = len(word)


if word[0] * reslen == word:
    reslen = 1
    
#elif RES_LEN % 2 == 0:
for i in xrange(1, reslen / 2 + 1):
    d, m = divmod(reslen, i)
        
    if m == 0:
        if d * word[:i] == word:
            reslen = i
            break
                
print (maxres / reslen) % (10**9 + 7)
