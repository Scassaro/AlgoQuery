from urllib.request import urlopen
import requests
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains

options = FirefoxOptions()
options.add_argument("--headless=new")

discord_url = "https://discord.com/api/webhooks/940365158629396510/mYkK_FRVE8ZbwbQnQxfDxNzJ7j3NKIbovBlNh_jhG6D3oG7KLMYTCmFlLJnFtFZJflvU"
url = "https://algoexplorer.io/"

driver = webdriver.Firefox(options=options)
actions = ActionChains(driver)
for i in range(100):
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
    pageIterations = driver.find_element_by_css_selector("[data-cy='pagination']").text
    # print('iterations ' + str(int(pageIterations)))
    for i in range(1, int(pageIterations.split(' ')[1])):
        for row in rows:
            if(row.text.find('Opt-In') > 0):
                optinCount+=1
                # data = {"content": '-----------\n' + row.text + '-----------\n'}
                # response = requests.post(discord_url, json=data)
                # print(response.status_code)
            if(row.text.find('Transfer') > 0):  
                transferCount+=1
            if(row.text.find('Config') > 0):
                print('Found a created coin!')
                print(row.text)
                createCount+=1
                data = {"content": '-----------\n' + row.text + '-----------\n'}
                response = requests.post(discord_url, json=data)
                print(response.status_code)

                print(response.content)
            # print(row.text)
            rows = driver.find_elements(By.CSS_SELECTOR, "tr[class^='row']")
        nextpageelement = driver.find_element_by_css_selector("button[data-cy='next']")
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_css_selector("button[data-cy='next']"))
        driver.find_element_by_css_selector("button[data-cy='next']").send_keys(Keys.RETURN)
        print('should have clicked')


print(optinCount)
print(transferCount)
print(createCount)
driver.quit()
