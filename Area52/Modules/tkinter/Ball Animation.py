import time, tkinter

WIDTH = 1280
HEIGHT = 720

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Ball Animation")
canvas.pack()

ball = canvas.create_oval(30, 30, 6, 6, fill="blue")
xspeed, yspeed = 4, 5
n = 0

while True:
	canvas.move(ball, xspeed, yspeed)
	pos = canvas.coords(ball)
	if pos[3] >= HEIGHT or pos[1] <= 0:
		yspeed = -yspeed
	if pos[2] >= WIDTH or pos[0] <= 0:
		xspeed = -xspeed
	tk.update()
	# time.sleep(0.02)
	while True:
		time.sleep(1)
		n += 1
	time.sleep(n)
	tk.update()
tk.mainloop()