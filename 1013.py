# -*- coding: utf-8 -*-
import math

valor = input().split(" ")

a, b, c = valor
a=int(a)
b=int(b)
c=int(c)
m=(a+b+abs(a-b))/2
m=int(m)
r=(m+c+abs(m-c))/2

print(r,"eh o maior")