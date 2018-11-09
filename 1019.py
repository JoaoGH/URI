# -*- coding: utf-8 -*-
s=int(input())
m=0
h=0
while(s>=60):
    s=s-60
    m+=1
while(m>=60):
    m=m-60
    h+=1

print(str(h)+":"+str(m)+":"+str(s))