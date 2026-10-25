from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from utils.browserutils import BrowserUtils


class getvaluePage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.employee = (By.XPATH, "//div[text()='Total Employees']/following-sibling::div[1]")

    def getvalue(self):
        self.driver.get("https://assertqa.com/practice/webtables")
        time.sleep(3)
        product = self.driver.find_element(*self.employee).text
        print(product)
        time.sleep(3)

