import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER = Path(r'C:\Program Files\teste_selenium\chromedriver\chromedriver.exe')



def clear_all_chrome():
    

    def start_driver():
   
        delete_cache(driver)
        return driver


    def delete_cache(driver):
        driver.execute_script("window.open('')")  
        driver.switch_to.window(driver.window_handles[-1]) 
        driver.get('chrome://settings/clearBrowserData')  
        perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)  
        driver.close() 
        driver.switch_to.window(driver.window_handles[0]) 


    def perform_actions(driver, keys):
        actions = ActionChains(driver)
        actions.send_keys(keys)
        time.sleep(2)
        print('Concluido')
        actions.perform()
        
    start_driver()
    delete_cache()
    perform_actions()
    
clear_all_chrome() 


if __name__ == '__main__':
    driver = clear_all_chrome()
          



'''
   
class AllowCaptchaReceita:
    def __init__(self,cpf, path):
        self.cpf = cpf
        self.path = path
        
    def get_url(self):
        driver.get("https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublicaSonoro.asp?CPF=&NASCIMENTO=%27")

    def get_image_captcha(self):
        try:
            image_captcha = WebDriverWait(driver, 30).until(
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
        
    def check_user(self) -> None:
        try:
            wait = WebDriverWait(driver, 30)
            cpfuser = wait.until(EC.element_to_be_clickable((By.ID, 'txtCPF')))
            #cpfuser.send_keys()

            wait = WebDriverWait(driver, 30)
            userdata = wait.until(EC.element_to_be_clickable((By.ID, 'txtDataNascimento')))
            #userdata.send_keys()
        
        except Exception as e:
            print(e)
            
    def confirm_captcha(self) -> None:
        time.sleep(2)
        try:
            wait = WebDriverWait(driver, 30)
            text_captcha = wait.until(EC.element_to_be_clickable((By.ID, 'txtTexto_captcha_serpro_gov_br')))
            time.sleep(4)
            imgvalor = self.resolve_captcha()
            
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
        
'''