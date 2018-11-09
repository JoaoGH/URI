# -*- coding: utf-8 -*-
d=int(input())
a=0
m=0
while(d>=365):
    d-=365
    a+=1
while(d>=30):
    d-=30
    m+=1
# while(m==12):
#     m-=12
#     a+=1
print(a,"ano(s)")
print(m,"mes(es)")
print(d,"dia(s)")