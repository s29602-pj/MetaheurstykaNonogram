


def porownaj_metody(wyniki):
    print("\n Porównanie metod optymalizacji\n")

    naglowek = f"{'Metoda':<30} {'Błędy':<10} {'Iteracje':<10} {'Czas [s]':<10}"
    print(naglowek)
    print("-" * len(naglowek))

    for nazwa, blad, iteracje, czas in wyniki:
        print(f"{nazwa:<30} {blad:<10} {iteracje:<10} {czas:.4f}")

    print("\n Wnioski:")

    # Filtrowanie
    min_blad = min(wyniki, key=lambda x: x[1])[1]
    najlepsze = [m for m in wyniki if m[1] == min_blad]

    # 1. Najlepszy zestaw parametrów = najmniej błędów + najmniej czasu + najmniej iteracji (łącznie)
    najlepszy_zestaw = min(najlepsze, key=lambda m: m[2] + m[3])  # iteracje + czas
    print(f"• Najlepszy zestaw parametrów: {najlepszy_zestaw[0]} (Błędy: {najlepszy_zestaw[1]}, "
          f"Iteracje: {najlepszy_zestaw[2]}, Czas: {najlepszy_zestaw[3]:.4f}s)")

    # 2. Najszybsza metoda (wśród najlepszych)
    najszybsza = min(najlepsze, key=lambda m: m[3])
    print(f"• Najszybsza metoda (przy {min_blad} błędach): {najszybsza[0]} ({najszybsza[3]:.4f}s)")

    # 3. Najmniej zasobów (czas + iteracje)
    najmniej_zasobow = min(najlepsze, key=lambda m: m[2] + m[3])
    print(f"• Najmniej zasobów przy {min_blad} błędach: {najmniej_zasobow[0]} (iteracje + czas: "
          f"{najmniej_zasobow[2]} + {najmniej_zasobow[3]:.4f})")

    # 4. Najszybsza zbieżność (najmniej iteracji wśród najlepszych)
    najszybsza_zbieznosc = min(najlepsze, key=lambda m: m[2])
    print(f"• Najszybsza zbieżność: {najszybsza_zbieznosc[0]} ({najszybsza_zbieznosc[2]} iteracji)")