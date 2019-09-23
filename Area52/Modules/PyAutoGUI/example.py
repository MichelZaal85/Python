# PyAutoGUI module

import pyautogui

# moveTo
# Go to dimension first, before start.
for i in range(10):
	pyautogui.moveTo(100,100, duration=0.25)
	pyautogui.moveTo(200,100, duration=0.25)
	pyautogui.moveTo(200,200, duration=0.25)
	pyautogui.moveTo(100,200, duration=0.25)
	
	# if counter hits 5, Crosslike!
	if i == 5:
		for i in range(5):
			pyautogui.moveTo(100,100, duration=0.25)
			pyautogui.moveTo(200,200, duration=0.25)
			pyautogui.moveTo(200,100, duration=0.25)
			pyautogui.moveTo(100,200, duration=0.25)


# moveRel
# start movement from location
for i in range(10):
	pyautogui.moveRel(100,0,duration=0.25)
	pyautogui.moveRel(0,100,duration=0.25)
	pyautogui.moveRel(-100,0,duration=0.25)
	pyautogui.moveRel(0,-100,duration=0.25)

# Getting the mouse position
pyautogui.position()