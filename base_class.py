

from controllers.controllers import get_user_infos
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import os
from selenium.webdriver.chrome.options import Options
import time
from controllers.controllers import get_user_infos
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path



"""CHROMEDRIVER"""

options = webdriver.ChromeOptions()

options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

DRIVER_PATH=r"C:\Program Files\teste_selenium\chromedriver\chromedriver.exe"
service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()


class visibility_of(object):
  
    def __init__(self, element):
        self.element = element

    def __call__(self, ignored):
        return _element_if_visible(self.element)


def _element_if_visible(element, visibility=True):
    return element if element.is_displayed() == visibility else False

class presence_of_all_elements_located(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        return _find_elements(driver, self.locator)


class visibility_of_any_elements_located(object):
   
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        return [element for element in _find_elements(driver, self.locator) if _element_if_visible(element)]


class visibility_of_all_elements_located(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elements = _find_elements(driver, self.locator)
            for element in elements:
                if _element_if_visible(element, visibility=False):
                    return False
            return elements
        except StaleElementReferenceException:
            return False


class text_to_be_present_in_element(object):
    """ An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = _find_element(driver, self.locator).text
            return self.text in element_text
        except StaleElementReferenceException:
            return False


class text_to_be_present_in_element_value(object):

    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = _find_element(driver,
                                         self.locator).get_attribute("value")
            if element_text:
                return self.text in element_text
            else:
                return False
        except StaleElementReferenceException:
                return False





    '''
    try:
        cliente_ref = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((
                    By.XPATH, '//*[@id="s_S_A2_div"]/form/div/span/div[3]/div/div/table/tbody/tr[3]/td[3]/div/input'))
                        )

    except Exception as e:
        print(e, "erro search_client")
    '''
        
   
    '''
    try:
        search = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((
                    By.ID,'Name_Label_2'))
                        )
        search.send_keys(next(get_user_infos())[0])
        
    except Exception as e:
        print(e, "erro search")
    '''
    '''
    try:
        my_element = driver.find_element(By.XPATH,"//div[text()='CPF/CNPJ']")
        my_element.send_keys(next(get_user_infos())[0])
    except Exception as e:
        print(e)
    
    time.sleep(3)
        
    try:
        cal =  WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((
                    By.ID,'s_2_1_4_0_Ctrl'))
                        )
        cal.click()
    except Exception as e:
        print(e, "erro cal")
    
    time.sleep(500)
        
    '''
    
    
    
    def search_client() -> None:
    time.sleep(4)
    
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((
            By.XPATH, "//*[contains(text(), 'Pesquise o Cliente')]")))
        #element.send_keys(next(get_user_infos())[0])
    except Exception as e:
        print(e)
        
    time.sleep(5)
    
    find_cliente_reference()
    '''
    try:
        cal =  WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((
                    By.ID,'s_2_1_4_0_Ctrl'))
                        )
        cal.click()
    except Exception as e:
        print(e, "erro cal")
    '''