from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pl.wikipedia.org/")

# amount=driver.find_element(By.XPATH,'//*[@id="main-page-intro"]/p/a[4]')
# print(amount.text)
# #amount.click()

# all_portals=driver.find_element(By.LINK_TEXT,"Kategorie Wikipedii")
# print(all_portals.text)
# all_portals.click()

search_toggle=driver.find_element(By.CLASS_NAME,"search-toggle")
search_toggle.click()
searchbar=driver.find_element(By.NAME,"search")
searchbar.send_keys("Python")
searchbar.send_keys(Keys.ENTER)