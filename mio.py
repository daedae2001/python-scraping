from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests


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
print(title.text)
