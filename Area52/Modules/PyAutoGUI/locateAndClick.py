import pyautogui

# Locate screenshot image on screen
coordinates = pyautogui.locateOnScreen('clickMe.png')

# click center of found area
if coordinates != None:
	pyautogui.moveTo(pyautogui.center(coordinates))
	print('There you go sir!')
else:
	print('uhmm...')