class Osoba:
    def __init__(self, n, c, w):
        self.wysokosc = w
        self.ciezar  = c
        self.name = n
        print("Utworzono!")
    def cechy(self, e):
        self.cecha = e

o1 = Osoba("Kacper",60,170)
o1.cechy("pracowity")
print(o1.cecha)
