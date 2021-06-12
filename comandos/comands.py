from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 


class Ligar:
    
    def __init__(self):
        pass
    def calculo(self, preco, quantidade):

		chrome_options = Options()
		#chrome_options.add_argument("--headless") 

		#lembrar de add no path e verificar versão do google chrome
		p = '/usr/local/bin'

		driver = webdriver.Chrome(p +'/chromedriver', options=chrome_options)