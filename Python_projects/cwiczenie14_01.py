class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.recs.append((self.width,self.length))

    def print_size(self):
        print("""{} na {}"""
               .format(self.width,self.length))

r1 = Rectangle(10,13)
r2 = Rectangle(5, 9)
r3 = Rectangle(7,89)
print(Rectangle.recs)
