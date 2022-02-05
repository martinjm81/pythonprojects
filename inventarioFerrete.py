# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:13:33 2021

@author: José-Manuel
"""

#sistema contable

BodegaDeProductos = []
poductosEnFactura = []

def programaVentaFerreteria():
    salir=False
    opcion = 0
    while not salir:
        print("--------------------------")
        opcion = int(input("1.Ir almenúde bodega. \n2.Ira la Facturación.\n3.. Salir \nDigiteopción \"))
        if opcion inrange(1,3):
            if opcion == 1: 
                menuBodega()
            if opcion == 2: