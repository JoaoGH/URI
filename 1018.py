# -*- coding: utf-8 -*-
saque=int(input())
if(saque>0 and saque<1000000):
    res=saque

    n100=int(res/100)
    res=res-n100*100

    n50=int(res/50)
    res=res-n50*50

    n20=int(res/20)
    res=res-n20*20

    n10=int(res/10)
    res=res-n10*10

    n5=int(res/5)
    res=res-n5*5

    n2=int(res/2)
    res=res-n2*2

    n1=int(res/1)
    res=res-n1

    print(saque)
    print(n100,"nota(s) de R$ 100,00")
    print(n50,"nota(s) de R$ 50,00")
    print(n20,"nota(s) de R$ 20,00")
    print(n10,"nota(s) de R$ 10,00")
    print(n5,"nota(s) de R$ 5,00")
    print(n2,"nota(s) de R$ 2,00")
    print(n1,"nota(s) de R$ 1,00")