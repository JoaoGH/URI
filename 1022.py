# # -*- coding: utf-8 -*-
v=int(input())
s=[]
n=[]
if(1<v<10**4):
    for i in range(v):
        s.insert(i,input())
        if(s[i].find("+")>1):
            n=(i,s[i].slipt(" "))
            print(n)
            # (N1 * D2 + N2 * D1) / (D1 * D2)
        elif(s[i].find("-")>1):
            print("sub")
        elif(s[i].find("*")>1):
            print("multi")
        elif(s[i].find("/")>1):
            print("div")
