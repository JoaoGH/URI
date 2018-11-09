# -*- coding: utf-8 -*-
saque=input()
res=float(saque)
if(res>0 and res<1000000):

    n100=res//100
    res=res-n100*100

    n50=res//50
    res=res-n50*50

    n20=res//20
    res=res-n20*20

    n10=res//10
    res=res-n10*10

    n5=res//5
    res=res-n5*5

    n2=res//2
    res=res-n2*2

    # n1=res//1
    # res=res-n1

    # cent=len(saque)-1
    # cent2=len(saque)-2
    #
    # if(saque[cent]!="" or saque[cent2]!=""):
    m1=res//1
    res=res-m1*1

    m50=res//0.5
    res=res-m50*0.5

    m25=res//0.25
    res=res-m25*0.25

    m10=res//0.10
    res=res-m10*0.10

    m5=res//0.05
    res=res-m5*0.05

    m01=res//0.01
    res=res-m01*0.01



    print("NOTAS:")
    print(n100,"nota(s) de R$ 100.00")
    print(n50,"nota(s) de R$ 50.00")
    print(n20,"nota(s) de R$ 20.00")
    print(n10,"nota(s) de R$ 10.00")
    print(n5,"nota(s) de R$ 5.00")
    print(n2,"nota(s) de R$ 2.00")
    # print(n1,"nota(s) de R$ 1,00")
    print("MOEDAS:")
    print(m1,"moeda(s) de R$ 1.00")
    print(m50,"moeda(s) de R$ 0.50")
    print(m25,"moeda(s) de R$ 0.25")
    print(m10,"moeda(s) de R$ 0.10")
    print(m5,"moeda(s) de R$ 0.05")
    print(m01,"moeda(s) de R$ 0.01")