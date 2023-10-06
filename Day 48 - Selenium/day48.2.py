from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org/")


# bug_link=driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(bug_link.get_attribute("href"))

event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
for time,name in zip(event_times,event_names):
    print(f"{time.text} - {name.text}")

driver.quit()