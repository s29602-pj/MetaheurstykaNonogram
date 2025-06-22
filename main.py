import sys
from podstawaNono import parsuj
from podstawaNono import rozwiaz
from podstawaNono import drukuj_siatke

from funkcjaCelu import generuj_sasiedztwo
from funkcjaCelu import generuj_losowa_siatke
from funkcjaCelu import porownaj_siatki

from algorytmy import pelny_przeglad
from algorytmy import klasyczna_wspinaczka
from algorytmy import losowa_wspinaczka

from wyzarzanie import algorytm_symulowanego_wyzarzania

from porowanie import  porownaj_metody

from tabu import algorytm_tabu
from zbieznosc import generuj_wykres_zbieznosci






def main():
    if len(sys.argv) != 2:
        print("Brak pliku wejściowego. Możesz wpisać dane ręcznie.")
        print("Wpisz dane w 4 liniach (szerokość, wysokość, kolumny, wiersze):")
        dane = [
            input("Wpisz szerokość: "),
            input("Wpisz wysokość: "),
            input("Wpisz kolumny: "),
            input("Wpisz wiersze: ")
        ]
    else:
        sciezka_pliku = sys.argv[1]
        try:
            with open(sciezka_pliku, 'r', encoding='utf-8') as file:
                dane = file.read().strip().split("\n")
        except Exception as e:
            print(f"Błąd przy wczytywaniu pliku: {e}")
            return
#Tak samo jak na ML zrobic!!!
    if len(dane) != 4:
        print(f"Błąd: Dane muszą zawierać dokładnie 4 linie, ale znaleziono {len(dane)}.")
        return

    szerokosc, wysokosc, kolumny_raw, wiersze_raw = dane
    szerokosc, wysokosc = int(szerokosc), int(wysokosc)
    kolumny = parsuj(kolumny_raw)
    wiersze = parsuj(wiersze_raw)

    siatka = [[0] * szerokosc for _ in range(wysokosc)]
    rozwiaz(wiersze, kolumny, siatka)
    print("Rozwiązanie początkowe (idealne):")
    drukuj_siatke(siatka)

    siatka_wzor = [wiersz.copy() for wiersz in siatka]
    siatka_start = generuj_losowa_siatke(wysokosc, szerokosc)

#Losowanie
    print("\nLosowa siatka:")
    siatka_losowa = generuj_losowa_siatke(wysokosc, szerokosc)
    drukuj_siatke(siatka_losowa)
    roznica = porownaj_siatki(siatka_losowa, siatka_wzor)
    print(f"Różnica względem wzorca: {roznica} pól")


#Najlepszy sasiad zmiana
    print("\nNajlepsze sąsiedztwo:")
    sasiedztwa = generuj_sasiedztwo(siatka)
    najlepszego_sasiedztwa = min(sasiedztwa, key=lambda s: porownaj_siatki(s, siatka_wzor))
    drukuj_siatke(najlepszego_sasiedztwa)
    print(f"Różnica względem wzorca: {porownaj_siatki(najlepszego_sasiedztwa, siatka_wzor)} pól")

#Pelen przeglad
    najlepsza, bledy = pelny_przeglad(wysokosc, szerokosc, siatka_wzor)
    drukuj_siatke(najlepsza)
    print(f"Różnica względem wzorca: {bledy} pól")

#Klasyczny polegajacy na prrawidlowej funkcji celu która Pan zatwierdził
    print("\nKlasyczny wspinaczkowy (funkcja_celu_dzialajaca):")
    siatka_klasyczna, blad_klasyczna, iter_klasyczna, czas_klasyczna = klasyczna_wspinaczka(siatka_start, wiersze,
                                                                                            kolumny)
    drukuj_siatke(siatka_klasyczna)
    print(f"Błędy w wierszach i kolumnach: {blad_klasyczna}, Iteracje: {iter_klasyczna}, Czas: {czas_klasyczna:.4f}s")
#Losowy polegajacy na prrawidlowej funkcji celu która Pan zatwierdził
    print("\nLosowy wspinaczkowy (funkcja_celu_dzialajaca):")
    siatka_losowa, blad_losowa, iter_losowa, czas_losowa = losowa_wspinaczka(siatka_start, wiersze, kolumny)
    drukuj_siatke(siatka_losowa)
    print(f"Błędy w wierszach i kolumnach: {blad_losowa} , Iteracje: {iter_losowa}, Czas: {czas_losowa:.4f}s")

#Algorytm tabu z cofnieciem
    wynik_tabu, blad_tabu, iteracje_tabu, czas_tabu, historia = algorytm_tabu(
        siatka_start, siatka_wzor, max_iteracje=1000
    )
    print("Tabu (bez ograniczeń):")
    drukuj_siatke(wynik_tabu)
    print(f"Błędy: {blad_tabu}, Iteracje: {iteracje_tabu}, Czas: {czas_tabu:.4f}s")

    if len(historia) > 1:
        print("\nCofnięcie o 1 krok:")
        drukuj_siatke(historia[-2])




#Algorytm wyzarzania
    wynik_sa, blad_sa, iteracje_sa, czas_sa = algorytm_symulowanego_wyzarzania(
        siatka_start, siatka_wzor, T_start=100.0, T_koniec=0.1, alfa=0.95)

    print("Symulowane wyżarzanie:")
    drukuj_siatke(wynik_sa)
    print(f"Błędy: {blad_sa}, Iteracje: {iteracje_sa}, Czas: {czas_sa:.4f}s")



#Wyniki i porownania czasow
    wyniki = [
        ("Wspinaczka klasyczna", blad_klasyczna, iter_klasyczna, czas_klasyczna),
        ("Wspinaczka losowa", blad_losowa, iter_losowa, czas_losowa),
        ("Tabu (bez ograniczeń)", blad_tabu, iteracje_tabu, czas_tabu),
        ("Symulowane wyżarzanie", blad_sa, iteracje_sa, czas_sa),
    ]

    porownaj_metody(wyniki)

    generuj_wykres_zbieznosci(siatka_start, wiersze, kolumny, liczba_prob=5)





if __name__ == "__main__":
    main()