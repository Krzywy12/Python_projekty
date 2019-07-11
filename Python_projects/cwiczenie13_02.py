class Prostokat():
    def __init__(self,l,w):
        self.lok = l
        self.wi = w
        print("Utworzono!")

    def pole(self):
        return self.lok * self.wi

prostokat1 = Prostokat(4,5)




class Kwadrat():
    def __init__(self,k,w):
        self.ked = k
        self.wh = w
        print("Utworzono!")

    def pole(self):
        return self.ked * self.wh

kwadrat1 = Kwadrat(0,0)

lista = [prostokat1, kwadrat1]

for i in lista:
    if type(i) == "Prostokat":
        print(i.pole())
    if type(i) == "Kwadrat":
        print(i.pole())


