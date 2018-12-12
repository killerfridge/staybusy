#! python3
# stayBusy.py - keeps the mouse moving despite me not being there to move my mouse
# as I am usually just using the keyboard

import pyautogui as pyg
import time
import datetime as dt

BREAKTIME = dt.time(18,30)
BREAKDATE = dt.datetime.combine(dt.date.today(), BREAKTIME)
counter = 0

try:
    while True:
        if dt.datetime.now() > BREAKDATE:
            print('Time to go home')
            time.sleep(10)
            break
        xThen, yThen = pyg.position()
        time.sleep(180)
        xNow, yNow = pyg.position()
        if (xThen,yThen) == (xNow, yNow):
            print(f'{dt.datetime.now(): %H:%M:%S}')
            pyg.moveRel(1,0,duration=0.01)
            pyg.moveRel(-1,0,duration=0.01)
            pyg.keyDown('shift')
            pyg.keyUp('shift')
            counter += 1
            # pyg.click()
        

            
except KeyboardInterrupt:
    string = f'Today you were saved {counter} times'
    filename = f'log {dt.datetime.now(): %y-%m-%d %H%M}.txt'
    f = open(filename, 'w')
    f.write(string)
    f.close()
    print('Done.')
