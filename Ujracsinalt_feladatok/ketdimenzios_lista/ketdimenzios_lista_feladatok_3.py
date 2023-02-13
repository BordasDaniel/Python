# 3. Feladat
"""
Készíts egy programot, amely egy kétdimenziós listában tárol ötször három darab véletlenszámot [-5;5] intervallumon. A program írja ki a kétdimenziós lista elemeit, majd fésülje át a lista tartalmát és törölje belőle a negatív számokat. Végül ismét kerüljön kiírásra lista tartalma!
"""

import random

def berak():
    lista = []
    for x in range(5):
        atmeneti = [random.randint(-5, 5) for x in range(3)]
        lista.append(atmeneti)
    print(lista)
    return lista

#Nem működik mivel több ugyanolyan negativ szám is van benne.
"""
def torol(lista):
    for x in lista:
        for y in x:
            if y <= -1:
                print(y)
                x.remove(y)
    return lista
"""

def torol(lista):
    uj_lista = []
    for x in lista:
            uj_lista.append(list(filter(lambda x: x > -1, x)))
    return uj_lista

def main():
    lista = berak()
    print(torol(lista))

main()