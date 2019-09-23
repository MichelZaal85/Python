import random, os

def RPSLS():
	os.system('clear')
	print('''
  Lets Play Rock-Paper-Scissors-Lizard-Spock.

	Enter a number between 1 and 5.
		0 = Rock	Beats -- Scissors & Lizard 
		1 = Spock	Beats -- Rock & Scissors
		2 = Paper	Beats -- Spock & Rock 
		3 = Lizard	Beats -- Paper & Spock
		4 = Scissors	Beats -- Lizzard & Paper
		''')
	
	computer_choice = random.randint(0,4)

	convert = {0:'rock',1:'spock',2:'paper',3:'lizard',4:'scissors','rock':0,'spock':1,'paper':2,'lizard':3,'scissors':4}

	
	user_choice = input('Enter option: ')
	if str(user_choice).lower() == 'chocolate':
		print('\n\tYes, chocoate is good, but we need to stay focused.\n\tHere have a quote instead:\n\n\t"If chocolate can\'t fix it, it\'s a serious problem!"')
		return
	if len(user_choice) < 3:	
		user_choice = int(user_choice)
	else:
		if user_choice not in convert:
			print('\nNo, No, No, No... The horror!')
			return
		user_choice = convert[user_choice.lower()]
	if user_choice > 4: user_choice %= 4
	
	print('You:\t\t', convert[user_choice],'\nComputers:\t', convert[computer_choice], '\n')

	battle = (computer_choice - user_choice) % 5

	if battle == 0:
		print('Player and computer tie!')
	elif battle < 3:
		print('Computer wins!')
	else:
		print('Player wins!')
RPSLS()
input()