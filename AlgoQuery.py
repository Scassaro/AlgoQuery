from urllib.request import urlopen
import requests
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless=new")

url = "https://algoexplorer.io/"
driver = webdriver.Firefox(options=options)
driver.get(url)
driver.find_element_by_css_selector("[data-cy='latestBlocksLink']").click()
driver.implicitly_wait(50)
array = driver.find_elements_by_xpath("//a[@data-cy='round']")
for select in array:
    print(select.text)
    if select.text != '':
        lastestEmpty = select.text
    else:
        print('could not find the latest empty block')
        driver.quit()
    select.click()
iterations = 0
identicals = 0
value = ''
time.sleep(4)
rows = driver.find_elements(By.CSS_SELECTOR, "tr[class^='row']")
optinCount = 0
transferCount = 0
createCount = 0
pageIterations = driver.find_element_by_css_selector("[data-cy='TotalTransactions']").text
print('iterations ' + str(int(pageIterations)//10))
for i in range(1, int(pageIterations)//10):
    for row in rows:
        if(row.text.find('Opt-In') > 0):
            optinCount+=1
        if(row.text.find('Transfer') > 0):  
            transferCount+=1
        if(row.text.find('Config') > 0):
            print('Found a created coin!')
            print(row.text)
            createCount+=1
        # print(row.text)
    pageIterations = driver.find_element_by_css_selector("[data-cy='next']").click


print(optinCount)
print(transferCount)
print(createCount)
driver.quit()
