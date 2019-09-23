''''
A reminder about the Honor Code

For previous mini-projects, we have had instances of students submitting solutions that have been copied from the web. 
Remember, if you can find code on the web for one of the mini-projects, we can also find that code. Submitting copied 
code violates the Honor Code for this class as well as Coursera's Terms of Service. Please write your own code and 
refrain from copying. If, during peer evaluation, you suspect a submitted mini-project includes copied code, please 
evaluate as usual and email the assignment details to iipphonorcode@online.rice.edu. We will investigate and handle as appropriate.

Mini-project description - Memory

Memory is a card game in which the player deals out a set of cards face down. In Memory, a turn (or a move) consists 
of the player flipping over two cards. If they match, the player leaves them face up. If they don't match, the player 
flips the cards back face down. The goal of Memory is to end up with all of the cards flipped face up in the minimum 
number of turns. For this project, we will keep our model for Memory fairly simple. A Memory deck consists of eight 
pairs of matching cards.

Mini-project development process

As usual, we suggest that you start from the program template for this mini-project.

Model the deck of cards used in Memory as a list consisting of 16 numbers with each number lying in the range [0,8) and 
appearing twice. We suggest that you create this list by concatenating two list with range [0,8) together. Use the Docs 
to locate the list concatenation operator.
Write a draw handler that iterates through the Memory deck using a for loop and uses draw_text to draw the number 
associated with each card on the canvas. The result should be a horizontal sequence of evenly-spaced numbers drawn on the canvas.
Shuffle the deck using random.shuffle(). Remember to debug your canvas drawing code before shuffling to make debugging easier.
Next, modify the draw handler to either draw a blank green rectangle or the card's value. To implement this behavior, 
we suggest that you create a second list called exposed. In the exposed list, the ith entry should be True if the ith card 
is face up and its value is visible or False if the ith card is face down and its value is hidden. We suggest that you 
initialize exposed to some known values while testing your drawing code with this modification.
Now, add functionality to determine which card you have clicked on with your mouse. Add an event handler for mouse clicks 
that takes the position of the mouse click and prints the index of the card that you have clicked on to the console. 
To make determining which card you have clicked on easy, we suggest sizing the canvas so that the sequence of cards 
entirely fills the canvas.
Modify the event handler for mouse clicks to flip cards based on the location of the mouse click. If the player 
clicked on the ith card, you can change the value of exposed[i] from False to True. If the card is already exposed, 
you should ignore the mouseclick. At this point, the basic infrastructure for Memory is done.
You now need to add game logic to the mouse click handler for selecting two cards and determining if they match. 
We suggest following the game logic in the example code discussed in the Memory video. State 0 corresponds to the start 
of the game. In state 0, if you click on a card, that card is exposed, and you switch to state 1. State 1 corresponds 
to a single exposed unpaired card. In state 1, if you click on an unexposed card, that card is exposed and you switch 
to state 2. State 2 corresponds to the end of a turn. In state 2, if you click on an unexposed card, that card is 
exposed and you switch to state 1. Note that if you are having difficulty with steps 6 and 7, please consult the 
tips # 5 and #6 on the Code Clinic tips page.
Note that in state 2, you also have to determine if the previous two cards are paired or unpaired. If they are 
unpaired, you have to flip them back over so that they are hidden before moving to state 1. We suggest that you 
use two global variables to store the index of each of the two cards that were clicked in the previous turn.
Add a counter that keeps track of the number of turns and uses set_text to update this counter as a label in the 
control panel. (BTW, Joe's record is 12 turns.) This counter should be incremented after either the first or 
second card is flipped during a turn.
Finally, implement the new_game() function (if you have not already) so that the "Reset" button reshuffles the 
cards, resets the turn counter and restarts the game. All cards should start the game hidden.
(Optional) You may replace the draw_text for each card by a draw_image that uses one of eight different images.
Once the run button is clicked in CodeSkulptor, the game should start. You should not have to hit the "Reset" 
button to start. Once the game is over, you should hit the "Reset" button to restart the game.

While this project may seem daunting at first glance, our full implementation took well under 100 lines with 
comments and spaces. If you feel a little bit intimidated, focus on developing your project to step six. 
Our experience is that, at this point, you will begin to see your game come together and the going will get much 
easier. For more helpful tips on implementing this mini-project, please visit the Code Clinic Tips page for this mini-project.

Grading Rubric - 11 pts total (scaled to 100)

1 pt - 	The game correctly draws 16 cards on the canvas (horizontally or as a grid). 
		Using images in place of textual numbers is fine. 
		However, it is the submitter's responsibility to ensure that custom images load during peer assessment.
1 pt - 	The cards appear in eight unique pairs.
1 pt - 	The game ignores clicks on exposed cards.
1 pt - 	At the start of the game, a click on a card exposes the card that was clicked on.
1 pt - 	If one unpaired card is exposed, a click on a second unexposed card exposes the card that was clicked on.
1 pt - 	If two unpaired cards are exposed, a click on an unexposed card exposes the card that was clicked on and 
		flips the two unpaired cards over.
1 pt - 	If all exposed cards are paired, a click on an unexposed card exposes the card that was clicked on and does not 
		flip any other cards.
1 pt - 	Cards paired by two clicks in the same turn remain exposed until the start of the next game.
1 pt - 	The game correctly updates and displays the number of turns in the current game in a label displayed 
		in the control area. 
		The counter may be incremented after either the first or second card is flipped during a turn.
1 pt - 	The game includes a "Reset" button that resets the turn counter and restarts the game.
1 pt - 	The deck is also randomly shuffled each time the "Reset" button is pressed, so that the cards are in a 
		different order each game. 


Tip #1

Many of you are tempted to make conditionals with 16 cases to handle every possible card position on the canvas. Please don't. 
Learn how to use loops. For example, if cards contains the list of card values, the following code is a good start towards 
drawing cards

	for card_index in range(len(cards)):
	    card_pos = 50 * card_index
	    canvas.draw_text(str(cards[card_index]), card_pos, ....)


Note that we could also iterate directly over the cards via for card in cards:. 
However, iterating over the indices of the cards will make adding code to expose cards based on mouse clicks easier.

Tip #2

In your mouse click handler, you need to determine which card you have clicked on. 
Compute the index of the card via pos[0] // 50. You can then use this index when manipulating 
the list exposed that control whether a card is drawn or not.

Tip #3
As you get close to the end of this mini-project, you will need to determine if the two cards match when you transition from 
state two to state one. The key here is to keep track of the indices of two cards that were clicked on during the last turn 
(in two separate variables) so you can test whether their values are equal during the next turn.

Tip #4 - Bonus tip for images
If you intend to use images in your mini-project, please remember to test your finished mini-project on a separate computer 
to make sure that your images will load successfully for your peers when they assess your project. It's your responsibility 
to make sure that the images load successfully.
Also, I would suggest that you hard code the size of your images into your mini-project. If you compute my_image.get_width() 
and my_image.get_height() before my_image has finished loading, these calls will return size zero. 
If you use a source rectangle of size zero in subsequent calls to draw_image(my_image, ...) , the call will throw a DOM error.


Tip #5 - A visual explanation of Memory's states (from post by Andrea)
I am seeing a lot of confusion over how the suggested implementation using states works in Memory. 
I suggest starting by reviewing this bit of code provided in the Memory lecture. 
Then I suggest that you review diagram below which is designed to show the the sequence of states 
that occur as the player clicks through the game. This is what steps 7 and 8 are asking you to code.



Tip #6 - Drawing cards using the list exposed and a for loop (from post by Rebecca)

I have seen lots of people confused by how to loop through the indices of the cards and draw the number or 
the blank card depending on the value of that card in the exposed list. I've written a version of the 
memory program that visualizes the indices of the cards, the values of the card list and the value of 
the exposed list, so you can see how these relate to each other, and how you can access them using the 
index of the cards. I hope this helps someone! Here is the start of the game: the game is in the first row, 
the card index is in the second row, the values of the cards in the third row, and the values of exposed in 
the fourth row. At the start of the game, all cards are face down, so the value of each element of exposed 
is False. (This is state 0.)




Below the first card has been clicked. The value of exposed[1] is True, so the draw handler draws the number at card_deck[1]. (This is state 1.)

Below a second, non-matching card has been clicked. The value of exposed[1] and exposed [3] are True, so the draw handler draws 
the number at card_deck[1] and card_deck[2]. All other values of exposed are False, so blank cards are drawn for these card indices. (This is state 2.)


Below the next unexposed card is clicked, the values of exposed in the first two cards are changed back to False. The new card index 
is 5, and now only exposed[5] is True in the exposed list so only card_deck[5] is drawn. (This is state 1.)


Below when there is a match, the corresponding elements in exposed are changed to True. (This is state 2.)


Below when another exposed card is clicked, with index 2, the exposed values for the matched cards stays as True, and exposed[2] is 
also changed to True, so the draw handler now draws the numbers at card_deck[2], card_deck[5] an card_deck[11]. (This is state 1.)


