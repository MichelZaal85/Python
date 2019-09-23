n = 23
def collatz(n):
	if n % 2:
		return n * 3 + 1
	return n / 2

while collatz(n) != 1:
	print(collatz(n))
	n = collatz(n)
print(collatz(n))
print('end of program')