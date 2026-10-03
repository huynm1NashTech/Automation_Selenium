import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/login")
driver.maximize_window()
driver.find_element(By.ID,"userName").send_keys("a")
driver.find_element(By.ID,"password").send_keys("Abcde@123789")
driver.find_element(By.XPATH,"//button[@id='login']").click()

#dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_index(1)
#message = driver.find_element(By.CLASS_NAME,"alert-success").text
#print(message)
#print(dropdown)
#print(driver.title)
#print(driver.current_url)

time.sleep(10)