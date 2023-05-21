from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get('https://www.mohmal.com/pt')

navegador.find_element('xpath','//*[@id="rand"]').click()

navegador.find_element('xpath', '//*[@id="email"]/div[1]')

email_element = navegador.find_element('xpath', '/html/body/div/div[1]/div[2]/div[3]/div[1]')

email = email_element.text

print(email)
