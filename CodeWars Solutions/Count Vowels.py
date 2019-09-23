def getCount(inputStr):
	num_vowels = 0
	num_vowels += inputStr.count('a')
	num_vowels += inputStr.count('A')
	num_vowels += inputStr.count('e')
	num_vowels += inputStr.count('E')
	num_vowels += inputStr.count('i')
	num_vowels += inputStr.count('I')
	num_vowels += inputStr.count('o')
	num_vowels += inputStr.count('O')    
	return num_vowels

print(getCount("abracadabra"))

