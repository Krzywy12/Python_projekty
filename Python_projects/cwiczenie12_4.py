class Hexagon:
    def __init__(self, b):
        self.bok = b

    def calculate_perimeter(self):
        return 6 * self.bok

hexagon1 = Hexagon(1)
print(hexagon1.calculate_perimeter())
