z = ' '
plansza = [[z, z, z], [z, z, z], [z, z, z]]


def kreator_planszy(rozmiar_planszy):
    print("( )(1)(2)(3)")
    for i in range(rozmiar_planszy):
        print(f"({i + 1})", end='')
        for j in range(rozmiar_planszy):
            print(f"[{plansza[i][j]}]", end='')
        print('')


def wygrana(gracz):
    print(f"Gracz {gracz} wygrywa!")


def sprawdzanie_wygranej(rozmiar_planszy_uzytkownika, gracz):
    warunek_wygranej = 0
    # pionowo
    for i in range(rozmiar_planszy_uzytkownika):
        licznik = 0
        for j in range(rozmiar_planszy_uzytkownika):
            if plansza[j][i] == gracz:
                licznik += 1
            if licznik == 3:
                warunek_wygranej = 1
                wygrana(gracz)
                break

    # poziomo
    for i in range(rozmiar_planszy_uzytkownika):
        licznik = 0
        for j in range(rozmiar_planszy_uzytkownika):
            if plansza[i][j] == gracz:
                licznik += 1
            if licznik == 3:
                warunek_wygranej = 1
                wygrana(gracz)
                break

    if plansza[0][0] == plansza[1][1] == plansza[2][2] or plansza[0][2] == plansza[1][1] == plansza[2][0]:
        wygrana(gracz)

    return warunek_wygranej


def gra():
    rozmiar_planszy_uzytkownika = 3
    print("Gra w kółko i krzyżyk")
    warunek_wygranej = 0
    gracz = 'X'
    while warunek_wygranej < 1:
        kreator_planszy(rozmiar_planszy_uzytkownika)
        wejscie = [int(i) for i in input(f"{gracz} podaj koordynaty: ")]
        if plansza[wejscie[0] - 1][wejscie[1] - 1] != ' ':
            print("Wybrałeś zajęte pole!")
            continue
        elif gracz == 'X':
            plansza[wejscie[0] - 1][wejscie[1] - 1] = 'X'
            warunek_wygranej = sprawdzanie_wygranej(rozmiar_planszy_uzytkownika, gracz)
            gracz = 'O'
        elif gracz == 'O':
            plansza[wejscie[0] - 1][wejscie[1] - 1] = 'O'
            warunek_wygranej = sprawdzanie_wygranej(rozmiar_planszy_uzytkownika, gracz)
            gracz = 'X'


gra()

""" RIPZONE
if plansza[i][j] == plansza[i + 1][j] and plansza[i][j] == plansza[i + 2][j]:
    wygrana(gracz)
if plansza[i][j] == plansza[i][j + 1] and plansza[i][j] == plansza[i][j + 2]:
    wygrana(gracz)
"""
