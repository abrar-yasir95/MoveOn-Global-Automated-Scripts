# SHIPPING_METHOD
# Test Case: Visit Product Details page->Select Variant->Select quantity->Scroll down till shipping method->Click
# Select Category->Select Shipping Type-> Select Radio Button-> Apply

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

driver.get("https://moveon.com.bd/product?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F532600651915.html")

print("Starting Test Case")

variant = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div[5]/div/div[1]/div/ul/li[3]/img")
variant.click()
time.sleep(3)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)

method = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div[8]/div/div/div/span/span[2]')
method.click()
time.sleep(2)

category = driver.find_element(By.CSS_SELECTOR, 'body > div.fade.modal.show > div > div > div > div.shipping-modal-body > div:nth-child(1) > div > div.col-7.mt-2 > div > div > div > div.css-1hwfws3')
category.click()
time.sleep(2)

# print("Select category below")
# cat = input("Your chosen category")
# time.sleep(2)

action = ActionChains(driver)
action.send_keys("Mouse")
# action.perform()
# action.send_keys(Keys.ENTER)
action.perform()
action.click()
time.sleep(2)

# s_type = Select(driver.find_element(By.XPATH,'//*[@id="shipping_type"]'))
# option = 'Air'
# s_type.select_by_visible_text(option)

# type = driver.find_element(By.TAG_NAME, value="option")
# i = 0
# while i < len(type):
#  if (type[i].text == "Ship"):
#      type[i].click()





# item = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]')
# item.click()



