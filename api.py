from fastapi import FastAPI
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import schedule
import time
import threading

app = FastAPI()

def get_email():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=chrome_options)
    navegador.get('https://www.mohmal.com/pt')
    navegador.find_element('xpath', '//*[@id="rand"]').click()
    email_element = navegador.find_element('xpath', '/html/body/div/div[1]/div[2]/div[3]/div[1]')
    email = email_element.text
    print(email)
    navegador.quit()
    return email

email = get_email()

def update_email():
    global email
    email = get_email()

schedule.every(1).seconds.do(update_email)  # Run update_email function every 1 second

@app.get("/")
def home():
    return {"emailmohmal": email}

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(0.1)

# Run the schedule in a separate thread
schedule_thread = threading.Thread(target=run_schedule)
schedule_thread.start()