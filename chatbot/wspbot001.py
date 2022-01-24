from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path= './driver/chromedriver.exe')

def botWhatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)

botWhatsapp()