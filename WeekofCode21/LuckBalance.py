#!/bin/python

__author__ = "Amal Krishna R"
    
n,k=map(int,raw_input().strip().split(' '));
sum=0
a=[]
imp_count=0;
i=0
while(i<n):
        a1,b=map(int,raw_input().strip().split(' '))
        if(b==1):
            imp_count=imp_count+1
            a.append(a1)
        else:
            sum=sum+a1     
        i=i+1
w=imp_count-k
a.sort()
i=0
while(i<len(a)):
        if(i<w):
            sum=sum-a[i];
        else:
            sum=sum+a[i];
        i=i+1
    
print sum
