try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


def tick():
    print('Tick')


timer = simplegui.create_timer(1000, tick)
timer.start()
