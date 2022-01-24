import pyautogui
import os
import time
import webbrowser

#numero_telefono = '+51981530448'
#url = 'https://web.whatsapp.com/send?phone='
#webbrowser.open(url+numero_telefono)

pyautogui.hotkey('alt', 'tab')
time.sleep(10)

pyautogui.write('Hola, soy un robot', interval=0.20)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('Mi nombre es OSI, pero no soy un osito, soy pachón', interval=0.2)
pyautogui.press('enter')
