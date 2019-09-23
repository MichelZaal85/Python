import random

def determine_winner():
	print('''
		0 = Rock 	Beats -- Scissors & Lizard 
		1 = Spock 	Beats -- Rock & Scissors
		2 = Paper 	Beats -- Spock & Rock 
		3 = Lizard 	Beats -- Paper & Spock
		4 = Scissors 	Beats -- Scissor > Lizzard & Paper
''')

	# compute difference of comp_num and player_num %5
	game_diff = (comp_number - player_number) % 5
	# use if/elif/else to determine winner, print winner message
	if game_diff == 0:
		print('Player and computer tie!')
	elif game_diff < 3:
		print('Computer wins!')
	else:
		print('Player wins!')

# player_number = input('1--5')
player_number = 0
comp_number = random.randint(0,4)
print('comp_number:', comp_number, '\nplayer_number:',player_number, '\n', (comp_number - player_number)%5)

determine_winner()