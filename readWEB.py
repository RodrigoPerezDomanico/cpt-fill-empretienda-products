import click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from credentials import CREDENTIALS
from readSheet import getNewValues
from xpath import USERXPATH, PASSXPATH, BUTTONXPATH, LISTXPATH, EDIT_PRODUCTFULLXPATH


 
product_list=['6928475','6841341','6840939']


def fillInput(elm_xpath,fill_with):
    print (elm_xpath,fill_with)
    elem = driver.find_element(By.XPATH, elm_xpath)
    elem.clear()
    elem.send_keys(str(fill_with))

def editProductByIdx(i_prod,Values):
    # PRODUCTNAMESELECTOR='#p_nombre'
    IdxPRODUCTXPATH=f'/html/body/div[1]/div/main/div[5]/div/div[{i_prod}]/div/div/div/div/div[2]/div/div[4]/a'

    PRODUCTNAMEXPATH='//*[@name="p_nombre"]'
    PRODUCTPRICEXPATH='//*[@name="p_precio"]'
    PRODUCTSTOCK='//*[@name="s_cantidad"]'
    CHECKPRICEXPATH='//*[@name="p_mostrar_precio"]'
    SUBMITBUTTON='//*[@id="root"]/div/main/div[2]/div/div[6]/div/div/div/div[1]/button'
    

   
    # url=str('https://panel.empretienda.com/productos')
    # driver.get(url)
    # time.sleep(2)
    try:
        prod_element=driver.find_element(By.XPATH,IdxPRODUCTXPATH)
        prod_url=prod_element.get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(prod_url)
        time.sleep(2)
        product_name = driver.find_element(By.XPATH, PRODUCTNAMEXPATH).get_attribute('value')
        product_price = driver.find_element(By.XPATH, PRODUCTPRICEXPATH).get_attribute('value')
        product_stock = driver.find_element(By.XPATH, PRODUCTSTOCK).get_attribute('value')
        product_check_price = driver.find_element(By.XPATH, CHECKPRICEXPATH).get_attribute('value')
        # getNewValues(product_name)
            
        print(product_name)
        for value in Values:
            if value[0]==product_name:
                if product_price!= value[1] or product_stock!= value[2]:
                    print(f'Actualizar precios de {product_name}')
                    if product_check_price==0:
                        driver.find_element(By.XPATH, CHECKPRICEXPATH).click()
                    fillInput(PRODUCTPRICEXPATH,value[1])
                    fillInput(PRODUCTSTOCK,int(value[2]))
                    driver.find_element(By.XPATH, SUBMITBUTTON).click()
                    time.sleep(1)


                    

                    
        i_prod+=1
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return i_prod
    except IndexError:
        print('Hubo un error')
        return 0

def editProduct(prod,Values):
    # PRODUCTNAMESELECTOR='#p_nombre'
    PRODUCTNAMEXPATH='//*[@name="p_nombre"]'
    PRODUCTPRICEXPATH='//*[@name="p_precio"]'
    PRODUCTSTOCK='//*[@name="s_cantidad"]'
   
    url=str('https://panel.empretienda.com/productos/'+str(prod))
    driver.get(url)
    time.sleep(3)
    product_name = driver.find_element(By.XPATH, PRODUCTNAMEXPATH).get_attribute('value')
    product_price = driver.find_element(By.XPATH, PRODUCTPRICEXPATH).get_attribute('value')
    product_stock = driver.find_element(By.XPATH, PRODUCTSTOCK).get_attribute('value')
    # getNewValues(product_name)
    	
    print(product_name)

def expandProductsList():
    see_more_products=True
    new_click=0
    while see_more_products:
        try:
            see_more_buton= driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div[6]/div/button')
            see_more_buton.click()
            time.sleep(2)
            new_click+=1
            if new_click==1:
                print('Aguarde mientras se expande la lisa de productos')
        except:
            see_more_products=False






Xpath='/html/body/div[4]/div/nav[1]/ul/li[2]/ul/li[4]/a'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
try:
    driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
except:
    driver = webdriver.Chrome('./chromedriver',chrome_options=options)
driver.get("https://panel.empretienda.com/login")
assert "Empretienda" in driver.title

fillInput(USERXPATH,CREDENTIALS['user'])
fillInput(PASSXPATH,CREDENTIALS['pass'])
search_button = driver.find_element(By.XPATH, BUTTONXPATH)
search_button.submit()
time.sleep(3)
driver.get("https://panel.empretienda.com/productos")
time.sleep(2)


SHEETSVALUES=getNewValues()

expandProductsList()



i_prod=1
while i_prod>0:
# for i_prod in range(1,4):
    i_prod=editProductByIdx(i_prod,SHEETSVALUES)


# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
time.sleep(1)
driver.close()
