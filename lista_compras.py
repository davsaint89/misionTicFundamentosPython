#!/usr/bin/env python3
lista_compras = [[1, '20/06/2021', '20:02:34', 1, 2, 'r1', 'n1', 2, 20000, 40000, 0, 10000, 50000, 'r2', 'n2', 10, 10000, 140000, 5000, 10000, 145000], [2, '20/06/2021', '20:03:15', 1, 2, 'r3', 'd3', 6, 30000, 180000, 9000, 10000, 181000]]

def calculo_total_compras(lista_compras):
    total_compras = sum([compra[-1] for compra in lista_compras])
    print(int(total_compras))

        

