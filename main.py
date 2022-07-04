import pandas as pd
# import webdriver
from selenium import webdriver
 
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
 
# import KEYS
from selenium.webdriver.common.keys import Keys

# import Options for chrome
from selenium.webdriver.chrome.options import Options

#waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "D:\webdriver\chromedriver.exe"
op = webdriver.ChromeOptions() 
op.add_argument("start-maximized")

driver = webdriver.Chrome(PATH, options = op)



class mr_scraper:

    def get(self,url):
        driver.get(url)

    def find(self,xpath):
        element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        #element.getText()

    def wait_for_element(self,xpath):
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))

    def text(self,xpath):
        element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, xpath))).text
        return element


list = []

x = mr_scraper()

x.get("https://www.thefoodcoach.com.au/food/?Alpha=%5BA-Z%5D")

x.wait_for_element('/html/body/div[6]/div[2]/div[1]')

x.find('/html/body/div[6]/div[2]/div[1]')

for z in range(1,4):
    for i in range(1,212):
        text = x.text(f'/html/body/div[2]/div[1]/table/tbody/tr[{i}]/td[{z}]/a')
        list.append(text)

df = pd.DataFrame(list).to_csv("text.csv", index=False)
driver.quit()