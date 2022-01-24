import pyautogui, webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+51962266334")
sleep(10)
pyautogui.typewrite("Probando")
sleep(2)
pyautogui.press("enter")
