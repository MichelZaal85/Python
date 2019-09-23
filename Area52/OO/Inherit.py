class Shape():
    def __init__(self):
        self.color = 'red'
        self.sides = 0

    def calcArea(self):
        return 0


class Square(Shape):
    def __init__(self, w):
        Shape.__init__(self)
        self.width = w

    # calcArea() is inherited, but overwritten in the class
    def calcArea(self):
        return self.width ** 2


class Circle(Shape):
    """docstring for Circle"""
    def __init__(self, r, c):
        Shape.__init__(self)
        self.radius = r
        self.color = c


sq1 = Square(5)
sq2 = Square(9)

cr1 = Circle(10, 'Blue')

print('Square sizes:', sq1.width)
print(cr1.color, cr1.radius)

print(sq1.calcArea())