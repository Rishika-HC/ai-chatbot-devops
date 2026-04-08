from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:5000")

time.sleep(2)

input_box = driver.find_element(By.ID, "message")
input_box.send_keys("Hello")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(3)

response = driver.find_element(By.ID, "response").text

assert response != ""

driver.quit()