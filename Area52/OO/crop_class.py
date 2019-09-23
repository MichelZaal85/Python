# https://pythonschool.net/oop/testing-the-functionality-of-the-class/
import random
class Crop:
	"""A generic food crop"""

	# constructor
	def __init__(self, growth_rate, light_need, water_need):
		
		#set the attributes with an initial value

		self._growth = 0
		self._days_growing = 0
		self._growth_rate = growth_rate
		self._water_need = growth_rate
		self._light_need = light_need
		self._water_need = water_need
		self._status = "Seed"
		self._type = "Generic"

		#the above attributes are prefixed with an underscore to indicate
		#that they should not be accessed directly from outwith the class
	
		#any method that is created must contain the SELF parameter
	
	def needs(self):
		#return a dictionary containing the light and water needs
		return {'light need':self._light_need, 'water need':self._water_need}
		
	def report(self):
		# method to report the provided information about the current state of the crop
		return {'type': self._type, 'status':self._status, 'growth': self._growth, 'days growing': self._days_growing}

	def _update_status(self):
		if self._growth > 15:
			self._status = 'Old'
		elif self._growth > 10:
			self._status = 'Mature'
		elif self._growth > 5:
			self._status = 'Young'
		elif self._growth > 0:
			self._status = 'Seeding'
		elif self._growth == 0:
			self._status = 'Seed'

	def grow(self,light, water):
		if light >= self._light_need and water >= self._water_need:
			self._growth += self._growth_rate
		# increment days growing
		self._days_growing += 1
		self._update_status()

def auto_grow(crop, days):
	# grow the crop
	for days in range(days):
		light = random.randint(1,10)
		water = random.randint(1,10)
		crop.grow(light, water)

def manual_grow(crop):
	# get the light and water values from the user
	valid = False
	while not valid:
		try:
			light = int(input('Please enter a light value (1-10): '))
			if 1 <= light <= 10:
				valid = True
			else:
				print('Value entered not valid - please enter value between 1 and 10')
		except ValueError:
			print('Value entered not valid - please enter value between 1 and 10')
	valid = False
	while not valid:
		try:
			water = int(input('Please enter a water value (1-10): '))
			if 1 <= water <= 10:
				valid = True
			else:
				print('Value entered not valid - please enter value between 1 and 10')
		except ValueError:
			print('Value entered not valid - Please enter value between 1 and 10')
	crop.grow(light,water)

def main():
	"""
	The private attributes should be accessed through
	a public interface (Method that makes the attributes accessible)
	this process is called encapsulation.

	Like a remote, changing the channel does not show 
	the process of changing the channel but only the outcome.
	# self is automaticly added to the method call
	"""
	#instantiate the class
	new_crop = Crop(1,4,3)
	#test to see whenether it works or not
	print(new_crop.needs())
	print(new_crop.report())
	# auto_grow(new_crop, 30)
	manual_grow(new_crop)
	print(new_crop.report())


if __name__ == "__main__":
	main()