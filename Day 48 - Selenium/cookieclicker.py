from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--mute-audio")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/cookieclicker/")

import time
time.sleep(2)

try:
    consent_button=driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    consent_button.click()
except:
    print("Couldnt press consent button")

try:
    cookies_consent_button=driver.find_element(By.CLASS_NAME,'cc_btn_accept_all')
    cookies_consent_button.click()
except:
    print("Couldnt press cookies consent button")

try:
    english_lang_button=driver.find_element(By.ID,"langSelect-EN")
    english_lang_button.click()
except:
    print("Couldnt press English lang button")
    

time.sleep(3)
try:
    close_cookies_popup=driver.find_element(By.XPATH,'/html/body/div[2]/div/ins/img[3]')
    close_cookies_popup.click()
except:
    pass

try:
    options_button=driver.find_element(By.ID,'prefsButton')
    options_button.click()
    volume_slider=driver.find_element(By.ID,'volumeSlider')
    driver.execute_script("arguments[0].setAttribute('value', 0);", volume_slider)
    options_button.click()
except:
    pass

TEST_LENGTH_IN_MIN=5
WAITTIME_BEFORE_UPGRADE_CHECK_IN_SEC=5
timeout = time.time() + 60*TEST_LENGTH_IN_MIN
upgradecheck_timer = time.time() + WAITTIME_BEFORE_UPGRADE_CHECK_IN_SEC
print(f"Test will stop on: {timeout}")

cookies=0
cookies_per_second=0
cookie_clicker_button=driver.find_element(By.ID,"bigCookie")
while cookie_clicker_button:
    cookie_clicker_button.click()
    cookies=int(driver.find_element(By.ID,"cookies").text.split()[0].replace(",",""))
    try:
        # cookies_per_second_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cookiesPerSecond')))
        # cookies_per_second=float(cookies_per_second_element.text.split(": ")[1].replace(",",""))
        cookies_per_second=float(driver.find_element(By.ID,"cookiesPerSecond").text.split(": ")[1].replace(",",""))
    except:
        pass
    print(f"Cookies: {cookies} | per second: {cookies_per_second}")
    
    if time.time() >= upgradecheck_timer:
        print("Checking for upgrades/buildings")
        prices=[]
        upgrades_elements=[]
        building_elements=[]
        
        
        #building_elements=driver.find_elements(By.CSS_SELECTOR,".product.unlocked.enabled")
        try:
            building_elements = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product.unlocked.enabled")))
        except:
            print("Couldnt get buildings")
        if(len(building_elements)>0):
            prices=[int(element.find_element(By.CLASS_NAME,"price").text.replace(",","")) for element in building_elements]
            print(prices)
        
        
        try:
            upgrades_elements = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".crate.upgrade")))
        except:
            print("Couldnt get upgrades")
        #upgrades_elements=driver.find_elements(By.CSS_SELECTOR,".crate.upgrade")
        if(len(upgrades_elements)>0):
            for upgrade in upgrades_elements:
                #upgrade.click()
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".crate.upgrade")))
                #upgrades_elements.remove(upgrade)
                try:
                    upgrade.click()
                    break
                except StaleElementReferenceException:
                    print("Cant purchase upgrade")
                #upgrades_elements=driver.find_elements(By.CSS_SELECTOR,".crate.upgrade")
                upgrade_elements = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".crate.upgrade")))
                break
        
        if(len(prices)>0):
            try:
                max_price_index = prices.index(max(prices))
                most_expensive_upgrade = building_elements[max_price_index]
                most_expensive_upgrade.click()
            except:
                print("Cant purchase building")
            
        upgradecheck_timer = time.time() + WAITTIME_BEFORE_UPGRADE_CHECK_IN_SEC
    if time.time() > timeout:
        break

try:
    cookies_per_second_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cookiesPerSecond')))
    cookies_per_second=float(cookies_per_second_element.text.split(": ")[1].replace(",",""))
    print(f"Final cookies per second: {cookies_per_second}")
except:
    print("Couldnt get final cookies per second")