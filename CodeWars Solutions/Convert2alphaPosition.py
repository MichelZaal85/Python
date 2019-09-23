# a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26  

def alphabet_position(text):
	l = []
	s = " "
	for i in text:
		if i.isalpha():
			l.append((ord(i.lower())-96))
	return(''.join(str(l).strip('[]').replace(',','')))


alphabet_position("The sunset sets at twelve o' clock.")


# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11 
# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11


# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())