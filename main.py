from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd


contacts = pd.read_excel('Enviar.ods')
message = urllib.parse.quote(input('Digite a mensaggem desejada:'))
browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/")

for index,person in enumerate(contacts['Person']):
    while len(browser.find_elements_by_id("side")) < 1:
        time.sleep(1)
    
    number = str(contacts['Number'][index])
    link = f'https://web.whatsapp.com/send?phone={number}&text={message}'
    browser.get(link)
    
    while len(browser.find_elements_by_id("side")) < 1:
        time.sleep(1)
    sended = False
    while not sended:
        try:
            browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
            time.sleep(10)
            sended = True
        except:
            pass
