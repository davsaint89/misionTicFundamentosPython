#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:02:28 2021

@author: david

"""
import time
import datetime
from datetime import date, datetime, time, timedelta

contador = 1
compras = list()
datos_clientes = list()
i = 0
j = 0

def datos_cliente():
    opt = 99
    global datos_clientes
    global j
    while opt != 2:

        datos_clientes.append([])
        print("Tipo de documento: ")
        tipo_doc = str(input("> "))
        datos_clientes[j].append(tipo_doc)
        print("Numero de documento: ")
        num_doc = int(input("> "))
        datos_clientes[j].append(num_doc)
        print("Nombre cliente:")
        nombre_cliente = str(input("> "))
        datos_clientes[j].append(nombre_cliente)
        print("Direccion:")
        dir_cliente = str(input("> "))
        datos_clientes[j].append(dir_cliente)
        print("Teléfono:")
        num_tel = str(input("> "))
        datos_clientes[j].append(num_tel)
        print("Ciudad:")
        ciudad = str(input("> "))
        datos_clientes[j].append(ciudad)
        print("País:")
        ciudad = str(input("> "))
        datos_clientes[j].append(ciudad)
        print("otro cliente?(1=Si; 2=No)")
        opt = int(input("> "))
        j += 1

    print(len(datos_clientes))

def calculo(forma, tipo):
    global contador
    global compras
    global i
    op2 = 88
    opb = 89
    subtotal = 0
    descuento_cant = 0
    valor_compra = 0
    total = 0
    while opb != 2:

        hoy= datetime.today()
        print(hoy.time())
        #print(hoy.time() > datetime.time(12,0,0))
        formatdate= "%d/%m/%Y %H:%M:%S"
        now = hoy.strftime(formatdate)
        compras.append([])
        compras[i].append(contador)
        compras[i].append(now.split()[0])
        compras[i].append(now.split()[1])
        while(op2!=2):

            print("Ingrese la referencia del producto: ")
            referencia_p = str(input("> "))
            compras[i].append(referencia_p)
            print("Ingrese nombre del producto: ")
            nombre_p = str(input("> "))
            compras[i].append(nombre_p)
            print("Ingrese cantidad de producto: ")
            cantidad_p = int(input("> "))
            compras[i].append(cantidad_p)
            print("Ingrese precio del producto: ")
            precio_p = int(input("> "))
            compras[i].append(precio_p)

            if cantidad_p > 3:
                descuento_cant += cantidad_p * precio_p * 0.05
                subtotal += cantidad_p * precio_p
                valor_compra = subtotal - descuento_cant

            else:
                descuento_cant += 0
                subtotal += cantidad_p * precio_p
                valor_compra = subtotal

            if forma == 1:
                if tipo == 1:
                    if valor_compra > 800000:
                        envio = 0
                        dscto_envio = 8000
                    else:
                        envio = 8000
                        dscto_envio = 0

                if tipo == 2:
                    envio = 10000
                    dscto_envio = 0

                if tipo == 3:
                    envio = 40000
                    dscto_envio = 0

            elif forma == 2:
                if tipo == 1:
                    if valor_compra > 500000:
                        envio = 0
                        dscto_envio = 4000
                    else:
                        envio = 4000
                        dscto_envio = 0

                if tipo == 2:
                    if valor_compra >= 1000000:
                        envio = 0
                        dscto_envio = 5000
                    else:
                        envio = 5000
                        dscto_envio = 0

                if tipo == 3:
                    if valor_compra >= 2000000:
                        envio = 0
                        dscto_envio = 20000
                    else:
                        envio = 20000
                        dscto_envio = 0
            print("Otro producto? (1=Si ; 2=No)")
            compras[i].append(int(subtotal))
            compras[i].append(int(descuento_cant))
            compras[i].append(int(envio))
            total = subtotal + envio - descuento_cant
            compras[i].append(int(total))
            op2 = int(input("> "))
        print(compras)
        print(int(subtotal)) #Valor compra
        print(int(descuento_cant)) # Valor descuento
        print(int(envio))# Valor envio
        print(int(total)) # Valor total a pagar
        print("Otra compra:")
        opb = int(input("> "))
        contador += 1
        i += 1
        subtotal = 0
        descuento_cant = 0
        valor_compra = 0
        total = 0
        op2 = 33


def main():
    opcion = 99
    while(opcion != 6):
        try:
            print("Menú de Opciones\n1.Ingreso Datos del cliente\n2.Ingreso Datos para cálculo de la compra e impresión resumen de la compra\n3. Impresion Cantidad de compras por turno\n4.Impresion valor compras por turno\n5.Datos del envío\n6.Salir")
            opcion=int(input("> "))

            if opcion == 1:
                datos_cliente()

            elif opcion == 2:

                print("Ingrese la forma me envío: 1= Rápido   2=Normal")
                forma_envio=int(input("> "))

                if forma_envio >= 1: # Rápido
                    print("Ingrese la forma me envío: 1=Local, 2=Nacional, 3=Internacional")
                    tipo_envio=int(input("> "))
                    #print(tipo_envio)
                    if tipo_envio >= 1 and tipo_envio <=3:
                        calculo(forma_envio, tipo_envio)

                elif forma_envio == 2: # normal
                    print("Ingrese la forma me envío: 1=Local, 2=Nacional, 3=Internacional")
                    tipo_envio=int(input("> "))
                    #print(tipo_envio)
                    if tipo_envio >= 1 and tipo_envio <=3:
                        calculo(forma_envio, tipo_envio)

            elif opcion == 3:
                print("Cantidad compras por turno")

            elif opcion == 4:
                print("Imprimir resumen compras por turno")

            elif opcion == 5:
                print("Pedir datos de envío")

            else:
                continue
                    #print("la opcion ingresada no existe")
        except:
            continue



if __name__ == '__main__':
    main()
