# pyautogui Click
import pyautogui
pyautogui.click(10,5, duration=0.25)
pyautogui.click(100,5, button='left', duration=0.25)
pyautogui.click(100,5, button='right', duration=0.25)


# Clicking
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.doubleClick()

pyautogui.click()
pyautogui.rightClick()
pyautogui.middleClick()

# Drag to
pyautogui.dragTo()
# equal to
pyautogui.moveTo

pyautogui.dragRel()
# equal to
pyautogui.moveRel()