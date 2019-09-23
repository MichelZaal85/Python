# RPSLS.py
# Rock-paper-scissors-lizard-Spock template

import random
# convert name to number
def name_to_number(name):
    if name.lower() == 'rock':
        return 0
    elif name.lower() == 'spock':
        return 1
    elif name.lower() == 'paper':
        return 2
    elif name.lower() == 'lizard':
        return 3
    elif name.lower() == 'scissors':
        return 4    
    else:
        return 'Oh No...'

# convert number
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Oh No...'

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print('\n\n')
    
    # print out the message for the player's choice
    print('Welcome to the world famous Rock, Spock, Paper, Lizard, Spock game!\n')

    # convert the player's choice to player_number using the function name_to_number()
    print('Your choice:    ', player_choice)
    player_choice = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    computer_choice = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    print('computer choice:', number_to_name(computer_choice))
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five
    difference = (computer_choice - player_choice) % 5
    print('\n')
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print('Oh, no! It\'s a Tie..')
    elif difference < 3:
        print('Uhm.. I hate to be the bringer of bad news, but... the computer has won.\nYou lose')
    else:
        print('Yeah! Show the computer who\'s boss!\nYou Won!')



    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


