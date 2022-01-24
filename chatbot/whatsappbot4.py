import pyautogui
import time
import webbrowser

numero_telefono = '+51962266334'
url = 'https://web.whatsapp.com/send?phone='
webbrowser.open(url+numero_telefono)
time.sleep(8)
pyautogui.write('mensaje de prueba')
pyautogui.press('enter')
