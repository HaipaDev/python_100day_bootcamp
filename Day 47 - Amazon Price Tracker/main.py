import requests
from bs4 import BeautifulSoup
import lxml

ENDPOINT="https://www.amazon.pl/SIHOO-Ergonomiczne-komputerowe-regulowanymi-podlokietnikami/dp/B08BBYG117/ref=sr_1_2?crid=58BOHVZU6SY2&keywords=hinomi+h1+pro&qid=1696491519&sprefix=hinomi%2Caps%2C107&sr=8-2"
response=requests.get(ENDPOINT,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0","Accept-Language": "en-US,en;q=0.5"})
html_response=response.text
soup=BeautifulSoup(html_response,"lxml")
print(soup)
with open("website.html","w",encoding="utf-8") as file:
    file.write(soup.prettify())
    #file.write(html_response)
    
print()
price_element=soup.find(name="span",class_="a-offscreen")
print(price_element.getText())
print(price_element.getText().split("zł")[0].replace("\xa0","").replace(",","."))
price=float(price_element.getText().split("zł")[0].replace("\xa0","").replace(",","."))
print(price)