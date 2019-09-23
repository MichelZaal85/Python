# test.assert_equals(evaporator(10, 10, 10), 22)
'''
After the first day it'd lose 10 percent 
of 10 which is 1 so we're left with 9, right? 
But after the next day we're gonna lose 10% 
of what's left (10% of 9 which is 0.9) instead 
of another 1. So the amount lost in a day gets 
lower in time.
'''

def evaporator(content, evap_per_day, threshold):
	counter = 0

	threshold /= 10
	while content >= threshold:
		counter += 1
		content -= content * (evap_per_day * 0.01)
	return counter

print(evaporator(10,10,10))

print(evaporator(100,5,50)) # 104 should be 59
