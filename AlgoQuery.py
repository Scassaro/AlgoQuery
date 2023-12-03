from urllib.request import urlopen
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
    
url = "https://algoexplorer.io/"
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/533.44 (KHTML, like Gecko) Chrome/47.0.2360.241 Safari/601'})
print()
# myopener = MyOpener()
# page = myopener.urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# print(html)
