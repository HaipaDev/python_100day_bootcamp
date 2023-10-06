from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.pl/SIHOO-Ergonomiczne-komputerowe-regulowanymi-podlokietnikami/dp/B08BBYG117/ref=sr_1_2?crid=58BOHVZU6SY2&keywords=hinomi+h1+pro&qid=1696491519&sprefix=hinomi%2Caps%2C107&sr=8-2")


price_dollars=int(driver.find_element(By.CLASS_NAME,"a-price-whole").text.replace("\xa0","").replace(" ",""))
price_cents=float("0"+"."+driver.find_element(By.CLASS_NAME,"a-price-fraction").text)
price=price_dollars+price_cents
print(f"The price is: {price}")


driver.quit()