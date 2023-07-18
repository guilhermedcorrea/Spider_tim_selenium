

```Python

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


```
<b>Fecha todas as abas abertas atualmente</b>

```Python

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


```
<b>Limpa todo historico e cookies de todo o periodo</b>


```Python

def query_database_akiva() -> Generator:
    engine = engine_akiva()
    with engine.begin () as conn:
        result = conn.execute(text(qry_select)).all()
        if next(filter(lambda k: k if len(k) >0 or re.search("[0-9]{8,}",str(k)) > 0 else None, result)):
            yield result


def get_user_infos() -> None:
    news = query_database_akiva()
    try:
        ref_user = [re.findall("[0-9]{9,16}",str(item)) for item in chain.from_iterable(news) if item != '']
        cont = len(ref_user)
        i = 0
        while i < cont:
            yield ref_user[i]
            
            i+=1

    except Exception as e:
        print(e)

```

<b>Executa consulta</b>


```Python

driver.get("https://pacportal.timbrasil.com.br/")

driver.delete_all_cookies()

""" SALVANDO E CARREGANDO COOKIES"""
driver.execute_script("return navigator.userAgent")

pickle.dump(driver.get_cookies() , open(r"C:\Program Files\teste_selenium\cookie\cookies.pkl","wb"))

cookies = pickle.load(open(r"C:\Program Files\teste_selenium\cookie\cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(4)
```


<b>Salva Cookies </b>



