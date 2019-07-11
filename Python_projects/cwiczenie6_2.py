try:
    x = input("Podaj imie osoby lub nazwe rzeczy: ")
    y = input("Podaj imie osoby lub nazwe rzeczy w bierniku: ")

    r = "Wczoraj napisalem {} i wyslalem do {}".format(x,y)
    print(r)
except:
    print("Podaj o co Cie prosze")
