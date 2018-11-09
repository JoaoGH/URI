# -*- coding: utf-8 -*-
n=input()
fixo=float(input())
fixo=float("%.2f"%fixo)
venda=float(input())
venda=float("%.2f"%venda)
bonus=venda*0.15
sal=fixo+bonus
print("TOTAL = R$ {}".format("%.2f"%sal))