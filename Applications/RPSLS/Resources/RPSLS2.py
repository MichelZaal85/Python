# RPSLS.py -- Rock-paper-scissors-lizard-Spock template
# By Michel Zaal

# import the random module
import random

# convert name to number function
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
        return 'No, no, no, no... the Horror!'

# convert number function
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
        return 'No, no, no, no... the Horror!'

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print('\n\n')
    
    # print out the message for the player's choice
    print('-------------------------------------------------------------------\nWelcome to the world famous Rock, Spock, Paper, Lizard, Spock game!\n-------------------------------------------------------------------\n')

    # convert the player's choice to player_number using the function name_to_number()
    print('Player chooses', player_choice)
    player_choice = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    computer_choice = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    print('Computer chooses', number_to_name(computer_choice))

    # compute difference of comp_number and player_number modulo five
    difference = (computer_choice - player_choice) % 5
    print('\n')
    
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print('Player and computer tie!')
    elif difference < 3:
        print('Computer wins!\nSorry.. Here have some chocolate to soften the blow')
        print(''' 
      __________________,.............,
     /_/_/_/_/_/_/_/_/,-',  ,. -,-,--/|
    /_/_/_/_/_/_/_/,-' //  /-| / /--/ /
   /_/_/_/_/_/_/,-' `-''--'  `' '--/ / * http://ascii.co.uk/art/chocolate *
  /_/_/_/_/_/_,:................../ /
  |________,'       -Shimrod      |/
          """""""""""""""""""""""'
          
    ''')
    else:
        print('Player wins!\nYeah, Show the computer who\'s boss!')

# tests:
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")