# type in IDLE and comment out line

import pyautogui
import time


def commentAfterDelay():
    pyautogui.click(100, 100)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)

    pyautogui.hotkey('alt', '3')
    # equilvilant to
    # pyautogui.keyDown('alt')
    # pyautogui.keyDown('3')
    # pyautogui.keyUp('3')
    # pyautogui.keyUp('alt')


commentAfterDelay()
