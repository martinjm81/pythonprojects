from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path= './driver/chromedriver.exe')

def validaQR():
    try:
        element = browser.find_element_by_tab_name("canvas")
    except:
        return False
    return True

def botWhatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)

    espera = True

    while espera:
        print("Esperando ...")
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            print("¡Autenticado!")
            break

botWhatsapp()


