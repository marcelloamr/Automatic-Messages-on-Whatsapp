from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import numpy as np

numeros= np.arange(5531987056101,5531987056301,1) # intervalo entre o primeiro e ultimo número 
# do +55 (31) 9 8705-6101 até o + 55 (31) 9 8705-6301
#caso queira pode usar a sua lista de números, usando csv ou outro meio, usei essa aleatória

message_text = 'Olá colega, tudo jóia? Desculpa por tomar seu tempo, mas essa é a mensagem automática ' # mensagem
no_of_message=1 # numero de mensagens  
moblie_no_list=numeros # lista de telefones


def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()

driver = webdriver.Chrome(executable_path="chromedriver.exe") # veja se o chromedriver está na mesma pasta em que o códigobase.py
driver.get("http://web.whatsapp.com")
sleep(10) #Tempo para você scanear o código com o seu telefone

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',12)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :"+str(phone_no)) #retorna os número que não foram reconhecidos
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)

    except Exception as e:
        sleep(5)
        is_connected()
