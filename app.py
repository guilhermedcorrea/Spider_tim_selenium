from controllers.controllers import get_user_infos
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.chrome.options import Options
import time
from controllers.controllers import get_user_infos
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, title_contains, title_is
from io import BytesIO
from PIL import Image
from base64 import b64decode
from anticaptchaofficial.imagecaptcha import *
import urllib
import urllib.request
import sys


"""CHROMEDRIVER"""

options = webdriver.ChromeOptions()

options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

DRIVER_PATH=r"C:\Program Files\teste_selenium\chromedriver\chromedriver.exe"
service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


driver.maximize_window()

myfile = r"C:\Program Files\teste_selenium\cookie\cookies.pkl"

"""HISTORICO COOKIES | LOGIN"""

try:
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:
        
        print("Error: %s Arquivo nao encontrado" % myfile)
except Exception as e:
    print(e)


"""Close All Chrome"""

def close_all_chrome() -> None:
    driver_len = len(driver.window_handles) 
    print("Tot abas = ", driver_len)
    if driver_len > 1:
        for i in range(driver_len - 1, 0, -1):
            driver.switch_to.window(driver.window_handles[i]) 
            driver.close()
            print("Fechar ", i)
        driver.switch_to.window(driver.window_handles[0]) 
    else:
        print("Nao encontrado.")

def clear_all_chromedriver() -> None:
    
    def start_driver() -> None:
        delete_cache(driver)
        return driver

    def delete_cache(driver) -> None:
        driver.execute_script("window.open('')")  
        driver.switch_to.window(driver.window_handles[-1]) 
        driver.get('chrome://settings/clearBrowserData')  
        perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)  
        driver.close() 
        driver.switch_to.window(driver.window_handles[0]) 

    def perform_actions(driver, keys) -> None:
        actions = ActionChains(driver)
        actions.send_keys(keys)
        time.sleep(2)
        print('Concluido')
        actions.perform()
        
    start_driver()
    
          
clear_all_chromedriver()

time.sleep(5)   

close_all_chrome()

time.sleep(5)



driver.get("https://pacportal.timbrasil.com.br/")

driver.delete_all_cookies()

""" SALVANDO E CARREGANDO COOKIES"""
driver.execute_script("return navigator.userAgent")

pickle.dump(driver.get_cookies() , open(r"C:\Program Files\teste_selenium\cookie\cookies.pkl","wb"))

cookies = pickle.load(open(r"C:\Program Files\teste_selenium\cookie\cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(4)

def login_usuario() -> None:
    """LOGIN USUARIO"""
    time.sleep(5)
    try:
        usuario = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.ID, "USERNAME"))
                    )
        usuario.send_keys('T3577034')
        password = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.ID, "PASSWORD"))
                    )
        password.send_keys('075393')
        
        button = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.ID, "btnSubmit"))
                    )

        button.click()
    except Exception as e:
        print(e, "erro login_usuario")
    
    time.sleep(5)

def find_cliente_reference(timeout=10):
    #RETORNA ELEMENTO DO CLIENTE
    global ref_user
    ref_user =next(get_user_infos())[0]
    if isinstance(ref_user, str):
        try:

            element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((
                By.NAME, "s_2_1_0_0")))
            #element.click()
            ActionChains(driver)\
            .send_keys_to_element(element,ref_user)\
            .perform()  
        except Exception as e:
            print(e) 
            
        try:
            confirma = WebDriverWait(driver, 40).until(EC.presence_of_element_located((
                    By.ID, "s_2_1_4_0_Ctrl")))
            actions = ActionChains(driver)
            actions.click(confirma)
            actions.perform()

        except Exception as e:
            print(e)
        
        time.sleep(4)
     
def wait_to_load(delay=40) -> None:
    driver.refresh()
    
    time.sleep(5)

    driver.get("https://siebelcrm.timbrasil.com.br/siebel/app/vnd/ptb/?SWECmd=Login&SWEPL=1&SRN=&SWETS=")

    time.sleep(7)
    find_cliente_reference(40)

        
login_usuario()        
wait_to_load(40)
#driver.quit()
