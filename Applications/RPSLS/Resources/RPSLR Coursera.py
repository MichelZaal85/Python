
0 — rock
1 — Spock
2 — paper
3 — lizard
4 — scissors

In this expanded list, each choice wins against the preceding two choices and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).

In all of the mini-projects for this class, we will provide a walk through of the steps involved in building your project to aid its development. A template for your mini-project is available here. Please work from this template.

Mini-project development process

Build a helper function name_to_number(name) that converts the string name into a number between 0 and 4 as described above. This function should use a sequence of if/elif/else clauses. You can use conditions of the form name == 'paper', etc. to distinguish the cases. To make debugging your code easier, we suggest including a final else clause that catches cases when name does not match any of the five correct input strings and prints an appropriate error message. You can test your implementation of name_to_number() using this name_to_number testing template. (Also available in the Code Clinic tips thread).
Next, you should build a second helper function number_to_name(number) that converts a number in the range 0 to 4 into its corresponding name as a string. Again, we suggest including a final else clause that catches cases when number is not in the correct range. You can test your implementation of number_to_name() using this number_to_name testing template.
Implement the first part of the main function rpsls(player_choice). Print out a blank line (to separate consecutive games) followed by a line with an appropriate message describing the player's choice. Then compute the number player_number between 0 and 4 corresponding to the player's choice by calling the helper function name_to_number() using player_choice.
Implement the second part of rpsls() that generates the computer's guess and prints out an appropriate message for that guess. In particular, compute a random number comp_number between 0 and 4 that corresponds to the computer's guess using the function random.randrange(). We suggest experimenting with randrange in a separate CodeSkulptor window before deciding on how to call it to make sure that you do not accidently generate numbers in the wrong range. Then compute the name comp_choice corresponding to the computer's number using the function number_to_name() and print an appropriate message with the computer's choice to the console.
Implement the last part of rpsls() that determines and prints out the winner. Specifically, compute the difference between comp_number and player_number taken modulo five. Then write an if/elif/else statement whose conditions test the various possible values of this difference and then prints an appropriate message concerning the winner. If you have trouble deriving the conditions for the clauses of this if/elif/else statement, we suggest reviewing the "RPSLS" video which describes a simple test for determine the winner of RPSLS.
This will be the only mini-project in the class that is not an interactive game. Since we have not yet learned enough to allow you to play the game interactively, you will simply call your rpsls function repeatedly in the program with different player choices. You will see that we have provided five such calls at the bottom of the template. Running your program repeatedly should generate different computer guesses and different winners each time. While you are testing, feel free to modify those calls, but make sure they are restored when you hand in your mini-project, as your peer assessors will expect them to be there.


Grading rubric — 18 pts total (scaled to 100 pts)

Your peers will assess your mini-project according to the rubric given below. To guide you in determining whether your project 
satisfies each item in the rubric, please consult the video that demonstrates our implementation of "Rock-paper-scissors-lizard-Spock". 
Small deviations from the textual output of our implementation are fine. You should avoid large deviations (such as using the Python 
function input to input your guesses). Whether moderate deviations satisfy an item of the grading rubric is at your peers 
discretion during their assessment.

Here is a break down of the scoring:

2 pts — A valid CodeSkulptor URL was submitted.
2 pts — Program implements the function rpsls() and the helper function name_to_number() with plausible code. 
	Give partial credit of 1 pt if only the function rpsls() has plausible code.
1 pt — Running program does not throw an error.
1 pt — Program prints blank lines between games.
2 pts — Program prints "Player chooses player_choice" where player_choice is a string of the 
	form "rock", "paper", "scissors", "lizard" or "Spock". 
	
	An example of a complete line of output is "Player chooses scissors". 
	Give 1 pt if program prints out number instead of string.


2 pts — Program prints "Computer chooses comp_choice" where comp_choice is a string of the form 
	"rock", "paper", "scissors", "lizard" or "Spock". 
	An example of a complete line of output is "Computer chooses scissors". 
	Give 1 pt if program prints out number instead of string.
1 pt — Computer's guesses vary between five calls to rpsls() in each run of the program.'
1 pt — Computer's guesses vary between runs of the program.'

3 pts — Program prints either "Player and computer tie!", "Player wins!" or "Computer wins!" to report outcome. 
	(1 pt for each message.)

3 pts — Program chooses correct winner according to RPSLS rules. 
	Please manually examine 5 cases for correctness. 
	If all five cases are correct, award 3 pts; 
	four cases correct award 2 pts; 
	one to three cases correct award 1 pt; 
	no cases correct award 0 pts.
 


