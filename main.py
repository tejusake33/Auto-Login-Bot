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

username = "Your-username"
password = "Your-Password"

url = "url-you-want-to-login"

startbot(username,password,url)