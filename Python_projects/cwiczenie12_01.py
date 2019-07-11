#Przyklad programowania procedularnego
rock = []         # |zmienne
country = []      # |globalne

def collect_songs():
    song = "Wpisz tytul piosenki: "
    ask = "Nacisnij r lub c albo q, by wyjsc."

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)
        if genre == ("c"):
            cy = input(song)
            country.append(cy)
    print(rock)    # (efekt
    print(country) # uboczny zostaje)

collect_songs()
