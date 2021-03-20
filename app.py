import requests
import time
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://www.binance.com/en/support/announcement/c-48?navId=48")
soup = BeautifulSoup(page.content, 'html.parser')
title = ""

while True:
    first_headline = soup.find_all("a", {"class": "css-1ej4hfo"})[0].text
    time.sleep(10)
    if title == first_headline:
        print("Title is the same")
    else:
        print(first_headline)
        title = first_headline







