import pyautogui
import os
import time
import webbrowser

# -*- coding: UTF-8 -*-

numero_telefono = pyautogui.prompt('Indique el número de telefono')
web = 'https://web.whatsapp.com/send?phone='
opciones = '&text&app_absent=1'

#url = 'https://web.whatsapp.com/send?phone=51992773744&text&app_absent=1'
#url = 'https://web.whatsapp.com/send?phone=51981530448&text&app_absent=1'
url = web + numero_telefono + opciones

webbrowser.open(url) 
time.sleep(20)
pyautogui.hotkey('ctrl','l')
pyautogui.press('tab', presses=11, interval=0.20)

pyautogui.write('Hola, me llamo Alex coronado, asistente academico en IEL', interval=0.10)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('Le escribimos porque mostro interes por nuestros cursos', interval=0.10)
pyautogui.press('enter')