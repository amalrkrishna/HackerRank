#!/bin/python3

__author__ = "Amal Krishna R"

dp = []
s1, s2 = None, None
def is_solve(n1, n2):
    if n1 == -1 and n2 == -1:
        return True
    if n1 == -1:
        return False
    if n2 == -1:
        return (s1[:n1+1].lower() == s1[:n1+1])
            
    if dp[n1][n2] != -1: return dp[n1][n2]
        
    sol = (is_solve(n1-1, n2) and s1[n1].lower() == s1[n1]) or (is_solve(n1-1, n2-1) and s1[n1].lower() == s2[n2].lower())
    dp[n1][n2] = sol
    return sol

for i in range(int(raw_input())):
    s1,s2 = raw_input().strip(), raw_input().strip()
    dp = [[-1,]*len(s2) for k in range(len(s1))]
    print("YES" if is_solve(len(s1)-1, len(s2)-1) else "NO")
