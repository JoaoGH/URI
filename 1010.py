# -*- coding: utf-8 -*-
cod1, qtd1, uni1=input().split(" ")
cod2, qtd2, uni2=input().split(" ")
final=(int(qtd1)*float(uni1))+(int(qtd2)*float(uni2))
print("VALOR A PAGAR: R$ %0.2f"%final)