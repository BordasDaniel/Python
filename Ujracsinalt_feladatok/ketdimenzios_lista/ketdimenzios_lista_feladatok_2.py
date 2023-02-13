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
