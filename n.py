from requests_html import HTMLSession
from bs4 import BeautifulSoup
session = HTMLSession()
resp = session.get("https://mi.tv/ar/canales/hbo/hoy")
resp.html.render()
soup = BeautifulSoup(resp.html.html, "html.parser")
print(soup)
