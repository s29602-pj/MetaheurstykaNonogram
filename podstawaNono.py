def parsuj(s: str) -> list[list[int]]:
    return [list(map(int, czesc.split(','))) for czesc in s[1:-1].split('","')]#map zwraca obiekt


def drukuj_siatke(siatka):
        for wiersz in siatka:
            print("".join("- *"[komorka] for komorka in wiersz))