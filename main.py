import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

def startbot(username, password, url):
    path = "E:\\Python\\chromedriver-win64\\chromedriver.exe"

    service = Service(path)
    # driver = webdriver.Chrome(path)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "btnSubmit").click()

    time.sleep(60)
    driver.quit()

username = "sakharetejashree@gmail.com"
password = "Tejashree@2002"

url = "https://intapidm.infosysapps.com/auth/realms/careersite/protocol/openid-connect/auth?client_id=careersite&redirect_uri=https%3A%2F%2Fcareer.infosys.com%2Fjobs%2Fmyapplication&state=1a8ecf4f-22dc-4f57-b83a-3747e7ae6871&response_mode=fragment&response_type=code&scope=openid&nonce=11ac6448-bad5-45e1-8d64-e0b6a2985d11"

startbot(username,password,url)