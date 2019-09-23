import random
try:
    import simplegui
except ImportError:
    try:
        import simpleguitk as simplegui
    except ImportError:
        print('No simplegui module installed.')

# define globals
WIDTH = 75
HEIGHT = 150
TILES = 8


# helper function to initialize globals
def new_game():
    global my_tiles, state, turns

    tile_numbers = [i for i in range(0, TILES)] * 2
    random.shuffle(tile_numbers)
    my_tiles = [Tile(tile_numbers[i], False, [WIDTH * i, HEIGHT]) for i in range(2 * TILES)]

    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))


# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.text_color = 'white'
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
            text_location = [loc[0] + 0.2 * WIDTH, loc[1] - 0.3 * HEIGHT]
            canvas.draw_text(str(self.number), text_location, WIDTH, self.text_color)
        else:
            tile_corners = (loc, [loc[0] + WIDTH, loc[1]], [loc[0] + WIDTH, loc[1] - HEIGHT], [loc[0], loc[1] - HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] <= self.location[0] + WIDTH
        inside_vert = self.location[1] - HEIGHT <= pos[1] <= self.location[1]
        return inside_hor and inside_vert


def mouseclick(pos):
    global state, turns, turn1_tile, turn2_tile

    for tile in my_tiles:
        if tile.is_selected(pos):
            clicked_tile = tile

    if clicked_tile.is_exposed():
        return

    clicked_tile.expose_tile()

    if state == 0:
        state = 1
        turn1_tile = clicked_tile
    elif state == 1:
        state = 2
        turn2_tile = clicked_tile
        turns += 1
        label.set_text("Turns = " + str(turns))
    else:
        if turn1_tile.get_number() != turn2_tile.get_number():
            turn1_tile.hide_tile()
            turn2_tile.hide_tile()
        else:
            turn1_tile.text_color = 'yellow'
            turn2_tile.text_color = 'yellow'
        state = 1
        turn1_tile = clicked_tile


# draw handler
def draw(canvas):
    for tile in my_tiles:
        tile.draw_tile(canvas)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * TILES * WIDTH, HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

# get things rolling
new_game()
frame.start()
