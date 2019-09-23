# spiralDraw.py
# Draw a spiral in paint like program

import pyautogui, time

time.sleep(5)

pyautogui.click()	# click to get focus
distance = 200
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.2) # move right
	distance -= 5
	pyautogui.dragRel(0, distance, duration=0.2) # move down
	pyautogui.dragRel(-distance, 0, duration=0.2) # move left
	distance -= 5
	pyautogui.dragRel(0, -distance, duration=0.2) # move up
