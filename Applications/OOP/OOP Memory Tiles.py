# Initialize a game of Memory using the Tile class

#################################################
# Student adds code where appropriate

import simpleguitk as simplegui
import random

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

# helper function to initialize globals
def new_game():
    global my_tiles, state, turns

    tile_numbers = [i for i in range(0, DISTINCT_TILES)] * 2
    random.shuffle(tile_numbers)
    my_tiles = [Tile(tile_numbers[i], False, [TILE_WIDTH * i, TILE_HEIGHT]) for i in range(2 * DISTINCT_TILES)]

    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))

# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # definition of getter for number
    def get_number(self):
        return self.number

    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed

    # expose the tile
    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    # string method for tiles
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] <= self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert


# draw handler
def draw(canvas):
    for tile in my_tiles:
        tile.draw_tile(canvas)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


###################################################
# Create a horizontal row of 16 Memory tile with numbers hidden


'''
We now return to Memory.
For this problem, your task is to initialize a game of Memory using the Tile class.
Starting from the provided template, complete the implementation of the function
new_game() that initializes our version of Memory.

In particular, create a list with two copies of the numbers in range(0, DISTINCT_TILES)
and use random.shuffle to shuffle the list. Then, use the initializer for the Tile class to create a horizontal
row of 2*DISTINCT_TILES tiles whose numbers are hidden.
Finally, implement a draw handler using the draw method for the Tile class that draw all 16 tiles on the canvas.
'''
# Initialize a game of Memory using the Tile class

#################################################
# Student adds code where appropriate

'''

import simpleguitk as simplegui
import random

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8


# helper function to initialize globals
def new_game():
    global my_tiles, state, turns

    # add code here
    my_tiles = [i for i in range(0, DISTINCT_TILES)] * 2
    my_tiles = random.shuffle(my_tiles)
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))


# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc
        self.tiles = 2 * DISTINCT_TILES

    # definition of getter for number
    def get_number(self):
        return self.number

    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed

    # expose the tile
    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    # string method for tiles
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return inside_hor and inside_vert


# draw handler
def draw(canvas):
	for card in my_tiles:
		card.draw_tile()

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


###################################################
# Create a horizontal row of 16 Memory tile with numbers hidden
'''