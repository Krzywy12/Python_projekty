#Slownik zawierajacy rozne informacje o mnie

o_mnie_slownik = {"kolor oczu":"niebieski",
                  "zainteresowania":"fizyka,astronomia",
                  "cechy charakteru":"cichy",
                  "wzrost":"sredni"}

n = input("Co chcesz wiedziec o mnie? ")

if n in o_mnie_slownik:
    x = o_mnie_slownik[n]
    print(x)
else:
    print("Nie znam odpowiedzi")
