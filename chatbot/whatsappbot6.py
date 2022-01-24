import pyautogui
import os
import time
import webbrowser

   #numero_telefono = '+51981530448'
    #url = 'https://web.whatsapp.com/send?phone='
    #webbrowser.open(url+numero_telefono)

#https: // web.whatsapp.com/send?phone = 51992773744 & text & app_absent = 1

with pyautogui.hold('alt'):
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','l')

time.sleep(1)
pyautogui.write('Hola, soy un robot', interval=0.20)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('Mi nombre es OSI, pero no soy un osito, soy pachón', interval=0.2)
pyautogui.press('enter')
