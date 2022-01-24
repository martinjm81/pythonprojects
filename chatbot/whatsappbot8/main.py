import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

def get_message():
    global x, y
    
    position = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x + 90, y - 40, duration=.5)
    pt.tripleClick()
    pt.hotkey('ctrl','c')
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_message)

    return whatsapp_message


def post_response(message):
    global x,y

    position = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration = .5)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)

def process_response(message):
    random_no = random.randrange(3)
    if "Buen día" in str(message).lower():
        return "Hola que tal!"
    else:
        if random_no == 0:
            return "Elegiste la opción 0!"
        elif random_no ==1:
            return "Elegiste la opción 1!"
        else:
            return "Por favor elije 0 o 1"

def check_for_new_messages():
    pt.moveTo(x + 50, y - 35, duration=.5)

    while True:
        posXY = pt.position()
        try:
            position = pt.locateOnScreen("green_circle.png", confidence=.8)
        
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
                processed_message = process_response(get_message())
                post_response(processed_message)

        except(Exception):
            print("No new users with new messages located")

#       if pt.pixelMatchesColor(int(x + 50), int(y - 35),(255,255,255), tolerance=10):
 #           print("is_white")
        #  else:
        #    print("no new messages yet...")
        sleep(5)

check_for_new_messages()
