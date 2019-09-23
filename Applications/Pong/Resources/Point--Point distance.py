print('''


def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)
    return math.sqrt(
    (X1 - Y1) ** 2 + (X2 - Y2) ** 2)


Two points

Math, point on canvas
p,q

Python, list of coordiantes
[p[0],p[1],q[0],q[1]]

...................
Pythagorean theorem
...................

Math
dist(p,q)²==(p[0]-q[0])² + (p[1] - q[1])²

Python
def dist(p,q):
	return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


==============================================================

Vector as difference of two points

Math
v = p - q
Python, list of components
v[0] = p[0] - q[0]
v[1] = p[1] - q[1]

Move / translate point using vector
Math p = q+v

Python
p[0] = q[0] + v[0]
p[1] = q[1] + v[1]


Update for motion

Math
point at position p with velocity v
p = p + a * v

Python
p[0] = p[0] + a * v[0]
p[1] = p[1] + a * v[1]
	''')

# http://www.codeskulptor.org/#examples-collisions_and_reflections.py