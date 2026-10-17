import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None

@pytest.fixture( scope="function" )
def browserInstance():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait( 5 )
    driver.get( "https://www.saucedemo.com/" )
    yield driver  #Before test function execution
    driver.close()  #post your test function execution
