import time, os, sys

while True:
	time.sleep(1)
	H = time.asctime()[11:13]
	M = time.asctime()[14:16]
	S = time.asctime()[17:19]
	print(str(H)+':'+str(M)+':'+str(S), end='\r')
	if time.asctime()[11:19] == '15:40:25':
		for i in range(3):
			print('\n')
			print('TIME')
			time.sleep(1)
		os.system('shutdown /p')
		sys.exit()