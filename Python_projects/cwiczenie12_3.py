class Triangle:
    def __init__(self, p, w):
        self.podstawa = p
        self.wysokosc = w

    def area(self):
        return self.podstawa * self.wysokosc * 0.5

triangle1 = Triangle(10, 10)
print(triangle1.area())
