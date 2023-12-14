# ADD_TO_CART

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://moveon.com.bd/product?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F532600651915.html")

variant = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div[5]/div/div[1]/div/ul/li[5]/img')
variant.click()
time.sleep(3)

plus_button = driver.find_element(By.CSS_SELECTOR,'#__next > div > div:nth-child(2) > div.ProductDetails_product-details__2IxtR > div:nth-child(2) > div > div > div > div.col-xl-9 > div > div > div.col-lg-7.mt-4.mt-lg-0 > div > div > div:nth-child(5) > div > div:nth-child(2) > div > div.table-responsive > table > tbody > tr:nth-child(1) > th:nth-child(4) > div > button:nth-child(3) > svg' )
plus_button.click()
time.sleep(3)

add = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div/div[3]/button[2]')
add.click()
time.sleep(2)

visit_cart = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div/div[3]/div/div[1]/a/div/img')
visit_cart.click()
time.sleep(2)