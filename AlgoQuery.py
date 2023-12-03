from urllib.request import urlopen
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless=new")

url = "https://algoexplorer.io/"
# response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/533.44 (KHTML, like Gecko) Chrome/47.0.2360.241 Safari/601'})
# print(str(response.content).replace('>', '\n'))
driver = webdriver.Firefox(options=options)
driver.get(url)
driver.find_element_by_css_selector("[data-cy='latestBlocksLink']").click()
driver.implicitly_wait(50)
array = driver.find_elements_by_xpath("//a[@data-cy='round']")
for select in array:
    print(select.text)
# elem = driver.find_elements(By.CY_ID, 'latestBlocksLink')
driver.quit()
# myopener = MyOpener()
# page = myopener.urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# print(html)
