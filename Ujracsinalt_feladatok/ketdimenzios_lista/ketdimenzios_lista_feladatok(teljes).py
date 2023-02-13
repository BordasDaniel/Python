#1. Feladat
"""
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál, és ezeket a listákat egy 'tarolo' nevű listába helyezi. A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
"""

"""
import random

def main():
    tarolo = []
    for x in range(4):
        lista = [random.randint(0, 25) for x in range(3)]
        tarolo.append(lista)
    print(tarolo)

main()
        """


#2.1 Feladat
"""
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista! Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '. A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki. A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!
"""
#2.2 Feladat
"""
Egészítsd ki úgy a programot, hogy a felhasználó megadhasson egy koordinátát (a bal felső rácspont koordinátája (0;0), a jobb alsó pedig (2;2)), és ekkor a program rajzolja ki úgy a 3x3-as rácsot, hogy a megadott koordinátán 'O ' helyett, '+ ' legyen!
"""
#2.3 Feladat
"""
Alakítsd át úgy a programot, hogy a koordinátapárok bekérése addig folytatódjon, míg a felhasználó intervallumon kívüli értéket nem ad meg! A program minden bekérés után rajzolja ki a rácsot úgy, hogy megjeleníti a már korábban megadott koordináták esetében is a '+' jelet!
"""

"""
def betesz():
    lista = [[] for x in range(3)]
    for x in lista:
        for y in lista:
            x.append('O')
    return lista

def megjelenites(tarolo):
    for x in tarolo:
        print(" ".join(x))

def sajat_jel(tarolo):
    koordinata = koordinataim()
    jel = input('Add meg a jelet!\t')
    print(koordinata)
    while not koordinata == []:
        del tarolo[koordinata[0]][koordinata[1]]
        tarolo[koordinata[0]].insert(koordinata[1], jel)
        for x in range(2):
            del koordinata[0]


def koordinataim():
    koordinatak = []
    while not (szam := int(input('Adj meg egy számot!\t'))) > 2:
        koordinatak.append(szam)
    return koordinatak

def main():
    tarolo = betesz()
    sajat_jel(tarolo)
    megjelenites(tarolo)

main()
"""

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