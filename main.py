import pyautogui as pg
import keyboard
import time

times = 10
delay = 5
paused = True
running = True

while running:
    if keyboard.is_pressed(']'):
        if paused:
            paused = False
        else: paused = True
    elif keyboard.is_pressed('escape'):
        running = False
    pg.leftClick(x = 500,y = 810)
    pg.leftClick(x = 500,y = 810)
    for i in range(times):
        pg.typewrite(';p\n')
        pg.leftClick(x = 500,y = 810)
        time.sleep(delay)
        pg.typewrite('pb\n')
        pg.leftClick(x = 500,y = 810)
        time.sleep(2)
    
    
    
