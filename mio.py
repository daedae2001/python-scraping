from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.div
    except AttributeError as e:
        return None
    return title

a=requests.get("https://mi.tv/ar/canales/hbo/hoy")

#print(a.text)
title = getTitle("https://mi.tv/ar/canales/hbo/hoy")
#print(title.text)
