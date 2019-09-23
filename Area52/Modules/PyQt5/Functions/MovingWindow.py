#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys, random, time, pyautogui
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.show()
    x = pyautogui.size()[0]
    y = pyautogui.size()[1]

    for i in range(100):
        w.resize(i+250, i+150)
        if i == 50:
            w.move(x/2-250,y/2)
            time.sleep(3)
        # w.move(random.randint(0,x), random.randint(0,y))
        time.sleep(0.1)
        print('Run: ',i)
    print('Done')
    w.setWindowTitle('You\'re Hacked')
    w.close()
    sys.exit()
