from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from credentials import CREDENTIALS
from readSheet import getNewValues
from xpath import USERXPATH, PASSXPATH, BUTTONXPATH, LISTXPATH, EDIT_PRODUCTFULLXPATH
from selenium.common.exceptions import NoSuchElementException


 
product_list=['6928475','6841341','6840939']


def fillInput(elm_xpath,fill_with):
    print (elm_xpath,fill_with)
    elem = driver.find_element(By.XPATH, elm_xpath)
    elem.clear()
    elem.send_keys(str(fill_with))

def sendProductsOutOfWEB(Values):
    products_out_of_web=[]
    for value in Values:
        if not value[4]:
            products_out_of_web.append([value[0],value[3]])
    print(products_out_of_web)
    return products_out_of_web

def editProductByIdx(i_prod,Values):
    # PRODUCTNAMESELECTOR='#p_nombre'
    IdxPRODUCTXPATH=f'/html/body/div[1]/div/main/div[5]/div/div[{i_prod}]/div/div/div/div/div[2]/div/div[4]/a'

    PRODUCTNAMEXPATH='//*[@name="p_nombre"]'
    PRODUCTPRICEXPATH='//*[@name="p_precio"]'
    PRODUCTSTOCK='//*[@name="s_cantidad"]'
    PRODUCTCODEXPATH='//*[@name="s_sku"]'
    CHECKPRICEXPATH='//*[@name="p_mostrar_precio"][@type="checkbox"]'
    SUBMITBUTTON='//*[@id="root"]/div/main/div[2]/div/div[6]/div/div/div/div[1]/button'
    PRODUCTTYPEXPATH='//*[@id="select-idCategorias"]'
    

   
    # url=str('https://panel.empretienda.com/productos')
    # driver.get(url)
    # time.sleep(2)
    try:
        prod_element=driver.find_element(By.XPATH,IdxPRODUCTXPATH)
        prod_url=prod_element.get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(prod_url)
        time.sleep(3)
        product_name = driver.find_element(By.XPATH, PRODUCTNAMEXPATH).get_attribute('value')
        product_price = driver.find_element(By.XPATH, PRODUCTPRICEXPATH).get_attribute('value')
        product_stock = driver.find_element(By.XPATH, PRODUCTSTOCK).get_attribute('value')
        product_type = driver.find_element(By.XPATH, PRODUCTTYPEXPATH).text

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        product_code = driver.find_element(By.XPATH, PRODUCTCODEXPATH).get_attribute('value') # Recordar revisar y cambiar -- por /, '/' esta en excel, -- en web
        print(product_type)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        product_check_price = driver.find_element(By.XPATH, CHECKPRICEXPATH)
        print(product_check_price.get_attribute('value'))
        # getNewValues(product_name)
            
        print(product_name)
        for idx, value in enumerate(Values):
            if product_type == 'Notebooks':
                if not product_code or product_check_price.get_attribute('value')=='0':
                    if product_check_price.get_attribute('value')=='0':
                        product_check_price.click() 
                    fillInput(PRODUCTSTOCK,'0')
                    fillInput(PRODUCTPRICEXPATH,'1')
                    Values.append([product_name,'No vinculado','No vinculado','No vinculado',False])
                    driver.find_element(By.XPATH, SUBMITBUTTON).click()
                    time.sleep(3)
                    i_prod+=1
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    return i_prod, Values

                elif value[3]==product_code.replace('--','/'):
                    Values[idx][4]=True

                    if product_check_price.get_attribute('value')=='0' and product_stock!=0:
                        product_check_price.click()
                        print(f'Actualizar precios de {product_name}')
                        if product_price!= value[1]:
                            fillInput(PRODUCTPRICEXPATH,value[1])
                        if product_stock!= value[2]:
                            fillInput(PRODUCTSTOCK,int(value[2]))
                        

                    # elif product_check_price.get_attribute('value')=='1' and product_stock==0:
                    #     product_check_price.click()

                    
                        
                        
                    driver.find_element(By.XPATH, SUBMITBUTTON).click()
                    time.sleep(3)
                    i_prod+=1
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    return i_prod, Values
                


                    

        #Values.append([product_name,'No vinculado'])                    
        i_prod+=1
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return i_prod, Values
    except NoSuchElementException:
        print('Se terminaron los elementos de la lista')
        # sendProductsOutOfWEB(Values)
        return 0, Values

# def editProduct(prod,Values):
#     # PRODUCTNAMESELECTOR='#p_nombre'
#     PRODUCTNAMEXPATH='//*[@name="p_nombre"]'
#     PRODUCTPRICEXPATH='//*[@name="p_precio"]'
#     PRODUCTSTOCK='//*[@name="s_cantidad"]'
   
#     url=str('https://panel.empretienda.com/productos/'+str(prod))
#     driver.get(url)
#     time.sleep(3)
#     product_name = driver.find_element(By.XPATH, PRODUCTNAMEXPATH).get_attribute('value')
#     product_price = driver.find_element(By.XPATH, PRODUCTPRICEXPATH).get_attribute('value')
#     product_stock = driver.find_element(By.XPATH, PRODUCTSTOCK).get_attribute('value')
#     # getNewValues(product_name)
    	
#     print(product_name)

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



def notRegistratedProducts(Values):
    noRegistrated=[]
    for value in Values:
        if not value[4]:
            noRegistrated.append([value[0],value[3]])
    
    return noRegistrated


Xpath='/html/body/div[4]/div/nav[1]/ul/li[2]/ul/li[4]/a'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument('headless')
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
time.sleep(5)
driver.get("https://panel.empretienda.com/productos")
time.sleep(2)


SHEETSVALUES=getNewValues()

expandProductsList()



i_prod=1
while i_prod>0:
# for i_prod in range(1,4):
    i_prod,SHEETSVALUES=editProductByIdx(i_prod,SHEETSVALUES)


# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# print(SHEETSVALUES)
not_edited=notRegistratedProducts(SHEETSVALUES)

with open('ProductosNoRegistrados.txt','w') as f:
    for product in not_edited:
        f.write(f'{product} \n')
time.sleep(1)
driver.close()
