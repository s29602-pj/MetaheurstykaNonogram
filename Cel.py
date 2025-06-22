def ekstrakt_bloki(ciag):
    bloki = []
    licznik = 0
    for x in ciag:
        if x == 2:
            licznik += 1
        elif licznik > 0:
            bloki.append(licznik)
            licznik = 0
    if licznik > 0:
        bloki.append(licznik)
    return bloki


def porownaj_bloki(aktualne, wzorzec):
    max_len = max(len(aktualne), len(wzorzec))
    bledy = 0
    for i in range(max_len):
        a = aktualne[i] if i < len(aktualne) else 0
        b = wzorzec[i] if i < len(wzorzec) else 0
        if a != b:
            bledy += 1
    return bledy


def funkcja_celu(siatka, wiersze, kolumny):
    wysokosc, szerokosc = len(siatka), len(siatka[0])
    bledy = 0


    for y in range(wysokosc):
        rzeczywiste = ekstrakt_bloki(siatka[y])
        wzorzec = wiersze[y]
        bledy += porownaj_bloki(rzeczywiste, wzorzec)


    for x in range(szerokosc):
        kolumna = [siatka[y][x] for y in range(wysokosc)]
        rzeczywiste = ekstrakt_bloki(kolumna)
        wzorzec = kolumny[x]
        bledy += porownaj_bloki(rzeczywiste, wzorzec)

    return bledy
