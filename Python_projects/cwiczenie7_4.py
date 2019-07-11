lista_liczb = [1,3,5,7,11,13,17]

i = 0
while True:
    print("Wpisz q,aby zakonczyc")
    a = input("Odgadnij liczbe z listy")
    x = lista_liczb[i]
    if x == a:
        print("Zgadles!")
    elif a == 'q':
        break
    else:
        print("Nie zgadles")
    i += 1
