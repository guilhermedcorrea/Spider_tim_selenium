
"""Clousure"""
'''
def spider_tim_vinculo():
    driver.get("https://pacportal.timbrasil.com.br/")

    driver.delete_all_cookies()
    
    def save_cookies() -> None:
        
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
            password.send_keys('468192')
            
            button = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.ID, "btnSubmit"))
                        )

            button.click()
        except Exception as e:
            print(e, "erro login_usuario")
        
        time.sleep(5)
        
    def find_cliente_reference(timeout=10) -> None:
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
    save_cookies()        
    wait_to_load(40)
                
            
    
   
spider_tim_vinculo()       
        
        
        
    
        
    
    
    
'''