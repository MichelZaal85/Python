class Person:
	'''
	object person
	__init__:
	self.name
	self.age
	self.height

	printProperties:
	print name, age, height & person count
	'''
	# the variables / properties that are defined here will be accesible for all methods
	count = 0

	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height
		Person.count += 1

	def printProperties(self):
		print(self.name, self.age, self.height)
		print('Person number:', self.count)

	def printCount(self):
		print(self.count)

one = Person('Hugh', 25, 1.75)
two = Person('Jack', 31, 1.92)
thr = Person('Gerald', 45, 2.05)

one.printProperties()
two.printProperties()
thr.printProperties()

one.printCount()
two.printCount()

# add properties:
one.weight = 50
print('Person one weight:',one.weight)

# alter properties:
one.age = 35
print('Persone one age:', one.age)

# delte properties:
del one.height
print(hasattr(one, 'height'))
print(hasattr(one, 'weight'))
