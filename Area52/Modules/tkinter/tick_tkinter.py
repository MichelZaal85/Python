#
#  this takes Scott's first simplegui example, 'tick', and shows how to
#    convert it to Python's built-in GUI, tkinter
#
#  http://www.codeskulptor.org/#user11_PZmhAoItSY0EA88.py for Scott's original
#     code
#
#  refer to this one as sg_tick_tkinter.py if asking questions
#
#  this runs in Python 3.2.3 ... to run in V2.7.3 change the first line
#
#  this does not print to the new tkinter window, it just prints to the
#    console (just as Scott's first example does)


# import simplegui      #$$  the next two lines replace this

from tkinter import *   #$$ change tkinter -> Tkinter to run on V2.7.3
root = Tk()             #   opens a new window I've named 'root'

#root.title("Tick")     # uncomment this to add a name to the top of the window
                        # replacing the default "Tk" name

#root.geometry("320x400")  # uncomment this to make the window 320x400 pixels
                           # rather than use the default size

#root.geometry("320x400+500+300")   # uncomment this to offset the window by
                                    #  500 pixels in X-direction and 300 pixels
                                    #   in y-direction


def tick():                # this is Scott's function but I've added one line
    print ("tick!")        #  to make it call itself every 1000 mseconds
    root.after( 1000, tick )

#timer = simplegui.create_timer(1000, tick)   #$$ replaced with 2 lines
#
root.after(1000, tick)   # this runs one time after 1,000 ms, calling 'tick'
              #  as the event handler.  Had to add this line inside the 'tick'
              #  function to get it to repeat in tkinter

# timer.start()    # replace this simplegui line with the next line
mainloop()