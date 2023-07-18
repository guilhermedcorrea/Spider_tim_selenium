from datetime import datetime
from typing import Any,Dict
import time
from io import BytesIO
from PIL import Image
from base64 import b64decode
from anticaptchaofficial.imagecaptcha import *
import urllib
import urllib.request
import sys
import os
try:
    sys.path.insert(0, r"C:\Users\Administrador\Documents\GitHub\rpa_rev1\app")
except Exception as e:
    print("error")
    
from typing import Any,Dict,Generator
#from get_capcha import resolve_captcha



path  = r"C:\Users\Administrador\Documents\GitHub\rpa_rev1\app\captchas\imagencaptcha"
solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("15c93d1529c3a1115d86f8d79b4c6a69")


class AllowCaptchaReceita:
    def __init__(self, driver, cpf):
        self.driver = driver
        self.cpf = cpf
        
    def get_url(self):
        self.driver.get("https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublicaSonoro.asp?CPF=&NASCIMENTO=%27")


    def get_image_captcha(self):
        
        try:
            image_captcha = self.WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((
                        By.ID, 'imgCaptcha'))
                )
            image_captcha_ = image_captcha.get_attribute("src")
        except Exception as e:
            print(e)

        return image_captcha_
    
    
    def download_image_captcha(self) -> None:
    
        src = self.get_image_captcha()

        imagem = urllib.request.urlretrieve(
                src, os.path.join(self.path,"image_captcha.png"))
        
        url_img = os.path.join(self.path,"image_captcha.png")
        
        return url_img
        
    def resolve_captcha(self) -> None:
        imagemdourl = self.download_image_captcha()

        self.solver.set_soft_id(0)

        captcha_text = self.solver.solve_and_return_solution(imagemdourl)
        if captcha_text != 0:
            textcaptcha = captcha_text.split()[0]
            dict_captcha = {"valorCaptcha":textcaptcha}
        
            return dict_captcha
            
        else:
            pass
    
    def check_user() -> None:
        try:
        
            wait = WebDriverWait(driver, 30)
            cpfuser = wait.until(EC.element_to_be_clickable((By.ID, 'txtCPF')))
            cpfuser.send_keys(cpf)

            wait = WebDriverWait(driver, 30)
            userdata = wait.until(EC.element_to_be_clickable((By.ID, 'txtDataNascimento')))
            userdata.send_keys(data)
        
        except Exception as e:
            print(e)

        
    def confirm_captcha() -> None:
        time.sleep(2)

        try:
            wait = WebDriverWait(driver, 30)
            text_captcha = wait.until(EC.element_to_be_clickable((By.ID, 'txtTexto_captcha_serpro_gov_br')))
            time.sleep(4)
            imgvalor = resolve_captcha()
            
            text_captcha.send_keys(imgvalor.get('valorCaptcha'))
            
            print(imgvalor.get('valorCaptcha'))
        
        except Exception as e:
            print(e, "error captcha")
            
        time.sleep(3)
        
        try:
            wait = WebDriverWait(driver, 40)
            buttomn = wait.until(EC.element_to_be_clickable((By.ID, 'id_submit')))
            buttomn.click()
            
        except Exception as e:
            print(e, "error Click")
        
    def get_cadastro_usuario(self) -> None:
    
        driver.implicitly_wait(5)
        try:
            user_values = driver.find_elements(
                By.XPATH, '//*[@id="mainComp"]/div[2]/p/span')
            items = [user.text for user in user_values]
            print(items)
        except Exception as e:
            print(e)
        


