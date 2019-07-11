import math


class Circle:
    def __init__(self, r):
        self.promien = r

    def area(self):
        return 2 * math.pi * (self.promien ** 2)


circle1 = Circle(1)
print(circle1.area())
