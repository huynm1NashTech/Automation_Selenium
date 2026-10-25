from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from pageObjects.shop import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        time.sleep(5)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        wait = WebDriverWait(self.driver, 10)
        toast_locator = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        wait.until(expected_conditions.visibility_of_element_located(toast_locator))
        print("Login Successful")
        time.sleep(2)

