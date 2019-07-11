class Shape():
    def what_am_i(self):
        print("Jestem figura")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.bok1 = a
        self.bok2 = b

    def calculate_perimeter(self):
        return 2 * (self.bok1 + self.bok2)

class Square(Shape):
    def __init__(self,a):
        self.bok = a

    def calculate_perimeter(self):
        return 4 * self.bok

    def change_size(self,z):
        self.zmiana_boku_o = z
        self.bok = self.bok + self.zmiana_boku_o


square1 = Square(2)
rectangle1 = Rectangle(5,10)

lista = [square1,rectangle1]

for i in lista:
    i.what_am_i()
