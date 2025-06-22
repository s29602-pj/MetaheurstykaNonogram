import itertools
import time
import copy
import random


from funkcjaCelu import porownaj_siatki
from funkcjaCelu import generuj_sasiedztwo
from Cel import funkcja_celu


#Pelen przeglad
def pelny_przeglad(wysokosc, szerokosc, siatka_wzor):
    start_time = time.time()
    licznik = 0

    for kombinacja in itertools.product([1, 2], repeat=wysokosc * szerokosc):
        licznik += 1

        siatka = [
            list(kombinacja[y * szerokosc:(y + 1) * szerokosc])
            for y in range(wysokosc)
        ]

        bledy = porownaj_siatki(siatka, siatka_wzor)

        if bledy == 0:
            czas = time.time() - start_time
            print(f"\n Znaleziono idealne rozwiązanie w próbie nr {licznik}")
            print(f" Czas przeszukiwania: {czas:.4f} sekundy")
            return siatka, 0



def klasyczna_wspinaczka(siatka_start, wiersze, kolumny, max_iter=10000):

    start_time = time.time()
    aktualna = copy.deepcopy(siatka_start)
    blad_aktualny = funkcja_celu(aktualna, wiersze, kolumny)
    iteracja = 0

    while iteracja < max_iter:
        iteracja += 1
        sasiedzi = generuj_sasiedztwo(aktualna)
        najlepszy = min(sasiedzi, key=lambda s: funkcja_celu(s, wiersze, kolumny))
        blad_najlepszy = funkcja_celu(najlepszy, wiersze, kolumny)

        if blad_najlepszy < blad_aktualny:
            aktualna = najlepszy
            blad_aktualny = blad_najlepszy
        else:
            break

        if blad_aktualny == 0:
            break

    czas = time.time() - start_time
    return aktualna, blad_aktualny, iteracja, czas


def losowa_wspinaczka(siatka_start, wiersze, kolumny, max_iter=100000):
    start_time = time.time()
    aktualna = copy.deepcopy(siatka_start)
    blad_aktualny = funkcja_celu(aktualna, wiersze, kolumny)
    iteracja = 0

    while iteracja < max_iter:
        iteracja += 1
        sasiedzi = generuj_sasiedztwo(aktualna)
        losowy = random.choice(sasiedzi)
        blad_losowy = funkcja_celu(losowy, wiersze, kolumny)

        if blad_losowy <= blad_aktualny:
            aktualna = losowy
            blad_aktualny = blad_losowy

        if blad_aktualny == 0:
            break

    czas = time.time() - start_time
    return aktualna, blad_aktualny, iteracja, czas