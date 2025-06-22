import copy
import random


def porownaj_siatki(s1, s2):
    bledy = 0
    for y in range(len(s1)):
        for x in range(len(s1[0])):
            if s1[y][x] != s2[y][x]:
                bledy += 1
    return bledy


#Stara wersja:
# def generuj_sasiedztwo(siatka):
#     wysokosc = len(siatka)
#     szerokosc = len(siatka[0])  # zakładamy, że wszystkie wiersze mają tę samą długość
#     liczba_sasiadow = wysokosc * szerokosc
#     sasiedzi = []
#
#     for _ in range(liczba_sasiadow):
#         nowa = copy.deepcopy(siatka)
#         y = random.randint(0, wysokosc - 1)
#         x = random.randint(0, szerokosc - 1)
#
#         # Zamień tylko 1 ↔ 2
#         if nowa[y][x] == 1:
#             nowa[y][x] = 2
#         elif nowa[y][x] == 2:
#             nowa[y][x] = 1
#
#         sasiedzi.append(nowa)
#
#     return sasiedzi
#Nowa wersja
def generuj_sasiedztwo(siatka):
    wysokosc = len(siatka)
    szerokosc = len(siatka[0])
    sasiedzi = []

    for y in range(wysokosc):
        for x in range(szerokosc):
            if siatka[y][x] == 1 or siatka[y][x] == 2:
                nowa = copy.deepcopy(siatka)
                if nowa[y][x] == 1:
                    nowa[y][x] = 2
                elif nowa[y][x] == 2:
                    nowa[y][x] = 1
                sasiedzi.append(nowa)

    return sasiedzi

def generuj_losowa_siatke(wysokosc, szerokosc):
    return [[random.choice([1, 2]) for _ in range(szerokosc)] for _ in range(wysokosc)]

