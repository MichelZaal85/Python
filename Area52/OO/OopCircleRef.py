import math, random


class Circle:
    def calcCircumference(self):
        # self.radius, self is being replaced by instance name
        return math.pi * 2 * self.radius


circles = []

for i in range(10):
    c = Circle()
    c.radius = random.uniform(1.1, 9.5)
    #  The parameter doesn't have to be given. Because
    # c.radius is already created. 
    c.Circumference = c.calcCircumference() 
    circles.append(c)

for c in circles:
    print('Radius:', c.radius,
        'Circumference:', c.Circumference)
