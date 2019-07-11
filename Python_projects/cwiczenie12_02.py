class Orange:
    def __init__(self, w, c):
        """waga jest podawana w gramach"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Utworzono!")

    def rot(self, days, temp):
        self.mold = days * temp

or1 = Orange(280,"ciemnopomaranczowy")
or2 = Orange(329,"limeta")
or3 = Orange(13,"czerwony")
or1.color = "jasnopomaranczowy"

or4 = Orange(289,"jasnopomaranczowy")
print(or4.mold)
or4.rot(10,29)
print(or4.mold)
print(or1.weight)
print(or1.color)
