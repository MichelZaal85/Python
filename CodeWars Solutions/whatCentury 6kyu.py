def whatCentury(year):
	century = 1 + (year -1) // 100
	append = {'1':'st', '2':'nd', '3':'rd'}
	if not str(century)[0] == '1' and str(century)[1] in [1,2,3]:
		return(str(century) + append[str(century)[1]])
	return(str(century) + 'th')

print(whatCentury(1234))
print(whatCentury(1034))

print(whatCentury(2100))
print(whatCentury(2200))
print(whatCentury(2300))
print(whatCentury(2400))
