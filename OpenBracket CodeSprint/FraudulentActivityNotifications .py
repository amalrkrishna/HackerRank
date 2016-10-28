#!/bin/python3

__author__ = "Amal Krishna R"

n,d = input().strip().split(' ')
n,d = [int(n),int(d)]
moneys = [int(money) for money in input().strip().split(' ')]
notification=0

med = moneys[:d]

def findIdx(st,ed,v):
	if(med[st]==v):
		return st
	if(med[ed]==v):
		return ed
	if st==ed or st+1==ed:
		return ed

	if med[int((st+ed)/2)]<=v:
		return findIdx(int((st+ed)/2),ed,v)
	else:
		return findIdx(st,int((st+ed)/2),v)

med.sort()

for i in range(d,n):
	if d%2==1:
		m = med[int(d/2)]*2
	else:
		m = med[int(d/2)]+med[int(d/2)-1]
	if moneys[i]>=m:
		notification+=1
	del med[findIdx(0,d-1,moneys[i-d])]
	med.insert(findIdx(0,d-2,moneys[i])+1,moneys[i])

print(notification)
