# Compute the distance between the points (x0, y0) and (x1, y1).

def Distance(x0, y0, x1, y1):
	distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
	print("The distance from (" + str(x0) + ", " + str(y0) + ") to", "(" + str(x1) + ", " + str(y1) + ") is " + str(distance) + ".")

Distance(2,2,5,6) # should return 5.0
Distance(1,1,2,2) # should return 1.41421356237
Distance(0,0,3,4) # should return 5.0
