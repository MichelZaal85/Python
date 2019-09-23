class Klas:
	variable = 'Hello'

	def function(self):
		print('message inside class')

instance1 = Klas()
instance2 = Klas()

instance2.variable = 'User'

print(instance1.variable)
print(instance2.variable)

instance1.function()


