# print("a:", ord('a'))
# print("z:", ord('z'))
# print("A:", ord('A'))
# print("Z:", ord('Z'))
# # 65 -- 90
# # 97 -- 122

# chars = []
# for i in range(90, 98):
# 	chars.append(chr(i))
# print(chars)


# def caesar_crypto_encode(text, shift):
# 	ROT_text = []
# 	for i in text:
# 		# print(i, (ord(i)))
# 		ROT_text.append(chr(ord(i)+shift))
# 	return("".join(ROT_text))

# print(caesar_crypto_encode('Michel', -1))


def caesar_crypto_encode(text, shift):
	ROT_text = []
	for i in text:
		shift = (shift%26)+6
		print(ord(i)+shift)

	# return("".join(ROT_text))

caesar_crypto_encode('H', 59)

# A	 B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z 		26
# 65 66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90

# 																											 7

# a	 b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z 		26
# 97 98	99	100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122

# if n < 65:
# 	%
# if > 122:
# 	%

# H   e   l   l   o      w   o   r   l   d
# 72  101 108 108 111	 119 111 114 108 100 

# e   B   I   I   L      T   L   O   I   A
# 101 66  73  73  76     84  76  79  73  65


# print(1, caesar_crypto_encode("Et tu, Brute?", 3)) 		# "Hw wx, Euxwh?"
# print(2, caesar_crypto_encode("Hw wx, Euxwh?", -3)) 		# "Et tu, Brute?"
# print(3, caesar_crypto_encode("123,.)(!?", 10))			# "123,.)(!?"
# print(4, caesar_crypto_encode("", 10))					# "", "Problem: empty string"
# # print(caesar_crypto_encode(None, 10))					# "", "Problem: null"
# # print(caesar_crypto_encode("   ", 10))					# "", "Problem: whitespaces"

# # print(caesar_crypto_encode("Hello world!", 127))		# "eBIIL TLOIA!"

# # print(caesar_crypto_encode("eBIIL TLOIA!", -127))		# "Hello world!"
# # print(caesar_crypto_encode("ksdjai8983hdk?}{", 15))		# "zHsypx8983wsz?}{"
															# "zdsypx8983wsz?}{"
# print(5, caesar_crypto_encode("Hello world!", 0))			# "Hello world!"

'''
	The function receives 2 parameters: an original text of any length of type “string” and a number of type “int” that represents shifts;
	only letters in both cases must be encrypted;
	alphabet contains only letters in this range: a-zA-Z;
	by encryption the letter can change the case;
	shift could be either positive or negative (for left shift);
	If the input text is empty, null or includes only whitespaces, return an empty string.
'''

