import simpleguitk as simplegui

def draw_handler(canvas):
    canvas.draw_polygon([(10, 20), (20, 30), (30, 10)], 12, 'Green')
    # canvas.draw_polygon([[30, 20], [40, 40], [50, 20], [10, 10]], 12, 'Red')
    # canvas.draw_polygon([(50, 70), (80, 40), (30, 90)], 5, 'Blue', 'White')
    # canvas.draw_polygon([[90, 70], [80, 40], [70, 90], [70, 70]], 12, 'Yellow', 'Orange')

frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()