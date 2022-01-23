import keyboard
import mouse
import time
clicking = False

def clicker():
    global clicking
    if clicking:
        clicking = False
        print('Off')
    else:
        clicking = True

keyboard.add_hotkey('Alt + 2', clicker)

while True:
    if clicking:
        mouse.double_click(button = 'left')
        time.sleep(0.1)
