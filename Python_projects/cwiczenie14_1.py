class Square:
    square_list = []

    def __init__(self, b):
        self.bok = b
        self.square_list.append(self)
    def __repr__(self):
        return "{} na {} na {} na {}".format(self.bok,self.bok,self.bok,self.bok)
square1 = Square(1)
square2 = square1
square3 = Square(3)

print(square1.square_list)

def funkcja(x,y):
    print (x is y)


funkcja(square1,square2)
