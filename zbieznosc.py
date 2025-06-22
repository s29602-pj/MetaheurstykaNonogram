import matplotlib.pyplot as plt
import copy
import random
import time
import numpy as np
import os
from funkcjaCelu import generuj_sasiedztwo
from Cel import  funkcja_celu



def wspinaczka_klasyczna(siatka_start, wiersze, kolumny, max_iter=500):
    aktualna = copy.deepcopy(siatka_start)
    blad_aktualny = funkcja_celu(aktualna, wiersze, kolumny)
    krzywa = [blad_aktualny]

    for _ in range(max_iter):
        sasiedzi = generuj_sasiedztwo(aktualna)
        najlepszy = min(sasiedzi, key=lambda s: funkcja_celu(s, wiersze, kolumny))
        blad_najlepszy = funkcja_celu(najlepszy, wiersze, kolumny)

        if blad_najlepszy < blad_aktualny:
            aktualna = najlepszy
            blad_aktualny = blad_najlepszy
            krzywa.append(blad_aktualny)
        else:
            break

        if blad_aktualny == 0:
            break

    return krzywa

def wspinaczka_losowa(siatka_start, wiersze, kolumny, max_iter=10000):
    aktualna = copy.deepcopy(siatka_start)
    blad_aktualny = funkcja_celu(aktualna, wiersze, kolumny)
    iteracja = 0
    krzywa = [blad_aktualny]

    while iteracja < max_iter:
        iteracja += 1
        sasiedzi = generuj_sasiedztwo(aktualna)
        losowy = random.choice(sasiedzi)
        blad_losowy = funkcja_celu(losowy, wiersze, kolumny)

        if blad_losowy <= blad_aktualny:
            aktualna = losowy
            blad_aktualny = blad_losowy
            krzywa.append(blad_aktualny)

        if blad_aktualny == 0:
            break


    return krzywa

def srednia_krzywa(lista_krzywych):
    max_len = max(len(k) for k in lista_krzywych)
    macierz = [k + [k[-1]] * (max_len - len(k)) for k in lista_krzywych]
    return list(np.mean(macierz, axis=0))

def generuj_wykres_zbieznosci(siatka_start, wiersze, kolumny, liczba_prob=10):
    klasyczne = []
    losowe = []
    czasy = {"klasyczna": [], "losowa": []}

    for i in range(liczba_prob):
        s1 = copy.deepcopy(siatka_start)
        start = time.time()
        wynik1 = wspinaczka_klasyczna(s1, wiersze, kolumny)
        czasy["klasyczna"].append(time.time() - start)
        klasyczne.append(wynik1)

        s2 = copy.deepcopy(siatka_start)
        start = time.time()
        wynik2 = wspinaczka_losowa(s2, wiersze, kolumny)
        czasy["losowa"].append(time.time() - start)
        losowe.append(wynik2)

    krzywa_klasyczna = srednia_krzywa(klasyczne)
    krzywa_losowa = srednia_krzywa(losowe)


    plt.figure(figsize=(10, 6))
    plt.plot(krzywa_klasyczna, label="Wspinaczka klasyczna")
    plt.plot(krzywa_losowa, label="Wspinaczka losowa")
    plt.xlabel("Iteracja")
    plt.ylabel("Funkcja celu (liczba błędów)")
    plt.title(f"Średnia krzywa zbieżności (na podstawie {liczba_prob} prób)")
    plt.legend()
    os.makedirs("wyniki", exist_ok=True)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("wyniki/wykres_zbieznosci.png")
    plt.show()