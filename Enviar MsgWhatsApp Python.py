
import pandas as pd

contatos_df = pd.read_excel("Arquivo .xlsx com numero e nome")
display(contatos_df)


# In[20]: entrar no navegador, (google (chromium))
#importar tempo de resposta para a api não pegar e as keys (enter - enviar)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
        
    


# In[ ]: dar play

#jupyter

# @herick.szz

