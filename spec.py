# review, details, spec
# Test Case: Visit Details Page->Select Variant->Scroll Down till Specification-> Select Spec at first
# Go down->Go up and select Product Details->Then select Reviews

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://moveon.com.bd/product?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F532600651915.html")
print("Starting Test Case")
variant = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div[5]/div/div[1]/div/ul/li[3]/img")
variant.click()
time.sleep(3)

# specification
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[5]/div/div/div/div/ul/li[1]")
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
time.sleep(4)

element1 = driver.find_element(By.XPATH, '//*[@id="react-tabs-1"]/div/div/table/tbody/tr[38]/td')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element1)
time.sleep(4)

element_up = driver.find_element(By.XPATH, '//*[@id="react-tabs-2"]')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center' });", element_up)
time.sleep(2)

# product details
detail = driver.find_element(By.XPATH,'//*[@id="react-tabs-2"]')
detail.click()

# reviews

review = driver.find_element(By.XPATH, '//*[@id="react-tabs-4"]')
review.click()



